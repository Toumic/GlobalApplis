# Python3 utf8
# En construction
# Mercredi 8 septembre 2021 2021

# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# GlobInverseAcc
# Parodie à double sens et accords 1357

import inspect
from typing import Callable
import GlobGamVers6

progam = GlobGamVers6

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# Table des degrés
table_deg = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

# dict_keys(['analyse', 'groupe', 'picolo', 'signaux'])


def inv_acc(pc, ego_p, ego_r, pratic_k):
    """Traitement pc clone dictionnaire global
    Synchronisation des modes diatoniques Formes classic et leurs inverses
    Approfondissement des mouvements des poids modaux, inversions incluses,
    ainsi que les types de résolution des poids (bruts et fins)"""
    ('\n§ GIA GlobInverseAcc  binaires \n', pc.keys(), pc['groupe'][66, 'I'], '\n')
    # (lineno(), 'GIA pratique', pratic_k.keys())
    pratic = pratic_k.copy()
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
            Miroir ISO = [10 doubles tuples]
                {[(1,i), (1,iii)], [(27,i), (27,ii)], [(30,i), (30,v)], 
                [(38,i), (38,iv)], [(42,i), (42,iii)], [(47,i), (47,ii)], [(53,i), (53,iii)], 
                [(57,i), (57,vi)], [(65,i), (65,iii)], [(66,i), (66,iv)]}.
            Miroir DUO : [28 tuples / 2 = 14 couples bipolaires]
                {(7,22), (11,15), (12,32), (13,31), (15,11), (16,35), 
                (22,7), (23,26), (24,25), (25,24), (26,23), (28,34), (29,33), (31,13), 
                (32,12), (33,29), (34,28), (35,16), (36,43), (39,41), (41,39), (43,36), 
                (44,49), (46,60), (49,44), (50,52), (52,50), (60,46)}.
        _ Autre degré :
            Miroir DUO : [28 tuples / 2 = 14 couples bipolaires]
                {[(2, 'I') (5, 'III')], [(3, 'I') (4, 'III')], [(4, 'I') (3, 'III')], 
                [(5, 'I') (2, 'III')], [(6, 'I') (18, 'V')], [(8, 'I') (21, 'IV')], 
                [(9, 'I') (20, 'III')], [(10, 'I') (19, 'IV')], [(14, 'I') (17, 'V')], 
                [(17, 'I') (14, 'V')], [(18, 'I') (6, 'V')], [(19, 'I') (10, 'IV')], 
                [(20, 'I') (9, 'III')], [(21, 'I') (8, 'IV')], [(37, 'I') (54, 'IV')], 
                [(40, 'I') (55, 'IV')], [(45, 'I') (58, 'IV')], [(48, 'I') (56, 'III')], 
                [(51, 'I') (59, 'IV')], [(54, 'I') (37, 'IV')], [(55, 'I') (40, 'IV')], 
                [(56, 'I') (48, 'III')], [(58, 'I') (45, 'IV')], [(59, 'I') (51, 'IV')], 
                [(61, 'I') (64, 'IV')], [(62, 'I') (63, 'III')], [(63, 'I') (62, 'III')], 
                [(64, 'I') (61, 'IV')], } '''
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
    # Glob = Tables des degrés miroirs (ISO/DUO)
    '''f10 = 0
    for gl in glob:  # glob[tableau]
        f10 += 1
        print('GLOBE', f10, gl, '\n')
        break'''
    '''
    Traitement données DANA(fonction) :
        - (Car DANA a traité les données avant le calcul des toniques)
        Les 1ères informations de DANA Voir : GlobalDoc/Notes Analyses :
            Ego_p = Poids situés en haut de la liste :
                Mêmes poids modal = Mêmes poids diatoniques
            Ego_r = Ordre croissant des mesures diatoniques :
                Quand deux modes ont le même poids, il se crée un doublon
    Les modes sont rangés de façon primitive, et en ordre inversé :
        Classic = De 1 à 7. DANA = De 7 à 1
    Le précédent module GlobEnModes a détecté les modulations toniques
    Il faut par conséquent refaire même si c'est identique, bien-qu'inversé'''
    # print('GIA EGO_poids', ego_p.keys(), '\nGIA EGO_rang', ego_r.keys(), '.keys()\n')
    dic_rng, dic_dic = {}, {}
    tab_rng_fins, tab_rng_forts, cop_rng_fins, ind_cop_f1 = [], [], [], []
    nbr_org = 0
    for val in pc['groupe']:
        ana = pc['analyse'][val][1][0]  # Poids fins majeurs
        gro = pc['groupe'][val][0][0][1]  # Poids forts majeurs
        tab_rng_fins.append(ana)  # Tab_rng_fins = Tableau : Poids fins
        tab_rng_forts.append(gro)  # tab_rng_forts = Tableau : Poids forts
        cop_cop = ana, gro  # Cop_cop = Clé (Fin, Fort)
        nbr_org += 1  # Nbr_org = Indice rang réel du poids
        dic_rng[nbr_org] = cop_cop  # Dic_rng = Classement original des poids
        if val[1] == 'VII':
            dic_dic[val[0]], ind_cop_f1, ind_cop_f2 = [], [], []
            cop_str_fins, cop_str_forts = '', ''
            cop_rng_fins = tab_rng_fins.copy()
            cop_rng_forts = tab_rng_forts.copy()
            cop_rng_fins.sort()
            cop_rng_forts.sort()
            for tr in tab_rng_fins:  # Poids fins pas triés
                for kd in dic_rng.keys():
                    if tr == dic_rng[kd][0]:
                        cop_str_fins += str(cop_rng_fins.index(tr))
                        ind_cop_f1.append(tr)
                        # print('.Original KD', kd, dic_rng[kd], 'TR', tr)
                        break
            for tr2 in tab_rng_forts:  # Poids forts pas triés
                for kd2 in dic_rng.keys():
                    if tr2 == dic_rng[kd2][1]:
                        cop_str_forts += str(cop_rng_forts.index(tr2))
                        ind_cop_f2.append(tr2)
                        # print('.Original KD2', kd2, dic_rng[kd2], 'TR2', tr2)
                        break
            dic_dic[val[0]] = cop_str_fins, ind_cop_f1, cop_str_forts, ind_cop_f2
            # print('..Fin', cop_str_fins, 'Fort', cop_str_forts)
            # print(val[0], 'Fin', tab_rng_fins, '\nFor', tab_rng_forts, '\n')
            tab_rng_fins.clear()
            tab_rng_forts.clear()
            nbr_org = 0
    '''Le dictionnaire dic_dic '''
    # Consultation dictionnaire dic_dic
    # #print('dic_dic', dic_dic[1], '\n', dic_dic.keys(), 'Quant. :', len(dic_dic.keys()))
    ego_f11, ego_f12 = {}, {}  # Pour les poids maximums
    ego_f01, ego_f02 = {}, {}  # Pour les rangs
    val_fax_f1, val_fax_f2 = {}, {}  # Dico des valeurs en ordre original (corps) (fins/forts)
    val_fax_f3 = {}  # Dico des rangs forts&fins
    val_max_f1, val_max_f2 = [], []  # Tableaux des Maximums en ordre original (keys)
    val_rng_f1, val_rng_f2 = [], []  # Tableaux des rangs en ordre original
    for d_key, d_val in dic_dic.items():
        lob_fax_f1 = d_val[1], d_val[0]  # lob_fax_f1 = Union Poids fins + Rangs fins
        lob_fax_f2 = d_val[3], d_val[2]  # lob_fax_f2 = Union Poids forts + Rangs forts
        '''Indexation sur les poids maximums'''
        # Condition sur les poids fins
        if max(d_val[1]) not in val_max_f1:  # d_val[1] = Poids fins
            ego_f11[max(d_val[1])] = []  # Clé = Poids(max)
            ego_f11[max(d_val[1])].append(d_key)  # d_key = Valeur = Numéro de gamme
            val_max_f1.append(max(d_val[1]))  # Liste des clés d'accès aux gammes
            val_fax_f1[max(d_val[1])] = []  # Clé = Poids(max)
            val_fax_f1[max(d_val[1])].append(lob_fax_f1)  # lob_fax_f1 = Poids&Rangs fins
        elif max(d_val[1]) in val_max_f1:
            ego_f11[max(d_val[1])].append(d_key)
            val_fax_f1[max(d_val[1])].append(lob_fax_f1)  # lob_fax_f1 = Poids&Rangs fins
        # Condition sur les poids forts
        if max(d_val[3]) not in val_max_f2:  # d_val[3] = Poids forts
            ego_f12[max(d_val[3])] = []
            ego_f12[max(d_val[3])].append(d_key)
            val_max_f2.append(max(d_val[3]))
            val_fax_f2[max(d_val[3])] = []
            val_fax_f2[max(d_val[3])].append(lob_fax_f2)  # lob_fax_f2 = Poids&Rangs forts
        elif max(d_val[3]) in val_max_f2:
            ego_f12[max(d_val[3])].append(d_key)
            val_fax_f2[max(d_val[3])].append(lob_fax_f2)  # lob_fax_f2 = Poids&Rangs forts
        '''Indexation sur les rangs unifiés'''
        # Condition sur les rangs fins
        if d_val[0] not in val_rng_f1:  # d_val[0] = Rangs fins
            ego_f01[d_val[0]] = []  # Clé = Rang fin
            ego_f01[d_val[0]].append(d_key)  # d_key = Valeur = Numéro de gamme
            val_rng_f1.append(d_val[0])  # Liste des clés d'accès aux gammes
        elif d_val[0] in val_rng_f1:
            ego_f01[d_val[0]].append(d_key)
        # Condition sur les rangs forts
        if d_val[2] not in val_rng_f2:  # d_val[2] = Rangs forts
            ego_f02[d_val[2]] = []  # Clé = Rang fort
            ego_f02[d_val[2]].append(d_key)  # d_key = Toutes = 66.keys()
            val_rng_f2.append(d_val[2])  # d_val[2] = Liste des rangs forts
            val_fax_f3[d_val[2]] = []  # Clé = Rangs fins
            val_fax_f3[d_val[2]].append(d_val[0])  # d_val[3] = Liste des poids forts
    # print('\nego_f11 Mêmes maximums fins:\n', ego_f11.keys(), 'Quant. :', len(ego_f11))
    # print('ego_f12 Mêmes maximums forts:\n', ego_f12.keys(), 'Quant. :', len(ego_f12))
    # #print('\n val_fax_f1 Mêmes poids&rangs fins:\n', val_fax_f1.keys(), 'Quant. :', len(val_fax_f1))
    # #print('val_fax_f2 Mêmes poids&rangs forts:\n', val_fax_f2.keys(), 'Quant. :', len(val_fax_f2))
    # #print('val_fax_f3 Rangs forts&fins:\n', val_fax_f3.keys(), 'Quant. :', len(val_fax_f3))
    # print('\nego_f01 Mêmes rangs fins:\n', ego_f01.keys(), 'Quant. :', len(ego_f01))
    # print('ego_f02 Mêmes rangs forts:\n', ego_f02.keys(), 'Quant. :', len(ego_f02))

    progam.progam(pratic, glob, ego_p, ego_r)


if __name__ == '__main__':
    # #print(f' GEM Quelle seption !')
    inv_acc({}, {}, {}, {})
