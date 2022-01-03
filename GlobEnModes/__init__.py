# Python utf8
# En cours de finalisation
# mardi 27 juillet 2021

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
# Dictionnaire final des noms des gammes
noms_dic = {66: 'maj'}
# Conteneur d'essai
essai, compteur = [], [0]

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
signes = ['', '+', 'x', '^', '+^', 'x^', 'o*', '-*', '*', 'o', '-']


def maj7_fonc(unic, fondre, binez):  # MAJ7 Fonction 1ères entrées UNIC/FONDRE
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
        g_maj = [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
        i_mod, z = [], 0
        for i_ in mode:  # Construction mode unaire
            if i_ == '1':  # [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]
                z += 1
                y = z
            else:
                y = 0
            i_mod.append(y)
        print('****', lineno(), 'I_mod', i_mod, '***********FOL', fol)
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
        print('.../** .| |. **', lineno(), ' ** PHOTO_temps réel:____', photo)
        print(lineno(), ' ** SIGNA_________', signatures, '..')
        informatif = ['x^', '+^', "^", 'x', '+', 'o*', '-*', '*', 'o', '-']
        # infime, survole = informatif[:5], informatif[5:]
        # (lineno(), 'INFOS', 'infime', infime, 'survole', survole)
        # 138 INFOS infime ['o*', '-*', '*', 'o', '-'] survole ['x^', '+^', '^', 'x', '+']

        # affirmatif = ['o*7', '-*6', '*5', 'o4', 'o3', '+^2', '^3', '^4', 'x5']
        amplifier = {
            'o3': ['-2'], 'o4': ['o3', '-2'], '*5': ['o4', 'o3', '-2'],
            '-*6': ['*5', 'o4', 'o3', '-2'], 'o*7': ['-*6', '*5', 'o4', 'o3', '-2'],
            '+^2': ['^3', '^4', 'x5', '+6'], '^3': ['^4', 'x5', '+6'],
            '^4': ['x5', '+6'], 'x5': ['+6']}
        alteractif = {
            'x2': ['x2', '+3', '+4'], '^2': ['^2', 'x3', 'x4', '+5'],
            '+3': ['+3', '+4'], 'x3': ['x3', 'x4', '+5'], '-4': ['-4', '-3'],
            'x4': ['x4', '+5'], 'o5': ['o5', '-4', '-3'], 'o6': ['o6', '-5'],
            '*6': ['*6', 'o5', '-4', '-3'], 'o7': ['o7', '-6'],
            '*7': ['*7', 'o6', '-5'], '-*7': ['-*7', '*6', 'o5', '-4', '-3']}

        def former(signal, topo, toc):  # FORMATAGE Fonction Origine
            """Passage par les signes invariants(affirmatif, amplifier, altéractif)
            Permet la détection des invariants dans la signature modale(photo)
            Définition des variables :
                Revu : True pour inverser sens lecture liste.
                Box : Tableau contenu altéractif. Values().
                Couler : Indice en cours de traitement."""
            (' S', lineno(), 'SIGNAL', signal, 'Topo', topo, 'Toc', toc)
            revu, box, big, couler, bil = False, {0: []}, [], [], False
            topos = topo.copy()
            envers = topo.copy()
            envers.reverse()
            # ('TOPO', topo, 'Dévers', envers)

            def bil_riff(t10):
                """Traitement des signatures complexes, quand plusieurs signes
                occupent les notes du mode. Aboutissant à une écriture du nom,
                qu'il soit entier ou décimal :
                    Entier = -35
                    Décimal = +45.-3"""
                # (' __ ^* _ B²_ ^* _ T10', t10)
                # ^* _ B²_ ^* _ T10 ['+4', '+5', '-3']
                dicter, dic, c10 = {}, '', ''
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
                # print(' __ B² BIL_Dicter', dicter, dicter.keys())
                for kt in dicter.keys():
                    c10 = ''
                    if len(dicter.keys()) == 1:  # . . . . . ... 1er. 1 note signée
                        c10 = kt + dicter[kt][0]
                        # (' __ L² DIC_1', dicter[kt][0], kt)
                    elif len(dicter.keys()) == 2:  # . . . . ... 2ème. 2 notes signées
                        lise = list(dicter.keys())
                        les1 = len(dicter[lise[0]][0])
                        les2 = len(dicter[lise[1]][0])
                        les3 = les1 + les2
                        # (les1, les2)
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
                        les1 = len(dicter[lise[0]][0])
                        if les1 != 1 and not lys0['bis']:
                            you = [lise[0], dicter[lise[0]][0]]
                            lys0['bis'].append(you)
                        les2 = len(dicter[lise[1]][0])
                        if les2 != 1 and not lys0['bis']:
                            you = [lise[1], dicter[lise[1]][0]]
                            lys0['bis'].append(you)
                        les3 = len(dicter[lise[2]][0])
                        if les3 != 1 and not lys0['bis']:
                            you = [lise[2], dicter[lise[2]][0]]
                            lys0['bis'].append(you)
                            # print(' LISE', dicter[lise[2]][0], dicter[lise[2]], lise[2])
                            # print(' LYS', lys0['bis'][0])
                        # les4 = les1 + les2 + les3  # "les4" = (1, 1, 1)
                        for yo in lise:
                            if yo in survole and yo not in lys0['aug']:
                                lys0['aug'].append(yo)
                            if yo in infime and yo not in lys0['dim']:
                                lys0['dim'].append(yo)
                        # print(' §§ Lys0[bis]', lys0['bis'], lys0)
                        bisou = []
                        if lys0['bis']:
                            bisou.append(lys0['bis'][0])
                            # print(lineno(), bisou[0], lys0['bis'][0][0])
                        x1 = ''
                        for ken in lys0.keys():
                            # print(' KEN', ken)
                            # x1 = ''
                            for v1 in lys0[ken]:
                                if not x1:
                                    x1 = v1[0] + dicter[v1[0]][0]
                                elif '.' not in x1:
                                    x1 += dicter[v1[0]][0] + v1[0] + '.'
                                else:
                                    if not lys0['bis']:
                                        x1 += v1[0] + dicter[v1[0]][0]
                                    elif ken == 'bis':
                                        x1 += bisou[0][0] + bisou[0][1]
                                # print('     V1 LEN1', v1, 'X1', x1, ' ')
                        c10 = x1
                        break
                # print(' _ B² BIL.dicter', dicter, '\n_B²', dicter)
                return c10

            if toc == '1':  # FORMATAGE Signatures 1 clé
                '''def former(signal, topo, toc('1')): FORME SIMPLE
                Nous avons là un signal simple de la tonalité
                len(signatures.keys()) == 1: Une clé(key) unique dans la signature.'''
                if signal[0][:1] in signes[6:]:
                    signal.reverse()
                    revu = True
                    # (lineno(), '*******def|FORMER__', '****** FORMER Sig', signal, signes[9:])
                for si in signal:
                    if si in alteractif.keys():  # altéractif: Zones des altéractions
                        couler.append(si)
                        for acte in alteractif[si]:
                            box[0].append(acte)
                        # ('  *******Altéractif', alteractif[si], 'Si', si, 'BOX', box)
                        # *******Altéractif ['+3', '+4'] Si +3 BOX ['+3', '+4']
                    if si not in box[0]:
                        couler.append(si)
                        # # ('  *******NotBox', 'Si', si, box)
                    # # ('  *******', lineno(), couler, 'COULER')
                if revu is True:
                    couler.reverse()
                roule = signal[0][:1]
                roule += ''.join(it[1:] for it in couler)
                (lineno(), '  ROULE **Signature simple*****:', couler, roule)
                # 285   ROULE **Signature simple*****: ['+2', '+3', '+5'] +235
                return roule
            else:  # FORMATAGE Signatures à clés multiples
                ''' def former(signal, topo, toc('2')): FORME MULTIPLE
                Dans ce cas, la signature est composée de plusieurs signes.
                En tenant compte du sens de lecture de la signature, et de la valeur
                signée : La priorité va au nombre d'altérations dans le signe (###(^)),
                donc au rang respectif de la table des signes. Ligne 70.'''
                # donc = None
                # informatif = ['o*', '-*', '*', 'o', '-', 'x^', '+^', "^", 'x', '+']
                box[0] = []  # Box office.point
                top, aff1, aff3, tap, tec = [], [], True, [], True  # top: Stocke, tip: Aussi
                # (lineno(), ' topo', topo, 'envers', envers)
                # 207  topo ['-2', '+3', '+4', '+5'] envers ['+5', '+4', '+3', '-2']
                # informatif = ['o*', '-*', '*', 'o', '-', 'x^', '+^', "^", 'x', '+']
                # Séparation des signatures opposées dans informatif['']
                infime = ['o*', '-*', '*', 'o', '-']
                survole = ['x^', '+^', '^', 'x', '+']
                # print(' infime', infime, 'survole', survole)
                # print(' topo', topo, 'envers', envers)
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
                    # for toto in topo:):):)
                    if tec:
                        tec = False
                        for tipi in topo:
                            t00 = tipi[:len(tipi) - 1]
                            if t00 in informatif[5:] and tipi in alteractif.keys():
                                topos = envers.copy()
                                # print('TIPI sort', tipi, envers)
                    for tipi in topos:  # Topo : Prise de vue binaire
                        if tipi[:len(tipi) - 1] == info:  # info = informatif[]
                            # ('TIPI sort', tipi[:len(tipi) - 1], topos, 'Info', info)
                            # Tipi diatonique.module
                            if tipi in alteractif.keys():  # Altéractive Keys()
                                # print(lineno(), '*** Tipi:', tipi, '. Box', box)
                                # Enregistre tipi.Keys() in original.Box[0] & Top[]
                                # tic = tipi[:len(tipi) - 1]  # Tic égal signes.tipi
                                if tipi not in box[0]:
                                    top.append(tipi)
                                    box[0].append(tipi)
                                    paris = tipi[len(tipi) - 1:]
                                    tap.append(paris)
                                    # print('** Lecture altéractif **', tipi, box, 'TOP', top)
                                # print(lineno(), tipi, '. TOP', top, '. BOX1', box, 'Tipi', bil)
                                # L'altéraction a des valeurs altératives
                                for ti in alteractif[tipi]:  # Tuteur des altéractions
                                    # print(lineno(), '  alteractif[]', 'TI', ti, box, 'Tap', tap)
                                    if aff1:
                                        ta = ti[len(ti) - 1:]
                                        # print('AMPLIFIER TIPI', aff1, )
                                        if ta in aff1[0]:
                                            aff3 = False
                                            # print('AMPLIFIER TIPI', aff1)
                                    if ti not in box[0] and aff3 is True:
                                        # titi, tio = ti[len(ti) - 1:], ''
                                        box[0].append(ti)
                                        if ti not in topo:
                                            paris = ti[len(ti) - 1:]
                                            tap.append(paris)
                                            top.append(ti)
                                            tut, tot = {}, []
                                            if tap.count(paris) > 2:
                                                # ww = 0
                                                for tip in top:
                                                    tac1s = tip[:len(tip) - 1]
                                                    tac1n = tip[len(tip) - 1:]
                                                    if tac1n == paris:
                                                        tut[tac1s] = []
                                                        tut[tac1s].append(tip)
                                                        tutu = informatif.index([tac1s][0])
                                                        tut[tac1s].append(tutu)
                                                        tot.append(tutu)
                                                        # print('info', tut[tac1s])
                                                for wkw, wvw in tut.items():
                                                    if wvw[1] == max(tot):
                                                        top.remove(wvw[0])
                                                        paris = wvw[0][len(wvw[0]) - 1:]
                                                        tap.remove(paris)
                                                        # print('.', lineno(), ':', wvw, tap, top)
                                                # print('.', lineno(), ':', 'T', tut, tot, max(tot))
                                            # print(lineno(), '. NotTopo', ti, '. Top', top, tap)
                                        else:
                                            tic = ti[len(ti) - 1]
                                            for sig in informatif:
                                                tiens = sig + tic
                                                if tiens in top:
                                                    paris = tiens[len(tiens) - 1:]
                                                    tap.remove(paris)
                                                    top.remove(tiens)
                                            # print(lineno(), '. YesTopo*', ti, '"T"', top, box, tap)
                                # print('* * * * * Altérer tipi0', tipi, 'Top', top, box, '"Tap"', tap)
                            elif tipi in amplifier.keys():  # L'amplification termine
                                # print('= = = = = Amplifier tipi0', tipi, 'Top', top, box, '"Tap"', tap)
                                for tipi_val in amplifier[tipi]:
                                    tv1 = tipi_val[len(tipi_val) - 1:]
                                    if tv1 not in aff1:
                                        aff1.append(tv1)
                                # print('AMPLIFIER TIPI', aff1)
                                if tipi not in box[0]:
                                    paris = tipi[len(tipi) - 1:]
                                    tap.append(paris)
                                    top.append(tipi)
                                    box[0].append(tipi)
                                    # print('=', lineno(), 'A_Tipi', tipi, 'Top', top, 'Box', box, tap)
                                for tu in amplifier[tipi]:
                                    # ('Amplifier tipi1', tipi)
                                    if tu not in box[0]:
                                        box[0].append(tu)
                                        # print('=', lineno(), 'A.Box*', '*T', tu, box, 'TOP', top, tap)
                                    if tu in topo:
                                        tee = tu[len(tu) - 1:]
                                        # print('=', '.A YesTopo ', tu, '"top"', top, 'Tee', tee, tap)
                                        for ton in top:
                                            toi = ton[len(ton) - 1:]
                                            # print('..YesTopo', tu, ton, 'Top', top, 'Toi', toi, tap)
                                            if toi == tee:
                                                paris = toi[len(toi) - 1:]
                                                tap.remove(paris)
                                                top.remove(ton)
                                                # print('=', lineno(), '.A._*_* Ton', ton, 'TOP', top, tap)
                                # (lineno(), 'TIPI', tipi, amplifier[tipi], box, 'TOP', top)
                            elif tipi not in box[0]:  # Cas extrême en traitement
                                (lineno(), '*********ELIF', 'TIPI', tipi)
                                paris = tipi[len(tipi) - 1:]
                                tap.append(paris)
                                top.append(tipi)
                                box[0].append(tipi)
                                big.append(tipi)
                                # (lineno(), '****ELIF tipi', tipi, 'Top', top, 'Box', box)
                # print('^\n^ >>>', '** TOP', top, '\n^ >>> ** TAP', tap, '\n^ >>> ** TOPO', topo)
                bis, top_copy = {}, top.copy()
                for tipi in top_copy:  # Déduire les doubles
                    ct2n = tipi[len(tipi) - 1:]
                    if tap.count(ct2n) == 1:
                        # print('...*', lineno(), '  *  Tipi', tipi, top, 'Tap', tap)
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
                        # print('bis[k_bis] = ', bis[k_bis], bon)
                        # print('Max', max(vb1, vb2), 'VB1&2&0', vb1, vb2, vb0, 'Min', min(vb1, vb2))
                        # print('V_BIS[1].survole', k_bis, v_bis[1], 'Rang VB0', vb0, top)
                    elif v_bis[1][0] in infime:
                        vb1 = infime.index(v_bis[1][0])
                        vb2 = infime.index(v_bis[1][1])
                        vb0 = min(vb1, vb2) - max(vb1, vb2)
                        top.remove(v_bis[0][0])
                        top.remove(v_bis[0][1])
                        bon = signes[vb0] + k_bis
                        top.append(bon)
                        # print('Max', max(vb1, vb2), 'VB1&2&0', vb1, vb2, vb0, 'Min', min(vb1, vb2))
                        # print('V_BIS[1].infime', k_bis, v_bis[1], 'Rang VB0', vb0)
                        # print('\n\n\n\n\n\n\n\n\n')
                # print('_BIS :', lineno(), 'bis', bis, 'vb0', vb0)
                cap = bil_riff(top)
                # print(':', lineno(), 'ToP', top, 'Cap', cap, 'BiS', bis)
                return cap
            #
            #
        # (lineno(), ' §  Signatures', signatures)
        # 249 §  Signatures {'-': [63, '-3', '-5']}
        for ks, kv in signatures.items():
            cou = None
            if len(signatures.keys()) == 1:  # Signatures 1 clé
                '''Quand il y a un seul signe dans la signature:'''
                # ('..... ', lineno(), '|', len(kv), kv, 'KV_valeur')
                if len(kv) == 2:
                    cou = kv[1]
                    # ('SK.1     *   len value = 2:', cou)
                elif len(kv) == 3:
                    for kepi in kv:
                        if kepi in alteractif.keys():
                            cou = kepi
                    if cou is None:
                        cou = kv[1] + kv[2][1:]
                    # ('SK.1     *   len value = 3:', cou)
                elif len(kv) > 3:
                    cou = former(kv[1:], [], '1')
                    # (lineno(), 'SK.1     *   len value > 3:', cou, 'cou')
                (lineno(), ' Signature 1 Clé_keys()) == 1:', fol, 'ks', ks, 'KVal', kv, 'COU', cou)
            else:  # Signatures à clés multiples
                cou = former(signatures, photo, '2')
                print(lineno(), ' Signature clé multi           ', '. COU ', cou, '\nµnit FONDRE')
                # ('C c c c c c c c c c c c c Compteur', compteur)
                break  # Traitement via formation
            noms_dic[kv[0]] = cou
            print(' *  ', lineno(), 'KV', kv, '\t\t COU _: ', cou, '\nµnit UNIC')
        if 'maj' in photo:
            cou = photo[0]
            print(' *  ', lineno(), '\t\t\t\t     COU _: ', cou, '')
        (lineno(), '  noms_dic', noms_dic[66], noms_dic, '\n')
        # print('affirmatif[0]', affirmatif[0], "alteractif['x2']", alteractif['x2'])

    fix = 0  # Section maj7_fonc(..)
    groupe = {}
    while fix < 66:  # dic_analyse: Infos gammes
        fix += 1
        tab_faible[fix] = []
        dia_binaire[fix] = []
        print('\n', lineno(), '__________________________________________________________________')
        # (lineno(), 'Fix', fix, 'FF', ff[:len(ff) - 1])  # Moins retour chariot
        # 88 Fix 61 FF ['1', '0', '2', '-3', '0', '0', '+4', '5', '0', '6', '0', '7',
        # [((1, 61), '101100110101')]]
        groupe[fix] = []
        if fix in unic.keys():  # Unic : Premières gammes faciles (Ligne 71)
            for fo in fondre[fix]:
                groupe[fix].append(fo)
            # print('', 'fondre', fondre[fix])
            for bi in binez[fix]:
                groupe[fix].append(bi)
            # print('', 'binez', binez[fix])
            depuis = len(groupe[fix])
            # print('FONDRE.GROUPE =', fix, groupe[fix])
            # 530 FONDRE.GROUPE = ['101010110101', '101011010101'] . FIX = 66
            # Unic dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
            dep = []
            while depuis:
                for i in range(0, 67):
                    # print('I', i)
                    for ff in groupe[fix]:
                        # print('.. FF', ff[0][1], i)
                        if i == ff[0][1] and ff[0][0] not in dep:
                            dep.append(ff[0][0])
                            # print('F F F F', ff[0], i, dep)
                            print('\n >>>>', lineno(), fix, '\tM22', ff[0][1], '\tM23:', ff[0][0])
                            depuis -= 1
                            fond_gam(ff[0][0], fix)  # fond_gam: Fonction envoi(unic-fondre)

            # print(lineno(), 'Fondre', fondre[fix], '\nUnic', unic.keys())
            # 529 Fondre [(('101101010101', 4), 65), (('101010101101', 11), 65)]
            # Unic dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
            #
            # print('**maj7(unic)** ', lineno(), fix, 'unic[fix][-1][0][1] =', unic[fix][-1][0][1])
            # **maj7(unic)**  253 66 unic[fix][-1][0][1] = 101011010101
        elif fix in fondre.keys():  # Fondre : Gammes secondaires (Ligne 72)
            # print('Fondre', fondre[fix])
            # print(lineno(), 'FIX', fix, 'Foule', len(fondre.keys()))
            for fo in fondre[fix]:
                groupe[fix].append(fo)
            # print('', 'fondre', fondre[fix])
            for bi in binez[fix]:
                groupe[fix].append(bi)
            # print('', 'binez', binez[fix])
            depuis = len(groupe[fix])
            # print('FONDRE.GROUPE =', fix, groupe[fix])
            # 530 FONDRE.GROUPE = ['101010110101', '101011010101'] . FIX = 66
            # Unic dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
            dep = []
            while depuis:
                for i in range(0, 67):
                    # print('I', i)
                    for ff in groupe[fix]:
                        # print('.. FF', ff[0][1], i)
                        if i == ff[0][1] and ff[0][0] not in dep:
                            dep.append(ff[0][0])
                            # print('F F F F', ff[0], i, dep)
                            print('\n >>>>', lineno(), fix, '\tM22', ff[0][1], '\tM23:', ff[0][0])
                            depuis -= 1
                            fond_gam(ff[0][0], fix)  # fond_gam: Fonction envoi(unic-fondre)
            '''my2 = []  # my2: Créer liste des poids légers par gamme
            for mz in fondre[fix]:
                my = mz[0][1]
                tab_faible[fix].append(my)
                my2.append(my)
            my2.sort()  # my2: Trié
            print('MY2', my2)
            double1 = []  # double1: Liste binaire lue
            double2 = []  # double2: Liste poids lue
            for m22 in my2:  # my2: Lecture liste Ordre croissant des pesants
                ('**_**', lineno(), 'FIX€', fix, '*M22*', m22, 'fondre[fix]', fondre[fix][0])
                for m23 in fondre[fix]:  # m23: Éléments origine fondre
                    if m22 in m23[0] and m23[0][0] not in double1:  # m22: Pesant local
                        double1.append(m23[0][0])  # double1: Forme binaire
                        double2.append(m22)  # double2: Mesure primaire
                        (lineno(), 'M23', m23, 'M22', m22, 'M23²', m23[0][0])
                        (lineno(), '>> double1', double1)
                        # print('\n\n>>>>', lineno(), fix, 'my2:', my2, 'M22:', m22, 'M23', m23[0])
                        # print('Fondre', fondre[fix])
                        (lineno(), '>> double2', double2)
                        # (fondre) 267 63 my2: [7, 10, 18] M22: 18 M23 100101101101
                        fond_gam(m23[0][0], fix)  # fond_gam: Fonction envoi(fondre)
                        break  # Stoppe quand binaire rencontré
            (lineno(), fix, 'MY2', my2, 'Fondre', fondre[fix][0], '\n')'''
    (lineno(), 'GEM DicFondre', fondre[66], '\nUnic', unic.keys())
    # print('Unic', unic[21], '\n\nFondre', fondre[29])


def dana_fonc(dana):
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
    Union : 1- Les tonalités aux mêmes poids. 2- Les poids aux mêmes rangs. 3- Les tonalités aux mêmes degrés
        1) Les gammes à masses égales. 2) Les reliefs des pesants. 3) Les fondements réguliers."""

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


def seption(mode_poids, k1, pc1, gm1, maj7, h_b):
    """Réception des poids modaux standards à augmenter & Création 'globdic_Dana.txt'.
    L'argument 'maj7' est le dictionnaire des modes maj 7èmes et poids standards par gamme"""
    # Mode_poids = Sept modes diatoniques par gamme. Comprend les 66 gammes.
    ('\n', lineno(), 'K1=', k1, ' ¤ GEM M_P', mode_poids, '\nPC1=', pc1, '\nGm1=', gm1.keys())
    # 238 K1= 66  ¤ GEM M_P [[0, 0, 0, 5, 0, 0, 0], [0, -3, -4, 0, 0, -7, -8],
    # [0, 0, -4, 0, 0, 0, -8], [0, 0, 0, 0, 0, 0, 0], [0, -3, -4, 0, -6, -7, -8],
    # [0, 0, -4, 0, 0, -7, -8], [0, 0, 0, 0, 0, 0, -8]]
    # PC1= ['1', '0', '2', '0', '3', '4', '0', '5', '0', '6', '0', '7', [((0, 66), '101011010101')]]
    # Gm1= dict_keys([21, 24, 38, 40, 45, 47, 48, 51, 55, 58, 61, 62, 64, 65, 66])
    goo = []
    cumul = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    dic_analyse[k1] = []  # :Dana initie table
    dic_diatonic[k1] = []  # :Maj7_fonction initie 66 diatoniques
    dic_diatonic[k1].append(mode_poids)
    if pc1:
        dic_pc[k1] = []  #
        dic_pc[k1].append(pc1)
        (lineno(), '.................', 'DIC PC', dic_pc)
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
    fil_analyse = open('GlobalTexte/globdic_Dana.txt', 'w')
    for ky1, va1 in dic_analyse.items():  # dic_analyse: Infos Dana
        mm = str(ky1) + str(va1)  # ky1: Numéro gamme
        mm += '\n'  # va1: Modes poids augmentés
        fil_analyse.write(mm)
    fil_analyse.close()  # Écriture fichier globdic_Dana.txt

    if len(dic_analyse.keys()) == 66:
        dana_fonc(dic_analyse)
        maj7_fonc(gm1, maj7, h_b)
        # glob_in_acc.inv_acc(dic_pc)


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

    seption(mode_po, 1, {}, {}, {}, {})
