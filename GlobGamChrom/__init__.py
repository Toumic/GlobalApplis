#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Origine 20 septembre 2022
# GlobGamChrom : Mémoriser le chromatisme original et modifié


import inspect
from typing import Callable


# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Module de chromatisation chromatique
dic_abc = {}
a_diatonic, b_diatonic, c_diatonic = [], [], []


def chromatic(a, b, c):
    """Définitions :
    A = Tonalité analogique inchangée
    B = Tonalité numérique modifiée
    C = Tonalité numérique inchangée"""
    a_diatonic.append(a)
    b_diatonic.append(b)
    c_diatonic.append(c)
    # print('GGC', ' A:', len(a), ' B:', len(b), ' C:', len(c))
    if len(a_diatonic) == 12:
        print(lineno(), len(a_diatonic), len(b_diatonic), len(c_diatonic))
        for ia in range(len(a_diatonic)):
            # print(lineno(), a_diatonic[ia][0])
            break
