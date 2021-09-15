# Python 3.9 UTF-8
# Lundi 19 avril 2021 à 13h 57m (premières lignes)
# Lundi 3 mai 2021 (Développements diatoniques)
# Mardi 27 juillet 2021
#
# Conçu par Vicenté Llavata Abreu | Vicenté Quantic | Toumic
# Module GlobModelGammy.py

""" Module d'application au traitement de la résultante clustérienne
en une diatonie relative à la gamme_majeure naturelle musicale.
    * L'aspect diatonique de la gamme_majeure:_ = Sur une octave de 12 notes
    * L'aspect diatonique du tétracorde:_ = Sur l'éventail du tétra
Il y a autant de notes que de modulations diatoniques et
les ensembles fondamentaux n'ont pas les mêmes modulations
Ce module trie les diatoniques afin d'un rassemblement fondamental
sans exécuter le traitement des tonalités avec les signes (b/#)
Afin de faciliter le traitement, chaque entrée [1,2,3,4] devient [1,1,1,1]
    Rajouté: Pour plusieurs tétracordes de même longueur
        Une suite consécutive de zéros tient de famille diatonique
"""

import GlobGamFonds

glob_fond = GlobGamFonds

fonder_tetra, fonder_gamme = [], []


def gammy():
    cluster, coupler, recoder = [], [], []
    diatonic_tetra = {4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    diatonic_gamme = {12: []}
    module_gamme, bineur_gamme = [], []

    # Chargement des fichiers
    def lecteur():
        """GlobDicTCord = Tétras uniques: 1234"""
        # Chargement Fichier.txt
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

    # Définition diatonic_tetra / Tétracordic
    """Cycle degrés tétras non signés (Quand 12340 = 34012)"""
    # Définition fondamental_gamme / Gammique
    """Cumul des 66 assimilés fondamentaux binaires"""

    def transpose(module):
        """Fonction Lecture Séquentielle Fichiers(Coupler, Cluster)"""
        modes, binez1, binez2 = [], '', []
        ozo, ooo = len(module), list(module)
        if ozo < 12:
            for o in range(ozo):
                ooo.insert(0, ooo.pop())
                mirez = ''.join(i for i in ooo)
                modes.append(mirez)
            diatonic_tetra[ozo].append(modes)
        else:
            """Flux du fichier coupler.txt Diatonic primitif"""
            """Cycle Global"""
            ooo.insert(0, ooo.pop())
            while ooo[0] == '0':
                ooo.insert(0, ooo.pop())
            mirez = ''.join(i for i in ooo)
            binez00 = ''
            for mi in mirez:
                if mi == '0':
                    binez00 += '0'
                else:
                    binez00 += '1'
            bins = list(binez00)
            stop = False
            for j in range(len(bins)):
                if bins not in fonder_gamme:
                    for i in range(len(bins)):
                        bins.insert(0, bins.pop())
                        while bins[0] == '0':
                            bins.insert(0, bins.pop())
                        break
                else:
                    stop = True
            if not stop:
                fonder_gamme.append(bins)

            # Zone Fin 2 Service Interne
            modes.append(mirez)

            for mo in modes[-1]:
                if int(mo) > 0:
                    binez1 += '1'
                else:
                    binez1 += '0'
            binez2.append(binez1)               # Fin 2 Service Interne
            diatonic_gamme[ozo].append(modes)   # Fin 2 Service Interne
            module_gamme.append(modes)          # Diatonic groupe Gammes
            bineur_gamme.append(binez2)         # Fin 2 Service Interne


    # Origine tétra cluster[]
    """Les tétras uniques: 1234"""
    col = [0]
    for clou in cluster:
        tr1 = str(clou[:len(clou) - 1])
        col[0] += 1
        transpose(tr1)

    # Diatoniques primitives coupler[]
    """Les fondamentales sont plus légères 1234,0,5678"""
    col = [0]
    for clou in coupler:
        tr1 = str(clou[:len(clou) - 1])
        col[0] += 1
        transpose(tr1[:12])

    # Envoi 66 Modes Binarisées
    glob_fond.diatonic(fonder_gamme)

    # Tétracorde binaire recoder[]
    """L'alternative tétracordique 1234=#/b(1234)#/b(5678)"""
