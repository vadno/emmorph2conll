#!/usr/bin/python3
# coding=utf-8

import sys
import mappings as cd
import lex_lists as ls
import print_conll as pr


def feats_to_dict(conllfeature, conllfeature_dict):
    """
    elrendezi a meglévő jegyeket a jegy-érték struktúrába
    :param conllfeature: a jegy-érték sztringek listája
    :param conllfeature_dict: dictonary-be rendezve
    """

    for inflex_feat in conllfeature:
        key, attribute = inflex_feat.split('=')
        conllfeature_dict[key] = attribute
    del conllfeature[:]


def parse(token, lemma, emmorph):
    """
    az emmorph címke feldolgozása
    :param token: szóalak
    :param lemma: tő
    :param emmorph: az emmorph címke
    :return: conll szófajcímke és formázott conll jegy-érték párok
    """

    # az emmorph kód szétvágása szófajra, derivációs és inflexiós jegyekre
    emmorph_features = emmorph.rstrip(']').lstrip('[').split('][')
    pos_feats = [feat for feat in emmorph_features if feat.startswith('/') or feat == 'OTHER']
    deriv_feats = [feat for feat in emmorph_features if feat.startswith('_')]
    infl_feats = [feat for feat in emmorph_features if feat not in pos_feats + deriv_feats]

    # punktuáció önmagában, vagy szóra tapadó punct
    punct_feat = False
    if emmorph_features[-1] == 'Punct':
        if len(emmorph_features) > 1:
            punct_feat = True
        else:
            return 'Punct', '_', ''

    # a felsőfok jele szófaj volt, átkerül az inflexiós jegyek közé
    for feat in pos_feats:
        if feat in cd.POS_TO_INFL_FEAT:
            if feat in cd.SUPERLATIVE:
                pos_feats.remove(feat)
            infl_feats.append(feat)

    # a középfok jele és az ige néhány jegye (műveltető, gyakoritó, ható)
    # és az igenevek jegyei átkerülnek az inflexiós jegyek közé
    # de megmaradnak a deriv jegyek között is a megfelelő szófaj miatt
    for feat in deriv_feats:
        if feat in cd.DERIV_TO_INFL_FEAT:
            infl_feats.append(feat)

    if not pos_feats:
        # ha egyáltalán nincs szófajcímke, akkor se akad el, majd a deriváció megoldja
        pos_feats.append('DERIV')

    # POS tagek feldolgozása
    pos_feat = pos_feats[0]
    conllpos = ''
    subpos = '_'
    if pos_feat in cd.POS_RULES:
        conllpos, subpos = cd.POS_RULES[pos_feat]

    # derivációs jegyek feldolgozása
    for deriv_feat in deriv_feats:
        if deriv_feat in cd.DERIV_RULES:
            conllpos, subpos = cd.DERIV_RULES[deriv_feat]

    if not conllpos:
        return 'Z', '_', ''
    elif conllpos in ('Y', 'X'):
        return conllpos, '_', ''

    # feature-ök feldolgozása
    conllfeature = []
    conllfeature_dict = {}

    # verb
    if conllpos == 'V':
        # jegyek a mappingsből
        for infl_feat in infl_feats:
            if '.' in infl_feat:
                subfeats = infl_feat.split('.')
                for subfeat in subfeats:
                    if subfeat in cd.VERBAL_INFL_RULES:
                        conllfeature.extend(cd.VERBAL_INFL_RULES[subfeat])

            elif infl_feat in cd.VERBAL_INFL_RULES:
                conllfeature.extend(cd.VERBAL_INFL_RULES[infl_feat])

        feats_to_dict(conllfeature, conllfeature_dict)

    # nominal
    elif conllpos in ('N', 'A', 'M', 'P', 'O'):

        for infl_feat in infl_feats:
            if infl_feat in cd.NOMINAL_INFL_RULES:
                conllfeature.extend(cd.NOMINAL_INFL_RULES[infl_feat])

        # tulajdonnév
        if conllpos == 'N' and lemma[0].isupper():
                subpos = 'p'

        # névmástípusok a lex_listből a névmásokra és a határozószókra
        elif conllpos in ('P', 'R'):
            if 'Per' not in conllfeature_dict:
                conllfeature_dict['Per'] = '3'
            if lemma in ls.PRON_DEM:
                subpos = 'd'
            elif lemma in ls.PRON_IND:
                subpos = 'i'
            elif lemma in ls.PRON_TOT:
                subpos = 'g'
            if conllpos == 'P':
                if lemma in ls.PRON_PRS:
                    subpos = 'p'
                elif lemma in ls.PRON_RCP:
                    subpos = 'y'
                elif lemma in ls.PRON_POSS:
                    subpos = 's'
                elif lemma in ls.PRON_REFL:
                    subpos = 'x'
            elif conllpos == 'R':
                if lemma in ls.NEG:
                    subpos = 'm'

        # ha felsőfok, akkor a középfok jegye már nem kell
        if 'Deg=s' in conllfeature:
            while 'Deg=c' in conllfeature:
                conllfeature.remove('Deg=c')

        feats_to_dict(conllfeature, conllfeature_dict)

        # ha olyan sorszámnév, amit az emmorph nem sorszámnévnek elemzett
        if conllpos == 'M' and punct_feat:
            subpos = 'o'

    elif conllpos == 'C':
        if lemma in ls.SCONJ:
            subpos = 's'
            conllfeature_dict['Form'] = 's'

    return conllpos, subpos, conllfeature_dict


def main():

    for line in sys.stdin:
        token, lemma, elemzes = line.strip().split('\t')[:3]
        conllpos, subpos, conllfeature_dict = parse(token, lemma, elemzes)

        # sorrendbe kerülnek a jegyek
        conllfeature = pr.order_feats(conllpos, subpos, conllfeature_dict)
        pr.print_conv(token, lemma, elemzes, conllpos, conllfeature)


if __name__ == "__main__":
    main()
