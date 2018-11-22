def addfeat(ordered_feats, feat, value):
    """
    a megfelelő formátumban hozzáadja a jegyet a jegy-érték párok dictionary-jéhez
    :param ordered_feats: sorrendezett jegy-érték párok dictionary-je
    :param feat: jegy
    :param value: érték
    :return:
    """

    ordered_feats.append('='.join((feat, value)))


def order_feats(pos, subpos, featdict):
    """
    sorrendezi a jegyeket (az MSD-nek megfelelő pozíciók adják a sorrendet)
    :param pos: conll szófaj
    :param subpos: conll alszófaj (MSD 2. poz)
    :param featdict: a jegy-érték párok dictionary-je
    :return:
    """

    ordered_feats = list()
    if subpos != '_':
        subpos = 'SubPOS={0}'.format(subpos)
    ordered_feats.append(subpos)

    if pos == 'A':
        addfeat(ordered_feats, 'Deg', featdict.get('Deg', 'p'))         # p, c, s
        addfeat(ordered_feats, 'Num', featdict.get('Num', 's'))         # p, s
        addfeat(ordered_feats, 'Cas', featdict.get('Cas', 'n'))         # betű
        addfeat(ordered_feats, 'NumP', featdict.get('NumP', 'none'))    # s, p, none
        addfeat(ordered_feats, 'PerP', featdict.get('PerP', 'none'))    # 1, 2, 3, none
        addfeat(ordered_feats, 'NumPd', featdict.get('NumPd', 'none'))  # s, p none

    elif pos == 'N':
        addfeat(ordered_feats, 'Num', featdict.get('Num', 's'))         # p, s
        addfeat(ordered_feats, 'Cas', featdict.get('Cas', 'n'))         # betű
        addfeat(ordered_feats, 'NumP', featdict.get('NumP', 'none'))    # s, p, none
        addfeat(ordered_feats, 'PerP', featdict.get('PerP', 'none'))    # 1, 2, 3, none
        addfeat(ordered_feats, 'NumPd', featdict.get('NumPd', 'none'))  # s, p none

    elif pos == 'M':
        addfeat(ordered_feats, 'Num', featdict.get('Num', 's'))         # p, s
        addfeat(ordered_feats, 'Cas', featdict.get('Cas', 'n'))         # betű
        addfeat(ordered_feats, 'Form', featdict.get('Form', 'l'))       # l, d, r
        addfeat(ordered_feats, 'NumP', featdict.get('NumP', 'none'))    # s, p, none
        addfeat(ordered_feats, 'PerP', featdict.get('PerP', 'none'))    # 1, 2, 3, none
        addfeat(ordered_feats, 'NumPd', featdict.get('NumPd', 'none'))  # s, p none

    elif pos == 'P':
        addfeat(ordered_feats, 'Per', featdict.get('Per', '3'))
        addfeat(ordered_feats, 'Num', featdict.get('Num', 's'))
        addfeat(ordered_feats, 'Cas', featdict.get('Cas', 'n'))
        addfeat(ordered_feats, 'NumP', featdict.get('NumP', 'none'))    # s, p, none
        addfeat(ordered_feats, 'PerP', featdict.get('PerP', 'none'))    # 1, 2, 3, none
        addfeat(ordered_feats, 'NumPd', featdict.get('NumPd', 'none'))  # s, p none

    elif pos == 'O':
        deg = featdict.get('Deg', None)                 # vagy p, c, s, vagy nincs
        if deg:
            addfeat(ordered_feats, 'Deg', deg)
        addfeat(ordered_feats, 'Num', featdict.get('Num', 's'))
        addfeat(ordered_feats, 'Cas', featdict.get('Cas', 'n'))
        addfeat(ordered_feats, 'NumP', featdict.get('NumP', 'none'))    # s, p, none
        addfeat(ordered_feats, 'PerP', featdict.get('PerP', 'none'))    # 1, 2, 3, none
        addfeat(ordered_feats, 'NumPd', featdict.get('NumPd', 'none'))  # s, p none

    elif pos == 'R':
        addfeat(ordered_feats, 'Deg', featdict.get('Deg', 'none'))  # p, c, s, none
        addfeat(ordered_feats, 'Num', featdict.get('Num', 'none'))  # s, p, none
        addfeat(ordered_feats, 'Per', featdict.get('Per', 'none'))  # 1, 2, 3, none

    elif pos == 'V':
        mood = featdict.get('Mood', 'i')        # i, m, c, o , n
        tense = featdict.get('Tense', None)     # vagy nincs p, s
        defi = featdict.get('Def', None)        # vagy nincs, vagy y, n, 2
        addfeat(ordered_feats, 'Mood', mood)
        if tense:
            if mood != 'n':
                addfeat(ordered_feats, 'Tense', tense)
        addfeat(ordered_feats, 'Per', featdict.get('Per', 'none'))      # none, 1, 2, 3
        addfeat(ordered_feats, 'Num', featdict.get('Num', 'none'))      # none, s, p
        if defi:
            if mood != 'n':
                addfeat(ordered_feats, 'Def', defi)

    elif pos == 'C':
        addfeat(ordered_feats, 'Form', featdict.get('Form', 'c'))       # c, s
        addfeat(ordered_feats, 'Coord', featdict.get('Coord', 'w'))     # p, w

    # a maradék szófajokkal nem kell semmit csinálni (POS=ISTYX)
    # else:
    #     pass

    return '|'.join(ordered_feats)


def print_conv(token, lemma, emmorph, conllpos, conllfeature):
    """
    a megfelelő sorrendben, tabbal elválasztva printeli az összes infót
    :param token: szóalak
    :param lemma: tő
    :param emmorph: emmorph címke
    :param conllpos: konvertált conll szófaj
    :param conllfeature: konvertált conll címke
    :return:
    """
    print(token, lemma, emmorph, conllpos, conllfeature, sep='\t')
