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


def gammy(mage, cape):
    cluster, coupler, recoder = [], [], []
    print(f' \n Mage:{mage} \n Cape:{cape} \n')
    diatonique = {}

    def lecteur():
        # Chargement Fichier.txt
        # print(f'Hi, {mage}')
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

    # Définition diatonique tétra / gamme
    def transpose(module):
        mirez, modes, motus = [], [], '1234'
        long = len(module)
        # wc= Tour entier; ok= Tour degré
        ok, go = -1, 0
        for wc in list(module):
            ok += 1
            ok += go
            print(f' WC{wc}')
            for cap in range(long):
                modes.append(list(module)[ok])
                print(f'Cap{cap} Modes{modes} OK{ok}')
                ok += 1
                if ok > long:
                    ok = -1
            go += 1
            des = ''.join(d for d in modes)
            modes.clear()
            mirez.append(des)
            print(f'Mirez{mirez}')
            # break
        # wc= Tour entier; ok= Tour degré
        # wc, ok, go = 0, 0, 0
        # mirez = [module[wc]]  # mirez= Index module clef
        # print(f'****    Module{mirez} module{module}  {motus[wc]}')
        """while 1:
            tonal = module[wc]  # tonal= Degré lecture module
            # Tonique premier degré [wc]
            for cas in range(1, long):
                if tonal != '0':
                    ok += 1
                    ok += go
                    posez = mage.index(list(motus)[ok])  # posez= Tonalité majeure
                    visez = module.index(module[wc])  # visez= Tonalité réelle
                    moins = visez - posez  # moins= Signature tonale
                    point = cape[moins] + tonal
                    modes.append(point)
                    if ok > len(motus):
                        ok = 0
                        go += 1
                    # print(f' Ok{ok} Mirez{mirez}{tonal}Tonal | Posez{posez} Point{point} Moins{moins}')
            if len(modes) == list(motus)[-1]:
                diatonique[module] = modes
            wc += 1
            if wc == long:
                print(f' Modes{modes}')
                break"""

        # print(f' Long: {str(long)}')
        print(f' T Longueur modèle{long},{module} Diatonique{diatonique}\n')
        pass

    # Particule tétracordique cluster[]
    """La plus petite partie d'une gamme 1234
        Définir les modulations diatoniques de l'élément"""
    col = 0
    for clou in cluster:
        tr1 = str(clou[:len(clou) - 1])
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
