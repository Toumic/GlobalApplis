#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Origine 20 septembre 2022
# GlobGamChrom : Mémoriser le chromatisme original et modifié

a_diatonic, b_diatonic, c_diatonic = [], [], []


def chromatic(a, b, c):
    """Définitions :
    A = Tonalité analogique inchangée
    B = Tonalité numérique modifiée
    C = Tonalité numérique inchangée"""
    a_diatonic.append(a)
    b_diatonic.append(b)
    c_diatonic.append(c)
    # print('GGC', 'A:', a[0], len(a), '\n', '   B:', b[0], '\n', '   C:', c[0])
