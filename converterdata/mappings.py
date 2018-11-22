#!/usr/bin/python3
# coding=utf-8

####################
# SZÓFAJ SZABÁLYOK #
####################

POS_RULES = {
    '/Adj': ('A', 'f'),
    '/Adj|Abbr': ('A', 'f'),
    '/Adj|Attr': ('A', 'f'),
    '/Adj|Attr|Abbr': ('Y', '_'),
    '/Adj|Attr|Pro': ('P', 'd'),
    '/Adj|Pred': ('A', 'f'),
    '/Adj|Pro': ('P', 'd'),
    '/Adj|Pro|Int': ('P', 'q'),
    '/Adj|Pro|Rel': ('P', 'r'),
    '/Adj|Unit': ('A', 'f'),
    '/Adj|col': ('A', 'f'),
    '/Adj|nat': ('A', 'f'),

    '/Adv': ('R', 'x'),
    '/Adv|(Adj)': ('R', 'x'),
    '/Adv|(Num)': ('R', 'x'),
    '/Adv|Abbr': ('Y', '_'),
    '/Adv|Acronx': ('R', 'x'),
    '/Adv|AdjMod': ('R', 'x'),
    '/Adv|Pro': ('R', 'd'),
    '/Adv|Pro|Int': ('R', 'q'),
    '/Adv|Pro|Rel': ('R', 'r'),

    '/Cnj': ('C', 'c'),
    '/Cnj|Abbr': ('Y', '_'),

    '/Det': ('R', 'x'),
    '/Det|Art.Def': ('T', 'f'),
    '/Det|Art.NDef': ('T', 'i'),
    '/Det|Pro': ('P', 'd'),
    '/Det|Pro|(Post)': ('P', 'd'),
    '/Det|Pro|Int': ('P', 'q'),
    '/Det|Pro|Rel': ('P', 'r'),
    '/Det|Pro|def': ('P', 'd'),
    '/Det|Q.NDef': ('P', 'g'),
    '/Det|Q|indef': ('P', 'g'),
    '/Det|Q': ('P', 'i'),

    '/Inj-Utt': ('I', 'o'),

    '/N': ('N', 'c'),
    '/N|Abbr': ('Y', '_'),
    '/N|Abbr|ChemSym': ('Y', '_'),
    '/N|Acron': ('N', 'c'),
    '/N|Acronx': ('N', 'c'),
    '/N|Ltr': ('N', 'c'),
    '/N|Pro': ('P', 'p'),
    '/N|Pro|(Post)': ('P', 'd'),
    '/N|Pro|Abbr': ('Y', '_'),
    '/N|Pro|Int': ('P', 'q'),
    '/N|Pro|Rel': ('P', 'r'),
    '/N|Unit': ('N', 'c'),
    '/N|Unit|Abbr': ('Y', '_'),
    '/N|lat': ('N', 'c'),
    '/N|mat': ('N', 'c'),

    '/Num': ('M', 'c'),
    '/Num|Abbr': ('Y', '_'),
    '/Num|Attr': ('M', 'c'),
    '/Num|Digit': ('M', 'c'),
    '/Num|Pro': ('P', 'd'),
    '/Num|Pro|Int': ('P', 'q'),
    '/Num|Pro|Rel': ('P', 'r'),
    '/Num|Roman': ('M', 'c'),

    '/Post': ('S', 't'),
    '/Post|(Abl)': ('S', 't'),
    '/Post|(All)': ('S', 't'),
    '/Post|(Ela)': ('S', 't'),
    '/Post|(Ins)': ('S', 't'),
    '/Post|(N0)': ('S', 't'),
    '/Post|(Poss)': ('S', 't'),
    '/Post|(Subl)': ('S', 't'),
    '/Post|(Supe)': ('S', 't'),
    '/Post|(Ter)': ('S', 't'),

    '/Prep': ('C', 'c'),
    '/Prev': ('R', 'p'),
    '/QPtcl': ('R', 'q'),

    '/V': ('V', 'm'),

    '/S|Abbr': ('Y', '_'),
    '/X': ('X', '_'),
    '/X|Abbr': ('Y', '_')
}

###################
# DERIV SZABÁLYOK #
###################

DERIV_RULES = {
    '_Abe/Adj': ('A', 'f'),                      # "-A?tlAn, -tAlAn" abessivus = melléknévképző (fosztóképző)
    '_AdjVbz_Ntr/V': ('V', 'm'),                 # "-Vs?Odik, -Ul" denominális (melléknévből) intranzitívige-képző
    '_AdjVbz_Tr/V': ('V', 'm'),                  # "-ít" denominális (melléknévből) tranzitívige-képző
    '_Adjz:i/Adj': ('A', 'f'),                   # "-i" melléknévképző
    '_VAdjz:nivaló/Adj': ('A', 'f'),             # "-nivaló" melléknévképző
    '_Adjz:s/Adj': ('A', 'f'),                   # "-Vs" melléknévképző
    '_Adjz:Ó/Adj': ('A', 'f'),                   # " -Ó" melléknévképző, mély hangrendű magánhangzók ragozott alakjaiban
    '_Adjz:Ú/Adj': ('A', 'f'),                   # " -Ú" melléknévképző
    '_Adjz_Hab/Adj': ('A', 'f'),                 # "-Ós" melléknévképző: habituális
    '_Adjz_Loc:beli/Adj': ('A', 'f'),            # "-beli" melléknévképző (helyjelölő)
    '_Adjz_Ord:VdlAgOs/Adj': ('A', 'f'),         # "-VdlAgOs" melléknévképző (számnévből)
    '_Adjz_Quant/Adj': ('A', 'f'),               # "-nyi" mennyiségnévképző
    '_Adjz_Type:fajta/Adj': ('A', 'f'),          # "-fajta" melléknévképző (típusjelölő)
    '_Adjz_Type:forma/Adj': ('A', 'f'),          # "-forma" melléknévképző (típusjelölő)
    '_Adjz_Type:féle/Adj': ('A', 'f'),           # "-féle" melléknévképző (típusjelölő)
    '_Adjz_Type:szerű/Adj': ('A', 'f'),          # "-szerű" melléknévképző (típusjelölő)
    '_AdvPerfPtcp/Adv': ('R', 'v'),              # "-vÁn" határozói igenév
    '_AdvPtcp/Adv': ('R', 'v'),                  # "-vA" határozói igenév
    '_AdvPtcp:ttOn/Adv': ('R', 'v'),             # "-ttOn" határozói igenév
    '_AdvPtcp:vÁst/Adv': ('R', 'v'),             # " -vÁst" határozói igenév
    '_Advz:rét/Adv': ('R', 'x'),                 # "-rét" számnévi határozóképző
    '_Advz_LocDistr:szerte/Adv': ('R', 'x'),     # "-szerte" határozóképző (térbeli fedés)
    '_Advz_Quant:szám/Adv': ('R', 'x'),          # "-szám" határozóképző mennyiségekre
    '_Aggreg/Adv': ('M', 'c'),                   # "-An" csoportszámosság-határozó
    # '_Caus/V': ('V', 'm'),                     # "-t?At" műveltetőige-képző                   #  nem módosít szófajt
    # '_Com:stUl/Adv'                            # "-stUl" comitativusi (társhatározói) esetrag #  nem módosít szófajt
    # '_Comp/Adj': ('A', 'f'),                   # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Adv': ('R', 'x'),                   # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Adv|Pro': ('P', 'd'),               # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Num': ('M', 'c'),                   # "-bb" középfok                               #  nem módosít szófajt
    # '_Comp/Post|(Abl)': ('R', 'x'),            # "-bb" középfok                               #  nem módosít szófajt
    # '_Design/Adj': ('A', 'f'),                 # "-(bb)ik" kijelölő                           #  nem módosít szófajt
    '_Des/N': ('N', 'c'),                        # "-hatnék" desiderativus
    # '_Dim:cskA/Adj': ('A', 'f'),               # "-VcskA" kicsinyítő képző                    # nem módosít szófajt
    # '_Dim:cskA/N': ('N', 'c'),                 # "-VcskA" kicsinyítő képző                    # nem módosít szófajt
    '_Distr:nként/Adv': ('R', 'x'),              # "-Vnként" disztributív
    '_DistrFrq:ntA/Adv': ('R', 'x'),             # "-VntA" gyakorisághatározó
    '_Frac/Num': ('M', 'f'),                     # "-Vd" törtszámnév
    # '_Freq/V': ('V', 'm'),                     # "-O?gAt" gyakorítóképző                      #  nem módosít szófajt
    '_FutPtcp/Adj': ('A', 'f'),                  # "-AndÓ" „beálló" melléknévi igenév
    '_Ger/N': ('N', 'c'),                        # "-Ás" nomen actionis igenominalizáló
    '_Ger:tA/N': ('N', 'c'),                     # "-tA" birtokos igenominalizáló
    '_ImpfPtcp/Adj': ('A', 'f'),                 # "-Ó" folyamatos melléknévi igenév
    # '_Manner/Adv',                             # "-An, -Ul" határozóképző: módhatározó        # nem módosít szófajt
    # '_Manner:0/Adv',                           # határozóképző: módhatározó (zéró)            # nem módosít szófajt
    # '_MedPass/V': ('V', 'm'),                  # "-Ódik" mediális ige                         # nem módosít szófajt
    # '_Mlt-Iter/Adv',                           # "-szOr" multiplikatív/iteratív               # nem módosít szófajt
    # '_MltComp/Adv',                            # "-szOrtA" összehasonlító multiplikatív       # nem módosít szófajt
    # '_Mod/V': ('V', 'm'),                      # -hAt" modális („ható") igeképző
    '_ModPtcp/Adj': ('A', 'f'),                  # "-hAtÓ" modális melléknévi igenév
    '_Mrs/N': ('N', 'p'),                        # "-né" asszonynévképző
    '_NAdvz:ilAg/Adv': ('A', 'f'),               # "-ilAg" denominális (főnévből) határozóképző
    '_NVbz_Ntr:zik/V': ('V', 'm'),               # "-zik" intranzitív igeképző
    '_NVbz_Tr:z/V': ('V', 'm'),                  # "-z" denominális (főnévből) tranzitívige-képző
    '_NegModPtcp/Adj': ('A', 'f'),               # "-hAtAtlAn" tagadó modális melléknévi igenév
    '_NegPtcp/Adj': ('A', 'f'),                  # "-AtlAn" tagadó passzív melléknévi igenév (igei fosztóképző)
    '_Nz:s/N': ('N', 'c'),                       # "-Vs" főnévképző
    '_Nz_Abstr/N': ('N', 'c'),                   # "-sÁg" főnévképző absztraktfőnév-képző
    # '_Nz_Type:féleség/N': ('N', 'c'),          # "-féleség" főnévképző (típusjelölő)       # nem módosít szófajt
    # '_Nz_Type:szerűség/N': ('N', 'c'),         # "-szerűség" főnévképző (típusjelölő)      # nem módosít szófajt
    '_Ord/Adj': ('M', 'o'),                      # "-Vdik" sorszámnév
    '_OrdDate/N': ('N', 'c'),                    # "-Vdika" dátumokban a nap sorszámnévképzője
    # '_Pass/V': ('V', 'm'),                     # "-t?Atik" passzív                         # nem módosít szófajt
    '_PerfPtcp/Adj': ('A', 'f'),                 # "-O?tt" befejezett melléknévi igenév
    '_PerfPtcp_Subj=tA/Adj': ('A', 'f'),         # "-tA" befejezett melléknévi igenév
    '_Tmp_Ante/Adv': ('N', 'c'),                 # "-jA" időbeli megelőzés
    '_Tmp_Loc/Adv': ('R', 'x'),                  # "-vAl, -0" időhatározói végződés
    '_VAdvz:ÓlAg/Adv': ('R', 'x'),               # "-ÓlAg" határozóképző: igéből
    '_VNz:nivaló/N': ('N', 'c'),                 # "-nivaló" főnévképző
    '_Vbz:kOd/V': ('V', 'm')                     # "-s?kOdik" denominális igeképző
}

#########################
# POS helyett INFL jegy #
#########################

POS_TO_INFL_FEAT = ('/Supl',
                    '/Num|Digit',
                    '/Num|Roman'
)

###############
# SUPERLATIVE #
###############

SUPERLATIVE = ('/Supl', )

###########################
# DERIV helyett INFL jegy #
###########################

DERIV_TO_INFL_FEAT = (
    '_Comp/Adj',                    # "-bb" középfok
    '_Comp/Adv',                    # "-bb" középfok
    '_Comp/Adv|Pro',                # "-bb" középfok
    '_Comp/Post|(Abl)'              # "-bb" középfok 
    '_Design/Adj',                  # "-(bb)ik" kijelölő

    '_Aggreg/Adv',                  # "-An" csoportszámosság-határozó
    '_Com:stUl/Adv',                # "-stUl" comitativusi (társhatározói) esetrag
    '_Distr:nként/Adv',             # "-Vnként" disztributív
    '_Manner/Adv',                  # "-An, -Ul" határozóképző: módhatározó
    '_Manner:0/Adv',                # határozóképző: módhat ha zéró toldalékként realizálódik a "-A?tlAn/-tAlAn" után
    '_Mlt-Iter/Adv',                # "-szOr" multiplikatív/iteratív
    '_MltComp/Adv'                  # "-szOrtA" összehasonlító multiplikatív
)

##########################
# inflexiós jegyek: igei #
##########################

VERBAL_INFL_RULES = {
    'Inf': ['Mood=n'],
    
    'Sbjv': ['Mood=m', 'Tense=p'],
    'Cond': ['Mood=c', 'Tense=p'],
    'Prs': ['Mood=i', 'Tense=p'],
    'Pst': ['Mood=i', 'Tense=s'],

    '1Sg': ['Num=s', 'Per=1'],
    '1Sg›2': ['Def=2', 'Num=s', 'Per=1'],
    '2Sg': ['Num=s', 'Per=2'],
    '3Sg': ['Num=s', 'Per=3'],
    '1Pl': ['Num=p', 'Per=1'],
    '1Pl*': ['Num=p', 'Per=1'],
    '2Pl': ['Num=p', 'Per=2'],
    '3Pl': ['Num=p', 'Per=3'],
    '3Pl*': ['Num=p', 'Per=3'],
    'Def': ['Def=y'],
    'NDef': ['Def=n']
}

#############################
# inflexiós jegyek: névszói #
#############################

NOMINAL_INFL_RULES = {
    '/Num|Digit': ['Form=d'],
    '/Num|Roman': ['Form=r'],
    '/Supl': ['Deg=s'],

    '_Comp/Adj': ['Deg=c'],
    '_Comp/Adv|Pro': ['Deg=c'],
    '_Comp/Adv': ['Deg=c'],
    '_Comp/Post|(Abl)': ['Deg=c'],
    '_Design/Adj': ['Deg=c'],

    '_Aggreg/Adv': ['Cas=w'],
    '_Com:stUl/Adv': ['Cas=q'],
    '_Distr:nként/Adv': ['Cas=u'],
    '_Manner/Adv': ['Cas=w'],           # Cas=w lehet A, N, M, P
    '_Manner:0/Adv': ['Cas=w'],
    '_Mlt-Iter/Adv': ['Cas=6'],
    '_MltComp/Adv': ['Cas=6'],

    'Nom': ['Cas=n'],
    'Acc': ['Cas=a'],
    'Dat': ['Cas=d'],                   # vagy Cas=g ha genivite
    'Ins': ['Cas=i'],
    'Cau': ['Cas=c'],
    'Ine': ['Cas=2'],
    'Supe': ['Cas=p'],
    'Ade': ['Cas=3'],
    'Ill': ['Cas=x'],
    'Ela': ['Cas=e'],
    'Del': ['Cas=h'],
    'Subl': ['Cas=s'],
    'Abl': ['Cas=b'],
    'All': ['Cas=t'],
    'Ter': ['Cas=9'],
    'Temp': ['Cas=m'],
    'Loc': ['Cas=l'],
    'Transl': ['Cas=y'],
    'Ess': ['Cas=w'],
    'EssFor:ként': ['Cas=f'],
    'EssFor:képp': ['Cas=f'],
    'EssFor:képpen': ['Cas=f'],

    'Pl': ['Num=p'],
    'Fam.Pl': ['Num=p'],
    '1Sg': ['Num=s', 'Per=1'],
    '2Sg': ['Num=s', 'Per=2'],
    '3Sg': ['Num=s', 'Per=3'],
    '1Pl': ['Num=p', 'Per=1'],
    '2Pl': ['Num=p', 'Per=2'],
    '3Pl': ['Num=p', 'Per=3'],

    'Poss.1Sg': ['NumP=s', 'PerP=1'],
    'Poss.2Sg': ['NumP=s', 'PerP=2'],
    'Poss.3Sg': ['NumP=s', 'PerP=3'],
    'Poss.1Pl': ['NumP=p', 'PerP=1'],
    'Poss.2Pl': ['NumP=p', 'PerP=2'],
    'Poss.3Pl': ['NumP=p', 'PerP=3'],

    'Pl.Poss.1Sg': ['Num=p', 'NumP=s', 'PerP=1'],
    'Pl.Poss.2Sg': ['Num=p', 'NumP=s', 'PerP=2'],
    'Pl.Poss.3Sg': ['Num=p', 'NumP=s', 'PerP=3'],
    'Pl.Poss.1Pl': ['Num=p', 'NumP=p', 'PerP=1'],
    'Pl.Poss.2Pl': ['Num=p', 'NumP=p', 'PerP=2'],
    'Pl.Poss.3Pl': ['Num=p', 'NumP=p', 'PerP=3'],

    'AnP': ['NumPd=s'],
    'AnP.Pl': ['NumPd=p']
}

