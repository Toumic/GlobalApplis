# Python 3.9 UTF-8
# Lundi 19 avril 2021 à 13h 57m (premières lignes)
# Lundi 3 mai 2021 (Développements diatoniques)
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
sans exécuter le traitement des tonalités avec les signatures (b/#)
Afin de faciliter le traitement, chaque entrée [1,2,3,4] devient [1,1,1,1]
    Rajouté: Pour plusieurs tétracordes de même longueur
        Une suite consécutive de zéros tient de famille diatonique
"""

import GlobGamFonds

glob_fond = GlobGamFonds


def gammy():
    cluster, coupler, recoder = [], [], []
    diatonic_tetra = {4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    diatonic_gamme = {12: []}
    module_gamme = []
    bineur_gamme = []

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

    # Définition diatonic_tetra tétra / gamme_majeure
    """Cycle degrés tétras non signés"""

    def transpose(module):
        mirez, modes, binez1, binez2 = '', [], '', []
        ozo, ooo = len(module), list(module)
        if ozo < 12:
            for o in range(ozo):
                ooo.insert(0, ooo.pop())
                mirez = ''.join(i for i in ooo)
                modes.append(mirez)
            diatonic_tetra[ozo].append(modes)
        else:
            for o in range(ozo):
                ooo.insert(0, ooo.pop())
                mirez = ''.join(i for i in ooo)
                modes.append(mirez)
            for mo in modes[-1]:
                if int(mo) > 0:
                    binez1 += '1'
                else:
                    binez1 += '0'
            binez2.append(binez1)
            diatonic_gamme[ozo].append(modes)
            module_gamme.append(modes)
            bineur_gamme.append(binez2)

    # Origine tétra cluster[]
    """Les tétras uniques: 1234"""
    col = [0]
    for clou in cluster:
        tr1 = str(clou[:len(clou) - 1])
        col[0] += 1
        transpose(tr1)

    # Fondamentales gammes coupler[]
    """Les fondamentales sont plus légères 1234,0,5678"""
    col = [0]
    for clou in coupler:
        tr1 = str(clou[:len(clou) - 1])
        col[0] += 1
        transpose(tr1[:12])

    # Envoi Binariseur
    glob_fond.diatonic(module_gamme, bineur_gamme)

    # Tétracorde binaire recoder[]
    """L'alternative tétracordique 1234=#/b(1234)#/b(5678)"""
