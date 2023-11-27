#!/usr/bin/env python 3
# -*- coding : utf-8 -*-
# Ce mercredi 3 mai 2023
# Module colorimétrique pour GlobalApplis

# Comment traiter les couleurs hexas chromatiques
from tkinter import *
import inspect
from typing import Callable
# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

col_class = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
col_hexas = ['#FF0000', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#4B0082', '#EE82EE']
col_modes = ['Chrome2', 'Chrome4', 'Chrome7', 'Chrome9', 'Chrome11']
col_diato = ['Tonice', 'Tonale', 'Mélody', 'Médian', 'Domine', 'Harmony', 'Sensif']
col_perso = {}


# code0: #FF0000  code1: #FFA500 col_perso[code0]: Tonice
def hex_trans(code0, code1, colo0, colo1):
    # liste_rvb = ''  # Fonction de translation int vers code couleur
    code00 = code0[1:]  # Former un code correct
    code01, code02, code03 = code00[:2], code00[2:4:], code00[4:]  # Sectionner code00
    code04 = [code01, code02, code03]  # Assemblage résultat
    code05 = [int(code01, 16), int(code02, 16), int(code03, 16)]  # Hexa vers integer
    code10 = code1[1:]  # Former un code correct
    code11, code12, code13 = code10[:2], code10[2:4:], code10[4:]  # Sectionner code10
    code14 = [code11, code12, code13]  # Assemblage résultat
    code15 = [int(code11, 16), int(code12, 16), int(code13, 16)]  # Hexa vers integer
    code20, code21 = [], '#'
    (lineno(), 'C/ colo0.1:', colo0, colo1, 'code04.14:', code04, code14)
    for lc in range(len(code05)):  # Calculer la différence pour obtenir une moyenne
        if code05[lc] == code15[lc]:
            code20.append(code05[lc])
        else:
            res_dif = (code05[lc] - code15[lc]) // 2
            res_fin = code05[lc] - res_dif
            code20.append(res_fin)
    for c20 in code20:  # Assembler les codes hexas
        c21 = hex(c20)[2:]
        if len(c21) == 1:
            c21 = '0' + c21
        code21 += c21
    liste_rvb = code21
    liste_rvb = liste_rvb.upper()
    return liste_rvb


res, col_count = 0, -1
autre_ligne, comment, ret_trans = True, '', None
for lin in range(7):
    col_perso[col_hexas[lin]] = col_diato[lin]
    res += 1  # Accès à la prochaine couleur
    if lin != 2:
        if res < 7:  # #FF5300 Envoi col_perso[ret_trans]: Chrome2 	col_count: 0
            autre_ligne = True
            col_count += 1
            col_hexa2 = col_hexas[res]
            ret_trans = hex_trans(col_hexas[lin], col_hexa2, col_class[lin], col_class[res])
            col_perso[ret_trans] = col_modes[col_count]
            comment = 'Intermédiaire entre ' + col_class[lin] + ' et ' + col_class[res]
        else:
            comment, autre_ligne = '', False
    elif lin == 2:
        autre_ligne = False
    if autre_ligne:
        (lineno(), 'autre_ligne:', autre_ligne)
print(lineno(), 'C/ col_perso:', col_perso.keys())
