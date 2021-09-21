# Python utf8
# En cours de finalisation
# Mardi 27 juillet 2021

# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# GlobEnModes
# Moulin modal à comparaisons majeures
#

import inspect
import os
from typing import Callable
import GlobInverseAcc
glob_in_acc = GlobInverseAcc
inspect.getsource(os)

# lineno() Pour déboguer le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Nécessités pour repérages:
"""
Tableau des signatures majeures (Comparaisons, :gamme_poids:)
    :gamme_poids: = {1: [0,0,0,0,0,0,0], 2: [0,0,-4,0,0,0,-8],
Tableaux modèles supposés fondamentaux (Toniques)
    1: Signature numérique pour chaque mode diatonique
        :mode_poids = [[0,-3, -5, 7, 7, 7,0],[0,-3, -5, -6, 7, 7,0],,,
    2: Signature binaire correspondante
        :mode_biner = ['111000001111','111100000111','111110000011',,,
Plonger dans le code à l'aide des 'print':
    Une ligne de code faite ainsi fonctionne: (choses à printer),
    print(1) = (1) = OK. Copier print à (1) = print(1)."""

mages_biner = ['101011010101', '101101010110', '110101011010',
               '101010110101', '101011010110', '101101011010',
               '110101101010']

gamme_poids = {1: [0, 0, 0, 0, 0, 0, 0], 2: [0, 0, -4, 0, 0, 0, -8],
               3: [0, -3, -4, 0, 0, -7, -8], 4: [0, 0, 0, +5, 0, 0, 0],
               5: [0, 0, 0, 0, 0, 0, -8], 6: [0, 0, -4, 0, 0, -7, -8],
               7: [0, -3, -4, 0, -6, -7, -8]}

signes = ['', '+', 'x', '^', '^+', '^x', 'o*', '-*', '*', 'o', '-']
dic_analyse = {}  # :Dana initie dico
dic_pc = {}
# Les clefs de ces dictionnaires valent chacune une gamme
tous_poi, tous_mod = {}, {}  # Poids division Modes diatonic's
dan_mode, dan_rang, dan_poids = {}, {}, {}  # Dico:dan. Trier infos
ego_mode, ego_rang, ego_poids = {}, {}, {}  # Dico:ego. Union gammes
maj_mode, maj_rang, maj_poids = {}, {}, {}  # Dico:maj. Diatonic majeur
# Pour éviter de tourner autour du pot!
maj_clef = [66]  # Table:maj_clef. Clef référence majeure. :dana.keys().


def dana_fonc(dana, gam1):
    """
    Les dictionnaires {dan/ego/maj}:
        Tous. Intégrales Poids/Modes
        Dan. Enregistrer infos gammes pour analyser
        Ego. Répertorier gammes mêmes types
        Maj. Référencer diatonic majeur
    Dana est le dictionnaire entrant:
        Dana Keys = Numéro des gammes
        Dana Values = Diatonic Poids & Divise Sept
        Logic histoire:
        Des gammes (dan.keys()) avec une unité majeure
        Diatonic (dan.values()) = 7 Modes signés & pesants
            La signature modale [[0,-3,-5,,,]_ Tonalité
            La démultiplication modale _[147,21.0,3.0,,,]]
                Divise Poids par 7 jusqu'à zéro entier
    Réunir: 1- Les tonalités aux mêmes poids. 2- Les poids aux mêmes rangs. 3- Les tonalités aux mêmes degrés
        1)  Les gammes à masses égales. 2) Les reliefs des pesants. 3) Les fondements réguliers.
    """
    (lineno(), 'GlobEnModes.Dana[dana]', len(dana), '[[forme.classic][poids]]', 'GAM1', gam1)
    # 73 GlobEnModes.Dana[dana] 66 [[forme.classic][poids]]
    # GAM1 [21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66]
    maj_poids[66], maj_rang[66], maj_mode[66] = [], [], []
    for dan in range(1, len(dana) + 1):  # Épisode Dana
        tous_poi[dan], tous_mod[dan] = [], []
        dan_mode[dan], dan_rang[dan], dan_poids[dan] = [], [], []
        if dan == 66:
            """Initialisation des tableaux majeurs du 66"""
            # Recherche Point Go & tonic [0, 0, 0, 0, 0, 0, 0] :maj_mode[66]
            # Enregistrement Poids modaux :maj_poids[66]
            (lineno(), 'Dana', dana[dan], dan)
            # 84 Dana [[[0, 0, 0, 5, 0, 0, 0], [588, 84.0, 12.0, 1.7142857142857142,
            # 0.24489795918367346]], [[0, -3, -4, 0, 0, -7, -8], [0]], [[0, 0, -4, 0, 0, 0, -8],
            # [490, 70.0, 10.0, 1.4285714285714286, 0.20408163265306123]], [[0, 0, 0, 0, 0, 0, 0],
            # [833, 119.0, 17.0, 2.4285714285714284, 0.3469387755102041]], [[0, -3, -4, 0, -6, -7, -8],
            # [196, 28.0, 4.0, 0.5714285714285714]], [[0, 0, -4, 0, 0, -7, -8], [343, 49.0, 7.0, 1.0]],
            # [[0, 0, 0, 0, 0, 0, -8], [784, 112.0, 16.0, 2.2857142857142856, 0.32653061224489793]]] 66
            for dn in range(7):
                tm = 0
                dd = dana[dan][dn][0]  # 66.dd: = [0, 0, 0, 5, 0, 0, 0]
                maj_poids[66].append(dana[dan][dn][1][0])  # 66.maj_poids: = 588
                for ide in dd:
                    tm += ide       # tm nul = ide§ nul§
                if tm == 0:         # 66.dd: = [0, 0, 0, 0, 0, 0, 0] = Tonique majeure
                    tempo = dn      # 66.Tempo: dana[dan][tempo]
                    maj_mode[66] = [dana[dan][dn][0]]   # Maj.Mode [0, 0, 0, 0, 0, 0, 0]
                    maj_mode[66].append(tempo)          # Maj.Mode [[0, 0, 0, 0, 0, 0, 0], 3]
                (lineno(), dn, '     Dd', dd, '\tDan', dan)
                # 92 3      Dd [0, 0, 0, 0, 0, 0, 0] 	Dan 66
            maj_lest = maj_poids[66].copy()
            maj_lest.sort()
            for mp in maj_poids[66]:
                maj_rang[66].append(maj_lest.index(mp))
            # print(f'* maj_poids:{maj_poids[66]}  \n* maj_rang:{maj_rang[66]}')
            # print(f'* maj_lest:{maj_lest}  \n* maj_mode:{maj_mode[66]}')
        # print(lineno(), dan, dana[dan][0][0])
        """Cette boucle récupère les modes maj7
            Comme on sait que les gammes fondamentales sont toutes...
                Ou chacune a une septième majeure"""
        for dn in range(7):  # Séquence les modes diatoniques (Mj7 & Non maj7)
            tous_poi[dan].append(dana[dan][dn][1])
            dan_poids[dan].append(dana[dan][dn][1][0])  # Poids Tonalité
            if dana[dan][dn][0][-1] == 0:
                vide = dana[dan][dn][0], dn
                tous_mod[dan].append(vide)
                # print(' ', lineno(), dan, 'Dn', dana[dan][dn][0])
        maj_lest = dan_poids[dan].copy()
        maj_lest.sort()
        for mp in dan_poids[dan]:
            dan_rang[dan].append(maj_lest.index(mp))
        # print(f' Dan: {dan} Dana :{dana[dan][0]}')
        # print(f'* DanPoi:{dan_poids[dan]}  \n* DanRng:{dan_rang[dan]}')
        # print(f'* MajMod:{dan_mode[dan]}  \n* MajLes:{maj_lest} Dan:{dan}')
        # print(f'* TouMod:{len(tous_mod[dan])} \n* TouPoi:{len(tous_poi[dan])}')
        # break
    # print(f' Nombre de poids de dan : {len(dan_poids)} exemplaires')
    # print(f' Nombre les poids modaux : {len(tous_poi)} gammes par 7 modes')  # {tous_poi[66]}
    # :iso_poids= Gammes de mêmes poids et rangs
    # :dif_poids= Mêmes rangées
    # :dat_rang= Tous les rangs
    vide, iso_poids, dif_poids, dat_rang = [], [], [], []
    for dr in dan_rang.values():  # Construction Data Rangs
        if dr not in dat_rang:
            dat_rang.append(dr)
            memo = ''.join(str(y) for y in dr)
            ego_rang[memo] = []
    for c1 in range(1, 67):
        ego_poids[dan_poids[c1][0]] = [c1]
        memo = ''.join(str(y) for y in dan_rang[c1])
        if c1 not in ego_rang[memo]:
            ego_rang[memo].append(c1)
        # ego_rang[c1] = []
        # print(' \n Dan_poids[c1]', c1, dan_poids[c1])
        # print(' ego_rang[memo]', c1, memo, ego_rang[memo])
        # print(f' ****** Clé 1:{c1}  LenIso:{len(iso_poids)}{iso_poids}')
        for c2 in range(1, 67):
            if c1 != c2:  # :c1==c2= Mêmes gammes
                if dan_poids[c1] == dan_poids[c2]:  # :dan_poids
                    if len(iso_poids) == 0:
                        c0 = [c1, c2]
                        vide = c0, dan_poids[c1]
                        iso_poids.append(vide)
                        # print('Vide', vide, iso_poids[0])
                    else:
                        if dan_poids[c2] not in iso_poids[0][0]:
                            vide = c2
                            iso_poids[0][0].append(vide)
                    # print(f' {c1} Clé_2:{c2} Poids:{dan_poids[c1][0]}, {iso_poids}')
                elif dan_rang[c1] == dan_rang[c2]:
                    dif_poids.append(c2)
                    # print(f' ** {c1} Clé_2:{c2} Rang:{dan_rang[c1]}, {dif_poids}')
            if c2 == 66:
                pass
                # print(f' *66* {c1} Clé_2:{c2} Rang:{dan_rang[c1]}, {dif_poids}')
        if iso_poids:
            for ip in iso_poids[0][0]:
                if ip not in ego_poids[dan_poids[c1][0]]:
                    ego_poids[dan_poids[c1][0]].append(ip)
            # ego_poids[dan_poids[c1][0]].append(iso_poids[0][0].copy())
        if len(dif_poids) > 0:
            memo = ''.join(str(y) for y in dan_rang[c1])
            for dp in dif_poids:
                if dp not in ego_rang[memo]:
                    ego_rang[memo].append(dp)
        dif_poids.clear()
        iso_poids.clear()
        # if c1 == 6: break
    # Lecture Ego Poids
    filer = []
    for kilo, vole in ego_poids.items():
        if vole:
            for vi in vole:
                vii = vi, kilo
                if vii not in filer:
                    filer.append(vii)
    # Lecture Ego Rangs
    filet = []
    for nom, rng in ego_rang.items():
        for rn in rng:
            if rn not in filet:
                filet.append(rn)
    # filer.sort()
    # print('Nombre Filer', len(filer),  'Long ego_poids', len(ego_poids), '\n ego_poids', ego_poids)
    # filet.sort()
    # print('Nombre Filet', len(filet), 'Long ego_rang', len(ego_rang), '\n ego_rang', ego_rang)

    # print('**** \n65', dana[65])
    # print('**** \n66', dana[66])
    for kd, vd in dana.items():
        # print('**GEM(Dana_fonc()**', kd, vd)
        # print()
        td, f0 = {}, -1
        for v1 in vd:
            # print(kd, v1[0], '\t', [v1[1][0]])
            f0 += 1
            f1 = 0
            td[f0] = []
            if v1[0][-1] == 0:
                # f1 = 0
                # print(kd, v1[0], 'f0', f0, 'f1', f1)
                for v2 in v1[0]:
                    if v2 != 0:
                        f1 += 1
                # print(kd, v1[0], 'f0', f0, 'f1', f1)
            else:
                f1 = 8
            td[f0] = f1
            # break
        mtd = min(td.values())                  # Valeur Minimum
        # ctd = list(td.values()).count(mtd)      # Nombre de Minimum(s)
        # Pour afficher Dana & Minimums altérés
        # print('* kd', kd, 'td', td)
        # print('* kd', kd, 'mtd', mtd, 'ctd', ctd)

        for kf, vf in td.items():
            if vf == mtd:
                # (f' Kf:{kf} Vf:{vf}  Dana:{dana[kd][kf][0]}')
                break
        # if kd == 3: break
    """Blague (science/musique)"""


def seption(mode_poids, k1, pc1, gm1):
    """Réception des poids modaux standards à augmenter"""
    ('\n', lineno(), ' ¤ GEM Mode_poids=', mode_poids, 'K1=', k1, 'PC1=', pc1, 'Gm1=', gm1)
    """ 219  ¤ GEM Mode_poids= [[0, 0, 0, 5, 0, 0, 0], [0, -3, -4, 0, 0, -7, -8], 
    [0, 0, -4, 0, 0, 0, -8], [0, 0, 0, 0, 0, 0, 0], [0, -3, -4, 0, -6, -7, -8], 
    [0, 0, -4, 0, 0, -7, -8], [0, 0, 0, 0, 0, 0, -8]] K1= 66 PC1= ['101010110101', '110101011010', 
    '101101010110', '101011010101', '110101101010', '101101011010', '101011010110'] 
    Gm1= [21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66]"""
    goo = []
    cumul = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    dic_analyse[k1] = []  # :Dana initie table
    dic_pc[k1] = []  #
    dic_pc[k1].append(pc1)
    # Dico gamme_poids & Key_mode Majeur Comparer
    for gpk, gpv in gamme_poids.items():  # Mode_poids & Comparer Mode naturel
        """:gpv = [0,0,0,0,0,0,0],[0,0,-4,0,0,0,-8],"""
        for com in gpv:  # :gpv= Valeur Majeure
            """:com = [0,0,0,0,0,0,0]"""
            """:mode_poids = [[0,-3, -5, 7, 7, 7,0],[0,-3, -5, -6, 7, 7,0],"""
            for mod in mode_poids:  # :mod= Section modale Non-Majeure
                modal, cc = [], 0
                """:mod = [0,-3, -5, 7, 7, 7,0]"""
                for mo in mod:  # :mo= Signature Non Majeure
                    diff = mo - com     # :com= Unité valeur Majeure
                    cc += diff          #
                modal.append(cc)        # Cumul cc Entre Maj ou pas
                cumul[gpk].append(modal)
    # Par degré[Cumul poids cumul.keys(values)]
    mana1, mana2 = [], []
    for kayac, rame in cumul.items():
        aaa = 0
        for van in rame:
            aaa += van[0]
        mana1.append(aaa)           # Version signée (±) Util False
        mana2.append(abs(aaa))      # Version absolue (|) Util True
    # Démultiplications des moyennes pour seption notes
    moyen = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    goo.clear()
    goo.append(k1)
    for moi in range(len(mana2)):  # Démultiplier :mana2 (|) Util True
        moyen[moi + 1].append(mana2[moi])
        accroc = mana2[moi]
        plouc = [mode_poids[moi], moyen[moi + 1]]
        dic_analyse[k1].append(plouc)  # :Dana value plouc
        """Échappement Fichier Notes Analyses TXT :mana2 (|) Util True
            Démultiplication Facteur 7 :
                Constituant à partir :mana2 (|) Util True. Série(centaines à zéro)"""
        (lineno(), moi, 'For moi in...  M_P', mode_poids[moi], 'M:', moyen[moi + 1])
        # 269 6 For moi in...  M_P [0, 0, 0, 0, 0, 0, -8], M:[784]
        # Fonction de démultiplication facteur 7
        while accroc > 1:  # Gammes Log.7
            accroc /= 7
            if accroc > 0:
                moyen[moi + 1].append(accroc)
                if int(accroc) == 1:
                    contre = accroc, mode_poids[moi]
                    if contre[1][-1] == 0:
                        goo.append(contre)
    (lineno(), 'Plouc', k1, type(k1), 'Dic_analyse', dic_analyse[k1][0])
    #  280 Plouc:66 <class 'int'> Dic_analyse:[[0, 0, 0, 5, 0, 0, 0],
    #  [588, 84.0, 12.0, 1.7142857142857142, 0.24489795918367346]]
    """GlobEnModes = Gammes"""
    fil_analyse = open('globdic_Dana.txt', 'w')
    for ky1, va1 in dic_analyse.items():  # dic_analyse: Infos Dana
        mm = str(ky1) + str(va1)
        mm += '\n'
        fil_analyse.write(mm)
    fil_analyse.close()  # Écriture fichier globdic_Dana.txt

    if len(dic_analyse.keys()) == 66:
        dana_fonc(dic_analyse, gm1)
        glob_in_acc.inv_acc(dic_pc)


if __name__ == '__main__':
    print(f' GEM Quelle seption !')
    mode_bi = ['111000001111', '111100000111', '111110000011',
               '111111000001', '111111100000', '100000111111',
               '110000011111']
    mages_bi = ['101011010101', '101101010110', '110101011010',
                '101010110101', '101011010110', '101101011010',
                '110101101010']
    mode_po0 = [[0, -3, -5, 0, -6, -8, 0], [0, -3, -5, -6, -6, -8, -10],
                [0, 4, 4, 5, 0, 7, 0], [0, -3, 4, 5, 0, -7, 0],
                [0, -3, -5, 5, 0, -7, -9], [0, 3, 0, 0, 7, 7, 0],
                [0, -3, 0, 0, -6, 7, 0]]
    mode_po = [[0, -3, -4, 6, 6, 0, 0], [0, -3, -5, -5, 6, 0, -8],
               [0, 0, -4, -5, -6, 7, 0], [0, -3, -4, -5, -7, -8, 0],
               [0, -3, -5, -5, -7, -9, -10], [0, 4, 4, 5, 6, 0, -8],
               [0, 0, 5, 6, 6, 7, 0]]
    mages_po = [[0, 0, 0, 0, 0, 0, 0], [0, 0, -4, 0, 0, 0, -8],
                [0, -3, -4, 0, 0, -7, -8], [0, 0, 0, +5, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, -8], [0, 0, -4, 0, 0, -7, -8],
                [0, -3, -4, 0, -6, -7, -8]]
    gamme_po = {1: [0, 0, 0, 0, 0, 0, 0], 2: [0, 0, -4, 0, 0, 0, -8],
                3: [0, -3, -4, 0, 0, -7, -8], 4: [0, 0, 0, +5, 0, 0, 0],
                5: [0, 0, 0, 0, 0, 0, -8], 6: [0, 0, -4, 0, 0, -7, -8],
                7: [0, -3, -4, 0, -6, -7, -8]}
    seption(mode_po, 1, {}, [])
