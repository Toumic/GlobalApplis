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

# lineno() Pour consulter le programme grâce au suivi des print's
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

dic_analyse = {}  # :Dana initie dico
dic_pc, dic_gammes, tab_faible = {}, {}, {}
# Les clefs de ces dictionnaires valent chacune une gamme
tous_poi, tous_mod = {}, {}  # Poids division Modes diatonic's
dan_mode, dan_rang, dan_poids = {}, {}, {}  # Dico:dan. Trier infos
ego_mode, ego_rang, ego_poids = {}, {}, {}  # Dico:ego. Union gammes
maj_mode, maj_rang, maj_poids = {}, {}, {}  # Dico:maj. Diatonic majeur
# Pour éviter de tourner autour du pot!
maj_clef = [66]  # Table:maj_clef. Clef référence majeure. :dana.keys().
# Dictionnaire final des noms des gammes
noms_dic = {66: 'maj'}

# Classement Gammes.mécanic
"""Les mutations sont chiffrées :
Noms mécaniques unic ou couple degrés centrés aux signes conjoins.
Les noms des gammes ont plusieurs formes :
    1- Forme simple. Do maj | Do -3 | Do -5         Max(1 degré, 1 signe)
    2- Forme double. Do -34+ | Do -25 | Do -36+     Max(2 degrés, 1 signe)
        Max(2 degrés, 2 signes) Les degrés prioritaires..
    3- Forme organe. Do o34x | Do ^3 | Do *5        Max(2 degrés, 3 signes)
    4- Forme groupe. Do -235 | Do +456              Ras(mêmes signes)
Les nomes des gammes ont deux types numériques :
    1- Type  entier. Voir exemples ci-dessus.
    2- Type décimal. Do -34.+56 | Do +24.-36        Associe(Type entier)
Les priorités des traitements :
    1- Traitement clustérien solution altéractivité.
    2- Traitement signature modèle altération."""
signes = ['', '+', 'x', '^', '^+', '^x', 'o*', '-*', '*', 'o', '-']


def maj7_fonc(unic, fondre):
    """Les gammes fondamentales enfin!
    Unic: Les quinze modèles légers renseignés
    Fondre: Les 66 gammes et leurs modes diatoniques binaires"""
    stop = False

    def fond_gam(mode, fol):
        """Développement diatonique du mode binaire
            Transforme binaire en unaire pour calculer
         Créer une liste de la topologie et mettre en forme le nom
         Format(nom) = Max(2 degrés, 2 signes) (Ligne 59)..
            Altéractifs = o3, +3, -4, o4, x4, o5, x5,,"""
        alteractif = {'o3': ['o3', '-2'], '+3': ['+3', '+4'], '^3': ['^3', '^4', 'x5', '+6'],
                      '-4': ['-4', '-3'], 'o4': ['o4', 'o3', '-2'], 'x4': ['x4', '+5'],
                      '*5': ['*5', 'o4', 'o3', '-2'], 'o5': ['o5', '-4', '-3'],
                      'x5': ['x5', '+6'], 'o6': ['o6', '-5']}
        signatures = {}
        # '+': [], 'x': [], '^': [], '^+': [], '^x': [],
        # 'o*': [], '-*': [], '*': [], 'o': [], '-': []

        g_maj = [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
        i_mod, z = [], 0
        for i in mode:              # Construction mode unaire
            if i == '1':            # [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
                z += 1
                y = z
            else:
                y = 0
            i_mod.append(y)
        print(' **', lineno(), 'I_mod', i_mod)
        photo, z = [], 0
        for im in i_mod:                            # Section lecture mode unaire
            if im > 0:
                pro1 = i_mod.index(im)
                pro2 = g_maj.index(im)
                prout = pro1 - pro2
                if prout != 0:
                    ph = signes[prout] + str(im)
                    photo.append(ph)
            z += 1
        for hot in photo:
            ist = (list(hot)[:len(hot)-1])[0]
            if ist not in signatures.keys():
                signatures[ist] = [fol]
                signatures[ist].append(hot)
            else:
                signatures[ist].append(hot)
            print(lineno(), signatures[ist], 'Photo', photo)
        duo = []
        for ks, kv in signatures.items():
            cou = ''
            if len(signatures.keys()) == 1:
                if len(kv) == 2:
                    cou = kv[1]
                if len(kv) > 2:
                    cou = kv[1] + kv[2][1:]
                # (fol, 'KS', ks, 'KV', kv, 'COU', cou)
            elif len(duo) != len(signatures.keys()):
                if not duo:
                    duo.append(kv[1])
                    # (lineno(), duo)
                else:
                    du = kv[1][1] + kv[1][0]
                    duo.append(du)
                if len(duo) == len(signatures.keys()):
                    cou = duo[0] + duo[1]
                    # ('     ', lineno(), 'Kv', kv, 'Cou', cou)
            noms_dic[kv[0]] = cou
            print(lineno(), fol, 'KS', ks, 'KV', kv, 'COU', cou)
        (lineno(), '  noms_dic', noms_dic[66], '\n')

    """GlobEnModes = Gammes-fichier:globdicTgams.txt (Ligne 72)"""
    fil_gammes = open('globdicTgams.txt', 'r')
    fix = 0
    for fil in fil_gammes:  # dic_analyse: Infos gammes
        fix += 1
        tab_faible[fix] = []
        ff = fil  # fil_gammes: Numéro gamme
        (lineno(), 'Fix', fix, 'FF', ff[:len(ff) - 1])  # [:len(ff)-1]: Moins retour chariot
        # 88 Fix 61 FF ['1', '0', '2', '-3', '0', '0', '+4', '5', '0', '6', '0', '7',
        # [((1, 61), '101100110101')]]

        if fix in unic.keys():  # Unic: Premières gammes faciles (Ligne 71)
            (lineno(), fix, 'unic[fix][-1][0][1] =', unic[fix][-1][0][1])
            # 91 66 unic[fix][-1][0][1] = 101011010101
            # fond_gam(unic[fix][-1][0][1], fix)  # fond_gam: Fonction envoi(unic)
        elif fix in fondre.keys():  # Fondre: Gammes secondaires (Ligne 72)
            my2 = []  # my2: Créer liste des poids légers par gamme
            for mz in fondre[fix]:
                my = mz[0][1]
                tab_faible[fix].append(my)
                my2.append(my)
            my2.sort()  # my2: Trié
            for m22 in my2:  # my2: Lecture liste
                for m23 in fondre[fix]:
                    if m22 in m23[0]:
                        print('\n ** ** ', lineno(), fix, 'my2:', my2, 'M22:', m22, '    M23', m23[0][0])
                        #  **** ****  173 63 my2 [7, 10, 18] M23 100101101101
                        fond_gam(m23[0][0], fix)           # fond_gam: Fonction envoi(fondre)
                    if stop is True:
                        break
            (lineno(), fix, 'MY2', my2, 'Fondre', fondre[fix][0], '\n')
    (lineno(), 'GEM DicFondre', fondre[66], '\nUnic', unic.keys())
    fil_gammes.close()  # Lecture fichier globdicTgams.txt


def dana_fonc(dana):
    """
    Les dictionnaires {dan/ego/maj}:
        Tous. Intégrales Poids/Modes
        Dan. Enregistrer infos gammes pour analyser
        Ego. Répertorier gammes mêmes types
        Maj. Référencer diatonic majeur
    Dana est le dictionnaire entrant:
        Dana Keys = Numéros des gammes
        Dana Values = Diatonic Poids & Divise Sept
        Logic histoire:
        Des gammes (dan.keys()) avec une unité majeure
        Diatonic (dan.values()) = 7 Modes signés & pesants
            La signature modale [[0,-3,-5,,,]_ Tonalité
            La démultiplication modale _[147,21.0,3.0,,,]]
                Divise Poids par 7 jusqu'à zéro entier
    Union: 1- Les tonalités aux mêmes poids. 2- Les poids aux mêmes rangs. 3- Les tonalités aux mêmes degrés
        1)  Les gammes à masses égales. 2) Les reliefs des pesants. 3) Les fondements réguliers."""

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
                    tm += ide  # tm nul = ide§ nul§
                if tm == 0:  # 66.dd: = [0, 0, 0, 0, 0, 0, 0] = Tonique majeure
                    tempo = dn  # 66.Tempo: dana[dan][tempo]
                    maj_mode[66] = [dana[dan][dn][0]]  # Maj.Mode [0, 0, 0, 0, 0, 0, 0]
                    maj_mode[66].append(tempo)  # Maj.Mode [[0, 0, 0, 0, 0, 0, 0], 3]
                (lineno(), dn, '     Dd', dd, '\tDan', dan)
                # 101 3      Dd [0, 0, 0, 0, 0, 0, 0] 	Dan 66
            maj_lest = maj_poids[66].copy()
            maj_lest.sort()
            for mp in maj_poids[66]:
                maj_rang[66].append(maj_lest.index(mp))
            # ('* maj_poids:', maj_poids[66], '\n* maj_rang:', maj_rang[66])
            # ('* maj_lest:', maj_lest, '\n* maj_mode:', maj_mode[66])
            # * maj_poids: [588, 0, 490, 833, 196, 343, 784]
            # * maj_rang: [4, 0, 3, 6, 1, 2, 5]
            # * maj_lest: [0, 196, 343, 490, 588, 784, 833]
            # * maj_mode: [[0, 0, 0, 0, 0, 0, 0], 3]

        """Cette boucle récupère les modes maj7
            Les gammes fondamentales ont une septième majeure"""
        for dn in range(7):  # Séquence les modes diatoniques (Mj7 & Non maj7)
            tous_poi[dan].append(dana[dan][dn][1])
            dan_poids[dan].append(dana[dan][dn][1][0])  # Poids Tonalité
            if dana[dan][dn][0][-1] == 0:  # Filtre 7èmes majeures
                vide = dana[dan][dn][0], dn
                tous_mod[dan].append(vide)
                (' ', lineno(), dan, 'Dn', dana[dan][dn][0])
                # 122 66 Dn [0, 0, 0, 5, 0, 0, 0]
                # 122 66 Dn [0, 0, 0, 0, 0, 0, 0]
        maj_lest = dan_poids[dan].copy()
        maj_lest.sort()
        for mp in dan_poids[dan]:
            dan_rang[dan].append(maj_lest.index(mp))
        # (' Dan:', dan, 'Dana[dan][0] :', dana[dan][0])
        # ('* DanPoi:', dan_poids[dan], '\n* DanRng:', dan_rang[dan])
        # ('* MajMod:', dan_mode[dan], '* MajLes:', maj_lest, 'Dan:', dan)
        # ('* TouMod:', len(tous_mod[dan]), '* TouPoi:', len(tous_poi[dan]))
        # Dan: 66 Dana[dan][0] : [[0, 0, 0, 5, 0, 0, 0],
        # [588, 84.0, 12.0, 1.7142857142857142, 0.24489795918367346]]
        # * DanPoi: [588, 0, 490, 833, 196, 343, 784]
        # * DanRng: [4, 0, 3, 6, 1, 2, 5]
        # * MajMod: [] * MajLes: [0, 196, 343, 490, 588, 784, 833] Dan: 66
        # * TouMod: 2 * TouPoi: 7
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
        for c2 in range(1, 67):
            if c1 != c2:  # Quand :c1==c2: Mêmes gammes
                if dan_poids[c1] == dan_poids[c2]:  # :dan_poids
                    if len(iso_poids) == 0:
                        c0 = [c1, c2]
                        vide = c0, dan_poids[c1]
                        iso_poids.append(vide)
                    else:
                        if dan_poids[c2] not in iso_poids[0][0]:
                            vide = c2
                            iso_poids[0][0].append(vide)
                elif dan_rang[c1] == dan_rang[c2]:
                    dif_poids.append(c2)
        # ('_C1', c1, ' Dan_poids[c1]', dan_poids[c1])
        # ('_C1', c1, ' ego_rang[memo]', ego_rang[memo], 'Ranger', memo)
        # (f'_ ****** Clé 1:{c1}  LenIso:{len(iso_poids)}|{iso_poids}')
        # _C1 66  Dan_poids[c1] [588, 0, 490, 833, 196, 343, 784]
        # _C1 66  ego_rang[memo] [47, 65, 66] Ranger 4036125
        # _ ****** Clé 1:66  LenIso:1|[([66, 65], [588, 0, 490, 833, 196, 343, 784])]
        if iso_poids:  # iso_poids: Construit :ego_poids
            for ip in iso_poids[0][0]:
                if ip not in ego_poids[dan_poids[c1][0]]:
                    ego_poids[dan_poids[c1][0]].append(ip)
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
    ('Nombre Filer', len(filer), 'Long ego_poids', len(ego_poids), '** ego_poids', ego_poids)
    # Nombre Filer 66 Long ego_poids 26 ** ego_poids {147: [1], 266: [18, 2, 5, 6],
    # 315: [33, 3, 4, 29], 378: [38, 7, 13, 22, 31], 413: [21, 8], 350: [20, 9],
    # 224: [19, 10], 308: [15, 11], 406: [54, 12, 28, 32, 34, 37], 238: [17, 14],
    # 343: [43, 16, 27, 35, 36], 329: [26, 23], 455: [25, 24], 301: [30], 476: [55, 39, 40, 41],
    # 371: [42], 427: [49, 44], 518: [58, 45], 392: [60, 46], 567: [47], 469: [57, 48, 50, 52, 56],
    # 462: [59, 51], 385: [53], 539: [64, 61], 497: [63, 62], 588: [66, 65]}
    # Lecture Ego Rangs
    filet = []
    for nom, rng in ego_rang.items():
        for rn in rng:
            if rn not in filet:
                filet.append(rn)
    ('Nombre Filet', len(filet), 'Long ego_rang', len(ego_rang), '** ego_rang', ego_rang)
    # Nombre Filet 66 Long ego_rang 10 ** ego_rang {'0352146': [1], '1253046': [2, 10, 14, 17, 19, 5, 6, 18],
    # '2153046': [3, 11, 15, 23, 26, 30, 4, 29, 33], '2154036': [7, 8, 9, 12, 20, 21, 28, 32, 34, 37, 42, 46,
    # 53, 54, 60, 13, 22, 31, 38], '2153036': [16, 27, 35, 36, 43], '2145036': [24, 44, 49, 51, 59, 25],
    # '3145026': [39, 48, 50, 52, 56, 57, 40, 41, 55], '3045126': [45, 62, 63, 58], '4036125': [47, 65, 66],
    # '3035126': [61, 64]}
    """Blague (science/musique)"""


def seption(mode_poids, k1, pc1, gm1, maj7):
    """Réception des poids modaux standards à augmenter & Création 'globdic_Dana.txt'.
    L'argument 'maj7' est le dictionnaire des modes maj 7èmes et poids standards par gamme"""
    ('\n', lineno(), 'K1=', k1, ' ¤ GEM M_P', mode_poids, '\nPC1=', pc1, '\nGm1=', gm1.keys())
    # 238 K1= 66  ¤ GEM M_P [[0, 0, 0, 5, 0, 0, 0], [0, -3, -4, 0, 0, -7, -8], [0, 0, -4, 0, 0, 0, -8],
    # [0, 0, 0, 0, 0, 0, 0], [0, -3, -4, 0, -6, -7, -8], [0, 0, -4, 0, 0, -7, -8], [0, 0, 0, 0, 0, 0, -8]]
    # PC1= ['1', '0', '2', '0', '3', '4', '0', '5', '0', '6', '0', '7', [((0, 66), '101011010101')]]
    # Gm1= dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
    """if maj7:
        for magie in maj7.keys():
            print(lineno(), 'Quant', magie, 'Magic Majeur 7ème \n', maj7[magie])
            # 245 Quant 66 Magic Majeur 7ème
            # [(('101010110101', 5), 66), (('101011010101', 0), 66)]"""
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
                    diff = mo - com  # :com= Unité valeur Majeure
                    cc += diff  #
                modal.append(cc)  # Cumul cc Entre Maj ou pas
                cumul[gpk].append(modal)
    # Par degré[Cumul poids cumul.keys(values)]
    mana1, mana2 = [], []
    for kayac, rame in cumul.items():
        aaa = 0
        for van in rame:
            aaa += van[0]
        mana1.append(aaa)  # Version signée (±) Util False
        mana2.append(abs(aaa))  # Version absolue (|) Util True
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
        mm = str(ky1) + str(va1)  # ky1: Numéro gamme
        mm += '\n'  # va1: Modes poids augmentés
        fil_analyse.write(mm)
    fil_analyse.close()  # Écriture fichier globdic_Dana.txt

    if len(dic_analyse.keys()) == 66:
        dana_fonc(dic_analyse)
        maj7_fonc(gm1, maj7)
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
    seption(mode_po, 1, {}, {}, {})
