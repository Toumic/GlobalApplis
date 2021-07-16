# Python 3.9 UTF-8
# Mercredi 12 mai 2021 à 20h 32m (premières lignes)
# Cabviva.fr Cab.Rich.Int.Music.Quant
# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# Module GlobGamFonds.py
"""Réception liste binaire Tétra + Gamme
Priorité aux gammes heptatoniques:
    classement par le poids altéré du degré modal"""

import GlobEnModes
import inspect
import os
from typing import Callable

inspect.getsource(os)
glob_en = GlobEnModes

# lineno() Pour déboguer le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

"""# Fondues Tableau préconçu servant de référence, il n'est pas exhaustif
fondues = ['0', '-2', '+2', '^2', '-3', '-23', '-34x', '+34', '+23x', '-34', 'x3',
           '°3', '+34x', '°34x', '^3', '-4', '-24', '^4', '°4', '-5', '-25', '-25+',
           '+25-', '-35', '-35+', '+45x', '+25x', '°35-', '+35x', '-45+', '-45',
           'x5', 'x45+', '-25°', '-35°', '-45°', '°45-', '°5', '°35+', '*5', '°35x',
           '-45x', '°45x', '-6', '+6', '-26', '-26+', '+26-', '+26', '-36', '-36+',
           '-56', '-56+', '+56', 'x46+', '-26°', '-46+', '-46°', 'x36+', '-56°',
           '°46-', '°36+', '*6', '°46+', '°6', 'x26-']"""
# Limites Tableau des signatures mini/maxi de chaque degré
# limites = {1: [], 2: [-1, 4], 3: [-2, 3], 4: [-2, 3], 5: [-3, 2], 6: [-4, 1], 7: [-5, 0]}
# Signes Table des différents niveaux d'altérations sur les degrés
# gamme_signaux = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
# gammic = {'maj': '102034050607'}
# Gamme_Pesante Tableau des poids modaux de la gamme majeure
gamme_pesante = {1: [[0], [0]], 2: [['b3', 'b7'], [-4, -8]],
                 3: [['b2', 'b3', '6', 'b7'], [-3, -4, -7, -8]], 4: [['#4'], [+5]],
                 5: [['b7'], [-8]], 6: [['b3', 'b6', 'b7'], [-4, -7, -8]],
                 7: [['b2', 'b3', 'b5', 'b6', 'b7'], [-3, -4, -6, -7, -8]]}
modes_major = {1: [0, 0, 0, 0, 0, 0, 0], 2: [0, 0, -4, 0, 0, 0, -8],
               3: [0, -3, -4, 0, 0, -7, -8], 4: [0, 0, 0, +5, 0, 0, 0],
               5: [0, 0, 0, 0, 0, 0, -8], 6: [0, 0, -4, 0, 0, -7, -8],
               7: [0, -3, -4, 0, -6, -7, -8]}
poids_major = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
modes_grade = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
# longs_modes = {4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 12: longs}
"""Poids Altéré Modal :gamme_pesante{}"""
kkk = 0
for deg, kg in gamme_pesante.items():
    kgk = 0
    if len(kg[1]) == 1:
        poids_major[deg] = kg[1][0]
        kkk += kg[1][0]
    else:
        for k in kg[1]:
            khk = 0
            khk += k
            kkk += khk
            kgk += k
        poids_major[deg] = kgk
    # print(f' {lineno()}, Poids_Major:{poids_major[deg]} Deg{modes_grade[deg-1]}')
# print(f' {lineno()}, Poids_Major:{poids_major}')
signes = ['', '+', 'x', '^', '^+', '^x', '°*', '-*', '*', '°', '-']
gamme_majeure, gamme_index = '102034050607', [0, 2, 4, 5, 7, 9, 11]  # Diatonisme naturel
poids_modal = []
modes_modal = []
gam_tonique, magma, tab_eh = [], [], []
# modes_modal = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}


def diatonic(topic):
    """Fonction de détection des gammes fondamentales,
    basée sur le poids le plus faible donné par les degrés modaux."""
    for top01 in topic:
        poids_class = {}
        modes_modal.clear()
        top00 = ''.join(t for t in top01)
        retour, poids_gen, dio = 0, 0, 0
        print(f' {lineno()}, {top00}')
        """Passe: Autres modes"""
        while retour < 7:  # Défaut retour < 8
            # print(lineno())
            retour += 1
            poids_modal.clear()
            grader, regard, lacune, pesant, poids = 0, -1, 0, [0], 0
            """Traitement d'Un Mode Fondamental |Pesant|"""
            for t00 in top00:
                regard += 1
                """Passe: Poids du Uème mode"""
                if t00 == '1':
                    grader += 1
                    extra = gamme_majeure.index(str(grader))  # :extra= Position Degré
                    lacune = regard - extra  # :lacune= Niveau Altération
                    # print(f' {lineno()} {lacune} |{grader}| {extra} ')
                    if lacune < 0:
                        pesant[0] = lacune - grader
                    elif lacune == 0:
                        pesant[0] = 0
                    else:
                        pesant[0] = grader + lacune
                    poids_modal.append(pesant[0])
                    poids += pesant[0]
                    pesant[0] = 0
            poids_gen += poids
            poids_class[top00] = top00, abs(poids)
            modes_modal.append(poids_modal.copy())
            # print(lineno(), modes_modal)
            # poids_modal.clear()
            pilote = list(top00)
            pilote.insert(0, pilote.pop())
            while pilote[0] == '0':
                pilote.insert(0, pilote.pop())
            top00 = ''.join(p for p in pilote)
            # print(lineno(), 'PM', poids_modal, len(poids_modal), retour)
            # modes_modal[] = poids_modal
        if len(modes_modal) == 7:
            # print(lineno(), modes_modal)
            ggg = glob_en.seption(modes_modal)
            print(lineno(), 'GGF Oblic', ggg)
        lys_0, dic_pt, dic_neg = [], {}, {}
        for c in poids_class.keys():
            if c[-1] == '1':
                lys_0.append(poids_class[c])
        for io in lys_0:
            q, m = io[0], io[1]
            dic_neg[m] = q
            dic_pt[q] = m
        mini = min(dic_pt.values())
        gamme, ga = [], ''
        pm, pp = 0, -1
        for p in dic_neg[mini]:
            pp += 1
            if p == '1':
                pm += 1
                alter = gamme_majeure.index(str(pm))
                if pp != alter:
                    dif = pp - alter
                    ga = signes[dif] + str(pm)
                else:
                    ga = str(pm)
            else:
                ga = '0'
            gamme.append(ga)
        # Magma Tableau des degrés les plus légers...
        magma.append(gamme)
        print('145 GGF Classic', gamme, '\n')
        # break
    """GlobDicTGams = Gammes fondamentales"""
    fil_gammes = open('globdicTgams.txt', 'w')
    f = 0
    while f < len(magma):
        mm = str(magma[f])
        mm += '\n'
        fil_gammes.write(mm)
        gam_tonique.append(mm)
        f += 1
    fil_gammes.close()
    ff_ = 0
    for gf in gam_tonique:
        ff_ += 1
        oh, eh = '', []
        for g in gf:
            if g not in ('[', ']', ',', "'", "\n") and g != ' ':
                if g in signes:
                    oh += g
                elif int(g) or g == '0':
                    oh += g
                    eh.append(oh)
                    oh = ''
        # hi = ','.join(i for i in eh)
        # print('****', ff_, 'HI', 'hi', hi)
        tab_eh.append(eh)
    # print(lineno(), 'MM', modes_modal)
