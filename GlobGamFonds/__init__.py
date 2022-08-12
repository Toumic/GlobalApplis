# !/usr/bin/env python 3.10
# -*- coding: utf-8 -*-
# mercredi 12 mai 2021 à 20 h 32 mn (premières lignes)
# Cabviva.fr Cab.Rich.Int.Music.Quant
# Mardi 27 juillet 2021

# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# Module GlobGamFonds.py
"""Réception liste binaire Tétra + Gamme
Priorité aux gammes heptatoniques :
    classement par le poids altéré du degré modal"""

import inspect
import os
from typing import Callable
import GlobEnModes

inspect.getsource(os)
glob_en = GlobEnModes

# lineno() Pour coder le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

"""# Fondues Tableau préconçu servant de référence
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

"""Poids Majeurs Altérés Modaux :gamme_pesante{}"""
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
# (f' {lineno()}: GGF Poids_Major:{poids_major}')
#  60: GGF Poids_Major:{1: 0, 2: -12, 3: -22, 4: 5, 5: -8, 6: -19, 7: -28}
signes = ['', '+', 'x', '^', '+^', 'x^', 'o*', '-*', '*', 'o', '-']
gamme_majeure, gamme_index = '102034050607', [0, 2, 4, 5, 7, 9, 11]  # Diatonisme naturel
poids_modal, modes_modal, tab_eh = [], [], []
poids_avals, gamme_avals, magma, gam_tonique, mode_maj7 = {}, {}, {}, {}, {}
h_bin = {}


def diatonic(table, topic):
    """Fonction de détection des gammes fondamentales & Écriture fichier 'globdicTgams.txt',
    basée sur le poids le plus faible donné par les degrés modaux."""
    kit = 0
    for top01 in topic:
        kit += 1
        poids_class = {}
        poids_avals[kit] = []
        modes_modal.clear()
        top00 = ''.join(t for t in top01)
        retour, poids_gen, dio = 0, 0, 0
        if '1' in table:
            print(f'\n {lineno()} : {top00} {kit}')  # Analyses.txt : Affichage mode binaire
        #  80 : 101010110101 66

        """Passe: Séquence Diatonie"""
        while retour < 7:
            # print(lineno())
            retour += 1
            poids_modal.clear()
            grader, regard, lacune, pesant, poids = 0, -1, 0, [0], 0
            """Traitement d'Un Mode Fondamental |Pesant|"""
            # (top00)
            for t00 in top00:
                regard += 1
                """Passe: Poids du Uème mode"""
                if t00 == '1':
                    grader += 1
                    extra = gamme_majeure.index(str(grader))  # :extra= Position Degré
                    lacune = regard - extra  # :lacune= Niveau Altération
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
            poids_class[kit, top00] = top00, abs(poids)
            poids_avals[kit].append(top00)
            modes_modal.append(poids_modal.copy())
            pilote = list(top00)
            pilote.insert(0, pilote.pop())
            while pilote[0] == '0':
                pilote.insert(0, pilote.pop())
            top00 = ''.join(p for p in pilote)
            ('GGF', lineno(), 'top00', top00)
        # Détection septièmes majeures
        lys_0, dic_pt, dic_neg, dico_neg = [], {}, {}, []
        h_bin[kit] = []
        for c in poids_class.keys():  # Selection modes
            lp = poids_class[c], c[0]
            # (lineno(), 'GGF C', c[0], kit)
            if c[1][-1] == '1':  # Mode Maj7
                lys_0.append(lp)
            else:
                h_bin[kit].append(lp)
        if '1' in table:
            print(lineno(), 'GGF Lys_0', lys_0)
        # 122 GGF Lys_0 [(('101010110101', 5), 66), (('101011010101', 0), 66)]
        mode_maj7[kit] = lys_0
        for io in lys_0:  # lys_0: Issue Select Modes Majeurs
            q, m, n = io[0], io[0][1], io[1]
            dic_neg[m] = q  # q: ('101011010101', 0)
            dic_pt[q] = m, n  # m: 0 | n: 66
        mono = min(dic_pt.values())[1]
        mini = min(dic_pt.values())[0], mono
        disco = mini, dic_neg[mini[0]][0]
        dico_neg.append(disco)
        """ GGF'135*DicoNeg[0][0]/mini(Poids_Faible.N°_Gam)
         GGF'135*DicoNeg[0][1]/binaire_Gam: 1010110101018)
          GGF'153*Standard_Gam >> 1020340506078 >> 102-3040506078"""
        # ('\n', lineno(), 'GGF*DicoNeg', dico_neg)  # 135 GGF*DicoNeg [((0, 66), '101011010101')]

        gamme, ga = [], ''
        pm, pp = 0, -1
        for p in dic_neg[mini[0]][0]:  # Binaire Affectation Altérative
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
        gamme.append(dico_neg)
        # ...
        if '1' in table:
            print(lineno(), '_Gam:12', gamme[:12], '\n', lineno(), '_Gam12:', gamme[12:])
        #  153 _Gam:12 ['1', '0', '2', '0', '3', '4', '0', '5', '0', '6', '0', '7']
        #  153 _Gam12: [[((0, 66), '101011010101')]]
        f0 = 0
        for n0 in gamme[:12]:  # Compter les notes altérées
            if len(n0) > 1:
                f0 += 1
        if f0 < 3:  # Select Max2 Signes
            # Gamme aval Des degrés simples et légers...
            gamme_avals[mini[1]] = gamme  # mini[1]: N°_Gam ou gamme[12:][0][0][0][1]
            ('*', lineno(), 'M', mini[1], '_G8', gamme[12:][0][0][0][1])  # *164 MINI 66 _Gam8 66
        magma[mini[1]] = gamme
        # (lineno(), mini[1], 'Magma[][:12]', magma[mini[1]][:12])
        # 166 66 Magma[][:12] ['1', '0', '2', '0', '3', '4', '0', '5', '0', '6', '0', '7']
        if len(modes_modal) == 7:
            if len(mode_maj7) == 66:
                glob_en.seption(table, modes_modal, kit, magma[kit], gamme_avals, mode_maj7, h_bin)
            else:
                glob_en.seption(table, modes_modal, kit, magma[kit], gamme_avals, {}, {})
    (lineno(), 'GGF gamme_avals', gamme_avals.keys())
    # 174 GGF gamme&avals dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
    # Long MagMa = Les modèles légers. Dictionnaire 66 éléments
    # (lineno(), 'GGF Long MagMa', len(magma), magma)

    """GlobDicTGams = Gammes fondamentales"""
    fil_gammes = open('GlobalTexte/globdicTgams.txt', 'w')
    f = 1
    while f <= len(magma):
        mm = str(magma[f])
        mm += '\n'
        fil_gammes.write(mm)
        gam_tonique[f] = magma[f]  # gam_tonique: Création
        # (lineno(), 'GGF MagMa', magma[f][12:])
        f += 1
    fil_gammes.close()
    (lineno(), 'GGF GamTon', gam_tonique)
