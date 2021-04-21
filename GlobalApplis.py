# Python 3.9 UTF-8
# Dimanche 28 mars 2021 à 19h 45m (premières lignes)
# Mardi 13 avril 2021 (Développement des tétracordes)
#
# Conçu par Vicenté Llavata Abreu alias Toumic

""" Script de construction des gammes musicales utilisant ces notes (C, D, E, F, G, A, B)
Explications:
    La création des gammes musicales englobe les notes & les intervalles dans une octave de 12 ½ tons,
    elle se concentre sur les tétracordes étant des corps de 4 notes. L'assemblage formé
    par les gammes gestionnaires de l'intervalle, assemble 2 modèles tétras superposés. La création
    tétracordique mène à une gammologie musicale à partir d'un simple cluster de 4 éléments."""

import GlobModelGammy

globgamy = GlobModelGammy

# Fichiers développés
"""..."""
# Fonction développement
"""..."""
# Déclarations des mémoires
tablette = []
dicoT, dicoM, dicoG = {}, {}, {}  # Dictionnaires(Tétra,Mode,Gamme)
voirT = {}
yoyoT = [0]
mini0 = '1234'  # Tétracorde primaire
octave = 13  # 13 emplacements
maxi0 = (octave - len(mini0)) - 1
tetra0, tetra1, t234 = [], ['1', '2', '3', '4'], []
tablette.append(tetra1)
# Itérations
t1, t2, t3, t4 = 0, 1, 2, 3  # maxi0 = 9
u, u1, u2, u3, u4 = 0, 0, 0, 0, 0  # unité de blocage
x, stop, stop0, stop1 = 0, True, False, 5
# Opération Dico(mixam)
mixam = {}  # Dépendances Degré(min/max)
""" Niveau T2 | MINI=1 MIDI=NULL MAXI=6 """
""" Niveau T3 | MINI=2 MIDI=T2+1 MAXI=7 """
""" Niveau T4 | MINI=3 MIDI=T3+1 MAXI=8 """
nt234 = [[2, [1, 6]], [3, [2, 7]], [4, [3, 8]]]
j = -1
gamme = '1020340506078'  # Chromatisme naturel
notes = 'CDEFGABC'  # Notes musique
alter = ['', '+', 'x', '^', '^+', '^x', '-*', '°*', '*', '°', '-']
tabas, tahau = [], []  # Tétra*défaut


# Fonction couplage tétracordique
def couple():
    x2, z = 0, 0
    for c in tablette:
        y, cyt, ctt = 0, [], []
        for tab in tablette:
            l_ct = len(c) + len(tab)  # Somme cas
            if octave >= l_ct:
                o_ct = octave - l_ct  # Différence
                if l_ct < octave and o_ct > 0:
                    for o in range(o_ct):
                        cyt.append('0')  # Vide zéro entre tétra
                ctt = []
                for t1f in tab:
                    if t1f != '0':
                        t2f = str(int(t1f) + 4)  # Vide zéro dans tétra
                    else:
                        t2f = '0'
                    ctt.append(t2f)
                dicoM[z] = tabas[x2] + tahau[y]
                """Suivre cot"""
                cot = c.copy()
                if len(cyt):
                    cot += cyt
                cot += ctt
                dicoT[z] = cot
                cyt = []
                y += 1
                z += 1
            # print(f'z{z} dicoT{dicoT[z]}\n')
        # if x2 == 2 and y == 2: break ####
        x2 += 1
    # for d in dicoT.values(): print(f'{d}\n')
    # for d in dicoM: print(f'{dicoM[d]}\n')


# Fonction format diatonique tétracordique
def diatone(dia):
    """ Chromatisation des tétras bas/haut """
    # print(f'Fonc Diatonie:{dia}')
    x1d, oo, o1o, o8o = -1, 0, [], []
    for deg in dia:
        oo = octave - len(dia)
        x1d += 1
        if int(deg) > 0:
            ged = str(int(deg) + 4)
            sign1 = x1d - gamme.index(deg)  # BAS bémol/dièse
            sign8 = (x1d + oo) - gamme.index(ged)  # HAUT bémol/dièse
            # print(f'Ged{ged}, sign8{sign8} x1d{x1d} oo{oo} dia{dia} gamme.index(ged){gamme.index(ged)}')
            if int(deg) > 0:
                # Signature dièse
                ego1 = alter[sign1]
                ego8 = alter[sign8]
            else:
                # Signature bémol
                ego1 = alter[sign1]
                ego8 = alter[sign8]
            ooo1 = str(notes[int(deg) - 1] + ego1 + deg)
            ooo8 = str(notes[int(ged) - 1] + ego8 + ged)
            # print(f'ego1&8 {ego1}:{ego8} | ooo1&8{ooo1}{ooo8}')
            if ooo1[1] in alter:
                o1o.append(ooo1)
            else:
                o1o.append(ooo1[0])
            if ooo8[1] in alter:
                o8o.append(ooo8)
            else:
                o8o.append(ooo8[0])
    tabas.append(o1o)
    tahau.append(o8o)
    # print(f'Tabas {tabas[-1]}:{tahau[-1]} Tahau | Dia{dia}')
    # print(f'TableT{tablette}')
    # print(f'Tabas{str(tabas)}')


# Charge limite tétra
for i in tetra1:
    if i != '1':
        j += 1
        mixam[j] = nt234[j][1]
# print(f'Mixam {mixam}')
# Développement tétracordique
while stop:
    # Fonction fabrication
    def brique(vrai):
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'FoncBric'
        # Vrai[1, 2, 4] Valeur(index) Nom(degré) Table[0]=['1', '2', '3', '4']
        # rang = tablette[0].index(nom)  # Index Nom Cluster[1,2,3,4]
        # print(f'_ Fonction nom:valeur {nom}:{valeur} Table {tablette[-1]} Vrai {vrai}|*FoncBric mox{maxi0}')
        vide, pose, terme, bric = 0, 0, vrai[-1], []
        # print(f'Rang={rang} pose={pose} vrai={vrai}')
        while 1:
            if vide == 0:
                pose += 1
                bric.append('1')
                # print(f'Fonc(0)|{bric}|Vide={vide}')
                vide += 1
            if vide in vrai:
                pose += 1
                bric.append(str(pose))
                # print(f'Fonc(vrai)|{bric}|Vide={vide}')
                if vide == vrai[-1]:
                    tetra3 = [o for o in bric]
                    tablette.append(tetra3)
                    # print(f'_ Fonction _ {bric}| brique_voirT')
                    break
                vide += 1
            if vide not in vrai:
                bric.append('0')
                # print(f'Fonc(faux)|{bric}|Vide={vide}')
                vide += 1


    # print(f'--------------------------------------Champ:{len(tablette)}:{tablette[-1]}')

    """Niveaux : T's : Comptes(T234|Routes(U234 """
    if u4 == 0 and t4 <= maxi0 and t2 < 6:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U4'
        """ Niveau T4 | MINI=3 MIDI=T3+1 MAXI=8"""
        # Cycle T4 | True:STOP(T3,T2);GO(T4) | False:GO(T3)
        # print(f'***T4 True:STOP(T3,T2);GO(T4)|T4={t4} maxi0:{maxi0}')
        # print(f'| if_T4_avant || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u3} | {tablette[-1]}')
        if (t4 + 1) > maxi0:
            u2, u3, u4 = 1, 0, 1  # .....    .....   .....       Tour Entier :GO(T3)
            # print(f'| if_T4_if_après || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
        else:
            t4 += 1
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....       Tour Entier :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |GO(T4)bric')
            # print(f'| if_T4_if_else_après || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
            brique(t234)  # .....    .....   .....         Fonction brique tétra
            t234 = []
    else:
        if t4 <= maxi0:
            # Ici U4 = 1 :(t4 <= maxi0)
            # print(f' else_IF:T4avant|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 1, 0  # .....   .....   .....   False :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |STOP(T4)bric')
            # print(f' else_IF:T4après|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234.clear()
        else:
            # print(f' else_IF_else:T4avant|False:GO(T3)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 0, 1  # .....    .....    .....     False:GO(T3)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |STOP(T4)bric')
            # print(f' else_IF_else:T4après|False:GO(T3)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234.clear()
    if u3 == 0 and t3 < maxi0:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U3'
        """ Niveau T3 | MINI=2 MIDI=T2+1 MAXI=7"""
        # Cycle T3 | True:GO(T4);STOP(T2);GO(T3) | False :GO(T2)
        # print(f'\n***T3 True:GO(T4);STOP(T2);GO(T3)|T3={t3} maxi0:{maxi0}')
        # print(f'| if_T3_avant || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
        t3 += 1
        t4 = t3 + 1  # Opération Test(T3)/in
        if t4 <= maxi0:
            # Test(T3) Ici T4 <= maxi0(8)"""
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....   .....   Tour unic :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |GO(T3)bric')
            # print(f'| if_T3_if_après || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
            brique(t234)  # .....    .....   .....         Fonction brique tétra
            t234.clear()
        else:
            # Test(T3) Ici T4 > maxi0(8)"""
            t3 -= 1
            t4 -= 1
            u2, u3, u4 = 0, 1, 1  # .....    .....   .....   .....   Tour unique :GO(T2)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |STOP(T3)bric')
            # print(f'| if_T3_if_else_après || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
            t234.clear()  # Opération Test(T3)/Out
    else:
        # De :if u3 == 0 and t3 < maxi0: Soit(U3=1;
        if u3 == 1 and t4 <= maxi0:
            # print(f' else_IF:T3avant|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....   .....   False :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |STOP(T3)bric')
            # print(f' else_IF:T3après|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234.clear()
        else:
            # print(f' else_IF_else:T3avant|False:GO(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 0, 1, 1  # .....    .....   .....   .....   False :GO(T2)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |STOP(T3)bric')
            # print(f' else_IF_else:T3après|False:GO(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234.clear()

    if u2 == 0 and t2 < maxi0 - 1:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U2'
        """ Niveau T2 | MINI=1 MIDI=NULL MAXI=6 """
        # Cycle T2 | True:GO(T4):GO(T3):GO(T2) | False:OUT
        # print(f'\n***T2 True:GO(T4):GO(T3):GO(T2)|T2={t2} maxi0:{maxi0}')
        # print(f'| if_T2_avant || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
        t2 += 1
        t3 = t2 + 1
        t4 = t3 + 1  # Opération Test(T2)/in
        if t4 <= maxi0:
            # Test(T2) Ici t4 <= maxi0(8)"""
            u2, u3, u4 = 1, 1, 0
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |GO(T2)bric')
            # print(f'| ifT2_if_après || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
            brique(t234)  # .....    .....   .....         Fonction brique tétra
            t234.clear()
        else:
            # Test(T2) Ici t4 > maxi0(8)"""
            t2 -= 1
            t3 -= 1
            t4 -= 1
            u2, u3, u4 = 1, 1, 1  # Opération Test(T2)/Out
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f' COMPTES_index: {t234} |STOP(T2)bric')
            # print(f'| if_T2if_else_après || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablette[-1]}')
            t234.clear()
            break
    else:
        # De u2 == 0 and t2 < maxi0 - 1:
        if t2 == mixam[0][1]:
            # print(f' else_IF:T2avant|False:STOP(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4}')
            u2, u3, u4 = 1, 1, 1
            # print(f' else_IF:T2après|False:STOP(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4}')
            break
        else:
            # print(f' else_IF_else:T2avant|False:OUT|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....   .....   False:OUT
# print(f'--------------------------------------Champ:{len(tablette)}:{tablette}:Nombre de tétras = {len(tablette)}')
unit = u
for t in range(len(tablette)):
    diatone(tablette[unit])
    unit += 1

couple()

# Écriture fichier tétra.
"""GlobDicTCord = Tétras uniques"""
fil_cluster = open('globdicTcord.txt', 'w')
for d in tablette:
    ee = ''.join(e for e in d)
    ee += '\n'
    fil_cluster.write(ee)
    # print(f'{ee}')
fil_cluster.close()

"""GlobDicTCoup = Tétras couplés"""
fil_couple = open('globdicTcoup.txt', 'w')
for d in dicoT.values():
    ee = ''.join(e for e in d)
    ee += '\n'
    fil_couple.write(ee)
    # print(f'{ee}')
fil_couple.close()

"""GlobDicTCode = Tétras codés"""
fil_codage = open('globdicTcode.txt', 'w')
f = 0
while f < len(tabas):
    ee = str(tabas[f] + tahau[f])
    ee += '\n'
    fil_codage.write(ee)
    # print(f'{ee}')
    f += 1
fil_codage.close()

# Direction GlobModelGammy
globgamy.gammy('')
