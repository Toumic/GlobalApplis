# Python utf8

# Moulin modal à comparaisons majeures
#
# Nécessités pour repérages:
"""
Tableau des signatures majeures (Comparaisons, :gamme_poids:)
    :gamme_poids: = {1: [0,0,0,0,0,0,0], 2: [0,0,-4,0,0,0,-8],
Tableaux modèles supposés fondamentaux (Toniques)
    1: Signature numérique pour chaque mode diatonique
        :mode_poids = [[0,-3, -5, 7, 7, 7,0],[0,-3, -5, -6, 7, 7,0],
    2: Signature binaire correspondante
        :mode_biner = ['111000001111','111100000111','111110000011',"""
mages_biner = ['101011010101', '101101010110', '110101011010',
               '101010110101', '101011010110', '101101011010',
               '110101101010']

gamme_poids = {1: [0, 0, 0, 0, 0, 0, 0], 2: [0, 0, -4, 0, 0, 0, -8],
               3: [0, -3, -4, 0, 0, -7, -8], 4: [0, 0, 0, +5, 0, 0, 0],
               5: [0, 0, 0, 0, 0, 0, -8], 6: [0, 0, -4, 0, 0, -7, -8],
               7: [0, -3, -4, 0, -6, -7, -8]}

signes = ['', '+', 'x', '^', '^+', '^x', '°*', '-*', '*', '°', '-']


def seption(mode_poids):
    print('GEM', mode_poids[0])
    cumul = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    # Dico gamme_poids & Key_mode Majeur
    for gpk, gpv in gamme_poids.items():
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
    # Cumul poids cumul.keys(values)
    mana1, mana2 = [], []
    for kayac, rame in cumul.items():
        aaa = 0
        for van in rame:
            aaa += van[0]
        mana1.append(aaa)  # Version signée (±)
        mana2.append(abs(aaa))  # Version absolue (|)
    # Démultiplications des moyennes pour seption notes
    moyen = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for moi in range(len(mana2)):
        moyen[moi + 1].append(mana2[moi])
        accroc = mana2[moi]
        while accroc > 1:  # Gammes Log.7
            accroc /= 7
            if accroc > 0:
                moyen[moi + 1].append(accroc)
    moo = []
    for mo0, mo1 in moyen.items():
        print('Intro  mo0:', mo0, '     moo:', moo, '\n', mo1, mode_poids[mo0-1])
        noo, mp7, my1 = True, 0, 0
        for mo7 in mode_poids:
            if mo7.count(0) == 7:
                mp7 = mo7.count(0)
        if len(mo1) != 1:
            # print('   If/len  mo0:', mo0, 'moo:', moo, mode_poids[mo0-1])
            for mno in mo1:
                # print(f' FOR Mno:{mno} {mo1}')
                if int(mno) == 1:
                    my1 = 1
                    print(f' GEM Mno:{mno} {mode_poids[mo0-1]} ')
                    for mmm in range(len(mode_poids[mo0 - 1])):
                        no0, no1 = mmm + 1, mode_poids[mo0 - 1][mmm]
                        if mp7 != 7:
                            if mmm in (0, 6):
                                no1 = 1
                                if mmm == 6 and mode_poids[mo0 - 1][mmm] == 0:
                                    no1 = 7
                            if no1 != 0:
                                no3 = abs(no1) - no0
                            # print('mmm', mmm, 'no1:', abs(no1), '- no0', no0, '= no3', no3)
                            if abs(no3) > 2:
                                # print(1, no0, 'no3:', no3)
                                noo = False
                                break
            if not noo:
                # print(2, noo, 'no3:', )
                break
        if noo and my1 == 1:
            moo.append(mo0)
            # print(3, noo, 'no3:', moo, my1)
            if mp7 == 7:
                break
    # print(moyen, '\n Diviser par le nombre de notes')
    """Cadence dégressive facteur seption résume.
    Démultiplication du poids modal"""
    mots = [[]] * len(moo)
    if moo:
        roue = 0
        # print('Moo:', moo)
        for oom in moo:
            # print(mode_poids[oom - 1], len(mode_poids[oom]))
            rote, rap = [], []
            for mon in range(len(mode_poids[oom - 1])):
                toto = mode_poids[oom - 1][mon]
                if toto == 0:
                    moto = 0
                elif toto < 0:
                    moto = toto + (mon + 1)
                else:
                    moto = toto - (mon + 1)
                # print('Mon', mon + 1, 'toto', toto, 'moto', moto)
                rote.append(moto)
            for ro1 in range(7):
                if ro1 in (0, 6):
                    rap.append(ro1 + 1)
                    # print('\n06', ro1)
                else:
                    rap.append(signes[rote[ro1]] + str(ro1+1))
                    # print('12345', ro1)
                # print('Rote', rote, rap, '   ', ro1)
            mots[roue].append(rap.copy())
            rote.clear()
            roue += 1
    return mots


if __name__ == '__main__':
    print(f' GEM Quelle seption !')
    mode_bi = ['111000001111', '111100000111', '111110000011',
               '111111000001', '111111100000', '100000111111',
               '110000011111']
    mages_bi = ['101011010101', '101101010110', '110101011010',
                '101010110101', '101011010110', '101101011010',
                '110101101010']
    mode_po = [[0, -3, -5, 0, -6, -8, 0], [0, -3, -5, -6, -6, -8, -10],
               [0, 4, 4, 5, 0, 7, 0], [0, -3, 4, 5, 0, -7, 0],
               [0, -3, -5, 5, 0, -7, -9], [0, 3, 0, 0, 7, 7, 0],
               [0, -3, 0, 0, -6, 7, 0]]
    mages_po = [[0, 0, 0, 0, 0, 0, 0], [0, 0, -4, 0, 0, 0, -8],
                [0, -3, -4, 0, 0, -7, -8], [0, 0, 0, +5, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, -8], [0, 0, -4, 0, 0, -7, -8],
                [0, -3, -4, 0, -6, -7, -8]]
    gamme_po = {1: [0, 0, 0, 0, 0, 0, 0], 2: [0, 0, -4, 0, 0, 0, -8],
                3: [0, -3, -4, 0, 0, -7, -8], 4: [0, 0, 0, +5, 0, 0, 0],
                5: [0, 0, 0, 0, 0, 0, -8], 6: [0, 0, -4, 0, 0, -7, -8],
                7: [0, -3, -4, 0, -6, -7, -8]}
    fff = seption(mages_po)
    print(' GEM FFF', fff)
