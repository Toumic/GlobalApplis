# Python utf8
# En construction
# Mercredi 8 septembre 2021 2021

# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# GlobInverseAcc
# Parodie à double sens et accords 1357

import inspect
from typing import Callable
# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno



gam_nat = "102034050607"
gam_not = "1234567"
gam_oblic = {}
# Table des degrés
table_deg = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

# dict_keys(['analyse', 'groupe', 'picolo', 'signaux'])


def inv_acc(pc, ego_p, ego_r):
    """Traitement pc clone dictionnaire global
    Synchronisation des modes diatoniques Formes classic et leurs inverses"""
    print('GIA GlobInverseAcc  binaires \n', pc.keys(), pc['groupe'][66, 'I'], '\n')
    compare = []
    # Traiter les premiers degrés à chaque fois
    for g1 in range(1, 67):  # g1 = Numéro gamme-indice
        deg_fix = table_deg[1]  # Fixation degré tonique 'I'
        prime = pc['groupe'][g1, deg_fix][0][0][0]
        pr_mod = list(prime)
        pr_mod.reverse()
        # print('Premier', g1, deg_fix, pr_mod)
        for g2 in range(1, 67):  # g2 = Numéro gamme-compare
            for d2 in range(1, 8):  # d2 = Degré diatonique
                d4 = table_deg[d2]
                second = pc['groupe'][g2, d4][0][0][0]
                sc_mod = list(second)
                # Mode symétrique visible (Quand g1 = g2)
                if pr_mod == sc_mod:
                    c1 = g1, deg_fix
                    c2 = g2, d4
                    c3 = c1, c2
                    compare.append(c3)
    # Comparaisons miroir (duo/iso)
    # Duo = Miroir 2 gammes | Iso = Miroir 1 gamme
    # Tonalité = Hauteur degré | Nom intervalle
    '''Notions basiques
        _ Quatrième degré :
            Par (altération ou altéraction) :
                Soit le nom compose une simple altération
                Soit le nom est influencé via l'altéractivité.
            Par (classic et/ou inverse) :
                Ordre diatonique classique et/ou inversé.
        _ Premier degré par (tonalité et/ou intervalle):
            Miroir ISO = 
                {[(1,i), (1,iii)], [(27,i), (27,ii)], [(30,i), (30,v)], 
                [(38,i), (38,iv)], [(42,i), (42,iii)], [(47,i), (47,ii)], [(53,i), (53,iii)], 
                [(57,i), (57,vi)], [(65,i), (65,iii)], [(66,i), (66,iv)]}.
            Miroir DUO : [28 tuples / 2 = 14 couples bipolaires]
                {(7,22), (11,15), (12,32), (13,31), (15,11), (16,35), 
                (22,7), (23,26), (24,25), (25,24), (26,23), (28,34), (29,33), (31,13), 
                (32,12), (33,29), (34,28), (35,16), (36,43), (39,41), (41,39), (43,36), 
                (44,49), (46,60), (49,44), (50,52), (52,50), (60,46)}. '''
    duo, iso, glob, cas = {}, {}, [], 0
    for com in compare:
        cas += 1
        # Arrangé problème nom majeur
        if not pc['signaux'][com[0]]:  # Majeur classé iso
            nom0 = 'Majeur'
        else:
            nom0 = pc['signaux'][com[0]][0][1]
        nom1 = pc['signaux'][com[1]][0][1]
        # Miroir ISO
        if com[0][0] == com[1][0]:
            # Cas majeur
            iso[cas] = []
            cas1 = com[0], nom0
            cas2 = com[1], nom1
            cas3 = cas1, cas2
            cas4 = 'ISO', cas3
            iso[cas].append(cas3)
            glob.append(cas4)
            # print(cas, 'ISO', com[0], nom0, '|==|', com[1], nom1)
        else:
            duo[cas] = []
            cas1 = com[0], nom0
            cas2 = com[1], nom1
            cas3 = cas1, cas2
            cas4 = 'DUO', cas3
            duo[cas].append(cas3)
            glob.append(cas4)
            # print(cas, '... DUO', com[0], nom0, '|!=|', com[1], nom1)
    for gl in glob:
        print('GLOBE', gl)
        break
    #
    '''Traitement données DANA(fonction)'''
    print('GIA EGO_poids', ego_p, '\nGIA EGO_rang', ego_r)


if __name__ == '__main__':
    print(f' GEM Quelle seption !')
    inv_acc({}, [], [])
