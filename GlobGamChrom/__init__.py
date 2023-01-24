#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Origine 20 septembre 2022
# GlobGamChrom : Traiter le chromatisme original pour le traduire en commatisme

import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Module de chromatisation chromatique
dic_ana, dic_mod, dic_inv, dic_abc = {}, {}, {}, {}  # Dictionnaires à utiliser
dic_rip0, dic_rip1, dic_rip2, dic_rip3 = {}, {}, {}, {}  # Dictionnaires diatoniques 1ère étape
dic_cap0, dic_cap1, dic_cap2, dic_cap3 = {}, {}, {}, {}  # Dictionnaires diatoniques 2ème étape
'''1ère et 2ème étape = Modules des secteurs "gamme"&"chrome", selon (couplé ou isolé)'''
dic_rapt = {}  # dic_rapt = Dictionnaire des premiers commatismes
dic_rap0, dic_rap2 = {}, {}  # Afficher les chromatismes parallèles
dic_com = {}  # dic_com = Premier dictionnaire des douze gammes commatiques.
a_diatonic, b_diatonic, c_diatonic = [], [], []
# dic_maj = Référence des tonalités majeures primaires
dic_maj = {'C': ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B'],
           'D': ['D', '', 'E', '', '+F', 'G', '', 'A', '', 'B', '', '+C'],
           'E': ['E', '', '+F', '', '+G', 'A', '', 'B', '', '+C', '', '+D'],
           'F': ['F', '', 'G', '', 'A', '-B', '', 'C', '', 'D', '', 'E'],
           'G': ['G', '', 'A', '', 'B', 'C', '', 'D', '', 'E', '', '+F'],
           'A': ['A', '', 'B', '', '+C', 'D', '', 'E', '', '+F', '', '+G'],
           'B': ['B', '', '+C', '', '+D', 'E', '', '+F', '', '+G', '', '+A']}
gam_abc = {'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
           'D': ['D', 'E', '+F', 'G', 'A', 'B', '+C'],
           'E': ['E', '+F', '+G', 'A', 'B', '+C', '+D'],
           'F': ['F', 'G', 'A', '-B', 'C', 'D', 'E'],
           'G': ['G', 'A', 'B', 'C', 'D', 'E', '+F'],
           'A': ['A', 'B', '+C', 'D', 'E', '+F', '+G'],
           'B': ['B', '+C', '+D', 'E', '+F', '+G', '+A']}
# 2912(self.nordiese) 2917(self.subemol)
tab_sup = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^', '+^^^^', 'x^^^^',
           '^^^^^', '+^^^^^', 'x^^^^^', '^^^^^^', '+^^^^^^', 'x^^^^^^', '^^^^^^^', '+^^^^^^^', 'x^^^^^^^', '^^^^^^^^']
tab_inf = ['', '-', 'o', '*', '-*', 'o*', '**', '-**', 'o**', '***', '-***', 'o***', '****', '-****', 'o****',
           '*****', '-*****', 'o*****', '******', '-******', 'o******', '*******', '-*******', 'o*******', '********']
cle_maj = [0, 2, 4, 5, 7, 9, 11]  # Emplacements majeurs
extension = [8, 9, 10, 11, 12, 13, 14]


def transposer(rip0, rip1, rip2, rip3):
    """Ici, on réceptionne les gammes qui ont leurs tonices altérées.
    Séquences du traitement : - Obtenir la gamme majeure signée ou non signée.
     - Transposer la gamme au niveau altéré. - Résoudre la tonalité.
    Rip0.1 = Huit notes. Rip2.3 = Cinq notes.☺
    Pour transposer les notes de la gamme (Rip0.1)
    Pour transposer les notes chromatiques (Rip2.3)"""
    (lineno(), rip0, '\n', rip1, '\n', rip2, '\n', rip3, 'len(rip0):', len(rip0))
    # Montage table des clés majeures de dic_maj
    cle_aut, note, note1, ok = [], '', '', False
    for i in range(1, 14):
        if i in rip1.keys():
            (lineno(), rip0, '\n', rip1, len(rip0), len(rip1))
            if len(rip0) > 1:
                note0 = rip0[i][0]
                ('>1>1>1', lineno(), 'len2 note0:', note0)
            else:
                note0, note1 = rip0[i], rip1[i]
                ('<1<1<1', lineno(), 'len1 note0:', note0, 'rip1[1]:', rip1[i])
            if note0 not in cle_aut and len(note0) > 1:
                cle_aut.append(note0)
                (lineno(), 'note0:', note0)
            if note1 not in cle_aut and len(note1) > 1:
                cle_aut.append(note1)
                (lineno(), 'note1:', note1)
        if i in rip2.keys():
            (lineno(), rip2, '\n', rip3, len(rip2), len(rip3))
            if len(rip2) > 2:
                if len(rip2[i]) == 1:
                    note2 = rip2[i]
                else:
                    note2 = rip2[i][0] + rip2[i][1]
                if len(rip3[i]) == 1:
                    note3 = rip3[i]
                else:
                    note3 = rip3[i][0] + rip3[i][1]
                (lineno(), rip2)
            else:
                note2, note3 = rip2[i], rip3[i]
                ok = True
            if note2 not in cle_aut and len(note2) > 1:
                cle_aut.append(note2)
                (lineno(), 'note2:', note2)
            if note3 not in cle_aut and len(note3) > 1:
                cle_aut.append(note3)
                (lineno(), 'note3:', note3)
        if ok:
            break
    (lineno(), 'cle_aut:', cle_aut)
    x = 0
    for ca in cle_aut:  # Lire les clés une par une
        ('\n', lineno(), 'ca:', ca)
        x += 1
        '''Commencement réitératif transposé majeur'''
        if len(ca) > 1:  # Assurance de la note altérée
            dic_maj[ca] = [ca]  # ca = La note signée ou non
            gam_abc[ca] = [ca]  # ca = La note signée ou non
            no, si = ca[len(ca) - 1:], ca[:len(ca) - 1]  # si = L'altération & La note tonique
            '''Assignation des valeurs (positives/négatives)'''
            if si in tab_sup:  # tab_si = Repère altératif du signe commun
                ind_si = tab_sup.index(si)  # ind_si = Index signe dans tab_sup
            else:
                ind_si = tab_inf.index(si)  # ind_si = Index signe dans tab_inf
                ind_si = ind_si - (ind_si * 2)  # ind_si = Pour une valeur négative
            (lineno(), '|  ind_si:', ind_si)

            for dm in dic_maj[no]:  # Lire les notes de la gamme majeure
                if len(dm) == 1:  # La note est absolument non altérée
                    note = si + dm
                    (lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                elif dm != '':  # Éviter les intervalles vides
                    et, to = dm[:len(dm) - 1], dm[len(dm) - 1:]  # et = L'altération sur le degré majeur
                    if et in tab_sup:  # L'altération majeure dans tab_supérieur(+, x, ^,)
                        ind_et = tab_sup.index(et)  # ind_et = Mesure l'Index dans tab_sup
                        dif_si = abs(ind_si) - ind_et  # ind_et = Toujours un nombre entier
                        ('***************', abs(dif_si), dif_si, 'ind_si:', ind_si, 'ind_et:', ind_et, dm)
                        if abs(dif_si) > ind_et:  # Si la différence est supérieure à l'état (et).
                            if ind_si > 0:
                                dif_et = ind_et + abs(ind_si)
                                note = tab_sup[abs(dif_et)] + to
                                (lineno(), 'dif_et:', dif_et)
                                # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            else:
                                dif_et = ind_et - abs(ind_si)
                                note = tab_inf[abs(dif_et)] + to
                                (lineno(), 'dif_et:', dif_et)
                                # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            (lineno(), 'Sup abs(dif_si)>ind_et', 'ind_si:', ind_si, 'ind_et:', ind_et, dm)
                        else:
                            if ind_si < 0:
                                if abs(ind_si) > ind_et:
                                    dif_et = ind_et - abs(ind_si)
                                    note = tab_inf[abs(dif_et)] + to
                                    (lineno(), 'dif_et:', dif_et)
                                    # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                                else:
                                    dif_et = ind_et - abs(ind_si)
                                    note = tab_sup[abs(dif_et)] + to
                                    (lineno(), 'dif_et:', dif_et)
                                    # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            else:
                                dif_et = ind_si + ind_et
                                note = tab_sup[dif_et] + to
                                (lineno(), 'dif_et:', dif_et)
                                # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            (lineno(), 'Sup abs(dif_si)=ind_et', 'ind_si:', ind_si, 'ind_et:', ind_et, dm)
                        # note = tab_sup[dif_et] + no     # no = La note absolue
                        (lineno(), 'sup', no)
                    else:  # L'altération majeure dans tab_inférieur(-, o, *,)
                        ind_et = tab_inf.index(et)
                        dif_si = abs(ind_si) - ind_et
                        if dif_si > ind_et:
                            if ind_si > 0:
                                dif_et = abs(ind_si) - ind_et
                                note = tab_sup[dif_et] + to
                                (lineno(), 'dif_et:', dif_et)
                                # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            else:
                                dif_et = abs(ind_si) - ind_et
                                note = tab_inf[dif_et] + to
                                (lineno(), 'dif_et:', dif_et)
                                # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            (lineno(), 'Inf dif_si>ind_et', 'ind_si:', ind_si, 'ind_et:', ind_et, dm)
                        else:
                            if ind_si > 0:
                                dif_et = ind_et - ind_si
                                note = tab_sup[abs(dif_et)] + to
                                (lineno(), 'dif_et:', dif_et)
                                # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            else:
                                dif_et = ind_et + abs(ind_si)
                                note = tab_inf[dif_et] + to
                                (lineno(), 'dif_et:', dif_et)
                                # print(lineno(), 'dm:', dm, 'si:', si, 'note:', note)
                            (lineno(), 'Sup abs(dif_si)=ind_et', 'ind_si:', ind_si, 'ind_et:', ind_et, dm)
                        # note = tab_inf[dif_si] + no
                        (lineno(), 'inf')
                    (lineno(), 'maj>1:', dm, 'si:', si, 'et:', et)
                else:
                    dic_maj[ca].append(dm)
                if note not in dic_maj[ca]:
                    dic_maj[ca].append(note)
                    gam_abc[ca].append(note)
    ('\n', lineno(), 'dic_maj:', dic_maj.keys(), '\ngam_abc:', gam_abc['C'])


def alteration(signe):
    """Permet d'obtenir la valeur numérique réelle de l'altération
    Quand le signe est dans tab_sup = Valeur(+ et son rang(index))
    Quand le signe est dans tab_inf = Valeur(- et son rang(index))"""
    retour = ''
    if signe in tab_sup:
        retour = '+' + str(tab_sup.index(signe))
        (lineno(), 'Alteration/signe(+):', signe, retour)
    elif signe in tab_inf:
        retour = '-' + str(tab_inf.index(signe))
        (lineno(), 'Alteration/signe(-):', signe)
    return retour


def chromatic(a, b, c, s):
    """Fonction chromatique afin de soulager le code GlobGamVers6
    Définitions :
    A = Gamme hepta en cours
    B = Nom de la tonalité analogique
    C = Tonalité numérique ordre croissant
    S = Degré d'inversion demandé ou donné par défaut :
        Ce degré est invariable, car il forme une chronologie.
        Tout changement fait une modulation de l'inversion parallèle.
        - Cette modulation de l'inversion pourrait, mais ici elle n'est pas dans le code."""
    (lineno(), '***\nGGC/', 'A:', type(a), 'B = Nom de la tonalité analogique:', b, '\nC:', c, 'S:', s)
    '''Exemples: Formats des premiers tableaux[Comment ils sont traités - |CHANGE = ERREUR| ]
    209 GGC/ A: ([('', 'C')], [(('+', 'C'), ('-', 'D'))], [('', 'D')], [(('+', 'D'), ('-', 'E'))], [('', 'E')], 
    [('', 'F')], [(('+', 'F'), ('-', 'G'))], [('', 'G')], [(('+', 'G'), ('-', 'A'))], [('', 'A')], 
    [(('+', 'A'), ('-', 'B'))], [('', 'B')]) B = Nom de la tonalité analogique: C Maj 
    C: {0: ['1', '+1', '2', '+2', '3', '4', '+4', '5', '+5', '6', '+6', '7'], 1: 
    ['1', '-2', '2', '-3', '-4', '4', '-5', '5', '-6', '6', '-7', '-8'], 2: ['1', '+1', '2', '-3', '3', '4', '+4', 
    '5', '+5', '6', '-7', '7'], 3: ['1', '-2', 'o3', '-3', '-4', '4', '-5', '5', '-6', 'o7', '-7', '-8'], 
    4: ['1', '-2', '2', '-3', '3', '4', '+4', '5', '-6', '6', '-7', '7'], 5: ['1', '+1', '2', '+2', '3', '+3', '+4', 
    '5', '+5', '6', '+6', '7'], 6: ['1', '-2', '2', '-3', '3', '4', '-5', '5', '-6', '6', '-7', '-8'], 7: ['1', '+1', 
    '2', '+2', '3', '4', '+4', '5', '+5', '6', '-7', '7'], 8: ['1', '-2', '2', '-3', '-4', '4', '-5', '5', '-6', 'o7', 
    '-7', '-8'], 9: ['1', '+1', '2', '-3', '3', '4', '+4', '5', '-6', '6', '-7', '7'], 10: ['1', '-2', 'o3', '-3', 
    '-4', '4', '-5', 'o6', '-6', 'o7', '-7', '-8'], 11: ['1', '-2', '2', '-3', '3', '4', '-5', '5', '-6', '6', '-7', 
    '7']} S: 12'''
    a_diatonic.clear()
    b_diatonic.clear()
    c_diatonic.clear()
    a_diatonic.append(a)  # Tonalité analogique
    b_diatonic.append(b)  # Nom de la tonalité
    c_diatonic.append(c)  # Tonalité numéric croissant
    # Mise en forme du dictionnaire dic_ana (analogie)
    for ia in range(len(a_diatonic[0])):
        dic_ana[ia + 1] = a_diatonic[0][ia][0]
        # (ia, 'a_diatonic[0][ia][0]:', a_diatonic)
        if ia == 11:
            (lineno(), 'GGC/dic_ana:', dic_ana, 'len:', len(a_diatonic[0][ia][0]), 'ia:', ia)
            '''232 GGC/dic_ana: {1: ('', 'C'), 2: (('+', 'C'), ('-', 'D')), 3: ('', 'D'), 4: (('+', 'D'), ('-', 'E')), 
            5: ('', 'E'), 6: ('', 'F'), 7: (('+', 'F'), ('-', 'G')), 8: ('', 'G'), 9: (('+', 'G'), ('-', 'A')), 
            10: ('', 'A'), 11: (('+', 'A'), ('-', 'B')), 12: ('', 'B')} len: 2 ia: 11'''
    # Mise en forme du dictionnaire dic_mod(ordre)(numéric)
    for ia in range(len(c_diatonic[0])):
        dic_mod[ia + 1] = c_diatonic[0][ia]
        (lineno(), 'GGC/dic_mod[ia+1]:', dic_mod[ia + 1], 'ia:', ia)
    if s == 0:  # Se produit lorsqu'on ne passe pas par le bouton scalaire
        s = 12
    # Mise en forme du dictionnaire dic_inv(inverse)(numéric)
    tab_inv = []  #
    graduation = s
    if s in range(1, 13):  # Occurrences d'arrivages (ne peut être autrement !)
        wh, wi, we = True, s, 0
        while wh:
            we += 1  # Clé du dico: dic_mod_al
            (lineno(), 'GGC/ 13: we', we, 'wi:', wi)
            if we == 12:
                wh = False
            dic_inv[we] = dic_mod[wi]
            (lineno(), 'GGC/we:', we, 'wi:', wi)
            (lineno(), 'GGC/dic_mod[wi]:', dic_mod[wi], 'wi:', wi)
            (lineno(), 'GGC/dic_inv[we]:', dic_inv[we], 'we:', we, '\n')
            wi -= 1  # Clé du dico: dic_inv_erse
            if wi == 0:
                wi = 12
        tab_inv = list(dic_inv.keys())
    dic_inv[13] = dic_inv[1]
    tab_inv.append(tab_inv[0])
    (lineno(), 'GGC/', 'tab envers\t', tab_inv, '\n***')
    '''Mettre en forme les données pour qu'elles s'adaptent au retour.
    Dessin de la table (gamme en cours):
        dic_ana[1] = [('Altération', 'C')], dic_ana[2] = [(('+', 'C'), ('-', 'D'))]
            La note.        # c_rip0 = Altération sur la note naturelle(gamme)(#/b)
            La note.        # c_rip1 = La note naturelle de la gamme en cours(C)
            Le supérieur.   # c_rip1 = Note chromatique du rang supérieur ('-', 'D')
            L'inférieur.    # c_rip2 = Note chromatique du rang inférieur ('+', 'C')
            La tonalité.    # c_rop2 = Valeur numérique de la tonalité
            dic_rip0, dic_rip1, dic_rip2, dic_rip3 = {}, {}, {}, {}'''

    '''Le cycle yep sépare les notes de la gamme de celles qui sont chromatiques
    1ère étape de mise en place des notes toniques en position 1.'''
    dic_rip0.clear()
    dic_rip1.clear()
    dic_rip2.clear()
    dic_rip3.clear()
    gam0 = gam1 = ''
    for yep in range(1, 13):  # Mesurer dic_ana[yep](notes:gamme ou chrome)
        (lineno(), '___________________*************___________________ Début de cycle yep:', yep)
        abc = 0
        for lie in dic_ana[yep]:  # Compter les éléments
            for eli in lie:
                if eli in gam_abc['C']:
                    abc += 1
        '''# abc < 2 = Note isolée dans dic_rip0 et dic_rip1'''
        if abc < 2:  # c_rip0, c_rip1 (note gamme avec/sans altération)
            (lineno(), "Qu'est dic_ana[yep]?:", dic_ana[yep])
            if not list(dic_ana[yep][0]):  # Indexe la partie gauche de ('','') où est la note naturelle
                dic_rip0[yep] = list(dic_ana[yep][1])
                dic_rip1[yep] = list(dic_ana[yep][1])
                if yep == 1 and 1 in dic_rip0.keys():
                    gam0, gam1 = dic_rip0[yep][0], dic_rip1[yep][0]  # Gamme en cours originale
                    (lineno(), 'gam0.1:', gam0, gam1)
                (lineno(), 'GGC/dic_rip0.1[yep]:\t', yep, dic_rip0[yep], dic_rip1[yep])
            else:  # Indexe la partie gauche de ('-','') où est la note altérée
                dic_rip0[yep] = [dic_ana[yep][0] + dic_ana[yep][1]]  # Assemble l'altération & la note
                dic_rip1[yep] = [dic_ana[yep][0] + dic_ana[yep][1]]  # Assemble l'altération & la note
                if yep == 1 and 1 in dic_rip0.keys():
                    gam0, gam1 = dic_rip0[yep][0], dic_rip1[yep][0]  # Gamme en cours originale
                    (lineno(), 'gam0.1:', gam0, gam1, 'dic_ana[yep]:', dic_ana[yep])
                (lineno(), 'GGC/dic_rip0.1[yep]:\t', yep, dic_rip0[yep], dic_rip1[yep])
            if yep == 12:
                dic_inv[13] = dic_inv[1]
            (lineno(), 'GGC/dic_rip0.1[yep]:\t', yep, dic_rip0[yep], dic_rip1[yep])
        else:  # c_rip2, c_rip3 : Entretiennent les couplages
            (lineno(), "Qu'est dic_ana[yep]?:", dic_ana[yep][0], dic_ana[yep][1], 'yep:', yep)
            dic_rip2[yep] = list(dic_ana[yep][1])
            dic_rip3[yep] = list(dic_ana[yep][0])
            (lineno(), "dic_rip2.3:", dic_rip2[yep], dic_rip3[yep], 'yep:', yep)
            if yep == 1 and 1 in dic_rip2.keys():
                (lineno(), "dic_rip2.3:", dic_rip2[yep], dic_rip3[yep], 'dic_ana[yep]:', dic_ana[yep], 'yep:', yep)
                if dic_rip2[yep][0] != '':
                    dic_rip2[yep] = [dic_ana[yep][0][0] + dic_ana[yep][0][1]]
                    (lineno(), "dic_rip2:", dic_rip2[yep])
                else:
                    dic_rip2[yep] = dic_ana[yep][0][1]
                    (lineno(), "dic_rip2:", dic_rip2[yep])
                if dic_rip3[yep][0] != '':
                    dic_rip3[yep] = [dic_ana[yep][1][0] + dic_ana[yep][1][1]]
                    (lineno(), "dic_rip3:", dic_rip3[yep])
                else:
                    dic_rip3[yep] = dic_ana[yep][1][1]
                    (lineno(), "dic_rip3:", dic_rip3[yep])
                gam0, gam1 = dic_rip2[yep][0], dic_rip3[yep]  # Gamme en cours originale
                (lineno(), 'gam0.1:', gam0, gam1)
            (lineno(), 'GGC/dic_inv[yep]:   \t', yep, dic_inv[yep])
            (lineno(), 'GGC/dic_rip2inf[yep]:\t', yep, dic_rip2[yep])
            (lineno(), 'GGC/dic_rip3sup[yep]:\t', yep, dic_rip3[yep])
    if 1 in dic_rip0.keys():
        dic_rip0[13], dic_rip1[13] = dic_rip0[1], dic_rip1[1]
    else:
        dic_rip2[13], dic_rip3[13] = dic_rip2[1], dic_rip3[1]
    (lineno(), 'transposer *rip0:', dic_rip0, '\n*rip1:', dic_rip1, '\n*rip2:', dic_rip2, '\n*rip3:', dic_rip3)
    transposer(dic_rip0, dic_rip1, dic_rip2, dic_rip3)
    (lineno(), '_GGC/dic_rip0.1:  \n', dic_rip0, '\n', dic_rip1)
    (lineno(), '_GGC/dic_rip2.3:  \n', dic_rip2, '\n', dic_rip3)
    (lineno(), 'Indices \tgam0:', gam0, '\t\tgam1:', gam1, '\t\tb_diatonic[0]:', b_diatonic[0])

    '''Phase de renseignement de la matrice (yep) | gam_mod = dic_maj = Modes majeurs avec les intervalles'''
    for yes in range(1, 13):  # Lecture des séquences chromatiques
        (lineno(), '_________________________*************_____________________ Début de cycle yes:', yes)
        (lineno(), 'Indices \tgam0:', gam0, '\t\tgam1:', gam1, '\t\tb_diatonic[0]:', b_diatonic[0])
        gam_mod, rip0, rip1 = {}, '', ''
        # Section rip0_1
        if yes in dic_rip0.keys():  # Si clé est dans dic_rip0
            (lineno(), type(dic_rip1), '\ndic_rip1[yes][0]:', dic_rip1[yes][0], dic_rip1[yes])
            if len(dic_rip1[yes][0]) > 1:
                rip1 = dic_maj[dic_rip1[yes][0]][0]  # La tonique de la gamme majeure
                gam_mod[rip1] = dic_maj[dic_rip1[yes][0]]  # Pour l'index gamme majeure long(12)
                (lineno(), 'GGC/dic_rip1[yes][0]:', dic_rip1[yes][0], 'rip1:', rip1)
            else:
                rip1 = dic_maj[dic_rip1[yes][0]][0]  # La tonique de la gamme majeure
                gam_mod[rip1] = dic_maj[dic_rip1[yes][0]]  # Pour l'index gamme majeure long(12)
                (lineno(), 'GGC/dic_rip1[yes][0]:', dic_rip1[yes][0], 'rip1:', rip1)
            rip0 = rip1
            (lineno(), 'gam_mod:', gam_mod)
            (lineno(), 'rip0:', rip0, 'rip1:', rip1, '\n# Section rip0_1')
            # Section rip0_2
        elif yes in dic_rip2.keys():  # Si clé est dans dic_rip2
            # print(lineno(), dic_rip2.keys(), 'dic_rip2[yes]:', dic_rip2[yes], 'dic_rip3[yes]:', dic_rip3[yes])
            (lineno(), 'len(dic_rip2[yes]):', len(dic_rip2[yes]))
            ripe = ''
            for no in dic_rip2[yes]:
                ripe += no
            dic_rip2[yes] = [ripe]
            gam_mod[ripe] = dic_maj[ripe]  # Notes avec intervalle de dic_maj
            rip0 = dic_maj[ripe][0]
            # Section rip1_3
            ripe = ''
            for no in dic_rip3[yes]:
                ripe += no
            dic_rip3[yes] = [ripe]
            gam_mod[ripe] = dic_maj[ripe]  # Notes avec intervalle de dic_maj
            rip1 = dic_maj[ripe][0]
            (lineno(), 'rip0:', rip0, 'rip1:', rip1, 'ripe:', ripe)
            (lineno(), 'gam_mod:', gam_mod)
            (lineno(), 'gam_mod:', gam_mod.keys(), ' dic_maj:\n', dic_maj.keys(), '\n# Section rip1_2.3')

        '''# Phase de renseignement des degrés modaux'''
        for yi in range(1, 12):  # Mise en forme pour un mode diatonique
            result0, result1, deg_maj = 0, 0, ''
            (lineno(), 'gam_mod[rip0]:', gam_mod[rip0], '\n    gam_abc[rip0]:', gam_abc[rip0], '\trip0:', rip0)
            (lineno(), 'gam_mod[rip1]:', gam_mod[rip1], '\n    gam_abc[rip1]:', gam_abc[rip1], '\trip1:', rip1)
            (lineno())
            # num_ava & num_sui = Degrés assignés aux lignes directives (supérieures(ava), inférieures(sui))
            num_ava, num_sui = dic_inv[yes][yi], dic_inv[yes + 1][yi]  # ava = Supérieur, sui = Inférieur
            (lineno(), 'GGC/num_ava:', num_ava, 'num_sui:', num_sui, '\t\t*** SUP-INF Valeurs à suivre')
            # deg_ava & sig_ava = abs(degré sup) et signe(degré sup)
            deg_ava = sig_ava = ''
            for y in num_ava:  # Trier(signe/degré)
                if y.isnumeric():
                    deg_ava += y
                else:
                    sig_ava += y
            rng_ava, cop_ava = alteration(sig_ava), int(deg_ava)
            (lineno(), 'GGC/AVA deg:', deg_ava, 'sig:', sig_ava, '\trng:', rng_ava, '\t\t\t*** SUP à suivre')
            # deg_sui & sig_sui = abs(degré inf) et signe(degré inf)
            deg_sui = sig_sui = ''
            for y in num_sui:  # Trier(signe/degré)
                if y.isnumeric():
                    deg_sui += y
                else:
                    sig_sui += y
            rng_sui, cop_sui = alteration(sig_sui), int(deg_sui)
            (lineno(), 'GGC/SUI deg:', deg_sui, 'sig:', sig_sui, '\trng:', rng_sui, '\t\t\t*** INF à suivre')
            (lineno(), 'cop_ava:', cop_ava, 'cop_sui:', cop_sui)
            if cop_ava > len(gam_abc[rip1]):  # Avant c'était avec deg_ava
                cop_ava -= 7
                (lineno(), 'cop_ava:', cop_ava, 'deg_ava:', deg_ava)
            if cop_sui > len(gam_abc[rip1]):  # Huitième degré simplifié (gam_abc = 7 éléments)
                cop_sui -= 7
                (lineno(), 'cop_sui:', cop_sui, 'deg_sui:', deg_sui)
            (lineno(), 'GGC/****cop_ava:', cop_ava, 'cop_sui:', cop_sui)
            # not_ava et not_sui tirées de gam_abc
            not_ava, not_sui = gam_abc[rip0][cop_ava - 1], gam_abc[rip1][cop_sui - 1]
            (lineno(), 'GGC/****not_ava:', not_ava, 'not_sui:', not_sui, 'Notes à altérer')
            rip_app0, rip_app1, rng_maj = '§', '§', ''
            (lineno(), 'GGC/rip_app0:', rip_app0, 'rip_app1:', rip_app1, '\t\t********INTRODUCTION******')

            '''Niveau des extensions (8, 9, 10, 11, 12, 13, 14)'''
            if (int(deg_ava) in extension) or (int(deg_sui) in extension):  # Dernier degré numérique (8 et extensions)
                '''Définition des variables
                    dif_bas = Différence (demande/état) = Nouveau signe
                    deg_ba0(1). sig_ba0(1) = Signe altératif de not_bas(gam_abc) en extension
                    sig_nu0(1). sig_nu0(1) = Suivre num_ava(dic_inv[yes]) pour extension
                    à suivre = Les lignes à suivre num_ava(dic_inv[yes]) num_sui(dic_inv[yes + 1])
                    rng_ba0(1). rng_nu0(1) = Signes recueillis. Signes à suivre en extension'''
                (lineno(), '§')
                deg_bas, rng_bas, rng_nue, dif_bas, sig_mod = '', '', '', '', ''
                deg_nu0, deg_nu1, sig_nu0, sig_nu1, rng_nu0, rng_nu1 = '', '', '', '', '', ''
                qui_ava, qui_sui, qui_est = False, False, {}  # qui_est = Accumule(qui_ava/qui_sui)
                if int(deg_ava) in extension:
                    qui_ava = True
                    (lineno(), 'deg_ava:', deg_ava, 'qui_ava:', qui_ava, 'num_ava:', num_ava)
                if int(deg_sui) in extension:
                    qui_sui = True
                    (lineno(), 'deg_sui:', deg_sui, 'qui_sui:', qui_sui, 'num_sui:', num_sui)
                '''À l'avenir, il est probable que deux extensions soient en parallèle'''
                if qui_ava:  # Besoins = deg_bas, rng_bas, rng_nue
                    qui_est['ava'] = []
                    not_ba0 = gam_abc[rip0][int(deg_ava) - 8]  # not_ba0 = Référence gam_abc
                    deg_ba0, sig_ba0 = not_ba0[len(not_ba0) - 1:], not_ba0[:len(not_ba0) - 1]
                    rng_ba0 = alteration(sig_ba0)  # sig_ba0 = Issue gam_abc
                    for y in num_ava:  # Trier(signe/degré)
                        if y.isnumeric():
                            deg_nu0 += y
                        else:
                            sig_nu0 += y
                    rng_nu0 = alteration(sig_nu0)  # sig_nu0 = Issue num_ava
                    qui_est['ava'].append(deg_ba0)  # Donnée à transmettre (Note/degré) à moduler
                    qui_est['ava'].append(rng_ba0)  # Donnée à transmettre (index/rang) à moduler
                    qui_est['ava'].append(rng_nu0)  # Donnée à transmettre (index/rang) à suivre
                    (lineno(), 'rng_nu0:', rng_nu0, 'rng_ba0:', rng_ba0, 'deg_nu0:', deg_nu0, 'sig_nu0:', sig_nu0)
                    (lineno(), 'not_ba0:', not_ba0, 'gam_abc[rip1]:', gam_abc[rip1])
                if qui_sui:  # Besoins = deg_bas, rng_bas, rng_nue
                    qui_est['sui'] = []
                    not_ba1 = gam_abc[rip1][int(deg_sui) - 8]
                    deg_ba1, sig_ba1 = not_ba1[len(not_ba1) - 1:], not_ba1[:len(not_ba1) - 1]
                    rng_ba1 = alteration(sig_ba1)  # sig_ba1 = Issue gam_abc
                    for y in num_sui:  # Trier(signe/degré)
                        if y.isnumeric():
                            deg_nu1 += y
                        else:
                            sig_nu1 += y
                    rng_nu1 = alteration(sig_nu1)  # sig_nu1 = Issue num_sui
                    qui_est['sui'].append(deg_ba1)
                    qui_est['sui'].append(rng_ba1)
                    qui_est['sui'].append(rng_nu1)
                    (lineno(), 'SUI not_ba1:', not_ba1, 'deg_sui:', deg_sui)
                    (lineno(), 'rng_nu1:', rng_nu1, 'rng_ba1:', rng_ba1)
                    (lineno(), 'deg_nu1:', deg_nu1, 'sig_nu1:', sig_nu1)
                '''Transmission des paramètres (# Besoins = deg_bas, rng_bas, rng_nue)
                Sérier selon la demande pour l'offre la moins altéractivement chargée.'''
                dic_est = qui_est.keys()  # dic_est = Liste de dictionnaire
                for dic_key in dic_est:
                    est_lis = list(qui_est[dic_key])
                    deg_bas = est_lis[0]  # deg_bas = Note à altérer
                    rng_bas = est_lis[1]  # rng_bas = Signe à moduler
                    rng_nue = est_lis[2]  # rng_nue = Signe dictateur
                    (lineno(), 'dic_key:', dic_key)
                    # result0 = Ligne supérieure
                    # result1 = Ligne inférieure
                    (lineno(), 'deg_bas:', deg_bas, '\trng_bas:', rng_bas, '\trng_nue:', rng_nue)
                    '''Passage aux traitements des modulations, avec deux choix possibles(qui_ava/qui_sui)'''
                    if int(rng_nue) > -1:  # rng_nue = dic_inv est altération à appliquer sur rng_bas
                        if int(rng_bas) < 0:  # rng_bas = tab_inf
                            '''Analyser la disposition altérative'''
                            dif_bas = abs(int(rng_bas)) - abs(int(rng_nue))
                            # Si dif_bas est négatif, il y a besoin d'utiliser tab_sup
                            # Autrement, utiliser tab_inf
                            (lineno(), 'dif_bas:', dif_bas)
                            if dif_bas > -1:
                                sig_mod = tab_inf[dif_bas]
                            else:
                                sig_mod = tab_sup[abs(dif_bas)]
                            if dic_key == 'ava':
                                result0 = sig_mod + deg_bas
                            else:  # dic_key = 'sui'
                                result1 = sig_mod + deg_bas
                            (lineno(), 'dif_bas:', dif_bas, 'sig_mod:', sig_mod, '')
                            (lineno(), 'EX/ba2>-1ba1<0 result0:', result0, 'result1:', result1)
                        else:  # rng_bas = tab_sup
                            '''Tout va bien on peut continuer'''
                            dif_bas = abs(int(rng_bas)) + abs(int(rng_nue))
                            sig_mod = tab_sup[dif_bas]
                            if dic_key == 'ava':
                                result0 = sig_mod + deg_bas
                            else:  # dic_key = 'sui'
                                result1 = sig_mod + deg_bas
                            (lineno(), 'dif_bas:', dif_bas, 'sig_mod:', sig_mod, '')
                            (lineno(), 'EX/nue>-1_bas>-1 result0:', result0, 'result1:', result1)
                    elif int(rng_nue) < 0:  # rng_nue = dic_inv est altération à appliquer sur rng_bas
                        if int(rng_bas) < 0:  # rng_bas = tab_inf
                            '''Tout va bien on peut continuer'''
                            dif_bas = abs(int(rng_bas)) + abs(int(rng_nue))
                            sig_mod = tab_inf[dif_bas]
                            if dic_key == 'ava':
                                result0 = sig_mod + deg_bas
                            else:  # dic_key = 'sui'
                                result1 = sig_mod + deg_bas
                            (lineno(), 'dif_bas:', dif_bas, 'sig_mod:', sig_mod, '')
                            (lineno(), 'EX/nue<0_bas<0 result0:', result0, 'result1:', result1)
                        else:  # rng_bas = tab_sup
                            '''Analyser la disposition altérative'''
                            dif_bas = abs(int(rng_bas)) - abs(int(rng_nue))
                            if dif_bas > -1:
                                sig_mod = tab_sup[dif_bas]
                            else:
                                sig_mod = tab_inf[abs(dif_bas)]
                            if dic_key == 'ava':
                                result0 = sig_mod + deg_bas
                            else:  # dic_key = 'sui'
                                result1 = sig_mod + deg_bas
                            (lineno(), 'dif_bas:', dif_bas, 'sig_mod:', sig_mod, '')
                            (lineno(), 'EX/nue<0_bas>-1 result0:', result0, 'result1:', result1)
                    (lineno(), 'EX/deg_sui:', deg_sui, 'sig_sui:', sig_sui, 'dif_bas:', dif_bas)
                    (lineno(), 'EX/rng_bas:', rng_bas, 'rng_nue:', rng_nue)
                    (lineno(), 'EX/GGC/SUP result0:', result0, 'result1:', result1)
                    (lineno(), 'EX/GGC/SUP deg_ava:', deg_ava, 'sig_ava:', sig_ava, 'not_sup:', '\n')

            '''Ligne supérieure des degrés à suivre: dic_inv[yes][yi]'''
            if len(not_ava) > 1 and int(deg_ava) not in extension:  # not_ava = Note maj signée SUP à modifier
                not_maj = not_ava  # Note issue gam_abc
                deg_maj, sig_maj = not_maj[len(not_maj) - 1:], not_maj[:len(not_maj) - 1]
                rng_maj = alteration(sig_maj)  # rng_maj = Nombre réel((-+)(index))
                (lineno(), 'not:', not_maj, 'deg:', deg_maj, '\t\tsig:', sig_maj, 'rng:', rng_maj, 'rip0:', rip0)
                if int(rng_maj) >= 0:  # int(rng_maj) = Signe parmi les altérations augmentées
                    ind_not = gam_mod[rip0].index(not_maj)
                    res_not = yi - ind_not  # res_not = Intervalle (Rang réel moins Rang majeur)
                    ind_sup = tab_sup.index(sig_maj)  # Rang du signe parmi les augmentés
                    (lineno(), 'sig:', sig_maj, 'res_not:', res_not, 'ind:', ind_sup, 'ind_not:', ind_not)
                    if len(num_ava) == 1:
                        result0 = not_maj
                        (lineno(), 'num_ava:', num_ava)
                    elif res_not < 0:  # Demande une soustraction
                        if abs(res_not) > ind_sup:  # Demande supérieure à l'offre augmentée
                            dif_not = abs(res_not) - ind_sup  # Calcul différence à reporter
                            sig_not = tab_inf[dif_not]  # Initialiser l'altération
                            result0 = sig_not + deg_maj  # Construire la note finale
                            (lineno(), 'GGC/SUP result0:', result0, '*******tab_sup********')
                        else:
                            dif_not = abs(res_not) - ind_sup  # Calcul différence à reporter
                            sig_not = tab_sup[abs(dif_not)]  # Initialiser l'altération
                            result0 = sig_not + deg_maj  # Construire la note finale
                            (lineno(), 'SUP dif_not:', dif_not, 'sig_not:', sig_not, 'deg_maj:', deg_maj)
                        (lineno(), 'GGC/SUP result0:', result0, '')
                    else:  # Demande une addition
                        dif_not = abs(res_not) + ind_sup  # Calcul différence à reporter
                        sig_not = tab_sup[dif_not]  # Initialiser l'altération
                        result0 = sig_not + deg_maj  # Construire la note finale
                        (lineno(), 'dif_not:', dif_not, 'sig_not:', sig_not)
                        (lineno(), 'GGC/SUP result0:', result0, '*******tab_sup********')
                else:  # int(rng_maj) = Signe parmi les altérations diminuées
                    ind_not = gam_mod[rip0].index(not_maj)
                    ind_inf = tab_inf.index(sig_maj)  # Rang du signe parmi les diminués
                    res_not = yi - ind_not  # res_not = Intervalle (Rang réel moins Rang majeur)
                    (lineno(), 'res_not:', res_not, 'ind_inf:', ind_inf)
                    if len(num_ava) == 1:
                        result0 = not_maj
                        (lineno(), 'num_ava:', num_ava)
                    elif res_not > -1:  # Demande une soustraction
                        if abs(res_not) > ind_inf:  # Demande supérieure à offre diminuée
                            dif_not = abs(res_not) - ind_inf  # Calcul différence à reporter
                            sig_not = tab_sup[dif_not]  # Initialiser l'altération
                            result0 = sig_not + deg_maj  # Construire la note finale
                            (lineno(), 'GGC/SUP result0:', result0,)
                        else:
                            rng_ava = alteration(not_ava[:len(not_ava) - 1])
                            if abs(int(res_not)) == abs(int(rng_ava)):
                                result0 = deg_maj
                                (lineno(), 'GGC/SUP res_not:', res_not, 'rng_sui:', rng_sui)
                            elif res_not < ind_inf:
                                dif_not = ind_inf - abs(res_not)  # Calcul différence à reporter
                                sig_not = tab_inf[dif_not]  # Initialiser l'altération
                                result0 = sig_not + deg_maj  # Construire la note finale
                                (lineno(), 'GGC/SUP result0:', result0,)
                            else:  # Laisser cette condition active pour prévenir d'un autre cas AVA
                                print(lineno(), 'Autre cas AVA:', )
                            (lineno(), 'GGC/SUP ind_inf:', ind_inf,)
                    elif res_not < 0:  # Demande une addition
                        dif_not = abs(res_not) + ind_inf  # Calcul différence à reporter
                        sig_not = tab_inf[dif_not]  # Initialiser l'altération
                        result0 = sig_not + deg_maj  # Construire la note finale
                        (lineno(), 'GGC/SUP result0:', result0, '*******tab_sup********')
                    (lineno(), 'SUP res_not:', res_not, 'ind_not:', ind_not, 'rng_maj:', rng_maj)
            elif int(deg_ava) not in extension:  # not_ava = Note majeure non signée SUP à modifier
                result0 = sig_ava + not_ava
                (lineno(), 'sig_ava:', sig_ava, 'not_ava:', not_ava)
            rip_app0 = result0
            (lineno(), 'GGC/SUP rip_app0:', rip_app0)

            '''Ligne inférieure des degrés à suivre: dic_inv[yes + 1][yi]'''
            if len(not_sui) > 1 and int(deg_sui) not in extension:  # Degré inférieur signé
                not_maj = not_sui
                deg_maj, sig_maj = not_maj[len(not_maj) - 1:], not_maj[:len(not_maj) - 1]
                rng_maj = alteration(sig_maj)  # rng_maj = Nombre réel((-+)(index))
                (lineno(), 'not:', not_maj, 'deg:', deg_maj, '\t\tsig:', sig_maj, 'rng:', rng_maj, yi)
                if int(rng_maj) >= 0:  # Signe parmi les altérations augmentées
                    ind_not = gam_mod[rip1].index(not_maj)
                    res_not = yi - ind_not  # res_not = Intervalle (Rang réel moins Rang majeur)
                    ind_sup = tab_sup.index(sig_maj)  # Rang du signe parmi les augmentés
                    (lineno(), 'ind_not:', ind_not, 'res_not:', res_not, 'ind_sup:', ind_sup)
                    if len(num_sui) == 1:
                        result1 = not_maj
                        (lineno(), 'num_sui:', num_sui)
                    elif res_not < 0:  # Demande une soustraction
                        if abs(res_not) > ind_sup:  # Demande supérieure à l'offre augmentée
                            dif_not = abs(res_not) - ind_sup  # Calcul différence à reporter
                            sig_not = tab_inf[dif_not]  # Initialiser l'altération
                            result1 = sig_not + deg_maj  # Construire la note finale
                            (lineno(), 'GGC/INF result1:', result1, '*****************')
                        else:  # Voir dans tab_inf
                            dif_not = abs(res_not) - ind_sup  # Calcul différence à reporter
                            sig_not = tab_sup[abs(dif_not)]  # Initialiser l'altération
                            result1 = sig_not + deg_maj  # Construire la note finale
                            (lineno(), 'SUP dif_not:', dif_not, 'sig_not:', sig_not, 'deg_maj:', deg_maj)
                            (lineno(), 'GGC/SUP result1:', result1, '')
                        (lineno(), 'GGC/ res_not < 0:',)
                    else:  # Demande une addition
                        dif_not = abs(res_not) + ind_sup  # Calcul différence à reporter
                        sig_not = tab_sup[dif_not]  # Initialiser l'altération
                        result1 = sig_not + deg_maj  # Construire la note finale
                        (lineno(), 'dif_not:', dif_not, ':', sig_not)
                        (lineno(), 'GGC/SUP result1:', result1, '*******tab_sup********')
                else:  # Signe parmi les altérations diminuées
                    ind_not = gam_mod[rip1].index(not_maj)
                    ind_inf = tab_inf.index(sig_maj)  # Rang du signe parmi les diminués
                    res_not = yi - ind_not  # res_not = Intervalle (Rang réel moins Rang majeur)
                    (lineno(), 'res_not:', res_not, 'ind_inf:', ind_inf, 'result1:', result1)
                    if len(num_sui) == 1:
                        result1 = not_maj
                        (lineno(), 'num_sui:', num_sui)
                    elif res_not > -1:  # Demande une soustraction
                        if abs(res_not) > ind_inf:  # Demande supérieure à offre diminuée
                            dif_not = abs(res_not) - ind_inf  # Calcul différence à reporter
                            sig_not = tab_sup[dif_not]  # Initialiser l'altération
                            result1 = sig_not + deg_maj  # Construire la note finale
                            (lineno(), 'GGC/SUP result1:', result1)
                        else:  # res_not < ind_inf
                            rng_sui = alteration(not_sui[:len(not_sui) - 1])
                            if abs(int(res_not)) == abs(int(rng_sui)):
                                result1 = deg_maj
                                (lineno(), 'GGC/SUP res_not:', res_not, 'rng_sui:', rng_sui)
                            elif abs(res_not) < ind_inf:
                                dif_not = ind_inf - abs(res_not)  # Calcul différence à reporter
                                sig_not = tab_inf[dif_not]  # Initialiser l'altération
                                result1 = sig_not + deg_maj  # Construire la note finale
                                (lineno(), 'GGC/SUP result1:', result1)
                            else:  # Laisser cette condition active pour prévenir d'un autre cas SUI
                                (lineno(), 'Autre cas SUI:')
                    else:  # Demande une addition
                        dif_not = abs(res_not) + ind_inf  # Calcul différence à reporter
                        sig_not = tab_inf[dif_not]  # Initialiser l'altération
                        result1 = sig_not + deg_maj  # Construire la note finale
                        (lineno(), 'GGC/SUP result1:', result1, '*******tab_sup********')
                    (lineno(), 'SUP res_not:', res_not, 'ind_not:', ind_not, 'rng_maj:', rng_maj, yi)
            elif int(deg_sui) not in extension:  # not_sui = Note majeure non signée INF à modifier
                result1 = sig_sui + not_sui
                (lineno(), "sig_sui:", sig_sui, 'not_sui:', not_sui)
            rip_app1 = result1
            (lineno(), 'GGC/SUP result1:', result1, '*******tab_sup********')
            if yes in dic_rip0.keys():
                dic_rip0[yes].append(rip_app0)
                dic_rip1[yes].append(rip_app1)
            elif yes in dic_rip2.keys():
                dic_rip2[yes].append(rip_app0)
                dic_rip3[yes].append(rip_app1)
            (lineno(), 'GGC/rip_app0:', rip_app0, '\t\t', rip_app1, ':rip_app1 ********************* yes:', yes)
            '''Maintenant, les notes diatoniques ont cessé d'être produites. Sans interférer dic_maj[]'''
            #
            # Séquence d'affichage pour d'éventuelles corrections
            # Ci-dessous. Déploiement diatonique analogique guidé par la formule numérique.
            if yi == 12:  # Normalement(yi == 11). Et yi = 12 est improbable.
                print(lineno(), '***** Résultat progressif par cycle ***** yi:', yi, '****** yes:', yes)
                print(lineno(), 'GGC/dic_inv[yes][yi]:\t', yes, dic_inv[yes][:yi + 1], '*yi:', yi)
                if yes in dic_rip0.keys():
                    print(lineno(), 'GGC/dic_rip0[yes]:\t\t', yes, dic_rip0[yes])
                    print(lineno(), 'GGC/dic_rip1[yes]:\t\t', yes, dic_rip1[yes])
                elif yes in dic_rip2.keys():
                    print(lineno(), 'GGC/dic_rip2[yes]:\t\t', yes, dic_rip2[yes])
                    print(lineno(), 'GGC/dic_rip3[yes]:\t\t', yes, dic_rip3[yes])
                if yes != 13:  # Lecture totale limitée à 12 (yes)
                    print(lineno(), 'GGC/dic_inv[yes+1][yi]:\t', yes, dic_inv[yes + 1][:yi + 1], '*yi:', yi)
                print(lineno(), '___________________________________________Fin de cycle yi:', yi)
            if yes == 12 and yi == 12:  # Lecture totale limitée à 12/12 (yes)/(yi)
                break
        if yes == 12:  # Lecture totale limitée à 12 (yes)
            break
        # Ci-dessus.
        # Séquence d'affichage pour d'éventuelles corrections
        #
    '''Tous les dic_rip's ont été initialisés selon la dictée numérique.
    Maintenant on passe à l'épisodique récupération des diatoniques commatiques:
    .   Suivre les colonnes une par une en commençant par la tonique la plus rapprochée de celle de la 1ère colonne.
    .   Une fois sélectionnée, la tonique se construit avec les notes de sa propre colonne.
    En ce moment le traçage récolte(la tonique, le nom de la gamme, la graduation)'''
    (lineno(), 'GGC/dic_maj.keys\n', dic_maj.keys(), 'len(dic_maj.keys()):', len(dic_maj.keys()))
    # Lecture de chaque colonne des dic_rip's pour trouver la tonique fondamentale
    tripe0, tripe1 = {1: ''}, {1: ''}  # Pour les notes de la gamme originale
    tripe2, tripe3 = {2: ''}, {2: ''}  # Pour les notes chromatiques parallèles
    if 1 in dic_rip0.keys():  # ton_un est inchangé
        ton_un = dic_rip0[1][0]
    else:  # ton_un change, car il a deux notes toniques.
        ton_un = dic_rip2[1][0], dic_rip3[1][0]
    (lineno(), 'ton_un:', ton_un, type(ton_un), dic_maj.keys(), 'len dic_maj:', len(dic_maj.keys()), '\n')
    val_rip = list(dic_inv.keys())
    (lineno(), 'val_rip:', val_rip)
    '''737 val_rip: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]'''
    dic_cas, dic_abs, maj = {}, {}, []  # dic_cas(gam0, 'casX', cas0 ou 2, key, clef) dic_abs(absences)
    for clef in range(12):
        cas3 = 0
        if not dic_cas:
            (lineno(), gam0, gam1)
            dic_cas[gam0, 'cas0'] = []  # dic_cas[tonique, cas]
            dic_cas[gam0, 'cas2'] = []
        for key in val_rip[:12]:
            cas3 += 1
            if key in dic_rip0.keys():
                cas0 = dic_rip0[key][clef], dic_rip1[key][clef]
                (lineno(), 'key:', key, 'cas0:', cas0, 'clef:', clef, 'gam0:', gam0)
                if gam0 in cas0:
                    ckc = cas0, (key, clef)  # ckc((notes(couple), (clé, verticale))
                    dic_cas[gam0, 'cas0'].append(ckc)
                    if cas0[0] not in dic_maj and cas0[0] not in maj:
                        maj.append(cas0[0])
                        tripe0[1] = cas0[0]
                        (lineno(), '____ cas0[0]:', cas0[0], 'tripe0:', tripe0[1], 'cas0:', cas0)
                    if cas0[1] not in dic_maj and cas0[1] not in maj:
                        maj.append(cas0[1])
                        tripe1[1] = cas0[1]
                        (lineno(), '____ cas0[1]:', cas0[1], 'tripe1:', tripe1[1], 'cas0:', cas0)
                    (lineno(), 'cas0:', cas0, 'ckc:', ckc, 'gam0:', gam0)
                    break
                (lineno(), 'dic_rip1:', key, dic_rip1[key][clef], clef)
            elif key in dic_rip2.keys():
                (lineno(), 'key:', key, 'clef:', clef, 'dic_rip2[key]:', dic_rip2[key])
                cas2 = dic_rip2[key][clef], dic_rip3[key][clef]
                (lineno(), 'key:', key, 'cas2:', cas2, 'clef:', clef)
                if gam0 in cas2:
                    ckc = cas2, (key, clef)
                    dic_cas[gam0, 'cas2'].append(ckc)
                    if cas2[0] not in dic_maj and cas2[0] not in maj:
                        maj.append(cas2[0])
                        tripe2[2] = cas2[0]
                        (lineno(), '**** cas2[0]:', cas2[0], 'tripe2:', tripe2[2], 'cas2:', cas2)
                    if cas2[1] not in dic_maj and cas2[1] not in maj:
                        maj.append(cas2[1])
                        tripe3[2] = cas2[1]
                        (lineno(), '**** cas2[1]:', cas2[1], 'tripe3:', tripe3[2], 'cas2:', cas2)
                    (lineno(), 'cas2:', cas2, 'ckc:', ckc, 'gam0:', gam0)
                    break
            if cas3 > 11 and key != 12:
                dic_abs[key, clef] = []
                ('. absences ', lineno(), 'Cas3 absences dic_abs[key]:', dic_abs.keys())
    (lineno(), 'Transposer ', tripe0, tripe1, tripe2, tripe3)
    transposer(tripe0, tripe1, tripe2, tripe3)
    '''Recueil des toniques présentes : gam0 = Tonalité principale parmi les toniques'''
    # Lecture des colonnes absentes pour trouver les toniques fondamentales
    (lineno(), 'Cas3 ABSENCES dic_abs:', dic_abs)
    '''790 Cas3 ABSENCES dic_abs: {}'''  # Toujours pas d'absence ?!
    for cas_duc in dic_abs.keys():
        print(lineno(), 'GGC/ton_un:', ton_un, '\n', dic_maj[ton_un])
        ('___ ___ ___ ___ ___ ___ ___ ;', lineno(), 'Cas3 cas_duc:', cas_duc[1])
        len_sos1 = len_sos2 = 0
        but = False
        # Définir les notes hautes et basses de gam0[0]
        axe = ici = 0
        sur_cas, bas_cas, cas_cas = [], [], []
        (lineno(), 'ton_un:', ton_un, 'ici:', ici)
        #
        while not but:
            ici += 1
            axe -= 1
            if ici == 12:
                ici = 0
            if axe == -1:
                axe = 11
            if dic_maj[ton_un][ici]:  # ic_cas = Cas à diminuer
                ic_cas = dic_maj[ton_un][ici]
                ic_deg, ic_sig = ic_cas[len(ic_cas) - 1:], ic_cas[:len(ic_cas) - 1]
                ic_rng = int(alteration(ic_sig))  # Rang de l'altération
                # Mise à niveau tonique des degrés(Cas à diminuer)
                if ic_rng < 0:  # 'diminuer un diminué'
                    (lineno(), 'ic_rng:', ic_rng, 'diminuer un diminué ici:', ici)
                    id_cas = abs(ic_rng) + ici
                    no_cas = tab_inf[id_cas] + ic_deg
                    if no_cas not in cas_cas:
                        cas_cas.append(no_cas)
                        (lineno(), 'cas_cas:', cas_cas)
                else:  # 'diminuer un augmenté'
                    (lineno(), 'ic_rng:', ic_rng, 'diminuer un augmenté ici:', ici)
                    if ic_rng - ici > 0:
                        id_cas = ic_rng - ici
                        no_cas = tab_sup[id_cas] + ic_deg
                        if no_cas not in cas_cas:
                            cas_cas.append(no_cas)
                            (lineno(), 'id_cas:', id_cas, 'ici:', ici, 'no_cas:', no_cas)
                    else:  # La différence est inférieure à zéro
                        id_cas = ici - ic_rng
                        no_cas = tab_inf[id_cas] + ic_deg
                        if no_cas not in cas_cas:
                            cas_cas.append(no_cas)
                            (lineno(), 'id_cas:', id_cas, 'ici:', ici, 'no_cas:', no_cas)
                    (lineno(), 'ici:', ici, 'ic_rng:', ic_rng)
                ic = dic_maj[ton_un][ici], ici
                sur_cas.append(ic)  # sur_cas = Couple (note/index) de la partie supérieure
                (lineno(), 'ic:', ic, ':', ic_deg, ic_sig, 'cas_cas:', cas_cas)
            if dic_maj[ton_un][axe]:  # ax_cas = Cas à augmenter
                ax_cas = dic_maj[ton_un][axe]
                ax_deg, ax_sig = ax_cas[len(ax_cas)-1:], ax_cas[:len(ax_cas)-1]
                ax_rng = int(alteration(ax_sig))
                # Mise à niveau tonique des degrés(Cas à augmenter)
                if ax_rng > -1:  # 'augmenter un augmenté'
                    (lineno(), 'ax_rng:', ax_rng, 'augmenter un augmenté axe:', axe)
                    if axe == 11:  # ax=11 = Emplacement 7ème majeure
                        no_cas = tab_sup[ax_rng + 1] + ax_deg
                        if no_cas not in cas_cas:
                            cas_cas.append(no_cas)
                            (lineno(), 'id_cas:', 'no_cas:', no_cas)
                    else:  # autre cas que 11
                        id_cas = (12 - axe) + ax_rng
                        no_cas = tab_sup[id_cas] + ax_deg
                        if no_cas not in cas_cas:
                            cas_cas.append(no_cas)
                            (lineno(), 'id_cas:', id_cas, 'axe:', axe)
                else:  # 'augmenter un diminué'
                    (lineno(), 'ax_rng:', ax_rng, 'augmenter un diminué axe:', axe)
                    if axe == 11:  # ax=11 = Emplacement 7ème majeure
                        id_cas = abs(ax_rng) - 1
                        no_cas = tab_inf[id_cas] + ax_deg
                        if no_cas not in cas_cas:
                            cas_cas.append(no_cas)
                            (lineno(), 'ax=11', cas_cas[0])
                    else:  # autre cas que 11
                        if abs(ax_rng) - (12 - axe) > 0:
                            id_cas = abs(ax_rng) - (12 - axe)
                            no_cas = tab_inf[id_cas] + ax_deg
                            if no_cas not in cas_cas:
                                cas_cas.append(no_cas)
                                (lineno(), 'id_cas:', id_cas, 'axe:', axe, 'no_cas:', no_cas)
                        else:  # La différence est inférieure à zéro
                            id_cas = (12 - axe) + ax_rng
                            no_cas = tab_sup[id_cas] + ax_deg
                            if no_cas not in cas_cas:
                                cas_cas.append(no_cas)
                                (lineno(), 'id_cas:', id_cas, 'axe:', axe, 'no_cas:', no_cas)
                ax = dic_maj[ton_un][axe], axe
                bas_cas.append(ax)  # bas_cas = Couple (note/index) de la partie inférieure
                (lineno(), 'ax:', ax, 'ax_deg:', ax_deg, 'ax_sig:', ax_sig, 'cas_cas:', cas_cas)
            if len(sur_cas) == len(bas_cas) == 12:
                but = True
                (lineno(), '(sur_cas):', len(sur_cas), '(bas_cas):', len(bas_cas), 'cas_duc[1]:', cas_duc[1])
                ('§', cas_duc[1], lineno())

        # Enregistrement des toniques absentes dans dic_cas et dans dic_maj, en passant par la fonction transposer()
        # def transposer(rip0, rip1, rip2, rip3):
        ('===== == ======', lineno(), 'cas_cas:', cas_cas)
        ('== == ==', lineno(), 'cas_cas:', dic_cas)
        # 804 cas_cas: ['+B', 'oD', '^A', '-*E', 'o*F', 'x^G', '-**G', '+^^F', 'x^^E', '***A', '+^^^D',
        # 'o***B', 'C', '^^^^C'] Exemple
        '''# cas_cas = Liste les notes diatoniques altérées jusqu'en position tonique'''
        (lineno(), 'dic_maj.keys():', dic_maj.keys())
        ''' tripe0 = tripe1 = {1: []}, {1: []}  # Pour les notes de la gamme originale(et plus)
            tripe2 = tripe3 = {2: []}, {2: []}  # Pour les notes chromatiques parallèles'''
        for key in range(1, 14):
            len_sos1, len_sos2 = len(dic_cas[gam0, 'cas0']), len(dic_cas[gam0, 'cas2'])
            if key in dic_rip0.keys():
                cas_sos = dic_rip0[key][cas_duc[1]], dic_rip1[key][cas_duc[1]], 'cas0'
                (lineno(), 'cas_sos:', cas_sos, 'key:', key, '...... Key in dic_rip0.keys()')
                for sos in range(2):
                    if cas_sos[sos] in cas_cas:
                        (lineno(), 'SOS:', sos, cas_sos[sos], 'dic_maj.keys():', dic_maj.keys())
                        ckc = cas_sos[:2], (key, cas_duc[1])
                        dic_cas[gam0, cas_sos[2]].append(ckc)
                        if cas_sos[0] not in dic_maj.keys():
                            tripe0[1] = cas_sos[0]
                            ('trip', lineno(), 'tripe0:', tripe0, 'cas_sos[0]:', cas_sos[0])
                        if cas_sos[1] not in dic_maj.keys():
                            tripe1[1] = cas_sos[1]
                            ('trip', lineno(), 'tripe1:', tripe1, 'cas_sos[1]:', cas_sos[1])
                        ('TRIP', lineno(), 'tripe0:', tripe0, 'tripe1:', tripe1)
                        (lineno(), 'sos:', dic_cas[gam0, cas_sos[2]], '\tkey:', key)
                        #
                (lineno(), 'cas_sos 0:', cas_sos, 'key:', key, 'cas_duc[1]:', cas_duc[1])
                (lineno(), 'dic_cas 0:', dic_cas[gam0, 'cas0'][0])
            else:
                cas_sos = dic_rip2[key][cas_duc[1]], dic_rip3[key][cas_duc[1]], 'cas2'
                (lineno(), 'cas_sos:', cas_sos, 'key:', key, '...... Key in dic_rip2.keys()')
                for sos in range(2):
                    if cas_sos[sos] in cas_cas:
                        (lineno(), 'SOS:', sos, cas_sos[sos], 'dic_maj.keys():', dic_maj.keys())
                        ckc = cas_sos[:2], (key, cas_duc[1])
                        dic_cas[gam0, cas_sos[2]].append(ckc)
                        if cas_sos[0] not in dic_maj.keys():
                            tripe2[2] = cas_sos[0]
                            ('TRIP', lineno(), 'tripe2:', tripe2)
                        if cas_sos[1] not in dic_maj.keys():
                            tripe3[2] = cas_sos[1]
                            ('TRIP', lineno(), 'tripe3:', tripe3)
                        ('TRIP', lineno(), 'tripe2:', tripe2, 'tripe3:', tripe3)
                        (lineno(), 'sos:', dic_cas[gam0, cas_sos[2]], '\tkey:', key, 'SOS:', sos)
                        #
                (lineno(), 'cas_sos 2:', cas_sos, 'key:', key, 'cas_duc[1]:', cas_duc[1])
                (lineno(), 'dic_cas 2:', dic_cas[gam0, 'cas2'])
            deg_cas, sig_cas = cas_sos[0][len(cas_sos[0])-1:], cas_sos[0][:len(cas_sos[0])-1]
            (lineno(), 'deg_cas:', deg_cas, 'sig_cas:', sig_cas)
        # Appel de fonction transposer avec passage de paramètres sans retour
        ('......Transposer trip', lineno(), '___ ___ Suite rip:', tripe0, tripe1, tripe2, tripe3)
        transposer(tripe0, tripe1, tripe2, tripe3)
        (lineno(), 'dic_cas:', dic_cas[gam0, 'cas0'], '\n :', dic_cas[gam0, 'cas2'])
        ('** ', lineno(), '** ** ** len_sos:', len_sos1, 'len_sos2:', len_sos2)
    #
    (lineno(), 'dic_cas:', dic_cas[gam0, 'cas0'], '\n', dic_cas[gam0, 'cas2'])
    (lineno(), 'dic_maj.keys():', dic_maj.keys(), 'len:', len(dic_maj.keys()))
    #
    '''Les clefs changent en fonction de chaque gamme originale.'''
    (lineno(), 'dic_cas:', dic_cas.keys())
    for dc in dic_cas.keys():
        for vc in dic_cas[dc]:
            aug_key = vc[1][0]  # La clef tonique (rapport dic_rip2.3[clef])
            aug_hau = vc[1][1]  # Position tonique (rapport dic_rip2.3[clef][position])
            aug_rng, aug_lop = 0, -1  # aug_rng = Incrémente la clef
            dic_rapt[aug_hau] = [[aug_key, aug_hau]]
            dic_rap0[aug_hau] = [[aug_key, aug_hau]]
            dic_rap2[aug_hau] = [[aug_key, aug_hau]]
            (lineno(), 'vc:', vc, '\t\trangeur_aug_key:', aug_key, 'hauteur_aug_hau:', aug_hau)
            (lineno(), 'dic_rap0:', dic_rap0, '\ndic_rap2:', dic_rap2)
            (lineno(), 'dic_rap0:', dic_rap0.keys(), '\ndic_rap2:', dic_rap2.keys())
            while aug_lop < 11:
                aug_lop += 1
                if aug_key in dic_rip0:
                    note0, note1 = dic_rip0[aug_key][aug_hau], dic_rip1[aug_key][aug_hau]
                    dic_rapt[aug_hau].append((note0, note1))
                    dic_rap0[aug_hau].append(note0)
                    dic_rap2[aug_hau].append(note1)
                    (lineno(), 'dic_rip0.1:\t', note0, note1)
                elif aug_key in dic_rip2:
                    note2, note3 = dic_rip2[aug_key][aug_hau], dic_rip3[aug_key][aug_hau]
                    dic_rapt[aug_hau].append((note2, note3))
                    dic_rap0[aug_hau].append(note2)
                    dic_rap2[aug_hau].append(note3)
                    (lineno(), 'dic_rip2.3:\t', note2, note3)
                aug_key += 1
                if aug_key == 13:
                    (lineno(), 'aug_key:', aug_key)
                    aug_key = 1
                (lineno(), 'aug_lop:', aug_lop, 'aug_key:', aug_key)
            (lineno(), 'vc:', vc, '\t\trangeur:', aug_key, 'hauteur:', aug_hau)
        (lineno(), 'dc:', dc, 'dic_cas[dc]:', dic_cas[dc])

    ''' Ici, nous connaissons les gammes commatiques qui sont impliquées au commatisme.
        Nous utilisons un dictionnaire modulaire des situations isolées ou couplées.
        Quand une note est isolée c'est qu'elle n'a pas de parallélisme chromatique.
        Par définition la note isolée est intégrée à la gamme diatonique, hors contexte chromatique.'''
    (lineno(), 'GGC/ton_un:', ton_un, '\ndic_maj', dic_maj.keys(), 'len(dic_maj.keys()):', len(dic_maj.keys()))

    # , dic_rap0, dic_rap2 = Modules de transport diatonique, des lignes supérieures et inférieures.
    # cap0[num_sup], cap1[not_sup], cap2[not_inf], cap3[num_inf]
    # dic_cap0, dic_cap1, dic_cap2, dic_cap3
    (lineno(), 'b_diatonic[0]:', b_diatonic[0], '= Le nom de la gamme fondamentale; exemple[C Maj]')
    for ik in dic_rap0.keys():
        # Initialiser la nouvelle clef du dictionnaire.
        dic_cap0[ik], dic_cap1[ik], dic_cap2[ik], dic_cap3[ik] = [], [], [], []
        dic_com[str(b_diatonic[0]), ik] = []  # dic_com = Encadrement : (dic_cap0, dic_cap1, dic_cap2, dic_cap3)
        (lineno(), 'b_diatonic[0]:', b_diatonic[0], ' = Le nom de la gamme fondamentale; exemple[C Maj]')
        not_iso0, not_iso1, not_iso2, not_gam, nom_gam = '', '', '',  [], ''
        '''# Compare, il n'y a pas de couplage chromatique?'''
        if dic_rap0[ik][1] == dic_rap2[ik][1]:  # Les notes (sup/inf) sont identiques.
            not_iso0 = dic_rap2[ik][1]  # not_iso0.1.2 = Notes toniques de la gamme (dic_maj[not_iso]).
            (lineno(), 'not_iso0:', not_iso0)
            gam_vol0 = dic_maj[not_iso0][0]  # gam_vol0 = Clé de la gamme majeure[dans dic_maj[]]
            gam_vol1 = dic_maj[not_iso0][0]  # gam_vol1 = Clé de la gamme majeure[dans dic_maj[]]
            (lineno(), 'gam_vol0:', gam_vol0, ':&1:', gam_vol1, '\t.\t\tPartie isolée.')
        else:  # Les notes (sup/inf) sont différentes.
            not_iso1, not_iso2 = dic_rap0[ik][1], dic_rap2[ik][1]  # Formation en couple.
            (lineno(), 'not_iso1.2:', not_iso1, not_iso2, 'ton_un:', ton_un)
            gam_vol0, gam_vol1 = dic_maj[not_iso1][0], dic_maj[not_iso2][0]
            (lineno(), 'not_iso1.2:', not_iso1, not_iso2, dic_maj.keys())
            (lineno(), 'gam_vol0:', gam_vol0, ':&1:', gam_vol1, '\t.\tPartie couplée.')
        '''Sortie des mises en forme des relatives majeures. ²La tonique fait la tonalité²
            En référencement aux tableaux des tonalités majeures[(bas, haut), (not_iso0, not_iso1, not_iso2)]
        Zone détaillant les notes[Signe, note, tonique, degré, tonalité]
            Formatage = alteration (Signe) + Tables (dic_maj[Notes. Intervalles], gam_abc[Notes])'''
        # Traitement de l'altération et de la note majeure.
        deg_maj0, deg_maj1 = gam_vol0[len(gam_vol0)-1:], gam_vol1[len(gam_vol1)-1:]  # Note absolue (naturelle)
        sig_maj0, sig_maj1 = gam_vol0[:len(gam_vol0)-1], gam_vol1[:len(gam_vol1)-1]  # Signe d'altération[b#]
        rng_maj0, rng_maj1 = alteration(sig_maj0), alteration(sig_maj1)
        # Construire les séquences des degrés absolus pour un accès rapide
        deg_abc0, deg_abc1 = [], []  # deg_abc0.1 = Adaptations des tonalités naturelles.
        for jin in gam_abc[gam_vol0]:
            deg_abc0.append(jin[len(jin)-1:])
        for jin in gam_abc[gam_vol1]:
            deg_abc1.append(jin[len(jin)-1:])
        (lineno(), 'dic_maj[.]:', dic_maj[gam_vol0], '\n \t \t : &1: ', dic_maj[gam_vol1], 'Index majeur')
        (lineno(), 'gam_abc[gam_vol0]:', gam_abc[gam_vol0], '&1:', gam_abc[gam_vol1])
        (lineno(), 'deg_abc0:', deg_abc0, 'deg_abc1:', deg_abc1)
        (lineno(), '___\trng_maj0 deg_maj0:', rng_maj0, deg_maj0, '\trng_maj1 deg_maj1:', rng_maj1, deg_maj1)
        (lineno(), '1er TOUR | GAMMES ENREGISTRÉES (dic_maj[gam_vol0], dic_maj[gam_vol1])')
        #
        #
        '''# Exécution du traitement diatonique (num + note).
            Le premier cycle a donné les principales valeurs diatoniques.
            Le développement diatonique modal de la gamme commatique énoncée.
                De sa position chromatique réelle, ou son emplacement diatonique.'''
        (lineno(), 'dic_cap0:', dic_cap0)
        for dia in range(1, 13):  # VERSIONS NUMÉRIQUES DES DEGRÉS MODAUX
            # dic_cap0[ik], dic_cap3[ik] = Parties numériques[inf/sup].
            # dic_cap1[ik], dic_cap2[ik] = Parties analogiques[inf/sup].
            '''# Compare s'il n'y a pas de couplage chromatique.'''
            (lineno(), 'dic_rap0:', dic_rap0, '\n\ndic_rap2:', dic_rap2, 'ik:', ik, 'dia:', dia)
            if dic_rap0[ik][dia] == dic_rap2[ik][dia]:  # Les notes (sup/inf) sont identiques.
                dic_cap1[ik].append(dic_rap2[ik][dia])  # not_iso = Note tonique de la gamme (dic_maj[not_iso])
                dic_cap2[ik].append(dic_rap2[ik][dia])  # not_iso = Note tonique de la gamme (dic_maj[not_iso])
                nom_gam += dic_rap2[ik][dia]  # Composition du nom en mode hors liste.
                not_gam.append(dic_rap2[ik][dia])  # not_gam = Note tonique de la gamme
                (lineno(), 'nom_gam:', nom_gam, '\t.\t Partie isolée.', 'dia:', dia)
            else:  # Les notes (sup/inf) sont différentes.
                dic_cap1[ik].append(dic_rap0[ik][dia])
                dic_cap2[ik].append(dic_rap2[ik][dia])
                (lineno(), 'nom_gam:', nom_gam, '\t..\t Partie couplée.', 'dia:', dia)
            (lineno(), 'dic_cap1[ik][dia-1]:', dic_cap1[ik][dia-1])
            (lineno(), 'dic_cap2[ik][dia-1]:', dic_cap2[ik][dia-1])
            '''Sortie de l'enregistrement des notes commatiques[dic_cap1.2[ik]]
            # Traitement des notes analogiques aux valeurs numériques.'''
            # Définition[note, degré, signe, valeur numérique de l'altération]
            not_com1, not_com2 = dic_rap0[ik][dia], dic_rap2[ik][dia]  # not_com1.2 = Notes (supérieure, inférieure)
            deg_com1, deg_com2 = not_com1[len(not_com1)-1:], not_com2[len(not_com2)-1:]  # deg_com1.2 = Note absolue
            ''' PARTIE DU CODE INUTILISÉ POUR L'INSTANT
            # sig_com1, sig_com2 = not_com1[:len(not_com1)-1], not_com2[:len(not_com2)-1]  # sig_com1.2 = Altérés[b#]
            # rng_com1, rng_com2 = alteration(sig_com1), alteration(sig_com2)  # rng_com1.2 = Altérations[±]
            # (lineno(), ' rng_com1 deg_com1:', rng_com1, deg_com1, ' rng_com2 deg_com2:', rng_com2, deg_com2)'''
            #
            '''# Indexation des notes commatiques aux positions réelles et majeures:
                Vrai = La note commatique énoncée supérieure.       Ou not_com1 de dic_rap0.
                Et, mage = La note commatique énoncée inférieure.   Ou not_com2 de dic_rap2.
                La note énoncée est relocalisée dans le dictionnaire des gammes majeures,
                sa nouvelle localisation donne la référence du même degré majeur.'''
            #   # deg_abc0.1 = Adaptations des tonalités naturelles.
            niv_vrai, niv_mage = deg_abc0.index(deg_com1), deg_abc1.index(deg_com2)  # Index gam_abc aussi
            (lineno(), 'niv_vrai:', niv_vrai+1, 'niv_mage:', niv_mage+1, '\t Numéroter les degrés deg_abc0')
            abc_vrai = gam_abc[gam_vol0][niv_vrai]  # abc_vrai = La note majeure altérative supérieure
            abc_mage = gam_abc[gam_vol1][niv_mage]  # abc_mage = La note majeure altérative inférieure
            ind_vrai = dic_maj[gam_vol0].index(abc_vrai)  # ind_vrai = Index dic_maj supérieur
            ind_mage = dic_maj[gam_vol1].index(abc_mage)  # ind_mage = Index dic_maj inférieur
            (lineno(), 'ind_vrai:', ind_vrai, 'ind_mage:', ind_mage, '\t Calcul position majeure dic_maj[.]')
            '''PARTIE DU CODE INUTILISÉ POUR L'INSTANT
            # dic_vrai = dic_maj[gam_vol0][ind_vrai]  # dic_vrai = La note majeure supérieure
            # dic_mage = dic_maj[gam_vol1][ind_mage]  # dic_mage = La note majeure inférieure
            # (lineno(), 'dic_vrai:', dic_vrai, 'dic_mage:', dic_mage, 'Notes majeures correspondantes[not_com1.2]')
            # deg_vrai, deg_mage = dic_vrai[len(dic_vrai)-1:], dic_mage[len(dic_mage)-1:]  # deg_vrai = Majeure absolue
            # sig_vrai, sig_mage = dic_vrai[:len(dic_vrai)-1], dic_mage[:len(dic_mage)-1]  # sig_vrai = Signe relatif
            # rng_vrai, rng_mage = alteration(sig_vrai), alteration(sig_mage)
            # (lineno(), 'rng_vrai :', rng_vrai, deg_vrai, 'rng_mage :', rng_mage, deg_mage)'''
            (lineno(), 'dia:', dia-1, '\t \t \t \t \t \t Position note commatique')
            '''Le niveau de l'altération majeure est une référence,
                aussi que sa position donne l'intervalle en rigueur.
                La position du comma énoncé est primordiale de part le rapport majeur.
                    Soustraire la position comma à la position majeure fait le résultat.
                        Comma local[dia-1]. Majeur local[ind_vrai, ind_mage]
                Le signe énoncé du comma est invariable.
                Le degré énoncé du comma donne sa localisation.'''

            #   Partie supérieure : Le dessus numérique'''
            ide_vrai, num_vrai = '', str(niv_vrai + 1)  # num_vrai = Numéro du degré
            dif_vrai = (dia - 1) - ind_vrai  # dia-1 = Position chromatique
            (lineno(), 'num_vrai:', num_vrai, 'dif_vrai:', dif_vrai, '\t\tPartie supérieure.\tDia:', dia)
            if abs(dif_vrai) > 6:
                if dif_vrai < 0:  # dif_vrai = Altération dans tab_inf
                    dif_dif = 12 - abs(dif_vrai)
                    tab_dif = tab_sup[dif_dif]
                    not_dif = int(num_vrai) + 7
                    ('***', lineno(), 'dif_vrai:', dif_vrai, 'num_vrai:', num_vrai)
                else:  # dif_vrai= Altération dans tab_sup
                    dif_dif = 12 - abs(dif_vrai)
                    tab_dif = tab_inf[dif_dif]
                    not_dif = int(num_vrai) + 7
                    ('***', lineno(), 'dif_vrai:', dif_vrai, 'num_vrai:', num_vrai)
                not_vrai = tab_dif + str(not_dif)
                ('**', lineno(), 'not_vrai:', not_vrai, '. if abs(dif_vrai) > 6:', 'num_vrai:', num_vrai)
            elif dif_vrai > -1:
                ide_vrai = tab_sup[dif_vrai]
                not_vrai = ide_vrai + num_vrai
            else:
                ide_vrai = tab_inf[abs(dif_vrai)]
                not_vrai = ide_vrai + num_vrai
            dic_cap0[ik].append(not_vrai)
            (lineno(), 'num_vrai:', num_vrai, 'dia-1:', dia - 1, 'ind_vrai:', ind_vrai)
            (lineno(), 'FINAL *** *** * not_vrai:', not_vrai, ide_vrai, '\t\tPartie supérieure.\tDia:', dia)

            #   Partie inférieure : Le dessous numérique'''
            ide_mage, num_mage = '', str(niv_mage + 1)  # num_mage = Numéro du degré
            dif_mage = (dia - 1) - ind_mage  # dia-1 = Position chromatique
            (lineno(), 'num_mage:', num_mage, 'dif_mage:', dif_mage, '\t\tPartie inférieure.\tDia:', dia)
            if abs(dif_mage) > 6:
                if dif_mage < 0:  # dif_mage = Altération dans tab_inf
                    dif_dif = 12 - abs(dif_mage)
                    tab_dif = tab_sup[dif_dif]
                    not_dif = int(num_mage) + 7
                    ('***', lineno(), 'dif_mage:', dif_mage, 'num_mage:', num_mage)
                else:  # dif_mage = Altération dans tab_sup
                    dif_dif = 12 - abs(dif_mage)
                    tab_dif = tab_inf[dif_dif]
                    not_dif = int(num_mage) + 7
                    ('***', lineno(), 'dif_mage:', dif_mage, 'num_mage:', num_mage)
                not_mage = tab_dif + str(not_dif)
                ('**', lineno(), 'not_mage:', not_mage, '. if abs(dif_mage) > 6:', 'num_mage:', num_mage)
            elif dif_mage > -1:
                ide_mage = tab_sup[dif_mage]
                not_mage = ide_mage + num_mage
                ('*', lineno(), 'not_mage:', not_mage, 'elif dif_mage > -1:', dif_mage)
            else:
                ide_mage = tab_inf[abs(dif_mage)]
                not_mage = ide_mage + num_mage
                ('*', lineno(), 'not_mage:', not_mage)
            dic_cap3[ik].append(not_mage)
            (lineno(), 'FINAL not_mage:', not_mage, """'dia-1:', dia - 1, 'ind_mage:', ind_mage""")
            (lineno(), '*** *** * not_com2:', not_com2, '\t.\tPartie inférieure.\tDia:', dia)

            if dia == 12:
                ok_print = 0  # ok_print = 1 Mise en route des print's
                # La production des résultantes numériques.
                if ok_print:
                    print(lineno(), 'INDES\t\tnom:', b_diatonic[0], '\tgrade:', graduation)
                    print(lineno(), 'ik:', ik, 'dic_cap0[clé]:', dic_cap0[ik])
                    print(lineno(), 'ik:', ik, 'dic_cap1[clé]:', dic_cap1[ik])
                    print(lineno(), 'ik:', ik, 'dic_cap2[clé]:', dic_cap2[ik])
                    print(lineno(), 'ik:', ik, 'dic_cap3[clé]:', dic_cap3[ik], '')
                    print(lineno(), 'not_gam:', not_gam, '. Les notes isolées de la gamme.', nom_gam)
                    print(lineno(), '... ;')
                dic_com[str(b_diatonic[0]), ik].append(nom_gam)
                dic_com[str(b_diatonic[0]), ik].append(dic_cap0[ik])
                dic_com[str(b_diatonic[0]), ik].append(dic_cap1[ik])
                dic_com[str(b_diatonic[0]), ik].append(dic_cap2[ik])
                dic_com[str(b_diatonic[0]), ik].append(dic_cap3[ik])
                (lineno(), 'dic_cap1[ik]:', dic_cap1[ik][0], 'dic_cap2[ik]:', dic_cap2[ik][0], 'not_gam:', not_gam)
                (lineno(), '[b_diatonic[0]:', [b_diatonic[0], ik])
            if dia == 13:  # Moduler en fonction du niveau recherché.
                break
        (lineno(), 'ik:', ik, 'dic_cap1[ik]:', dic_cap1[ik])
        (lineno(), 'ik:', ik, 'dic_cap2[ik]:', dic_cap2[ik])
        ('dic_rap0:\t', dic_rap0[ik], len(dic_rap0[ik]), '\t', lineno())
        ('dic_rap2:\t', dic_rap2[ik], len(dic_rap2[ik]), '\t', lineno())
        (lineno(), 'not_gam:', not_gam, 'nom_gam:', nom_gam, '. Les notes isolées de la gamme.')
        '''1080 not_gam: ['C', 'D', 'E', 'F', 'G', 'A', 'B'] nom_gam: CDEFGAB . Les notes isolées de la gamme.
            1080 not_gam: ['-D', 'G', '-A'] nom_gam: -DG-A . Les notes isolées de la gamme.
            1080 not_gam: ['+C', 'E', '+F', 'G', 'B'] nom_gam: +CE+FGB . Les notes isolées de la gamme.
            1080 not_gam: ['C', '-E', 'F', 'A', '-B'] nom_gam: C-EFA-B . Les notes isolées de la gamme.
            1080 not_gam: ['+D', '+G', 'A'] nom_gam: +D+GA . Les notes isolées de la gamme.
            1080 not_gam: ['C', 'D', 'E', 'F', 'G', 'A', 'B'] nom_gam: CDEFGAB . Les notes isolées de la gamme.
            1080 not_gam: ['-G'] nom_gam: -G . Les notes isolées de la gamme.
            1080 not_gam: ['C', 'D', 'E', '+F', 'A', 'B'] nom_gam: CDE+FAB . Les notes isolées de la gamme.
            1080 not_gam: ['D', '-E', '-A', '-B'] nom_gam: D-E-A-B . Les notes isolées de la gamme.
            1080 not_gam: ['+C', 'D', '+F', '+G'] nom_gam: +CD+F+G . Les notes isolées de la gamme.
            1080 not_gam: ['C', 'D', 'E', 'F', 'G', '-B'] nom_gam: CDEFG-B . Les notes isolées de la gamme.
            1080 not_gam: ['+A'] nom_gam: +A . Les notes isolées de la gamme.'''
        '''#'''
        if ik == 12:  # Fermeture au premier cycle (de 0 à 11)
            print(lineno(), '(if ik == 0), (de 0 à 11), break. Ne sera jamais écrit.')
            break
        # OUT OF DIATONIC
    (lineno(), '... dic_com ;', dic_com.keys())
    # La ZONE d'ANALYSE des COUPLES et des doublons.
    tab_gam, tab_uni, tab_nom, tab_cop, tab_key = 'CDEFGAB', [], {}, {}, []
    for k_duo, v_duo in dic_com.items():
        '''Compter le nombre de notes dans v_duo[0], '''
        nbr_not, nbr_aut, tab_aut = 0, 0, []
        for tube in v_duo[0]:  # v_duo = Nom de la gamme en script
            if tube in list(tab_gam):  # Tube est une note
                nbr_not += 1
            else:  # Tube est une altération = +^^ = nbr_aut = 3
                nbr_aut += 1
        tab_aut.append((nbr_not, nbr_aut))
        trans = v_duo, tab_aut  # trans = Nom gamme, tab_aut = Nombres notes et altérations
        (lineno(), 'trans:', trans)
        # Mémorisation et séparation des doublons
        if trans[0] in tab_uni:  # tab_uni = Stoke uniquement les noms (facilité de recherche)
            '''Voir si ce doublon est entièrement identique'''
            for k_key in range(12):
                if k_key in dic_com.keys():
                    (lineno(), 'trans[0][0]:', trans[0][0], '[k_duo[0], k_key]:', [k_duo[0], k_key])
                    (lineno(), 'trans[0][0]:', trans[0][0], '[k_duo[0], k_key]:', [k_duo[0], k_key])
                    # Capter la clé k_key du doublon
                    if dic_com[k_duo[0], k_key][0] == trans[0][0]:  # Ici, seulement les noms sont comparés
                        if dic_com[k_duo[0], k_key] != trans[0]:  # Ici, les valeurs sont différentes (noms égaux)
                            tab_uni.append(trans[0])  # Tableau basic des notes isolées
                            tab_nom[trans[0][0]] = []
                            tab_nom[trans[0][0]].append([k_duo[0], k_key])  # Dictionnaire évolué des unités isolées
                            (lineno(), 'IF val != val:', trans[0])
                        else:  # Plusieurs égalités (noms égaux, valeurs égales, cles inégales)
                            tab_cop[trans[0][0]] = []
                            tab_cop[trans[0][0]].append([k_duo[0], k_key])  # Dictionnaire des clones isolés
                            (lineno(), 'ELSE val = val:', trans[0][0], 'tab_cop:', tab_cop)
                        (lineno(), 'dic_com_clé:', [k_duo[0], k_key])
        else:
            tab_uni.append(trans[0])  # Tableau basic des notes isolées
            tab_nom[trans[0][0]] = []
            tab_nom[trans[0][0]].append([k_duo[0], k_duo])  # Dictionnaire évolué des unités isolées
            (lineno(), 'EL trans0:', trans[0], tab_nom)
        (lineno(), '.\tNotes:', nbr_not, 'Signes:', nbr_aut, '\tv_duo[0]:', v_duo[0])
        (lineno(), '.\tv_duo[0]:', v_duo[0], '\tlen():', len(v_duo[0]))
        (lineno(), 'v_duo[1:]...:', v_duo[1:][:2][0][:3], trans[0][0], '\t\tk_duo:', k_duo)
    (lineno(), 'tab_nom:', tab_nom, 'tab_nom = Dictionnaire évolué des unités isolées sans les doublons')
    (lineno(), 'tab_cop:', tab_cop, 'tab_cop = Dictionnaire évolué des unités isolées doublons')
    (lineno(), '... dic_com ;', dic_com.keys())
    return [dic_com, tab_nom, tab_cop]


'''print(exemple = "{}".format(a + b)
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
print(☺)'''
