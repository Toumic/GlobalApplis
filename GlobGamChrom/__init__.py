#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Origine 20 septembre 2022
# GlobGamChrom : Mémoriser le chromatisme original et modifié


import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Module de chromatisation chromatique
dic_ana, dic_mod, dic_inv = {}, {}, {}  # Dictionnaires à utiliser
dic_abc = [dic_ana, dic_mod, dic_inv]
a_diatonic, b_diatonic, c_diatonic = [], [], []


def chromatic(a, b, c, s):
    """Fonction chromatique afin de soulager le code GlobGamVers6
    Définitions :
    A = Gamme hepta en cours
    B = Nom de la tonalité analogique
    C = Tonalité numérique ordre croissant
    S = Degré d'inversion demandé ou par défaut"""
    print(lineno(), 'GGC/', ' A:', a[0], '\t...\tB = Nom de la tonalité analogique:', b, '\nC:', c[0], '\t...S:', s)
    a_diatonic.append(a)  # Tonalité analogique
    b_diatonic.append(b)  # Nom de la tonalité
    c_diatonic.append(c)  # Tonalité numéric croissant
    (lineno(), 'GGC/', b, '= Nom de la tonalité analogique')
    # Mise en forme du dictionnaire dic_ana(analogie)
    for ia in range(len(a_diatonic[0])):
        dic_ana[ia+1] = a_diatonic[0][ia]
        (lineno(), 'GGC/', a_diatonic[0][ia], 'ia:', ia)
    # Mise en forme du dictionnaire dic_mod(ordre)
    for ia in range(len(c_diatonic[0])):
        dic_mod[ia+1] = c_diatonic[0][ia]
        (lineno(), 'GGC/', c_diatonic[0][ia], 'ia:', ia)
    if s == 0:
        s = 12
    if s in range(1, 13):  # Occurrences d'arrivages (ne peut être autrement !)
        wh, wi, we = True, s, 0
        while wh:
            we += 1  # Clé du dico: dic_mod_al
            (lineno(), 'GGC/ 13: we', we, 'wi:', wi)
            if we == 12:
                wh = False
            dic_inv[wi] = dic_mod[we]
            wi -= 1  # Clé du dico: dic_inv_erse
            if wi == 0:
                wi = 12
            (lineno(), 'GGC/ 13: we', we, 'wi:', wi)
        (lineno(), 'GGC/ s:', s)
    '''ckt = list(dic_mod.keys())
    dkt = list(dic_inv.keys())
    # Décoration dico[clés]
    for ikt in range(len(ckt)):
        ck, dk = ckt[ikt], dkt[ikt]
        (lineno(), 'clés: (div_mod) = ', ck, '(div_inv) = ', dk)'''
    (lineno(), 'GGC/', 'dic analog', dic_ana)
    print(lineno(), 'GGC/', 'dic modal\t', dic_mod.keys())
    print(lineno(), 'GGC/', 'dic envers\t', dic_inv.keys())
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
