# Python 3.9 UTF-8
# Lundi 19 avril 2021 à 13h 57m (premières lignes)
# Mardi ... 2021 (Développement des tétracordes)
#
# Conçu par Vicenté Llavata Abreu alias Toumic

""" Module d'application au traitement de la résultante clustérienne
en une diatonie relative à la gamme naturelle musicale.
    * L'aspect diatonique de la gamme
    * L'aspect diatonique du tétracorde
"""


def gammy(name):
    cluster, coupler, recoder = [], [], []

    def lecteur():
        # Chargement Fichier.txt
        print(f'Hi, {name}')
        """GlobDicTCord = Tétras uniques: 1234"""
        fil_cluster = open('globdicTcord.txt', 'r')
        for d in fil_cluster:
            cluster.append(d)
        # print(f'{cluster[0]}')
        fil_cluster.close()
        """GlobDicTCoup = Tétras couplés: 1234,0,5678"""
        fil_couple = open('globdicTcoup.txt', 'r')
        for d in fil_couple:
            coupler.append(d)
        # print(f'{coupler[0]}')
        fil_couple.close()
        """GlobDicTCode = Tétras codés:1234=#/b(1234)#/b(5678)"""
        fil_codage = open('globdicTcode.txt', 'r')
        for d in fil_codage:
            recoder.append(d)
        # print(f'{recoder[0]}')
        fil_codage.close()

    """CLUSTER GlobDicTCord = Tétras uniques: 1234 cluster[]"""
    """COUPLER GlobDicTCoup = Tétras couplés: 1234,0,5678 coupler[]"""
    """RECODER GlobDicTCode = Tétras codés:1234=#/b(1234)#/b(5678) recoder[]"""
    lecteur()

    # Développé diatonique tétra / gamme
    def transpose(module):
        long = len(module) - 1
        # print(f' Long: {str(long)}')
        print(f' Longueur modèle: {long} , {module} \n')
        pass

    # Particule tétracordique cluster[]
    """La plus petite partie d'une gamme 1234
        Définir les modulations diatoniques de l'élément"""
    col = 0
    for clou in cluster:
        tr1 = str(clou[:len(clou) - 1]) + '*****'
        print(f' Cloud[]: {clou[:len(clou) - 1]} Col {col}')
        # print(f' Clou: {clou}')
        if col > 2:
            break
        col += 1
        transpose(tr1)

    # Fondamentales gammes coupler[]
    """Les fondamentales sont plus légères 1234,0,5678"""

    # Tétracorde binaire recoder[]
    """L'alternative tétracordique 1234=#/b(1234)#/b(5678)"""
