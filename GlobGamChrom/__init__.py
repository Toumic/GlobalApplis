#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Origine 20 septembre 2022
# GlobGamChrom : Mémoriser le chromatisme original et modifié


import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Module de chromatisation chromatique
dic_ana, dic_mod, dic_inv, dic_abc = {}, {}, {}, {}  # Dictionnaires à utiliser
dic_rip0, dic_rip1, dic_rip2, dic_rip3 = {}, {}, {}, {}
dic_rapt = {}  # dic_rapt = Dictionnaire des premiers commatismes
dic_rap0, dic_rap2 = {}, {}  # Afficher les chromatismes parallèles
gam_com = {}  # gam_com = Faire la distinction entre notes gamme uniques et notes chromatiques
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
    Séquences du traitement : - Obtenir la gamme majeure non signée.
     - Transposer la gamme au niveau altéré. - Résoudre la tonalité.
    Rip0.1 = Huit notes. Rip2.3 = Cinq notes.☺
    Pour transposer les notes de la gamme (Rip0.1)
    Pour transposer les notes chromatiques (Rip2.3)"""
    (lineno(), rip0, rip1, rip2, rip3)
    if rip0[1]:
        (lineno(), rip0)
        (lineno(), 'rip0[1][0]:', rip0[1][0])
        (lineno(), 'rip1:[1]', rip1[1])
    # Montage table des clés majeures de dic_maj
    cle_aut, note, ok = [], '', False
    for i in range(1, 14):
        if rip1[1] and i in rip1.keys():
            note0 = rip0[i][0]
            if note0 not in cle_aut and len(note0) > 1:
                cle_aut.append(note0)
                (lineno(), 'note0:', note0)
        if i in rip2.keys():
            (lineno(), rip2, rip3, len(rip2), len(rip3))
            if len(rip2) > 2:
                note2, note3 = rip2[i][0] + rip2[i][1], rip3[i][0] + rip3[i][1]
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
        ('\n', lineno(), 'aut:', ca)
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
    S = Degré d'inversion demandé ou donné par défaut"""
    (lineno(), 'GGC/', 'A:', a[0], 'B = Nom de la tonalité analogique:', b, '\nC:', c[0], 'S:', s)
    a_diatonic.append(a)  # Tonalité analogique
    b_diatonic.append(b)  # Nom de la tonalité
    c_diatonic.append(c)  # Tonalité numéric croissant
    # Mise en forme du dictionnaire dic_ana (analogie)
    for ia in range(len(a_diatonic[0])):
        dic_ana[ia + 1] = a_diatonic[0][ia][0]
        (lineno(), 'GGC/dic_ana:', dic_ana, 'len:', len(a_diatonic[0][ia][0]), 'ia:', ia)
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

    '''Le cycle yep sépare les notes de la gammes de celles qui sont chromatiques'''
    gam0 = gam1 = ''
    for yep in range(1, 13):  # Mesurer dic_ana[yep](notes:gamme ou chrome)
        (lineno(), '___________________*************___________________ Début de cycle yep:', yep)
        abc = 0
        for lie in dic_ana[yep]:  # Compter les éléments
            for eli in lie:
                if eli in gam_abc['C']:
                    abc += 1
        (lineno(), 'abc:', abc)
        if abc < 2:  # c_rip0, c_rip1 (note gamme avec/sans altération)
            (lineno(), "Qu'est dic_ana[yep]?:", dic_ana[yep], ":= ('', 'C') ou ('^', 'F')")
            if not list(dic_ana[yep][0]):  # Indexe la partie gauche de ('','') où est la note naturelle
                dic_rip0[yep] = list(dic_ana[yep][1])
                dic_rip1[yep] = list(dic_ana[yep][1])
                if yep == 1:
                    gam0 = gam1 = dic_rip0[yep]  # Gamme en cours originale
                (lineno(), 'GGC/dic_rip0.1[yep]:\t', yep, dic_rip0[yep], dic_rip1[yep])
            else:  # Indexe la partie gauche de ('-','') où est la note altérée
                dic_rip0[yep] = [dic_ana[yep][0] + dic_ana[yep][1]]  # Assemble l'altération & la note
                dic_rip1[yep] = [dic_ana[yep][0] + dic_ana[yep][1]]  # Assemble l'altération & la note
                if yep == 1:
                    gam0 = gam1 = dic_rip0[yep]  # Gamme en cours originale
                (lineno(), 'GGC/dic_rip0.1[yep]:\t', yep, dic_rip0[yep], dic_rip1[yep])
            if yep == 12:
                dic_inv[13] = dic_inv[1]
            (lineno(), 'GGC/dic_rip0.1[yep]:\t', yep, dic_rip0[yep], dic_rip1[yep])
        else:  # c_rip2,  c_rip3
            dic_rip2[yep], dic_rip3[yep] = list(dic_ana[yep][1]), list(dic_ana[yep][0])
            (lineno(), 'GGC/dic_inv[yep]:   \t', yep, dic_inv[yep])
            (lineno(), 'GGC/dic_rip2inf[yep]:\t', yep, dic_rip2[yep])
            (lineno(), 'GGC/dic_rip3sup[yep]:\t', yep, dic_rip3[yep])
    dic_rip0[13], dic_rip1[13] = dic_rip0[1], dic_rip1[1]
    transposer(dic_rip0, dic_rip1, dic_rip2, dic_rip3)
    (lineno(), '_GGC/dic_rip0.1:  \n', dic_rip0, '\n', dic_rip1)
    (lineno(), '_GGC/dic_rip2.3:  \n', dic_rip2, '\n', dic_rip3)
    (lineno(), 'Indices \tgam0[0]:', gam0[0], '\t\tgam1[0]:', gam1[0], '\t\tb_diatonic[0]:', b_diatonic[0])

    '''Phase de renseignement de la matrice'''
    for yes in range(1, 13):  # Lecture des séquences chromatiques
        (lineno(), '_________________________*************_____________________ Début de cycle yes:', yes)
        (lineno(), 'Indices \tgam0[0]:', gam0[0], '\t\tgam1[0]:', gam1[0], '\t\tb_diatonic[0]:', b_diatonic[0])
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
            (lineno(), 'GGC/rip_app0:', rip_app0, 'rip_app1:', rip_app1, '********************* yes:', yes)
            #
            # Séquence d'affichage pour d'éventuelles corrections
            # Ci-dessous.
            if yi == 12:  # Normalement(yi == 11)
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
            (lineno())
        if yes == 12:  # Lecture totale limitée à 12 (yes)
            break
        # Ci-dessus.
        # Séquence d'affichage pour d'éventuelles corrections
        #
    print(lineno(), '\nGGC/dic_rip0.1.keys:', dic_rip0.keys(), dic_rip1.keys())
    print(lineno(), 'GGC/dic_rip2.3.keys:', dic_rip2.keys(), dic_rip3.keys())
    (lineno(), 'GGC/dic_inv.keys', dic_inv.keys())
    '''Tous les dic_rip's ont été initialisés selon la dictée numérique.
    Maintenant on passe à l'épisodique récupération des diatoniques commatiques:
    .   Suivre les colonnes une par une en commençant par la tonique la plus rapprochée de celle de la 1ère colonne.
    .   Une fois sélectionnée, la tonique se construit avec les notes de sa propre colonne.
    En ce moment le traçage récolte(la tonique, le nom de la gamme, la graduation)'''
    print(lineno(), 'INDICES \tgam0:', gam0[0], '\tgam1:', gam1[0], '\t\tnom:', b_diatonic[0], '\tgrade:', graduation)
    (lineno(), 'GGC/dic_maj.keys\n', dic_maj.keys(), 'len(dic_maj.keys()):', len(dic_maj.keys()))
    # Lecture de chaque colonne des dic_rip's pour trouver la tonique fondamentale
    ton_un = dic_rip0[1][0]
    tab_loi = dic_maj[ton_un]
    val_rip = list(dic_inv.keys())
    (lineno(), 'ton_un:', ton_un)
    dic_cas, dic_abs = {}, {}  # dic_cas(gam0, 'casX', cas0 ou 2, key, clef) dic_abs(absences)
    for clef in range(12):
        cas3 = 0
        if not dic_cas:
            dic_cas[gam0[0], 'cas0'] = []  # dic_cas[tonique, cas]
            dic_cas[gam0[0], 'cas2'] = []
        (lineno())
        for key in val_rip[:13]:
            cas3 += 1
            if key in dic_rip0.keys():
                cas0 = dic_rip0[key][clef], dic_rip1[key][clef]
                (lineno(), 'cas0:', key, cas0, clef)
                if gam0[0] in cas0:
                    ckc = cas0, (key, clef)  # ckc((notes(couple), (clé, verticale))
                    dic_cas[gam0[0], 'cas0'].append(ckc)
                    (lineno(), 'cas0:', cas0, 'ckc:', ckc)
                    break
                (lineno(), 'dic_rip1:', key, dic_rip1[key][clef], clef)
            elif key in dic_rip2.keys():
                cas2 = dic_rip2[key][clef], dic_rip3[key][clef]
                (lineno(), 'cas2:', key, cas2, clef)
                if gam0[0] in cas2:
                    ckc = cas2, (key, clef)
                    dic_cas[gam0[0], 'cas2'].append(ckc)
                    (lineno(), 'cas2:', cas2, 'ckc:', ckc)
                    break
            if cas3 > 11 and key != 12:
                dic_abs[key, clef] = []
                (lineno(), 'Cas3 absences dic_abs[key]:', dic_abs.keys())
    '''Recueil des toniques présentes : gam0 = Tonalité principale parmi les toniques'''
    (lineno(), 'tab_loi:', tab_loi)
    tripe0, tripe1 = {1: ''}, {1: ''}  # Pour les notes de la gamme originale
    tripe2, tripe3 = {2: ''}, {2: ''}  # Pour les notes chromatiques parallèles
    # Lecture des colonnes absentes pour trouver les toniques fondamentales
    (lineno(), 'Cas3 ABSENCES dic_abs:', dic_abs)
    for cas_duc in dic_abs.keys():
        (lineno(), 'GGC/ton_un:', ton_un, '\n', dic_maj[ton_un])
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
                    cas_cas.append(no_cas)
                    (lineno(), 'cas_cas:', cas_cas)
                else:  # 'diminuer un augmenté'
                    (lineno(), 'ic_rng:', ic_rng, 'diminuer un augmenté ici:', ici)
                    if ic_rng - ici > 0:
                        id_cas = ic_rng - ici
                        no_cas = tab_sup[id_cas] + ic_deg
                        cas_cas.append(no_cas)
                        (lineno(), 'id_cas:', id_cas, 'ici:', ici, 'no_cas:', no_cas)
                    else:  # La différence est inférieure à zéro
                        id_cas = ici - ic_rng
                        no_cas = tab_inf[id_cas] + ic_deg
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
                        cas_cas.append(no_cas)
                        (lineno(), 'id_cas:', 'no_cas:', no_cas)
                    else:  # autre cas que 11
                        id_cas = (12 - axe) + ax_rng
                        no_cas = tab_sup[id_cas] + ax_deg
                        cas_cas.append(no_cas)
                        (lineno(), 'id_cas:', id_cas, 'axe:', axe)
                else:  # 'augmenter un diminué'
                    (lineno(), 'ax_rng:', ax_rng, 'augmenter un diminué axe:', axe)
                    if axe == 11:  # ax=11 = Emplacement 7ème majeure
                        id_cas = abs(ax_rng) - 1
                        no_cas = tab_inf[id_cas] + ax_deg
                        cas_cas.append(no_cas)
                        (lineno(), 'ax=11', cas_cas[0])
                    else:  # autre cas que 11
                        if abs(ax_rng) - (12 - axe) > 0:
                            id_cas = abs(ax_rng) - (12 - axe)
                            no_cas = tab_inf[id_cas] + ax_deg
                            cas_cas.append(no_cas)
                            (lineno(), 'id_cas:', id_cas, 'axe:', axe, 'no_cas:', no_cas)
                        else:  # La différence est inférieure à zéro
                            id_cas = (12 - axe) + ax_rng
                            no_cas = tab_sup[id_cas] + ax_deg
                            cas_cas.append(no_cas)
                            (lineno(), 'id_cas:', id_cas, 'axe:', axe, 'no_cas:', no_cas)
                ax = dic_maj[ton_un][axe], axe
                bas_cas.append(ax)  # bas_cas = Couple (note/index) de la partie inférieure
                (lineno(), 'ax:', ax, 'ax_deg:', ax_deg, 'ax_sig:', ax_sig, 'cas_cas:', cas_cas)
            if len(sur_cas) == len(bas_cas) == 12:
                but = True
                (lineno(), '(sur_cas):', len(sur_cas), '(bas_cas):', len(bas_cas), 'cas_duc[1]:', cas_duc[1])
                ('§', cas_duc[1], lineno())

        # Enregistrement des toniques absentes dans dic_cas et dans dic_maj, en passant par la fonction transposer
        # def transposer(rip0, rip1, rip2, rip3):
        (lineno(), 'cas_cas:', cas_cas)
        (lineno(), 'dic_maj.keys():', dic_maj.keys())
        ''' tripe0 = tripe1 = {1: []}, {1: []}  # Pour les notes de la gamme originale(et plus)
            tripe2 = tripe3 = {2: []}, {2: []}  # Pour les notes chromatiques parallèles'''
        for key in range(1, 14):
            len_sos1, len_sos2 = len(dic_cas[gam0[0], 'cas0']), len(dic_cas[gam0[0], 'cas2'])
            if key in dic_rip0.keys():
                cas_sos = dic_rip0[key][cas_duc[1]], dic_rip1[key][cas_duc[1]], 'cas0'
                (lineno(), 'cas_sos:', cas_sos, 'key:', key)
                for sos in range(2):
                    if cas_sos[sos] in cas_cas:
                        ckc = cas_sos[:2], (key, cas_duc[1])
                        dic_cas[gam0[0], cas_sos[2]].append(ckc)
                        if cas_sos[0] not in dic_maj.keys() and cas_sos[0] not in tripe0[1]:
                            tripe0[1] = cas_sos[0]
                            (lineno(), 'tripe0:', tripe0, 'cas_sos[0]:', cas_sos[0])
                        if cas_sos[1] not in dic_maj.keys() and cas_sos[1] not in tripe1[1]:
                            tripe1[1] = cas_sos[1]
                            (lineno(), 'tripe1:', tripe1, 'cas_sos[1]:', cas_sos[1])
                        (lineno(), 'tripe0:', tripe0, 'tripe1:', tripe1)
                        (lineno(), 'sos:', dic_cas[gam0[0], cas_sos[2]], '\tkey:', key)
                        break
                (lineno(), 'cas_sos 0:', cas_sos, 'key:', key, 'cas_duc[1]:', cas_duc[1])
                (lineno(), 'dic_cas 0:', dic_cas[gam0[0], 'cas0'][0])
            else:
                cas_sos = dic_rip2[key][cas_duc[1]], dic_rip3[key][cas_duc[1]], 'cas2'
                (lineno(), 'cas_sos:', cas_sos, 'key:', key)
                for sos in range(2):
                    if cas_sos[sos] in cas_cas:
                        ckc = cas_sos[:2], (key, cas_duc[1])
                        dic_cas[gam0[0], cas_sos[2]].append(ckc)
                        if cas_sos[0] not in dic_maj.keys() and cas_sos[0] not in tripe2[2]:
                            tripe2[2] = cas_sos[0]
                            tripe3[2] = cas_sos[1]
                            (lineno(), 'tripe2:', tripe2, 'tripe3:', tripe3)
                        (lineno(), 'sos:', dic_cas[gam0[0], cas_sos[2]], '\tkey:', key)
                        break
                (lineno(), 'cas_sos 2:', cas_sos, 'key:', key, 'cas_duc[1]:', cas_duc[1])
                (lineno(), 'dic_cas 2:', dic_cas[gam0[0], 'cas2'])
            deg_cas, sig_cas = cas_sos[0][len(cas_sos[0])-1:], cas_sos[0][:len(cas_sos[0])-1]
            (lineno(), 'deg_cas:', deg_cas, 'sig_cas:', sig_cas)
        # Appel de fonction transposer avec passage de paramètres sans retour
        (lineno(), '___ ___ Suite rip:', tripe0, tripe1, tripe2, tripe3)
        transposer(tripe0, tripe1, tripe2, tripe3)
        (lineno(), 'dic_cas:', dic_cas[gam0[0], 'cas0'], '\n :', dic_cas[gam0[0], 'cas2'])
        ('** ', lineno(), '** ** ** len_sos:', len_sos1, 'len_sos2:', len_sos2)
    (lineno(), 'dic_cas:', dic_cas[gam0[0], 'cas0'], '\n', dic_cas[gam0[0], 'cas2'])
    (lineno(), 'dic_maj.keys():', dic_maj.keys())
    '''Les clefs changent en fonction de chaque gamme originale.'''
    for dc in dic_cas.keys():
        for vc in dic_cas[dc]:
            aug_key = vc[1][0]  # La clef tonique (rapport dic_rip2.3[clef])
            aug_hau = vc[1][1]  # Position tonique (rapport dic_rip2.3[clef][position])
            aug_rng, aug_lop = 0, -1  # aug_rng = Incrémente la clef
            dic_rapt[aug_hau] = [[aug_key, aug_hau]]
            dic_rap0[aug_hau] = [[aug_key, aug_hau]]
            dic_rap2[aug_hau] = [[aug_key, aug_hau]]
            (lineno(), 'vc:', vc, '\t\trangeur:', aug_key, 'hauteur:', aug_hau)
            while aug_lop < 11:
                aug_lop += 1
                if aug_key in dic_rip0:
                    note0, note1 = dic_rip0[aug_key][aug_hau], dic_rip1[aug_key][aug_hau]
                    dic_rapt[aug_hau].append((note0, note1))
                    dic_rap0[aug_hau].append(note0)
                    dic_rap2[aug_hau].append(note1)
                    (lineno(), 'dic_rip0.1:\t', note0)
                else:
                    note2, note3 = dic_rip2[aug_key][aug_hau], dic_rip3[aug_key][aug_hau]
                    dic_rapt[aug_hau].append((note2, note3))
                    dic_rap0[aug_hau].append(note2)
                    dic_rap2[aug_hau].append(note3)
                    (lineno(), 'dic_rip2.3:\t', note2)
                aug_key += 1
                if aug_key == 13:
                    aug_key = 1
                (lineno(), 'aug_lop:', aug_lop)
            (lineno(), 'vc:', vc, '\t\trangeur:', aug_key, 'hauteur:', aug_hau)
        (lineno(), 'dc:', dc, 'dic_cas[dc]:', dic_cas[dc])
    '''Ici, nous connaissons les gammes commatiques qui sont impliquées au commatisme'''
    (lineno(), 'GGC/ton_un:', ton_un, '\n', dic_maj.keys(), 'len(dic_maj.keys()):', len(dic_maj.keys()))
    for ik in range(12):
        print('dic_rap0:\t', dic_rap0[ik], len(dic_rap0[ik]), '\t', lineno())
        print('dic_rap2:\t', dic_rap2[ik], len(dic_rap2[ik]), '\t', lineno())
        # break
    (lineno(), dic_rapt)
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
    print()'''
