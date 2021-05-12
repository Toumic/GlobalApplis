# Python 3.9 UTF-8
# Lundi 19 avril 2021 à 13h 57m (premières lignes)
# Lundi 3 mai 2021 (Développements diatoniques)
#
# Conçu par Vicenté Llavata Abreu | Vicenté Quantic | Toumic
# Module GlobModelGammy.py

""" Module d'application au traitement de la résultante clustérienne
en une diatonie relative à la gamme naturelle musicale.
    * L'aspect diatonique de la gamme:_ = Sur une octave de 12 notes
    * L'aspect diatonique du tétracorde:_ = Sur l'éventail du tétra
Il y a autant de notes que de modulations diatoniques et
les ensembles fondamentaux n'ont pas les mêmes modulations
Ce module trie les diatoniques afin d'un rassemblement fondamental
sans exécuter le traitement des tonalités avec les signatures (b/#)
Afin de faciliter le traitement, chaque entrée [1,2,3,4] devient [1,1,1,1]
    Rajouté: Pour plusieurs tétracordes de même longueur
        Une suite consécutive de zéros tient de famille diatonique
"""

import GlobGamFonds

glob_fond = GlobGamFonds


def gammy():
    cluster, coupler, recoder = [], [], []
    diatonic_tetra = {}
    diatonic_gamme = {}
    zoom_local = {4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 13: []}
    zoom_biner = []
    binariseur = ['1111']

    # Définition fondamentale de base
    """Degrés diatonic's tétras"""

    def tonale(tone):
        # Fonction Cas(Compare/Renverse)
        def compare(idem, tete):
            """:idem = Liste | :tete = String"""
            c10, t10 = tete.count('1'), ''
            if c10 != len(idem):
                for tee in range(len(idem)):
                    idem.insert(0, idem.pop())
                    eden = ''.join(i for i in idem)
                    if eden in binariseur:
                        break
                else:
                    binariseur.append(tete)
        """ & Apprendre & Compose Long Degré
        :Tone est un dictionnaire a clef & définition diatonique
            Tone{1: ['1234', '2341', '3412', '4123'], 2:}
        :Vas liste les clefs des définitions diatoniques
            Vas[1]
        :Clef = 1
            Tone[Clef] = ['1234', '2341', '3412', '4123'] """
        fille = [0]  # Longueur Tone(Values())
        """& Apprendre & Binariser Long Degré"""
        for uns, vas in tone.items():  # 1ère tone(Entrée tétra/gamme)
            fille[0] = len(vas)
            """& Apprendre Long Degré (Zoom_Local)      """
            zoom_local[fille[0]].append(uns)
        """& Binariser Long Degré (Zoom_Biner) = ['1111','11101','11011,,     """

        for key, tilt in zoom_local.items():
            """Exp: Zoom.() = {Key(4): Tilt([1]), K(5): T([2, 7, 22]), K(6): T([3, 8, 12, 23,]),}"""
            for indy in tilt:  # Indy = Tilt[Value].Key()
                titre, trans = '', []
                entre = tone[indy][0]  # :entre = Tone[Indy][1er Degré]
                for en in list(entre):  # :en = :entre Chiffre À Chiffre
                    if int(en) > 0:     # Trans (1,2,3) en (1,1,1)
                        titre += '1'    # True (0,0) en (0,0)
                        trans.append('1')
                    else:
                        titre += '0'
                        trans.append('0')
                """Opération Compare"""
                compare(trans, titre)
                zoom_biner.append(titre)

    # Chargement des fichiers
    def lecteur():
        # Chargement Fichier.txt
        """GlobDicTCord = Tétras uniques: 1234"""
        fil_cluster = open('globdicTcord.txt', 'r')
        for d in fil_cluster:
            cluster.append(d)
        fil_cluster.close()
        """GlobDicTCoup = Tétras couplés: 1234,0,5678"""
        fil_couple = open('globdicTcoup.txt', 'r')
        for d in fil_couple:
            coupler.append(d)
        fil_couple.close()
        """GlobDicTCode = Tétras codés:1234=#/b(1234)#/b(5678)"""
        fil_codage = open('globdicTcode.txt', 'r')
        for d in fil_codage:
            recoder.append(d)
        fil_codage.close()

    """CLUSTER GlobDicTCord = Tétras uniques: 1234 cluster[]"""
    """COUPLER GlobDicTCoup = Tétras couplés: 1234,0,5678 coupler[]"""
    """RECODER GlobDicTCode = Tétras codés:1234={[#/b(1234)][#/b(5678)]} recoder[]"""
    lecteur()

    # Définition diatonic_tetra tétra / gamme
    """Cycle degrés tétras non signés"""

    def transpose(module):
        mirez, modes = '', []
        oxo, oyo, ozo = 0, 0, module[-1]
        while 1:
            mirez += module[oxo]  # Donnée :module
            if ozo != '8':
                if module[oxo] == '4':  # Entrave :'8'
                    oxo = 0
                else:
                    oxo += 1
            else:
                if module[oxo] == '8':  # Entrave :'8'
                    oxo = 0
                else:
                    oxo += 1
            if len(mirez) == len(module):
                oyo += 1
                oxo = oyo
                modes.append(mirez)
                if ozo != '8':
                    if mirez[0] == '4':  # Entrave :'8'
                        break
                else:
                    if mirez[0] == '8':  # Entrave :'8'
                        break
                mirez = ''
        if len(module) < 10:
            diatonic_tetra[col[0]] = modes
        else:
            diatonic_gamme[col[0]] = modes

    # Origine tétra cluster[]
    """Les tétras uniques: 1234"""
    col = [0]
    for clou in cluster:
        tr1 = str(clou[:len(clou) - 1])
        col[0] += 1
        transpose(tr1)
    tonale(diatonic_tetra)

    # Fondamentales gammes coupler[]
    """Les fondamentales sont plus légères 1234,0,5678"""
    col = [0]
    for clou in coupler:
        tr1 = str(clou[:len(clou) - 1])
        col[0] += 1
        transpose(tr1)
    tonale(diatonic_gamme)

    # Envoi Binariseur
    glob_fond.diatonic(binariseur)

    # Tétracorde binaire recoder[]
    """L'alternative tétracordique 1234=#/b(1234)#/b(5678)"""
    """Binariseur des couples tétras 99/462"""
