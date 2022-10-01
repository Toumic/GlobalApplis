#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Origine 20 septembre 2022
# GlobGamChrom : Mémoriser le chromatisme original et modifié


import inspect
from typing import Callable


# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Module de chromatisation chromatique
dic_ana, dic_mod, dic_inv = {}, {}, {}
dic_abc = [dic_ana, dic_mod, dic_inv]
a_diatonic, b_diatonic, c_diatonic = [], [], []


def chromatic(a, b, c, d):
    """Fonction chromatique afin de soulager le code GlobGamVers6
    Définitions :
    A = Tonalité analogique inchangée
    B = Tonalité numérique modifiée
    C = Tonalité numérique inchangée
    D = Nom de la tonalité analogique"""
    a_diatonic.append(a)
    b_diatonic.append(b)
    c_diatonic.append(c)
    # print(lineno(), 'GGC', ' A:', len(a), ' B:', len(b), ' C:', len(c), d)
    if len(a_diatonic) == 12:
        print(lineno(), d[0], '= Nom de la tonalité analogique')
        for ia in range(len(a_diatonic)):
            print(lineno(), a_diatonic[ia][0])
            # break
