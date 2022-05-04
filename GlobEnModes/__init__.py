# Python utf8
# En cours de finalisation
# mardi 27 juillet 2021

# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# GlobEnModes
# Moulin modal à comparaisons majeures
#

import inspect
import os
import GlobInverseAcc
from typing import Callable

glob_in_acc = GlobInverseAcc
inspect.getsource(os)

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Nécessités pour repérages :
"""
Tableau des signatures majeures (Comparaisons, :gamme_poids:)
    :gamme_poids: = {1: [0,0,0,0,0,0,0], 2: [0,0,-4,0,0,0,-8],
Tableaux modèles supposés fondamentaux (Toniques)
    1: Signature numérique pour chaque mode diatonique
        :mode_poids = [[0,-3, -5, 7, 7, 7,0],[0,-3, -5, -6, 7, 7,0],,,
    2: Signature binaire correspondante
        :mode_biner = ['111000001111','111100000111','111110000011',,,
Plonger dans le code à l'aide des 'print':
    Une ligne de code faite ainsi, fonctionne: (choses à printer),
    print(1) <=> (1) = OK. Copier print à (1) => print(1)."""

mages_biner = ['101011010101', '101101010110', '110101011010',
               '101010110101', '101011010110', '101101011010',
               '110101101010']

gamme_poids = {1: [0, 0, 0, 0, 0, 0, 0], 2: [0, 0, -4, 0, 0, 0, -8],
               3: [0, -3, -4, 0, 0, -7, -8], 4: [0, 0, 0, +5, 0, 0, 0],
               5: [0, 0, 0, 0, 0, 0, -8], 6: [0, 0, -4, 0, 0, -7, -8],
               7: [0, -3, -4, 0, -6, -7, -8]}

dic_analyse = {}  # :Dana initie dico
dic_diatonic = {}  # :Seption initie dico
dia_binaire = {}  # :Maj7_fonc initie binaires
dic_pc, dic_gammes, tab_faible = {}, {}, {}
# Les clefs de ces dictionnaires valent chacune une gamme
tous_poi, tous_mod = {}, {}  # Poids division Modes diatonic's
dan_mode, dan_rang, dan_poids = {}, {}, {}  # Dico:dan. Trier infos
ego_mode, ego_rang, ego_poids = {}, {}, {}  # Dico:ego. Union gammes
maj_mode, maj_rang, maj_poids = {}, {}, {}  # Dico:maj. Diatonic majeur
# Pour éviter de tourner autour du pot !
maj_clef = [66]  # Table : maj_clef. Clef référence majeure. :dana.keys().
# Conteneur d'essai
# essai, compteur = [], [0]

# Classement Gammes.mécanic
"""Les mutations sont chiffrées :
Noms mécaniques unic ou couple degrés centrés aux signes conjoins.
Les noms des gammes ont plusieurs formes :
    1- Forme simple. Do maj | Do -3 | Do -5         Max(1 degré, 1 signe)
    2- Forme double. Do -34+ | Do -25 | Do -36+     Max(2 degrés, 1 signe)
        Max(2 degrés, 2 signes) Les degrés prioritaires..
    3- Forme organe. Do o34x | Do ^3 | Do *5        Max(2 degrés, 3 signes)
    4- Forme groupe. Do -235 | Do +456              Ras(mêmes signes)
Les noms des gammes ont deux types numériques :
    1- Type  entier. Voir exemples ci-dessus.
    2- Type décimal. Do -34.+56 | Do +24.-36        Associe(Type entier)
Les priorités des traitements :
    1- Traitement clustérien solution altéractivité.
    2- Traitement signature modèle altération."""

# Signes = Matrice des altérations
signes = ['', '+', 'x', '^', '+^', 'x^', 'o*', '-*', '*', 'o', '-']

# Altéraction polyvalent
alteractif = {
    'x2': ['x2', '+3', '+4'], '^2': ['^2', 'x3', 'x4', '+5'], 'o3': ['-2'],
    '+3': ['+3', '+4'], 'x3': ['x3', 'x4', '+5'], '-4': ['-4', '-3'],
    'x4': ['x4', '+5'], 'o5': ['o5', '-4', '-3'], 'o6': ['o6', '-5'],
    '*6': ['*6', 'o5', '-4', '-3'], 'o7': ['o7', '-6'],
    '*7': ['*7', 'o6', '-5'], '-*7': ['-*7', '*6', 'o5', '-4', '-3']}

'''Configuration des éléments :
    Entiers)                    Caractères)
    num = Numéro de gamme       binaire = 101011010101
    poids = Poids modal         unaire = 1o2o34o5o6o7
    typo = Type de gamme        nomme = Nom de gamme
    Liste) photos = Notes altérées (-2, x4, +5) telles qu'elles sont.'''
groupe, picolo, signaux, brouillon, toniques = {}, {}, {}, {}, {}
# Création dictionnaire picolo signaux[].append()
for pi in range(1, 67):  # Clés + Table
    picolo[pi] = [], []
    signaux[pi] = []
    brouillon[pi] = []
    toniques[pi] = []

# Table des degrés
table_deg = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII']


def maj7_fonc(table, unic, fondre, binez):  # MAJ7 Fonction 1ères entrées UNIC/FONDRE
    """Les gammes fondamentales enfin !
    Unic : Les quinze modèles légers renseignés. [Alpha. Binaire. Poids]
        **maj7(unic)** 253 66 unic[fix][-1][0][1] = 101011010101
        ... /**.| |. ** 137 ** PHOTO_temps réel:____ ['maj']
    Fondre : Les 66 gammes et leurs modes diatoniques binaires"""

    def fond_gam(mode, fol):  # FOND Fonction
        """Développement diatonique du mode binaire
            Transforme binaire en unaire à calculer
         Crée une liste de la topologie et met en forme le nom
         Format(nom) = Max(2 degrés, 2 signes) (Ligne 59).
            Altéractifs = o3, +3, -4, o4, x4, o5, x5,"""
        '''Les intermédiaires : Définition altéractive.
        La    direction altéractive
            Lecture de gauche à droite pour les signes augmentés: '+', 'x', '^', '+^', 'x^'
            Lecture de droite à gauche pour les signes  diminués: '-', 'o', '*', '-*', 'o*'
        La        liste affirmative
            Ses éléments sont les terminaisons altératives :
                Cluster bémol | 1, -2, o3, o4 pour o4   | 1234000506078
                Cluster dièse | x5, +6, 7 pour x5       | 1020340005678
        Le dictionnaire altéractif
            Ses éléments sont des évènements intermédiaires :
                Cluster bémol | 2, -3, -4, o5 pour o5   | 1023450006078
                Cluster dièse | x3, x4, +5 pour x3      | 1020003456078'''
        signatures = {}
        dicter = {}
        g_maj = [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
        i_mod, z = [], 0
        for i_ in mode:  # Construction mode unaire
            if i_ == '1':  # [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
                z += 1
                y = z
            else:
                y = 0
            i_mod.append(y)
        picolo[fol][0].append(i_mod)
        if '2' in table:
            print('****', lineno(), 'I_mod', i_mod, '***********FOL', fol, 'n Picolo', 'fol')
        ''' Construction PHOTO d'où TOPO
            La photo est vue en ordre croissant du degré ou (1234567).
            *   L'ordre du degré numérique est donné par défaut = (1234567),
            *    une série modale de comparaison majeure finalement signée (b ou #).'''
        photo, z = [], 0
        for im in i_mod:  # Section lecture mode unaire
            if im > 0:
                pro1 = i_mod.index(im)  # Exemple : I_mod = [1, 0, 2, 3, 0, 0, 4, 0, 5, 6, 0, 7]
                pro2 = g_maj.index(im)  # Majeur : g_maj = [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
                prout = pro1 - pro2     # Prout : Niveau d'altération réel
                if prout != 0:
                    ph = signes[prout] + str(im)  # Affectation signe sur degré
                    photo.append(ph)
            z += 1
        for hot in photo:  # Photos-Les modulations modales
            ist = (list(hot)[:len(hot) - 1])[0]
            if len((list(hot)[:len(hot) - 1])) > 1:
                ist = str((list(hot)[:len(hot) - 1])[0]) + str((list(hot)[:len(hot) - 1])[1])
            if ist not in signatures.keys():
                signatures[ist] = [fol]
                signatures[ist].append(hot)
            else:
                signatures[ist].append(hot)
        if not photo:
            photo.append('maj')
        # ('.../** .| |. **', lineno(), ' ** PHOTO_temps réel:____', photo)
        # (lineno(), ' ** SIGNA_________', signatures, '..')
        informatif = ['x^', '+^', "^", 'x', '+', 'o*', '-*', '*', 'o', '-']
        infime, survole = informatif[5:], informatif[:5]
        (lineno(), 'INFOS', 'infime', infime, 'survole', survole)
        # 138 INFOS infime ['o*', '-*', '*', 'o', '-'] survole ['x^', '+^', '^', 'x', '+']
        # affirmatif = ['o*7', '-*6', '*5', 'o4', 'o3', '+^2', '^3', '^4', 'x5']
        # Amplifier affirmatif
        amplifier = {
            'o3': ['-2'], 'o4': ['o3', '-2'], '*5': ['o4', 'o3', '-2'],
            '-*6': ['*5', 'o4', 'o3', '-2'], 'o*7': ['-*6', '*5', 'o4', 'o3', '-2'],
            '+^2': ['^3', '^4', 'x5', '+6'], '^3': ['^4', 'x5', '+6'],
            '^4': ['x5', '+6'], 'x5': ['+6']}

        def former(signal, topo, toc):  # FORMATAGE Fonction Origine
            """Passage par les signes invariants(affirmatif, amplifier, altéractif)
            Permet la détection des invariants dans la signature modale(photo)
            Définition des variables :
                Revu : True pour inverser sens lecture liste.
                Box : Tableau contenu altéractif. Values().
                Couler : Indice en cours de traitement."""
            (' S', lineno(), 'SIGNAL', signal, 'Topo', topo, 'Toc', toc)
            box, big, couler, bil = {0: []}, [], [], False
            topos = topo.copy()
            envers = topo.copy()
            envers.reverse()

            def bil_riff(t10):
                """Traitement des signatures complexes, quand plusieurs signes
                occupent les notes du mode. Aboutissant à une écriture du nom,
                qu'il soit entier ou décimal :
                    Entier = -35
                    Décimal = +45.-3"""
                # (' __ ^* _ B²_ ^* _ T10', t10)
                # ^* _ B²_ ^* _ T10 ['+4', '+5', '-3']
                dic, c10 = '', ''
                for t0p in t10:
                    t0 = t0p[:len(t0p) - 1]
                    t1 = t0p[len(t0p) - 1:]
                    if t0 not in dicter:
                        dicter[t0] = []
                    dicter[t0].append(t1)
                for kt, vt in dicter.items():
                    if len(vt) > 1:
                        vt.sort()
                        if kt in infime:  # Sens lecture signes diminués
                            vt.reverse()
                        for v0 in vt:
                            dic += v0
                        dicter[kt] = []
                        dicter[kt].append(dic)
                        dic = ''
                lys0 = {'aug': [], 'dim': [], 'bis': []}
                lise = list(dicter.keys())
                biseau, biaise = {1: None, 2: None, 3: None}, None
                for kt in dicter.keys():
                    c10 = ''
                    if len(dicter.keys()) == 1:  # . . . . . ... 1er. 1 note signée
                        '''|56(26)[+2346]||54(24)[o73]||52(19)[+234]|...'''
                        # ('\n\n\n\n\n  REPÈRE 1 Clé. \n\n\n\n\n')
                        c10 = kt + dicter[kt][0]
                    elif len(dicter.keys()) == 2:  # . . . . ... 2ème. 2 notes signées
                        '''|65(3)[+47-]||64(34)[o7.-542]||64(7)[+4.-73]|...'''
                        # ('\n\n\n\n\n  REPÈRE 2 Clés. \n\n\n\n\n')
                        lise = list(dicter.keys())
                        les1 = len(dicter[lise[0]][0])
                        les2 = len(dicter[lise[1]][0])
                        les3 = les1 + les2
                        if les1 == 1 and les2 == 1:
                            c1 = lise[0] + dicter[lise[0]][0]
                            c2 = dicter[lise[1]][0] + lise[1]
                            c10 = c1 + c2
                        elif 6 > les3 > 2:
                            c1 = lise[0] + dicter[lise[0]][0]
                            c2 = lise[1] + dicter[lise[1]][0]
                            c10 = c1 + '.' + c2
                    elif len(dicter.keys()) == 3:  # . . . . ... 3ème. 3 notes à double-signe
                        # Exemple = B² BIL.dicter {'x': ['4'], '+': ['6'], '-': ['32']}
                        '''|60(11)[+43o.-7]||53(15)[x46+.-3]||43(5)[]|...'''
                        # ('\n\n\n\n\n  REPÈRE 3 Clés. \n\n\n\n\n')
                        les1 = len(dicter[lise[0]][0])
                        if les1 != 1 and not lys0['bis']:
                            you = lise[0], dicter[lise[0]][0]
                            lys0['bis'].append(you)
                        les2 = len(dicter[lise[1]][0])
                        if les2 != 1 and not lys0['bis']:
                            you = lise[1], dicter[lise[1]][0]
                            lys0['bis'].append(you)
                        les3 = len(dicter[lise[2]][0])
                        if les3 != 1 and not lys0['bis']:
                            you = lise[2], dicter[lise[2]][0]
                            lys0['bis'].append(you)
                        les4 = les1 + les2 + les3
                        if les4 == 4:
                            '''|43(5)[o37-.+45]||38(18)[]||43(5)[]|...'''
                            # ('\n\n\n\n\n REPÈRE Les4. \n\n\n\n\n')
                        # Il n'y a pas de 'les4' supérieur à 4
                        for yo in lise:
                            if yo in survole and yo not in lys0['aug']:
                                lys0['aug'].append(yo)
                            if yo in infime and yo not in lys0['dim']:
                                lys0['dim'].append(yo)
                        x2, x4 = '', ''
                        if lys0['bis']:
                            biaise = lys0['bis'].copy()
                            biaise = biaise[0]
                            x2 = biaise[0] + biaise[1]
                            x4 = biaise[0]
                            biseau[3] = '.' + x2
                        x1, oxo, pensif1, pensif2 = '', 0, None, None
                        # Construction liste ordonnée des signes
                        for lys in lys0.keys():  # Initialiser famille signes
                            if lys == 'bis':
                                break
                            elif len(lys0[lys]) > 1:  # Famille 2 signes
                                pensif1 = lys
                                # ('Pension1', pensif1)
                            elif len(lys0[lys]) == 1:  # Signe orphelin
                                pensif2 = lys
                                # ('Pensif2', pensif2)
                        # Traitement familles des signes réunis
                        if lys0[pensif1]:
                            if x4 in lys0[pensif1]:
                                ox0 = lys0[pensif1].index(x4)
                                if ox0 > 0:
                                    ox1 = dicter[lys0[pensif1][0]][0] + lys0[pensif1][0]
                                else:
                                    ox1 = dicter[lys0[pensif1][1]][0] + lys0[pensif1][1]
                                biseau[2] = ox1
                            else:
                                ox2 = 0
                                for li in lys0[pensif1]:
                                    if not ox2:
                                        ox1 = li + dicter[li][0]
                                        biseau[1] = ox1
                                    elif ox2:
                                        ox1 = dicter[li][0] + li
                                        biseau[2] = ox1
                                    ox2 += 1
                        if biaise is None:  # Valeur positive
                            ox1 = '.' + lys0[pensif2][0] + dicter[lys0[pensif2][0][0]][0]
                            if biseau[3] is None:
                                biseau[3] = ox1
                        elif not biseau[1]:  # Biseau[3] avec pensif1
                            o1, o2 = lys0[pensif2][0], dicter[lys0[pensif2][0][0]][0]
                            ox1 = o1 + o2
                            biseau[1] = ox1
                        # Oxo = Groupement des candidatures
                        # ('\n\n\n\n\n REPÈRE Zone en cours. \n\n\n\n\n')
                    break
                if len(dicter.keys()) == 3:
                    ox1 = ''
                    for bof in biseau.keys():
                        ox1 += biseau[bof]
                    c10 = ox1
                return c10

            if toc == '1':  # FORMATAGE Signatures 1 clé
                '''def former(signal, topo, toc('1')): FORME SIMPLE
                Nous avons là un signal simple de la tonalité
                len(signatures.keys()) == 1: Une clé(key) unique dans la signature.'''
                # ('\n\n\n\n\n REPÈRE Signature 1 clé. \n\n\n\n\n')
                if signal[0][:1] in signes[6:]:
                    signal.reverse()
                for si in signal:
                    if si in alteractif.keys():  # altéractif: Zones des altéractions
                        couler.append(si)
                        for acte in alteractif[si]:
                            box[0].append(acte)
                    if si not in box[0]:
                        couler.append(si)
                roule = signal[0][:1]
                roule += ''.join(it[1:] for it in couler)
                return roule
            else:  # FORMATAGE Signatures à clés multiples
                ''' def former(signal, topo, toc('2')): FORME MULTIPLE
                Dans ce cas, la signature est composée de plusieurs signes.
                En tenant compte du sens de lecture de la signature, et de la valeur
                signée : La priorité va au nombre d'altérations dans le signe (###(^)),
                donc au rang respectif de la table des signes. Ligne 70.'''
                # donc = None
                box[0] = []  # Box office.point
                top, aff1, aff3, tap, tec = [], [], True, [], True  # top: Stocke, tip: Aussi
                # (lineno(), ' topo', topo, 'envers', envers)
                # 207  topo ['-2', '+3', '+4', '+5'] envers ['+5', '+4', '+3', '-2']
                # informatif = ['o*', '-*', '*', 'o', '-', 'x^', '+^', "^", 'x', '+']
                # Séparation des signatures opposées dans informatif['']
                # infime = ['o*', '-*', '*', 'o', '-'], survole = ['x^', '+^', '^', 'x', '+']
                for info in informatif:
                    # Lecture constructive sur un suivi informatif['']
                    # Une série ordonnée aux plus fortes altéractions.
                    # Décrivant une décroissance des degrés allant de CINQ à Un.
                    # En deux lignes parallèles (±) en dégénérescence altéractive.
                    ''' GÉNÉRATION INVERSÉE :
                        Informatif[Bémols] = informatif[de 0 à 4]. Ou infime
                            ['o*', '-*', '*', 'o', '-']
                        Informatif[Dièses] = informatif[de 5 à 9]. Ou survole
                            ['x^', '+^', '^', 'x', '+']
                        AU CROISEMENT DES CROISÉES :
                            |C|o|D|o|E|F|o|G|o|A|o|B|C|
                            |C|o|o|D|E|F|o|G|A|o|o|B|C|
                            |C|_|_|D|E|F|G|A|_|_|_|B|C|
                        RAPPEL ÉLÉMENT :
                            a = a - (a+1). Produit négatif'''
                    if tec:
                        tec = False
                        for tipi in topo:
                            t00 = tipi[:len(tipi) - 1]
                            if t00 in informatif[5:] and tipi in alteractif.keys():
                                topos = envers.copy()
                    for tipi in topos:  # Topo : Prise de vue binaire
                        if tipi[:len(tipi) - 1] == info:  # info = informatif[]
                            # Tipi diatonique.module
                            if tipi in alteractif.keys():  # Altéractive Keys()
                                # Enregistre tipi.Keys() in original.Box[0] & Top[]
                                # tic = tipi[:len(tipi) - 1]  # Tic égal signes.tipi
                                if tipi not in box[0]:
                                    top.append(tipi)
                                    box[0].append(tipi)
                                    paris = tipi[len(tipi) - 1:]
                                    tap.append(paris)
                                # L'altéraction a des valeurs altératives
                                for ti in alteractif[tipi]:  # Tuteur des altéractions
                                    if aff1:
                                        ta = ti[len(ti) - 1:]
                                        if ta in aff1[0]:
                                            aff3 = False
                                    if ti not in box[0] and aff3 is True:
                                        # titi, tio = ti[len(ti) - 1:], ''
                                        box[0].append(ti)
                                        if ti not in topo:
                                            paris = ti[len(ti) - 1:]
                                            tap.append(paris)
                                            top.append(ti)
                                            tut, tot = {}, []
                                            if tap.count(paris) > 2:
                                                for tip in top:
                                                    tac1s = tip[:len(tip) - 1]
                                                    tac1n = tip[len(tip) - 1:]
                                                    if tac1n == paris:
                                                        tut[tac1s] = []
                                                        tut[tac1s].append(tip)
                                                        tutu = informatif.index([tac1s][0])
                                                        tut[tac1s].append(tutu)
                                                        tot.append(tutu)
                                                for wkw, wvw in tut.items():
                                                    if wvw[1] == max(tot):
                                                        top.remove(wvw[0])
                                                        paris = wvw[0][len(wvw[0]) - 1:]
                                                        tap.remove(paris)
                                        else:
                                            tic = ti[len(ti) - 1]
                                            for sig in informatif:
                                                tiens = sig + tic
                                                if tiens in top:
                                                    paris = tiens[len(tiens) - 1:]
                                                    tap.remove(paris)
                                                    top.remove(tiens)
                            elif tipi in amplifier.keys():  # L'amplification termine
                                for tipi_val in amplifier[tipi]:
                                    tv1 = tipi_val[len(tipi_val) - 1:]
                                    if tv1 not in aff1:
                                        aff1.append(tv1)
                                if tipi not in box[0]:
                                    paris = tipi[len(tipi) - 1:]
                                    tap.append(paris)
                                    top.append(tipi)
                                    box[0].append(tipi)
                                for tu in amplifier[tipi]:
                                    if tu not in box[0]:
                                        box[0].append(tu)
                                    if tu in topo:
                                        tee = tu[len(tu) - 1:]
                                        for ton in top:
                                            toi = ton[len(ton) - 1:]
                                            if toi == tee:
                                                paris = toi[len(toi) - 1:]
                                                tap.remove(paris)
                                                top.remove(ton)
                            elif tipi not in box[0]:  # Cas extrême en traitement
                                paris = tipi[len(tipi) - 1:]
                                tap.append(paris)
                                top.append(tipi)
                                box[0].append(tipi)
                                big.append(tipi)
                bis, top_copy = {}, top.copy()
                for tipi in top_copy:  # Déduire les doubles
                    ct2n = tipi[len(tipi) - 1:]
                    if tap.count(ct2n) == 1:
                        continue
                    else:
                        for cop in top_copy:
                            # ca2s = cap[:len(cop) - 1]
                            co2n = cop[len(cop) - 1:]
                            if ct2n == co2n and tipi != cop:
                                ct2s = tipi[:len(tipi) - 1]
                                co2s = cop[:len(cop) - 1]
                                bis[ct2n] = [[tipi, cop], [ct2s, co2s]]
                # Mise à jour. Traitement des doublures(top)
                for k_bis, v_bis in bis.items():
                    if v_bis[1][0] in survole:
                        vb1 = survole.index(v_bis[1][0])
                        vb2 = survole.index(v_bis[1][1])
                        vb0 = max(vb1, vb2) - min(vb1, vb2)
                        top.remove(v_bis[0][0])
                        top.remove(v_bis[0][1])
                        bon = signes[vb0] + k_bis
                        top.append(bon)
                    elif v_bis[1][0] in infime:
                        vb1 = infime.index(v_bis[1][0])
                        vb2 = infime.index(v_bis[1][1])
                        vb0 = min(vb1, vb2) - max(vb1, vb2)
                        top.remove(v_bis[0][0])
                        top.remove(v_bis[0][1])
                        bon = signes[vb0] + k_bis
                        top.append(bon)
                cap = bil_riff(top)
                # (' ♥♦♣♠ Dicter', lineno(), dicter)
                return cap
            #
            #
        picolo[fol][1].append(signatures)
        # (lineno(), ' §  Signatures', signatures)
        # 249 §  Signatures {'-': [63, '-3', '-5']}
        '''Détecte le nombre de signes dans la signature.'''
        for ks, kv in signatures.items():
            cou = None
            if len(signatures.keys()) == 1:  # Signatures 1 signe(clé)
                '''Quand il y a un seul signe dans la signature:
                    Longueur kv Quant + Multi Notes. Q = numéro-gamme.
                    En soustrayant Qµ-unité. Reste Notes.'''
                if len(kv) == 2:  # Signature 1 signe(clé) + 1 note
                    '''|66(8)[-7]||66(5)[+4]|...'''
                    # ('#\n###\n###\n###\n###\n###\n###\n###\n#####\n#####\n#####')
                    cou = kv[1]
                elif len(kv) == 3:  # Signature 1 signe(clé) + 2 notes
                    for kepi in kv:
                        if kepi in alteractif.keys():  # Les cas altéractifs sont uniques
                            '''|56(9)[-4]||40(9)[+3]|'''
                            cou = kepi
                    if cou is None:
                        '''|66(12)[-73]||65(15)[-76]||65(11)[+45]||64(11)[-63]|...'''
                        # ('\n\n\n\n\nLigne de repérage\n\n\n\n\n')
                        pot1, pot2, bloc = [], [], None
                        for im2 in kv:
                            if type(im2) is str:
                                pot1.append(int(im2))
                                pot2.append(im2)
                        if ks in informatif[5:]:
                            pot1.sort()
                            bloc = str(pot1[0]) + str(pot1[1])[1:]
                        else:
                            bloc = pot2[0] + pot2[1][1:]
                        cou = bloc
                elif len(kv) > 3:  # Signature 1 signe(clé) + 3 notes
                    '''|66(28)[-76532]||66(2)[-7632]||66(19)[-763]||65(3)[-76542]|...'''
                    # ('\n\n\n\n\nLigne de repérage\n\n\n\n\n')
                    cou = former(kv[1:], [], '1')
            else:  # Signatures aux clés multiples
                cou = former(signatures, photo, '2')
                col = photo, cou
                signaux[fol].append(col)
                if '2' in table:
                    print(lineno(), ' Clé multi', 'COU ', cou, ' µnit FONDRE')
                break  # Traitement via formation
            cou = cou
            col = photo, cou
            signaux[fol].append(col)
            if '2' in table:
                print(' *  ', lineno(), '    COU _: ', cou, ' µnit UNIC KS', ks)
        if 'maj' in photo:
            col = photo, '0'
            signaux[fol].append(col)
            if '2' in table:
                print(' *  ', lineno(), '     COL _: ', col[0][0], ' µnit MAJEUR')

    fix = 0  # Section maj7_fonc(..)
    while fix < 66:  # dic_analyse: Infos gammes
        fix += 1
        if '2' in table:
            print('\n', lineno(), '__________________________TERMINAL MODES DIATONIQUES')
        # (lineno(), 'Fix', fix, 'FF', ff[:len(ff) - 1])  # Moins retour chariot
        # 88 Fix 61 FF ['1', '0', '2', '-3', '0', '0', '+4', '5', '0', '6', '0', '7',
        # [((1, 61), '101100110101')]]
        groupe[fix] = []
        # Lecture du fichier entrant unic
        if fix in unic.keys():  # Unic : Premières gammes faciles (Ligne 71)
            for fo in fondre[fix]:
                groupe[fix].append(fo)
            for bi in binez[fix]:
                groupe[fix].append(bi)
            depuis = len(groupe[fix])
            if '2' in table:
                print(lineno(), 'UNIC.GROUPE =', fix, groupe[fix])
            # 530 FONDRE.GROUPE = ['101010110101', '101011010101'] . FIX = 66
            # Unic dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
            dep = []
            while depuis:
                for i in range(0, 67):
                    for ff in groupe[fix]:
                        if i == ff[0][1] and ff[0][0] not in dep:
                            dep.append(ff[0][0])
                            # ('\n >>', lineno(), fix, '\tM22', ff[0][1], '\tM23:', ff[0][0])
                            depuis -= 1
                            fond_gam(ff[0][0], fix)  # fond_gam: Fonction envoi(unic-fondre)
            # (lineno(), 'Fondre', fondre[fix], '\nUnic', unic.keys(), '\n', len(groupe))
            # 529 Fondre [(('101101010101', 4), 65), (('101010101101', 11), 65)]
            # Unic dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
        # Lecture du fichier entrant fondre
        elif fix in fondre.keys():  # Fondre : Gammes secondaires (Ligne 72)
            for fo in fondre[fix]:
                groupe[fix].append(fo)
            for bi in binez[fix]:
                groupe[fix].append(bi)
            depuis = len(groupe[fix])
            if '2' in table:
                print(lineno(), 'FONDRE.GROUPE =', fix, groupe[fix])
            # 530 FONDRE.GROUPE = ['101010110101', '101011010101'] . FIX = 66
            # Unic dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
            dep = []
            while depuis:
                for i in range(0, 67):
                    for ff in groupe[fix]:
                        if i == ff[0][1] and ff[0][0] not in dep:
                            dep.append(ff[0][0])
                            # ('\n >', lineno(), fix, '\tM22', ff[0][1], '\tM23:', ff[0][0])
                            depuis -= 1
                            fond_gam(ff[0][0], fix)  # fond_gam: Fonction envoi(unic-fondre)


def dana_fonc(table, dana):
    """
    Les dictionnaires {dan/ego/maj} :
        Tous. Intégrales_Poids/Modes
        Dan. Enregistrer infos gammes pour analyser
        Ego. Répertorier gammes mêmes types
        Maj. Référencer diatonic majeur
    Dana est le dictionnaire entrant :
        Dana Keys = Numéros des gammes
        Dana Values = Diatonic Poids & Divise Sept
        Logic histoire :
        Des gammes (dan.keys()) avec une unité majeure
        Diatonic (dan. Values()) = 7 Modes signés & pesants
            La signature modale [[0,-3,-5,,,]_ Tonalité
            La démultiplication modale _[147,21.0,3.0,,,]]
                Divise Poids par 7 jusqu'à zéro entier
    Union : 1- Les tonalités aux mêmes poids.
        2- Les poids aux mêmes rangs.
        3- Les tonalités aux mêmes degrés
        1) Les masses égales. 2) Les reliefs pesants. 3) Les fondements réguliers."""
    # (lineno(), ' GEM DANA', dana[1][0])  # Vision du 1er mode (il y a 7 modes)
    # 610  GEM DANA [[0, -3, -5, 7, 7, 7, 0], [147, 21.0, 3.0, 0.42857142857142855]]
    maj_poids[66], maj_rang[66], maj_mode[66] = [], [], []
    for dan in range(1, len(dana) + 1):  # Épisode Dana
        tous_poi[dan], tous_mod[dan] = [], []
        dan_mode[dan], dan_rang[dan], dan_poids[dan] = [], [], []
        if dan == 66:
            """Initialisation des tableaux majeurs du 66"""
            # Recherche Point Go & tonic [0, 0, 0, 0, 0, 0, 0] :maj_mode[66]
            # Enregistrement Poids modaux :maj_poids[66]
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
            maj_lest = maj_poids[66].copy()
            maj_lest.sort()
            for mp in maj_poids[66]:
                maj_rang[66].append(maj_lest.index(mp))

        """Cette boucle récupère les modes maj7
            Les gammes fondamentales ont une septième majeure"""
        for dn in range(7):  # Séquence les modes diatoniques (Mj7 & Non maj7)
            tous_poi[dan].append(dana[dan][dn][1])
            dan_poids[dan].append(dana[dan][dn][1][0])  # Poids Tonalité
            if dana[dan][dn][0][-1] == 0:  # Filtre 7èmes majeures
                vide = dana[dan][dn][0], dn
                tous_mod[dan].append(vide)
        maj_lest = dan_poids[dan].copy()
        maj_lest.sort()
        for mp in dan_poids[dan]:
            dan_rang[dan].append(maj_lest.index(mp))
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
    # Lecture Ego Rangs
    filet = []
    for nom, rng in ego_rang.items():
        for rn in rng:
            if rn not in filet:
                filet.append(rn)
    if '3' in table:
        print(lineno(), 'EGO poids: ', ego_poids, '\n EGO rang: ', ego_rang)


def seption(table, mode_poids, k1, pc1, gm1, maj7, h_b):
    """Réception des poids modaux standards à augmenter & Création 'GlobalTexte/globdic_Dana.txt'.
    L'argument 'maj7' est le dictionnaire des modes maj 7èmes et poids standards par gamme"""
    # Mode_poids = Sept modes diatoniques par gamme. Comprend les 66 gammes.
    goo = []
    cumul = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    dic_analyse[k1] = []  # :Dana initie table
    dic_diatonic[k1] = []  # :Maj7_fonction initie 66 diatoniques
    dic_diatonic[k1].append(mode_poids)
    if pc1:
        dic_pc[k1] = []  #
        dic_pc[k1].append(pc1)
    # Dico gamme_poids & Key_mode Majeur Comparer
    for gpk, gpv in gamme_poids.items():  # Mode_poids & Comparer Mode naturel
        """:gpv = [0,0,0,0,0,0,0],[0,0,-4,0,0,0,-8],"""
        for com in gpv:  # :gpv= Valeur Majeure et mode dico gamme_poids
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
        # Fonction de démultiplication facteur 7
        while accroc > 1:  # Gammes Log.7
            accroc /= 7
            if accroc > 0:
                moyen[moi + 1].append(accroc)
                if int(accroc) == 1:
                    contre = accroc, mode_poids[moi]
                    if contre[1][-1] == 0:
                        goo.append(contre)

    if len(dic_analyse.keys()) == 66:
        """GlobEnModes = Gammes"""
        fil_analyse = open('GlobalTexte/globdic_Dana.txt', 'w')
        for ky1, va1 in dic_analyse.items():  # dic_analyse: Infos Dana
            mm = str(ky1) + str(va1)  # ky1: Numéro gamme
            mm += '\n'  # va1: Modes poids augmentés
            fil_analyse.write(mm)
        fil_analyse.close()  # Écriture fichier globdic_Dana.txt
        dana_fonc(table, dic_analyse)
        maj7_fonc(table, gm1, maj7, h_b)


    if groupe:  # Seption accessibilités
        '''num, poidsB/F, typoB/U/N, signetsU/F/M, unaire, nommeC/P
            Puis la recherche du mode tonique (entier-léger)
            Le degré i_grade a un poids nul et point zéro absolu et majeur'''
        # Formatage diatonique des degrés majeurs
        grade_maj = {'1': ['0'], '-2': ['+2', '+4', '+5', '+6'],
                     '+2': ['-2', 'o3', '-4', '-5', '-6', 'o7'],
                     '2': ['-3', '-7'], '3': ['-2', '-3', '-6', '-7'],
                     '4': ['+4'], '5': ['-7'], '6': ['-3', '-6', '-7'],
                     '7': ['-2', '-3', '-5', '-6', '-7']}
        index = 0  # Mettre à zéro pour tout traiter
        while index < 66:  # Résolution des degrés
            index += 1
            if '4' in table:
                print('\n', lineno(), '=====================CHOIX TONIQUE POSITION', index)
            #
            # Détecter les noms entiers majeurs sept
            # Et quand il n'y en a qu'un seul, il devient le choix unique
            inutile, calme, utile = [], 0, False
            for si in signaux[index]:
                inuit = 0
                for noe in si[1]:
                    if noe not in signes:
                        inuit += 1
                if '.' not in si[1] and inuit < 3 and '7' not in si[1]:
                    calme += 1
                    inutile.append(si[1])
            if calme == 1:
                utile = True
                if '4' in table:
                    print(lineno(), 'CALME INUTILE', inutile)
            else:
                if '4' in table:
                    print(lineno(), 'CALME UTILE', inutile)
                pass
            # Opération : Trier groupe[index]
            # Poids croissants comme l'original
            masse = []  # Copier les poids modaux
            for clef in groupe[index]:
                if clef[0][1] in masse:
                    # (lineno(), '... Alerte *** *** *** *** *** *** Polar', clef)
                    pass
                masse.append(clef[0][1])  # Initialisation des poids
            masse.sort()  # Trier les poids modaux
            brouillon[index] = []  # Trie groupe selon les masses
            brouille_binaires = []
            for tri in masse:
                for clef in groupe[index]:
                    if clef[0][1] == tri and clef[0][0] not in brouille_binaires:
                        brouillon[index].append(clef)
                        brouille_binaires.append(clef[0][0])
            groupe[index] = brouillon[index].copy()
            '''Cette section trouve le mode tonique ou le nom de gamme fondamentale,
            l'algorithme n'est pas parfait quand le choix n'est pas unique.'''
            cesse, relax, stock_nom, stock_bin = False, -1, [], []
            for s0 in signaux[index]:  # S0[0] = Photo. S0[1] = Nom
                relax += 1
                g0 = groupe[index][relax]
                labo, st9, st10 = [], [], 0
                # Sélection degré majeur sept
                if g0[0][0][-1] == '1':  # Septième degré majeur
                    for u1 in s0[1]:
                        if u1 not in signes:
                            st10 += 1
                    # Passage pour noms (2 signes + 2 chiffres)
                    if '.' not in s0[1] and st10 < 3:
                        stock_nom = s0[1]  # Premier degré mémorisé NOM ENTIER
                        stock_bin = g0[0][0]  # Premier degré mémorisé NOM BINAIRE
                        # ('***\n_ ^ ^ Zéro point', s0[0], s0[1], g0[0][0], 'N', stock_nom)
                        sgn1, deg1, deg2, sgn2 = None, None, None, None
                        s0n, s0t, s0i = '', -1, True
                        # Apprentissage Labo
                        for s00 in s0[1]:
                            s0t += 1
                            if s00 in signes:
                                s0n += s00
                                s0i = True
                                if s0t + 1 < len(s0[1]) and s0[1][s0t + 1] in signes:
                                    s0i = False
                            else:
                                s0n = s00
                            if s0i:
                                labo.append(s0n)
                            s0n = ''
                        # Labo Issue St9 = Degré(s) absolu(s) (non-altérés)
                        if len(labo) == 1:  # Ici labo contient '0' ou majeur
                            source = [stock_nom, stock_bin]
                            toniques[index] = source
                            # (lineno(), 'Majeur Break', toniques[index], 'Index', index)
                            break
                        elif len(labo) == 2:
                            sgn1, deg1 = labo[0], int(labo[1])
                            st9.append(deg1)
                        elif len(labo) == 3:
                            sgn1, deg1, deg2 = labo[0], labo[1], labo[2]
                            st9.append(deg1)
                            st9.append(deg2)
                        elif len(labo) == 4:
                            sgn1, deg1, deg2, sgn2 = labo[0], labo[1], labo[2], labo[3]
                            st9.append(deg1)
                            st9.append(deg2)
                        # Labo Issue St9 = Degré(s) absolu(s) (non-altérés)
                        # (lineno(), '+*° LABO', labo, 'LABO', sgn1, deg1, deg2, sgn2)
                        # Trouver le degré voisin supérieur
                        roule_bin = list(g0[0][0])
                        roule_bin.insert(-1, roule_bin.pop(0))
                        while roule_bin[0] == '0':
                            roule_bin.pop(0)
                            roule_bin.append('0')
                        moule_bin = ''.join(rb for rb in roule_bin)
                        # (lineno(), ' * MOULE_BIN 2ème degré', moule_bin, '        ***')
                        mia, mod_origine, mod_cours, mod_so9, mod_1 = -1, [], [], [], False
                        # Transpose 2ème degré majeur vers grand1
                        for gr in grade_maj['2']:
                            gr = gr[len(gr) - 1:]
                            gr1 = int(gr)
                            mod_origine.append(gr1)
                        for bof in range(7):
                            mia += 1
                            sto = signaux[index][mia]
                            gmo = groupe[index][mia]
                            if moule_bin == gmo[0][0]:
                                fsn = ''
                                for so9 in st9:
                                    so1 = int(so9) - 1
                                    fss = st9.index(so9)
                                    if fss == 0:
                                        fsn = sgn1 + str(so1)
                                    elif fss == 1:
                                        if sgn2:
                                            fsn = sgn2 + str(so1)
                                        else:
                                            fsn = sgn1 + str(so1)
                                    mod_so9.append(fsn)
                                    # Ajouter à l'original le degré descendant (so1)
                                    if so1 not in mod_origine and so1 != 1:
                                        mod_origine.append(so1)
                                        mod_origine.sort()
                                    elif so1 == 1:  # À faire quand so1=1
                                        mod_1 = True
                                    # (lineno(), 'St', sto, 'SO', so1, 'F', fsn, 'm', mod_1)
                                for st in sto[0]:
                                    st0 = st[len(st) - 1:]
                                    sto1 = int(st0)
                                    # Suite altéractive ?
                                    if sto1 not in mod_origine:  # Degré descendant signé
                                        for fsn_alt in mod_so9:
                                            if fsn_alt in alteractif.keys():
                                                for f0 in alteractif[fsn_alt]:
                                                    f1 = f0[len(f0) - 1:]
                                                    # ('F1', f1, )
                                                    if int(f1) == sto1 and sto1 not in mod_origine:
                                                        mod_origine.append(sto1)
                                                        mod_origine.sort()
                                    # Selon la non-altéraction
                                    if sto1 not in mod_origine:  # Contenu
                                        for fsn_sto in sto[0]:
                                            if fsn_sto in alteractif.keys():
                                                for f0 in alteractif[fsn_sto]:
                                                    f1 = f0[len(f0) - 1:]
                                                    if int(f1) == sto1 and sto1 not in mod_origine:
                                                        mod_origine.append(sto1)
                                                        mod_origine.sort()
                                    if sto1 not in mod_cours:
                                        mod_cours.append(sto1)
                                        mod_cours.sort()
                                # Traitement so1= '-1' ou '+1'
                                if mod_1:
                                    mod_origine = []
                                    for ms9 in mod_so9:
                                        ms0 = ms9[len(ms9) - 1]
                                        if int(ms0) not in mod_cours and ms0 != '1':
                                            mod_cours.append(int(ms0))
                                            mod_cours.sort()
                                            # (lineno(), '.    Courses', mod_cours)
                                        # Secteur '-1'
                                        if ms9 in ('-1', 'o1', '*1'):
                                            # Origine grade_maj['-2']
                                            for gm2 in grade_maj['-2']:
                                                gm0 = gm2[len(gm2) - 1:]
                                                mod_origine.append(int(gm0))
                                            # Quand '-3' = '+2'
                                            for ms8 in mod_so9:
                                                if 2 in mod_origine:
                                                    if ms8 in ['-3', 'o4']:
                                                        mod_origine.remove(2)
                                                        mod_origine.append(3)
                                                        mod_origine.sort()
                                                    elif ms8 == '^3':
                                                        ms7 = ms8[len(ms8) - 1:]
                                                        if ms7 not in mod_origine:
                                                            mod_origine.append(3)
                                                            mod_origine.sort()
                                        # Secteur '+1'
                                        if ms9 in ('+1', 'x1', '^1'):
                                            # Origine grade_maj['+2']
                                            for gm2 in grade_maj['+2']:
                                                gm0 = gm2[len(gm2) - 1:]
                                                mod_origine.append(int(gm0))
                                            # Quand '+2' = '-3' et '-4'
                                            for ms8 in mod_so9:
                                                if ms8 == 'x2':
                                                    if 3 in mod_origine and 4 in mod_origine:
                                                        mod_origine.remove(3)
                                                        mod_origine.remove(4)
                                                        mod_origine.sort()
                                    # (lineno(), 'grade_maj-- SO1', mod_so9)
                                # (lineno(), 'Origine', mod_origine, 'Cours', mod_cours)
                            if mod_origine == mod_cours or utile:
                                cesse = True
                                # ('Origine = Cours', mod_origine, mod_cours, 'Utile:', utile)
                                break
                        else:
                            pass
                            # ('***Else***M_origine != M_cours***')
                if cesse:
                    source = [stock_nom, stock_bin]
                    toniques[index] = source
                    # (lineno(), 'Cesse Break', cesse, toniques[index], 'Index', index)
                    break
        # Mise en ordre des degrés via transfert dictionnaires respectifs
        # ('\n', lineno(), '******* ******* ******* ******* ******* ORDRE DIATONIQUE')
        trans_dic, trans_groupe, trans_picolo, trans_signaux = {}, {}, {}, {}
        clefs_toniques = list(toniques.keys())
        clefs_toniques.reverse()
        couche = 0
        # Mise en ordre diatonique du GROUPE
        for tonice in clefs_toniques:
            if '5' in table:
                t = tonice
                print('\n', lineno(), 'OO__OOO_O_OOOO_______', '\n _____o ooo o o o  ooo MODÈLES RAPPORTÉS   ', t)
            couche += 1
            ton = 0
            rang_deg = list(toniques[tonice][1])
            while ton < 7:  # Développement des binaires diatoniques
                # Modulations diatoniques : Mode 1 à Mode 7
                if ton == 0:
                    ton += 1
                elif rang_deg[0] == '1':
                    rang_deg.pop(0)
                    rang_deg.append('1')
                    if rang_deg[0] == '1':
                        ton += 1
                else:
                    while rang_deg[0] == '0':
                        rang_deg.pop(0)
                        rang_deg.append('0')
                    ton += 1
                if rang_deg[0] == '1':  # Définition des 7 modes diatoniques
                    ton0 = table_deg[ton]
                    if '5' in table:
                        print(lineno(), '     DEGRÉ', ton0)
                    '''diC_AnaLySe 66[[0,-3,-4,0,-6,-7,-8],[196,28.0,4.0,0.5714285714285714]]'''
                    trans_dic[tonice, table_deg[ton]] = []
                    '''*. TraNs_GRouPe .* [(('101011010101', 0), 66)]'''
                    trans_groupe[tonice, table_deg[ton]] = []
                    '''picolo 66 [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]'''
                    trans_picolo[tonice, table_deg[ton]] = []
                    '''signaux 66 (['maj'], '0') : Photo. Nom.'''
                    trans_signaux[tonice, table_deg[ton]] = []
                    deg_txt = ''.join(rd for rd in rang_deg)
                    for t_grp in groupe[tonice]:  # Trans_Groupe OK
                        if t_grp[0][0] == deg_txt:  # Enregistrer Groupe
                            trans_groupe[tonice, ton0].append(t_grp)
                            if '5' in table:
                                print(lineno(), 'T_t_grp', t_grp[0][0], t_grp, ton0)
                            break
                        # break # Coupure développement diatonique
                    s_tab1, s_tab2 = [], []
                    for pic in range(len(picolo[tonice][0])):
                        stop_pic = False
                        for pt0 in picolo[tonice][0]:  # Forme neutre
                            d = 1  # De 1 à 7. De binaire à numéral
                            mod_txt = []
                            # Construction Forme neutre Photo
                            # Final = [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
                            for dxt in deg_txt:  # Photo Négatif Deg_Txt
                                if dxt == '1':
                                    mod_txt.append(d)
                                    d += 1
                                else:
                                    mod_txt.append(0)
                            s_num = {'2': [], '3': [], '4': [], '5': [], '6': []}
                            if mod_txt == pt0:  # Photo deg_txt = Forme neutre
                                tm = picolo[tonice][0].index(pt0)
                                trans_picolo[tonice, ton0].append(picolo[tonice][0][tm])
                                trans_picolo[tonice, ton0].append(picolo[tonice][1][tm])
                                stop_pic = True
                                if '5' in table:
                                    print(lineno(), '*..* tag_mod 0', trans_picolo[tonice, ton0][0])
                                    (lineno(), '*..* tag_mod 1', trans_picolo[tonice, ton0][1])
                                for v_tp in trans_picolo[tonice, ton0][1].values():
                                    # Construction table pour signaux
                                    for vt in v_tp:
                                        if type(vt) is str:
                                            v1 = vt[len(vt) - 1:]
                                            s_num[v1] = vt
                                # Rapport table pour signaux et analyse
                                for vs in s_num.values():
                                    s_tab2.append(vs)  # s_tab2 pour trans_dic ([]=0)
                                    if vs:
                                        s_tab1.append(vs)  # s_tab1 pour signaux (!=[])
                                for sig0 in signaux[tonice]:
                                    if sig0[0] == s_tab1:
                                        trans_signaux[tonice, table_deg[ton]].append(sig0)
                                        if '5' in table:
                                            print(lineno(), '. Signaux', trans_signaux[tonice, ton0])
                                        break
                                tab, sur = [0], ''  # Rapport tab trans_dic
                                # Table convertie pour dic_analyse (trans_dic)
                                for st_dic in s_tab2:
                                    if st_dic:
                                        sd0 = st_dic[:len(st_dic) - 1]
                                        ss0 = ''
                                        sd1 = st_dic[len(st_dic) - 1:]
                                        sig = signes.index(sd0)
                                        if signes.index(sd0) > 5:
                                            sig = signes.index(sd0) - 11
                                            ss0 = '-'
                                        aug = str(abs(sig) + int(sd1[0]))
                                        sur = int(ss0 + aug)
                                    else:
                                        sur = 0
                                    tab.append(sur)
                                if len(tab) < 7:
                                    while len(tab) != 7:
                                        tab.append(0)
                                for ta0 in dic_analyse[tonice]:
                                    if tab == ta0[0]:
                                        trans_dic[tonice, ton0] = ta0
                                if '5' in table:
                                    print(lineno(), 'TA0', trans_dic[tonice, table_deg[ton]])
                                break
                        if stop_pic:
                            break  # Coupure développement diatonique
            # break # Coupure développement des toniques (66 gammes)
        modes = {
            'analyse': trans_dic,
            'groupe': trans_groupe,
            'picolo': trans_picolo,
            'signaux': trans_signaux}
        # table_deg = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
        """Glob_DataGams = Gammes données fondamentales"""
        m_ana = modes['analyse']
        m_grp = modes['groupe']
        m_pic = modes['picolo']
        m_sgn = modes['signaux']
        data_gammes = open('GlobalTexte/glob_datagams.txt', 'w')
        fun = 0
        while fun <= 65:
            fun += 1
            dan, t_dan = 0, []
            while dan < 7:
                dan += 1
                don = table_deg[dan]
                din = [fun, don]
                t_dan.append(din)
                t_dan.append(m_ana[fun, don])
                t_dan.append(m_grp[fun, don])
                t_dan.append(m_pic[fun, don])
                t_dan.append(m_sgn[fun, don])
            for nrj in t_dan:
                maj = str(nrj)
                for mm in maj:
                    data_gammes.write(mm)
                mm = '\n'
                data_gammes.write(mm)
            t_dan.clear()
        data_gammes.close()
        glob_in_acc.inv_acc(modes, ego_poids, ego_rang)


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

    seption('0', mode_po, 1, {}, {}, {}, {})

""" 
        *   *   * HORS NOTION RANGEMENT
Signaux.dic66: 
[['maj'], ['+4'], ['-7'], ['-3', '-7'], ['-3', '-6', '-7'], 
['-2', '-3', '-6', '-7'], ['-2', '-3', '-5', '-6', '-7']]}
        *   *   *
Dic_analyse.dic66: 
[[[0, 0, 0, 5, 0, 0, 0], [588, 84.0, 12.0, 1.7142857142857142, 0.24489795918367346]], 
[[0, -3, -4, 0, 0, -7, -8], [0]], 
[[0, 0, -4, 0, 0, 0, -8], [490, 70.0, 10.0, 1.4285714285714286, 0.20408163265306123]], 
[[0, 0, 0, 0, 0, 0, 0], [833, 119.0, 17.0, 2.4285714285714284, 0.3469387755102041]], 
[[0, -3, -4, 0, -6, -7, -8], [196, 28.0, 4.0, 0.5714285714285714]], 
[[0, 0, -4, 0, 0, -7, -8], [343, 49.0, 7.0, 1.0]], 
[[0, 0, 0, 0, 0, 0, -8], [784, 112.0, 16.0, 2.2857142857142856, 0.32653061224489793]]]}
        *   *   *
Groupe.dic66: 
[(('101010110101', 5), 66), (('101011010101', 0), 66), 
(('110101011010', 22), 66), (('101101010110', 12), 66), (('110101101010', 28), 66), 
(('101101011010', 19), 66), (('101011010110', 8), 66)]}
        *   *   *
Picolo.dic66:
[[1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7], {}, 
[1, 0, 2, 0, 3, 0, 4, 5, 0, 6, 0, 7], {'+': [66, '+4']}, 
[1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 7, 0], {'-': [66, '-7']}, 
[1, 0, 2, 3, 0, 4, 0, 5, 0, 6, 7, 0], {'-': [66, '-3', '-7']}, 
[1, 0, 2, 3, 0, 4, 0, 5, 6, 0, 7, 0], {'-': [66, '-3', '-6', '-7']}, 
[1, 2, 0, 3, 0, 4, 0, 5, 6, 0, 7, 0], {'-': [66, '-2', '-3', '-6', '-7']}, 
[1, 2, 0, 3, 0, 4, 5, 0, 6, 0, 7, 0], {'-': [66, '-2', '-3', '-5', '-6', '-7']}]}
        *   *   *
"""