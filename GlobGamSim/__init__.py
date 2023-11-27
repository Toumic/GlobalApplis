#!/usr/bin/env python 3
# -*- coding : utf-8 -*-
# Le dimanche 12 février 2023 (Commencement du script)
# GlobGamSim : Pour présenter les propriétés de la gamme en cours

# Modules importés
from tkinter import *
from tkinter.font import Font
import GlobGamVers6
import GlobGamChrom

# lineno() Pour consulter le programme grâce au suivi des print's
import inspect
from typing import Callable
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Lier les modules utiles
progam_vers6 = GlobGamVers6
progam_chrom = GlobGamChrom

# GGV6/2974(self.nordiese) 2978(self.subemol)
tab_sup = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^', '+^^^^', 'x^^^^',
           '^^^^^', '+^^^^^', 'x^^^^^', '^^^^^^', '+^^^^^^', 'x^^^^^^', '^^^^^^^', '+^^^^^^^', 'x^^^^^^^', '^^^^^^^^']
tab_inf = ['', '-', 'o', '*', '-*', 'o*', '**', '-**', 'o**', '***', '-***', 'o***', '****', '-****', 'o****',
           '*****', '-*****', 'o*****', '******', '-******', 'o******', '*******', '-*******', 'o*******', '********']
tab_abc = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Dictionnaires des miroirs symétriques
iso_quant, duo_quant, gen_quant = {}, {}, {}
# Dictionnaires des poids et des rangs mesurés
dat_poids, dat_rangs, dat_singe = {}, {}, {}
# Utilités (signe[altération], nom[tonalité], valeur[forme numérique])
# Exemple : #C Maj. Signe = #.
number, name, value, signe = [], [], [], []


def simili(sim, dat, nom):
    """Partie analytique liée à la gamme en cours et déclare les similitudes.
    Similitudes (sim = Selon les noms des gammes[classique ou calculée])
        Sim_keys() = Noms des gammes numériques (sans les notes)
        Sim_values() = Formule modale aux intervalles cumulés (comme dat[1])
    Poids modaux :
        (dat[1] = Dictionnaire. Clefs ('Maj', '-3',,,). Intervalles modaux à genre cumulatif),
        (dat[2] = Liste. Format dictionnaire[('ISO', (((1, 'I'), '+^2'), ((1, 'III'), '-*6')))],
        : L'iso = Deux degrés d'une gamme sont croisés, en cas de lecture en sens inversé.
        : Le duo = Même chose qu'iso, sauf que les gammes et les degrés sont différents.),
        (dat[3] = Dictionnaire. Clefs (147, 266,,,). Groupe des gammes aux mêmes poids),
        (dat[4] = Dictionnaire. Clefs ('0352146', '1253046',,,). Groupe des gammes aux mêmes rangs),
        (dat[5] = Dictionnaire. Clefs (de 1 à 66). Groupe les noms entiers diatoniques),
        (dat[6] = Dictionnaire. Clefs ((66, 'I'), (66, 'II'),,,). Groupe poids modaux diatoniques),
        (dat[7] = Dictionnaire. Clefs ((66, 'I'), (66, 'II'),,,). Degrés et noms[entiers/décimaux] modaux)
    Le nom de la gamme en cours (attention aux compositions : Exemple = 'oF x54o')"""
    # Objectif mettre en forme les données reçues pour une meilleure gestion
    (lineno(), 'GGS/sim:', sim, '\n', 'dat:', dat.keys(), type(dat), 'nom:', nom)
    # ('\n dat[7]:', dat[7])

    # print(' dat[3]:poids', dat[3], '\n dat[4]:rangs', dat[4], '\n dat[5]:noms', dat[5])

    def numismate(titre, tom):
        """(dat[5] = Dictionnaire. Clefs (de 1 à 66). Groupe les noms entiers diatoniques),
        Fonction de recherche du numéro de la gamme par rapport à son titre, et inversement.
        Titre = Soit 'tom', soit 'num'
            Quand c'est 'tom' = Valeur tonale sans la tonalité de la note.
            Quand c'est 'num' = Numéro de la gamme en paramètre."""
        titre1 = ()
        if tom == 'tit':
            # Retrouver les numéros des gammes grâce au nom
            if titre == 'Maj':  # 'Maj' de dat[5] = '0'
                titre = '0'
            for kt, vt in dat[5].items():
                if titre in vt:
                    titre1 = kt, vt
                    (lineno(), 'TIT_titre1:', titre1, 'titre:', titre, kt)
                    break
        elif tom == 'num':  # Retrouver les noms des gammes grâce au numéro
            titre1 = titre, dat[5][titre]
            (lineno(), 'NUM_titre1:', titre1, 'titre:', titre)
        return titre1

    # Formatage du nom de la gamme en cours : 'C Maj' devient 'C' et 'Maj'
    n0, max_n0 = 0, len(nom)
    n1 = ''
    sig_ava, sig_abc, sig_sui = '', '', ''
    '''# Obtenir le nom de la gamme. (Format retour1 est OK)'''
    for no in nom:
        if n0 == 0 and no not in tab_abc:
            for ma in range(max_n0):
                if nom[ma] not in tab_abc:
                    n1 += nom[ma]
                    (lineno(), 'N1 en construction:', n1)
                else:
                    sig_ava = n1
                    (lineno(), 'N1 sig_ava:', sig_ava, n0)
                    break
        elif no in tab_abc:
            sig_abc = no
            (lineno(), 'No sig_abc:', sig_abc, n0)
        elif no != ' ':
            sig_sui += no
            (lineno(), 'sig_sui:', sig_sui, n0)
        n0 += 1
    (lineno(), 'sig_ava:', sig_ava, 'sig_abc:', sig_abc, 'sig_sui:', sig_sui)
    retour1 = numismate(sig_sui, 'tit')
    retour10 = 0
    for rr1 in retour1:
        number.append(rr1)
        retour10 = rr1
        break
    signe.append(sig_ava)
    name.append(sig_abc)
    value.append(sig_sui)
    (lineno(), 'retour1:', retour1, 'sig_ava:', sig_ava, 'sig_abc:', sig_abc, 'sig_sui:', sig_sui)

    '''# Réussir une synthèse des deux courants de symétrie'''
    # duo_est = Mémoriser les numéros des gammes, en trouver d'autres (DUO)
    # duo_duo = Vérification du couple en jeu (DUO)
    dat_miroir, duo_duo, duo_est = {}, [], []
    # iso(duo)_quant = Figuré rythmique (iso&duo) : Cadence présence nivelée
    # gen_quant = Généralité rythmique des cadences des présences nivelées
    # iso_quant, duo_quant, gen_quant = {}, {}, {}
    gen_ = 0  # Indexation dictionnaire-ordre général
    for sid in dat[2]:
        gen_ += 1  # Indexation dictionnaire-ordre général
        iso_quant[gen_], duo_quant[gen_], gen_quant[gen_] = [], [], []
        (lineno(), '_ _ _ _ _ sid:', sid[1], 'gen_:', gen_)
        if sid[0] == 'ISO':
            (lineno(), '_ _ _ _ _ sid:', sid[1][1][1])
            sid_i = sid[1][0][0][0]  # sid_i = Numéro de gamme
            iso_inf = [sid[1][0][0][1], sid[1][0][1], sid[1][1][0][1], sid[1][1][1]]
            dat_miroir['ISO', sid_i] = iso_inf
            iso_quant[gen_] = iso_inf
            gen_quant[gen_] = iso_inf
            (lineno(), 'iso', 'iso_inf:', iso_inf)
        elif sid[0] == 'DUO':
            (lineno(), '_ _ _ _ _ sid:', sid[1][0], sid[1][1])
            bis_i = sid[1][0][0][0]  # bis_i = Numéro de gamme
            dat_miroir['DUO', bis_i] = []
            duo_1, duo_2 = sid[1][0][0][0], sid[1][1][0][0]
            (lineno(), 'duo_1:', duo_1, '2:', duo_2)
            if duo_1 not in duo_duo:  # Première reconnaissance
                (lineno(), '_ _ _ _ _ sid:', sid[1][0], sid[1][1])
                duo_duo.append(duo_1)
                duo_duo.append(duo_2)
                duo_est.append(duo_1)  # duo_duo = Vérification du couple en jeu (DUO)
                duo_est.append(duo_2)  #
                duo_inf = [sid[1][0][0][0], sid[1][0][0][1], sid[1][0][1],
                           sid[1][1][0][0], sid[1][1][0][1], sid[1][1][1]]
                dat_miroir['DUO', bis_i].append(duo_inf)
                ('*', lineno(), 'duo_inf:', duo_inf)
                (lineno(), '_', duo_est, "Partie = 'DUO'", 'dat_miroir:', dat_miroir['DUO', bis_i])
            '''# Construction en cours de duo_duo. Général (DUO)
                En analysant les résultats de go et d2 on a des intervalles significatifs'''
            go, duo_ = 0, gen_
            for d2 in range(duo_, len(dat[2])):
                go += 1  # Limite boucles for 'sid_bis'
                sid_bis = dat[2][d2]
                if sid_bis[0] != 'ISO' and duo_est:
                    bis_1, bis_2 = sid_bis[1][0][0][0], sid_bis[1][1][0][0]
                    (d2, lineno(), 'bis_1:', bis_1, 'bis_2:', bis_2, 'duo_est:', duo_est)
                    if duo_est[0] != bis_1 and bis_2 in duo_est:
                        duo_sup = [sid_bis[1][0][0][0], sid_bis[1][0][0][1], sid_bis[1][0][1],
                                   sid_bis[1][1][0][0], sid_bis[1][1][0][1], sid_bis[1][1][1]]
                        dat_miroir['DUO', bis_i].append(duo_sup)
                        duo_quant[gen_] = dat_miroir['DUO', bis_i]
                        gen_quant[gen_] = dat_miroir['DUO', bis_i]
                        (lineno(), 'duo_sup:', duo_sup, 'dat_miroir[DUO, bis_i]:', dat_miroir['DUO', bis_i])
                        ('**', lineno(), 'duo_quant[gen_]:', duo_quant[gen_], 'gen_:', gen_)
                        (lineno(), 'gen_:', gen_, 'go:', go, 'd2:', d2)  # go, d2 = Intervalles significatifs
                        # 139 gen_: 62 go: 63 d2: 62
                        (lineno(), duo_1, 'dat_miroir:', dat_miroir['DUO', bis_i])
                        # 143 62 dat_miroir: [[62, 'I', '+53-', 63, 'III', '+45.-3'],
                        # [63, 'I', '-53', 62, 'III', '+35']]
                        break
            duo_est.clear()
            if not gen_quant[gen_]:
                (lineno(), '. *|* gen_quant[gen_]:', gen_quant[gen_], gen_)

    (lineno(), '. *|* dat_miroir["ISO&DUO", bis_i]:', dat_miroir)
    (lineno(), '. *|* iso_quant[gen_]:', iso_quant)
    (lineno(), '. *|* duo_quant[gen_]:', duo_quant)
    (lineno(), '. *|* gen_quant[gen_]:', gen_quant)

    ''' dat_poids traitement au cas-par-cas où un cas = une gamme (en cours)
    # Liste les gammes aux mêmes poids dat3, clé égal poids'''
    for k3, v3 in dat[3].items():
        if retour10 in v3:
            dat_poids[sig_sui] = []
            for n3 in v3:
                retour3 = [numismate(n3, 'num')]  # Avec les crochets,
                (lineno(), 'retour3:', retour3)
                for r3 in retour3:
                    dat_poids[sig_sui].append(r3)
                (lineno(), 'POIDS dat_poids:', dat_poids)
            break
    (lineno(), 'GGS/dat[3]:', dat[3], '\n dat_poids:', dat_poids)
    '''184 GGS/dat[3]: {147: [1], 266: [18, 2, 5, 6], 315: [33, 3, 4, 29], 378: [38, 7, 13, 22, 31], 
    413: [21, 8], 350: [20, 9], 224: [19, 10], 308: [15, 11], 406: [54, 12, 28, 32, 34, 37], 238: [17, 14], 
    343: [43, 16, 27, 35, 36], 329: [26, 23], 455: [25, 24], 301: [30], 476: [55, 39, 40, 41], 371: [42], 
    427: [49, 44], 518: [58, 45], 392: [60, 46], 567: [47], 469: [57, 48, 50, 52, 56], 462: [59, 51], 385: [53], 
    539: [64, 61], 497: [63, 62], 588: [66, 65]}
    dat_poids: {'Maj': [(66, ['0', '+4']), (65, ['-3', '+45'])]}'''

    ''' dat_rangs traitement au cas-par-cas où un cas = une gamme (en cours)
    # Liste les gammes aux mêmes rangs dat4, clé égal rang'''
    for k4, v4 in dat[4].items():
        if retour10 in v4:
            dat_rangs[sig_sui] = []
            for n4 in v4:
                retour4 = [numismate(n4, 'num')]
                (lineno(), 'retour4:', retour4)
                '''171 retour4: [(47, ['-32'])]'''
                for r4 in retour4:
                    dat_rangs[sig_sui].append(r4)
                (lineno(), 'RANGS dat_rangs:', dat_rangs)
            break
    (lineno(), 'GGS/dat[4]:', dat[4], '\n dat_rangs:', dat_rangs)
    '''206 GGS/dat[4]: {'0352146': [1], '1253046': [2, 10, 14, 17, 19, 5, 6, 18], '2153046': [3, 11, 15, 
    23, 26, 30, 4, 29, 33], '2154036': [7, 8, 9, 12, 20, 21, 28, 32, 34, 37, 42, 46, 53, 54, 60, 13, 22, 
    31, 38], '2153036': [16, 27, 35, 36, 43], '2145036': [24, 44, 49, 51, 59, 25], '3145026': [39, 48, 50, 
    52, 56, 57, 40, 41, 55], '3045126': [45, 62, 63, 58], '4036125': [47, 65, 66], '3035126': [61, 64]} 
    dat_rangs: {'Maj': [(47, ['-32']), (65, ['-3', '+45']), (66, ['0', '+4'])]}'''

    ''' dat_signaux traitement au cas-par-cas où un cas = une gamme (en cours)
    # Liste les modes diatoniques dat7, signatures et noms modaux'''
    for k7, v7 in dat[7].items():
        if not v7:
            dat_singe[k7] = ['Maj']
        for vis in v7:
            dat_singe[k7] = vis
            (lineno(), 'vis:', vis, 'k7:', k7)
        (lineno(), 'dat7:', k7, v7)
    (lineno(), 'GGS/dat[7]:', 'dat[7]', '\n dat_singe:', dat_singe)
    ''' Comment obtenir une gamme majeure à n'importe quel moment
    gamme_maj7 = progam_chrom.transposer({1: 'xB'}, {1: ''}, {1: ''}, {1: ''}, 'sub')
    print(lineno(), 'GGS/gamme_maj7:', gamme_maj7)'''


def approprier():
    """Nouvelle fenêtre faisant le support des propriétés simili[poids, rangs, iso, duo]
        Les propriétés portent sur """
    gamme = signe[0] + name[0] + ' ' + value[0] + '(' + str(number[0]) + ')'
    proprio = Toplevel()
    proprio.title('Propriété de la  Gamme : Chromatisme en %s' % gamme)
    proprio.geometry('1000x800+900+40')
    proprio.configure(bg='moccasin')
    f_titre = Font(family='Liberation Serif', size=14)
    f_proprio0 = Frame(proprio, bg='beige')
    f_proprio0.pack(side=LEFT, expand=True)
    f_proprio1 = Frame(proprio, bg='beige')
    f_proprio1.pack(side=RIGHT, expand=True)
    c_proprio0 = Canvas(f_proprio0, bg='Ivory', height=30, width=410)
    c_proprio0.pack(padx=15, pady=15)  # c_proprio = Premier Canvas original (pack_forget ou pas)
    c_proprio0.delete(ALL)
    t_titre = 'Les propriétés de ' + gamme
    c_proprio0.create_text(163, 13, font=f_titre, text=t_titre, fill='blue')
    c_proprio1 = Canvas(f_proprio0, bg='lightgrey', height=500, width=410)
    c_proprio1.pack(padx=15, pady=15)  # c_proprio = Premier Canvas original (pack_forget ou pas)
    c_proprio1.delete(ALL)
    c_proprio2 = Canvas(f_proprio1, bg='wheat', height=500, width=410)
    c_proprio2.pack(padx=15, pady=15)  # c_proprio = Premier Canvas original (pack_forget ou pas)
    c_proprio2.delete(ALL)
    (lineno(), 'GGS/Écriture simili.duo_quant:', duo_quant.keys(), '\n', 'signe:', signe[0], name[0], value[0])
    #

    #
    #
    #
    #
    #
    #
    #
    #
