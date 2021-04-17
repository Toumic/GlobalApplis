
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


# Fonction développement
"""..."""
# Déclarations des mémoires
tablT = []
dicoT, dicoM, dicoG = {}, {}, {} # Dictionnaires(Tétra,Mode,Gamme)
voirT = {}
yoyoT = [0]
mini0 = '1234'              # Tétracorde primaire
octave = 13         # 13 emplacements
maxi0 = (octave - len(mini0)) - 1
tetra0, tetra1, t234 = [], ['1', '2', '3', '4'], []
# Itérations
t1, t2, t3, t4 = 0, 1, 2, 3 # maxi0 = 9
u, u1, u2, u3, u4 = 0, 0, 0, 0, 0 # unité de blocage
x, stop, stop0, stop1 = 0, True, False, 5
# Opération Dico(mixam)
mixam = {} # Dépendances Degré(min/max)
""" Niveau T2 | MINI=1 MIDI=NULL MAXI=6 """
""" Niveau T3 | MINI=2 MIDI=T2+1 MAXI=7 """
""" Niveau T4 | MINI=3 MIDI=T3+1 MAXI=8 """
nt234= [[2,[1, 6]], [3,[2, 7]], [4,[3, 8]]]
j = -1
gamme = '1020340506078'     # Chromatisme naturel
notes = 'CDEFGABC'          # Notes musique
alter = ['', '+', 'x', '^', '^+', '^x', '-*', '°*', '*', '°', '-']
tabas, tahau = [], []       # Tétra*défaut

# Fonction couplage
def couple():
    x = 0
    for c in tablT:
        y, cyt, ctt = 0, [], []
        for t in tablT:
            l_ct = len(c) + len(t)              # Somme cas
            # print(f'C:{c} T:{t}')
            if octave >= l_ct:
                o_ct = octave - l_ct            # Différence
                if l_ct < octave and o_ct > 0 and x == 0:
                    for o in range(o_ct):
                        cyt.append('0')         # Vide zéro entre tétra
                    # print(f'CYT:{cyt}')
                ctt = []
                for t1 in t:
                    if t1 != '0':
                        t2 = str(int(t1) + 4)   # Vide zéro dans tétra
                    else:
                        t2 = '0'
                    ctt.append(t2)
                cot = c.copy()
                dicoM[x] = tabas[x] + tahau[y]
                if len(cyt):
                    cot += cyt
                cot += ctt
                dicoT[x] = cot
                cyt = []
                y += 1
        # if x == 3 and y == 3: break ####
        x += 1
    for d in dicoT: print(f'{dicoT[d]}\n')
    # for d in dicoM: print(f'{dicoM[d]}\n')

# Fonction diatonique
def diaton(uni, dia):
    """ Chromatisation des tétras bas/haut """
    # print(f'Fonc Unité:{uni} Diatonie:{dia}')
    x, oo, o1o, o8o = -1, 0, [], []
    for deg in dia:
        ego1, ego8 = '', ''
        oo = octave - len(dia)
        x += 1
        if int(deg) > 0:
            ged = str(int(deg) + 4)
            sign1 = x - gamme.index(deg) # BAS bémol/dièse
            sign8 = (x + oo) - gamme.index(ged) # HAUT bémol/dièse
            # print(f'Ged{ged}, sign8{sign8} x{x} oo{oo} dia{dia} gamme.index(ged){gamme.index(ged)}')
            if int(deg) > 0:
                # Signature dièse
                ego1 = alter[sign1]
                ego8 = alter[sign8]
            else:
                # Signature bémol
                ego1 = alter[sign1]
                ego8 = alter[sign8]
            ooo1 = str(notes[int(deg)-1] + ego1 + deg)
            ooo8 = str(notes[int(ged)-1] + ego8 + ged)
            # print(f'ego1&8 {ego1}{ego8}|ooo1&8{ooo1}{ooo8}')
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
    # print(f'TableT{tablT}')

for i in tetra1:
    if i != '1':
        j += 1
        mixam[j] = nt234[j][1]
        # print('I', i, 'J', j, 'nt234:', nt234[j][1])
# print(f'Mixam {mixam[0][1]}')
tablT.append(tetra1)
# print(f'Maxi0={maxi0} Mini0={mini0}')
while stop:
    # Fonction fabrication
    def brique(nom, valeur, vrai):
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'FoncBric'
        # Vrai[1, 2, 4] Valeur(index) Nom(degré) Table[0]=['1', '2', '3', '4']
        rang = tablT[0].index(nom) # Index Nom Cluster[1,2,3,4]
        # print(f'_ Fonction nom:valeur {nom}:{valeur} Table {tablT[-1]} Vrai {vrai}|*FoncBric mox{maxi0}')
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
                    tetra1 = [o for o in bric]
                    tablT.append(tetra1)
                    # print(f'_ Fonction _ {bric}| brique_voirT')
                    break
                vide += 1
            if vide not in vrai:
                bric.append('0')
                # print(f'Fonc(faux)|{bric}|Vide={vide}')
                vide += 1

    # print(f'--------------------------------------Champ:{len(tablT)}:{tablT[-1]}')

    """Niveaux : T's : Comptes(T234|Routes(U234 """
    if u4 == 0 and t4 <= maxi0 and t2 < 6:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U4'
        """ Niveau T4 | MINI=3 MIDI=T3+1 MAXI=8"""
        # Cycle T4 | True:STOP(T3,T2);GO(T4) | False:GO(T3)
        # print(f'***T4 True:STOP(T3,T2);GO(T4)|T4={t4} maxi0:{maxi0}')
        # print(f'| ifT4avant || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u3} | {tablT[-1]}')
        if (t4 + 1) > maxi0:
            u2, u3, u4 = 1, 0, 1 # .....    .....   .....       Tour Entier :GO(T3)
            # print(f'| ifT4ifaprès || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
        else:
            t4 += 1
            u2, u3, u4 = 1, 1, 0 # .....    .....   .....       Tour Entier :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |GO(T4)bric')
            # print(f'| ifT4ifelseaprès || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
            brique('4', t4, t234) # .....    .....   Fonction brique tétra
            t234 = []
    else:
        if t4 <= maxi0:
            # Ici U4 = 1 :(t4 <= maxi0)
            # print(f'elseIF:T4avant|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 1, 0 #     .....   .....   .....   False :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |STOP(T4)bric')
            # print(f'elseIF:T4après|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234 = []
        else:
            # print(f'elseIFelse:T4avant|False:GO(T3)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 0, 1 #      .....    .....    .....     False:GO(T3)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |STOP(T4)bric')
            # print(f'elseIFelse:T4après|False:GO(T3)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234 = []

    if u3 == 0 and t3 < maxi0:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U3'
        """ Niveau T3 | MINI=2 MIDI=T2+1 MAXI=7"""
        # Cycle T3 | True:GO(T4);STOP(T2);GO(T3) | False :GO(T2)
        # print(f'\n***T3 True:GO(T4);STOP(T2);GO(T3)|T3={t3} maxi0:{maxi0}')
        # print(f'| ifT3avant || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
        t3 += 1
        t4 = t3 + 1 # Opération Test(T3)/in
        if t4 <= maxi0:
            # Test(T3) Ici T4 <= maxi0(8)"""
            u2, u3, u4 = 1, 1, 0 # .....    .....   .....   .....   Tour unic :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |GO(T3)bric')
            # print(f'| ifT3ifaprès || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
            brique('3', t3, t234) #      .....   .....   Fonction brique tétra
            t234 = []
        else:
            # Test(T3) Ici T4 > maxi0(8)"""
            t3 -= 1
            t4 -= 1
            u2, u3, u4 = 0, 1, 1 # .....    .....   .....   .....   Tour unic :GO(T2)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |STOP(T3)bric')
            # print(f'| ifT3ifelseaprès || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
            t234 = [] # Opération Test(T3)/Out
    else:
        # De :if u3 == 0 and t3 < maxi0: Soit(U3=1;
        if u3 == 1 and t4 <= maxi0:
            # print(f'elseIF:T3avant|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 1, 0 # .....    .....   .....   .....   False :GO(T4)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |STOP(T3)bric')
            # print(f'elseIF:T3après|False:GO(T4)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234 = []
        else:
            # print(f'elseIFelse:T3avant|False:GO(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 0, 1, 1 # .....    .....   .....   .....   False :GO(T2)
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |STOP(T3)bric')
            # print(f'elseIFelse:T3après|False:GO(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            t234 = []
    
    if u2 == 0 and t2 < maxi0 - 1:
        yoyoT[0] += 1
        voirT[yoyoT[0]] = 'Cond_U2'
        """ Niveau T2 | MINI=1 MIDI=NULL MAXI=6 """
        # Cycle T2 | True:GO(T4):GO(T3):GO(T2) | False:OUT
        # print(f'\n***T2 True:GO(T4):GO(T3):GO(T2)|T2={t2} maxi0:{maxi0}')
        # print(f'| ifT2avant || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
        t2 += 1
        t3 = t2 + 1
        t4 = t3 + 1 # Opération Test(T2)/in
        if t4 <= maxi0:
            # Test(T2) Ici t4 <= maxi0(8)"""
            u2, u3, u4 = 1, 1, 0
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |GO(T2)bric')
            # print(f'| ifT2ifaprès || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
            brique('2', t2, t234) # .....    .....   .....         Fonction brique tétra
            t234 = []
        else:
            # Test(T2) Ici t4 > maxi0(8)"""
            t2 -= 1
            t3 -= 1
            t4 -= 1
            u2, u3, u4 = 1, 1, 1 # Opération Test(T2)/Out
            """ Motif T234;Index Degrés"""
            t234 = [t2, t3, t4]
            # print(f'COMPTESindex: {t234} |STOP(T2)bric')
            # print(f'| ifT2ifelseaprès || T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} | {tablT[-1]}')
            t234 = []
            break
    else:
        # De u2 == 0 and t2 < maxi0 - 1:
        if t2 == mixam[0][1]:
            # print(f'elseIF:T2avant|False:STOP(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4}')
            u2, u3, u4 = 1, 1, 1
            # print(f'elseIF:T2après|False:STOP(T2)|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4}')
            break
        else:
            # print(f'elseIFelse:T2avant|False:OUT|| T234;{t2},{t3},{t4} : U234;{u2},{u3},{u4} ')
            u2, u3, u4 = 1, 1, 0 # .....    .....   .....   .....   False:OUT             
# print(f'--------------------------------------Champ:{len(tablT)}:{tablT}:Nombre de tétras = {len(tablT)}')
unit = u
for t in range(len(tablT)):
    diaton(unit, tablT[unit])
    unit += 1
couple()
