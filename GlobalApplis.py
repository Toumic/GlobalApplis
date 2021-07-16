# Python 3.9 UTF-8
# Dimanche 28 mars 2021 à 19h 45m (premières lignes)
# Mardi 13 avril 2021 (Développement des tétracordes)
#
# Conçu par Vicenté Llavata Abreu | Vicenté Quantic | Toumic
# Module GlobalApplis.py
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
# Opération Dico(maxime)
maxime = {}  # Dépendances Degré(min/max)
""" Niveau T2 | MINI=1 MIDI=NULL MAXI=6 """
""" Niveau T3 | MINI=2 MIDI=T2+1 MAXI=7 """
""" Niveau T4 | MINI=3 MIDI=T3+1 MAXI=8 """
nt234 = [[2, [1, 6]], [3, [2, 7]], [4, [3, 8]]]
j = -1
gamme = '1020340506078'  # Chromatisme naturel
notes = 'CDEFGABC'  # Notes musique
alter = ['', '+', 'x', '^', '^+', '^x', '°*', '-*', '*', '°', '-']
t_bas, t_haut = [], []  # Tétra*défaut


# Fonction couplage tétracordique
def couple():
    """Fonderie tétras & Moulage gammes"""
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
                dicoM[z] = t_bas[x2] + t_haut[y]
                """Suivre cot"""
                cot = c.copy()
                if len(cyt):
                    cot += cyt
                cot += ctt
                dicoT[z] = cot
                cyt = []
                y += 1
                z += 1
        x2 += 1


# Fonction format diatonique tétracordique
def diatone(dia):
    """Chromatisation des tétras bas/haut"""
    x1d, oo, o1o, o8o = -1, 0, [], []
    for deg in dia:
        oo = octave - len(dia)
        x1d += 1
        if int(deg) > 0:
            ged = str(int(deg) + 4)
            sign1 = x1d - gamme.index(deg)  # BAS bémol/dièse
            sign8 = (x1d + oo) - gamme.index(ged)  # HAUT bémol/dièse
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
            if ooo1[1] in alter:
                o1o.append(ooo1)
            else:
                o1o.append(ooo1[0])
            if ooo8[1] in alter:
                o8o.append(ooo8)
            else:
                o8o.append(ooo8[0])
    t_bas.append(o1o)
    t_haut.append(o8o)


# Charge limite tétra
for i in tetra1:
    if i != '1':
        j += 1
        maxime[j] = nt234[j][1]
# Développement tétracordique
while stop:
    # Atelier fabrication
    def brique(vrai):
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'FoncBric'
        vide, pose, terme, bric = 0, 0, vrai[-1], []
        while 1:
            if vide == 0:
                pose += 1
                bric.append('1')
                vide += 1
            if vide in vrai:
                pose += 1
                bric.append(str(pose))
                if vide == vrai[-1]:
                    tetra3 = [o for o in bric]
                    tablette.append(tetra3)
                    break
                vide += 1
            if vide not in vrai:
                bric.append('0')
                vide += 1


    # print(f'--------------------------------------Champ:{len(tablette)}:{tablette[-1]}')

    """Niveaux : T's : Comptes(T234|Routes(U234 """
    if u4 == 0 and t4 <= maxi0 and t2 < 6:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U4'
        """ Niveau T4 | MINI=3 MIDI=T3+1 MAXI=8"""
        if (t4 + 1) > maxi0:
            u2, u3, u4 = 1, 0, 1  # .....    .....   .....       Tour Entier :GO(T3)
        else:
            t4 += 1
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....       Tour Entier :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            brique(t234)  # .....    .....   .....         Fonction brique tétra
            t234 = []
    else:
        if t4 <= maxi0:
            # Ici U4 = 1 :(t4 <= maxi0)
            u2, u3, u4 = 1, 1, 0  # .....   .....   .....   False :GO(T4)
        else:
            u2, u3, u4 = 1, 0, 1  # .....    .....    .....     False:GO(T3)
    if u3 == 0 and t3 < maxi0:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U3'
        """ Niveau T3 | MINI=2 MIDI=T2+1 MAXI=7"""
        t3 += 1
        t4 = t3 + 1  # Opération Test(T3)/in
        if t4 <= maxi0:
            # Test(T3) Ici T4 <= maxi0(8)"""
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....   .....   Tour unique :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            brique(t234)  # .....    .....   .....         Fonction brique tétra
            t234.clear()
        else:
            # Test(T3) Ici T4 > maxi0(8)"""
            t3 -= 1
            t4 -= 1
            u2, u3, u4 = 0, 1, 1  # .....    .....   .....   .....   Tour unique :GO(T2)
    else:
        # De :if u3 == 0 and t3 < maxi0: Soit(U3=1;
        if u3 == 1 and t4 <= maxi0:
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....   .....   False :GO(T4)
        else:
            u2, u3, u4 = 0, 1, 1  # .....    .....   .....   .....   False :GO(T2)

    if u2 == 0 and t2 < maxi0 - 1:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U2'
        """ Niveau T2 | MINI=1 MIDI=NULL MAXI=6 """
        t2 += 1
        t3 = t2 + 1
        t4 = t3 + 1  # Opération Test(T2)/in
        if t4 <= maxi0:
            # Test(T2) Ici t4 <= maxi0(8)"""
            u2, u3, u4 = 1, 1, 0
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            brique(t234)  # .....    .....   .....         Fonction brique tétra
            t234.clear()
        else:
            # Test(T2) Ici t4 > maxi0(8)"""
            t2 -= 1
            t3 -= 1
            t4 -= 1
            u2, u3, u4 = 1, 1, 1  # Opération Test(T2)/Out
            break
    else:
        # De u2 == 0 and t2 < maxi0 - 1:
        if t2 == maxime[0][1]:
            u2, u3, u4 = 1, 1, 1
            break
        else:
            u2, u3, u4 = 1, 1, 0  # .....    .....   .....   .....   False:OUT
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
fil_cluster.close()

"""GlobDicTCoup = Tétras couplés"""
fil_couple = open('globdicTcoup.txt', 'w')
for d in dicoT.values():
    ee = ''.join(e for e in d)
    ee += '\n'
    fil_couple.write(ee)
fil_couple.close()

"""GlobDicTCode = Tétras codés"""
fil_codage = open('globdicTcode.txt', 'w')
f = 0
while f < len(t_bas):
    ee = str(t_bas[f] + t_haut[f])
    ee += '\n'
    fil_codage.write(ee)
    f += 1
fil_codage.close()

# Direction GlobModelGammy
globgamy.gammy()
