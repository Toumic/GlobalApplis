#!/usr/bin/env python 3.10
# -*- coding: utf-8 -*-
# * samedi 20 août 2022.
# Application gammique évolutive
# Operate Envol sysTM
# ProgamV6encore 1.0
# Approche commatique (Empreinte chromatique)

import inspect
from math import *
from pyaudio import *
from struct import *
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox, simpledialog
from typing import Callable
from wave import *

import GlobGamChrom
import GlobGamMicro
import GlobTetraCord
import GlobGamSim

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

progam_chrom = GlobGamChrom
progam_micro = GlobGamMicro
progam_tetra = GlobTetraCord
progam_simis = GlobGamSim


def progam(pratic, glob, ego_p, ego_r, utile, dana, pc):
    """Pratic = Dictionnaire(clé=nom)(val=cumul).
        Glob = Modes à effet miroir (ISO = unique ou DUO = double).
        Ego_p = Gammes mêmes poids.
        Ego_r = Gammes mêmes rangs.
        Utile = Les noms entiers dans un mode unique.
        Dana = Les poids modaux des gammes (Attention au changement)"""
    pf_ku = 0  # Quand pf_ku > 0 = Liste les détails des paramètres
    (lineno(), 'GGV6/dana:', dana, type(dana))
    if pf_ku:
        for pp in pratic.keys():
            (lineno(), "GGV6/Pratique:", pratic[pp], 'pp:', pp)
            # 38 GGV6/Pratique: [1, 1, 0, 1, 1, 1, 0] pp: Maj
            break
        for ff in glob:
            (lineno(), 'GGV6/glob:', ff)
            # 44 GGV6/glob: ('ISO', (((1, 'I'), '+^2'), ((1, 'III'), '-*6')))
            break
        for kk in ego_p.keys():
            (lineno(), 'GGV6/ego_p:', ego_p[kk], 'kk:', kk)
            # 47 GGV6/ego_p: [1] kk: 147
            break
        for kk1 in ego_r.keys():
            (lineno(), 'GGV6/ego_r:', ego_r[kk1], 'kk1:', kk1)
            # 50 GGV6/ego_r: [1] kk1: 0352146
            break
        for uu in utile.keys():
            (lineno(), 'GGV6/utile:', utile[uu], 'uu:', uu)
            # 53 GGV6/utile: ['x54o', '^43o', '+65*', '^32-', '-*6', '+^2'] uu: 1
            break
        for dd in dana.keys():
            (lineno(), 'GGV6/dana:', dana[dd], 'dd:', dd)
            # 61 GGV6/dana: [[0, 0, 0, 0, 0, 0, 0], [833, 119.0, 17.0, 2.4285714285714284, 0.3469387755102041]]
            # dd: (66, 'I')
            break
    # class Gammique
    data_gam = {1: pratic, 2: glob, 3: ego_p, 4: ego_r, 5: utile, 6: dana, 7: pc}
    Gammique(data_gam).mainloop()


class Gammique(Tk):
    """ Ramification Gammique """

    def __init__(self, data_gam):
        Tk.__init__(self)
        "Tableau de bord"
        # Titre principal
        self.title('Entité Gammique :')
        self.geometry('1500x700+91+14')

        # Fenêtre écran_résultat
        self.can = Canvas(self, bg='beige', height=666, width=666)
        self.can.pack(side=RIGHT, padx=6, pady=6)  # side=RIGHT [curseurs + notes graphiques]

        # Fenêtre écran_utilitaire : VISIONS =
        self.cat = Canvas(self, bg='beige', height=600, width=300, bd=10,
                          highlightthickness=1, highlightbackground="black")
        self.cat.pack(side=RIGHT, expand=True, ipadx=10, ipady=10)
        self.cat.create_text(160, 30, text='§ VISIONS §', font='bold')

        # Fenêtre des utilités
        self.cad = Frame(self, bg='white', width=300, height=800)
        self.cad.pack(side=LEFT, padx=30, pady=30)  # Les boutons situés à gauche

        # Bouton type de fondamentaux
        self.gamclas = None
        self.gamcalc = None
        self.btclas = Button(self.cad, text='Gammes classiques', width=15, bg='light blue',
                             command=lambda: self.typgam(1))
        self.btclas.pack()
        self.btfond = Button(self.cad, text='Gammes calculées', width=15, bg='light blue',
                             command=lambda: self.typgam(2))
        self.btfond.pack()

        # Bouton gamme_radio
        tab_do = tab_re = tab_mi = tab_fa = tab_so = tab_la = tab_si = 0

        # self.tablenotes = les positions du cours self.gama
        self.tablenotes = [tab_do, tab_re, tab_mi, tab_fa, tab_so, tab_la, tab_si]
        self.tbdegre = [0]  # Contient le mode tonique en cours
        self.btrad = Button(self.cad, text='Radio', width=15, bg='light blue', command=self.radio)
        self.btrad.pack()

        # Bouton gamme_audio avec écriture sur le disque dur
        # self.fichnom = les noms des fichiers audio_notes (communs)
        self.presaudio = 0  # Utile au bouton accord/sans le résultat audio
        self.gamula = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.framno = [0, 0, 0, 0, 0, 0, 0]
        # self.fichnom : Ces fichiers vont être écrits sur votre disque dur
        self.fichnom = ['a1.wav', 'a2.wav', 'a3.wav', 'a4.wav', 'a5.wav', 'a6.wav', 'a7.wav']
        self.btaud = Button(self.cad, text='Audio', width=15, bg='light blue', command=lambda: self.actuac(1))
        self.btaud.pack()
        self.btaud2 = Button(self.cad, command=self.audio)
        self.btaud2.pack_forget()  # Pantomime

        # Bouton choix chromatique
        self.chm = None
        hau_do = hau_re = hau_mi = hau_fa = hau_so = hau_la = hau_si = 0
        # self.tablehaute = les hauteurs (y) des notes graphiques
        self.tablehaute = [hau_do, hau_re, hau_mi, hau_fa, hau_so, hau_la, hau_si]
        self.chrmaj = [0, 20, 40, 50, 70, 90, 110]  # Forme graphique majeure
        self.chrgen = {}  # Tableau chromatique généré
        # self.ntchtxt = 'Chrome naturel'
        self.btchr = Button(self.cad, text='Chrome naturel', width=15, bg='light blue', command=self.chrome)
        self.btchr.pack()

        # Bouton tableaux instruments
        # self.piano_wav : Ces fichiers vont être écrits sur votre disque dur
        self.tur = None
        self.sel_nbr = -1
        self.sel_stp = 0
        self.tbltr_nom = ['Tonice', 'Tonale', 'Mélodie', 'Médiane', 'Domine', 'Harmonie']
        self.piano_wav = ['p_w1.wav', 'p_w2.wav']
        self.seldiaton = []
        self.bttab = Button(self.cad, text='Tablature', width=15, bg='light blue', command=lambda: self.actuac(9))
        self.bttab.pack()
        self.bttab_2 = Button(self.cad, text='Tablature', width=15, bg='light blue', command=self.tabla)
        self.bttab_2.pack_forget()  # Pantomime

        # Bouton accords avec écriture sur le disque dur
        # self.fichacc = les noms des fichiers audio_accords (communs)
        self.acc = None
        self.accdiese = ['', '+', 'x', '^', '+^', 'x^', '^^']  # Tableaux des accords - altérations
        self.accbemol = ['', '**', 'o*', '-*', '*', 'o', '-']  # Tableaux des accords - altérations
        # self.fichacc : Ces fichiers vont être écrits sur votre disque dur
        self.fichacc = ['acc1.wav', 'acc2.wav', 'acc3.wav', 'acc4.wav', 'acc5.wav', 'acc6.wav', 'acc7.wav']
        self.btacc = Button(self.cad, text='Accords', width=15, bg='light blue', command=self.accord)
        self.btacc.pack()

        # Bouton tables tétracordiques
        self.ttt = None
        # self.tet_maj = {}
        self.pretetutil = 0
        self.bttet = Button(self.cad, text='Tétracorde', width=15, bg='ivory', command=self.tetra)
        self.bttet.pack()

        # # Bouton tables commatiques :
        # self.notespace = Dico degrés limités aux compressions
        self.com, self.pal = '', ''  # Caractères d'adressage ponctuel
        self.notespace = {180: ['', '+', 'x', '^', '+^', 'x^', '^^'],
                          290: ['-', '', '+', 'x', '^', '+^', 'x^'],
                          310: ['o', '-', '', '+', 'x', '^', '+^'],
                          411: ['o', '-', '', '+', 'x', '^', '+^'],
                          512: ['*', 'o', '-', '', '+', 'x', '^'],
                          613: ['-*', '*', 'o', '-', '', '+', 'x'],
                          714: ['o*', '-*', '*', 'o', '-', '', '+'],
                          888: [self.com, self.pal]}
        # self.notespec6 = Dico degrés limités aux signes cumulés à six
        self.notespec6 = {1: [['+^^', 'o*'], ['x^^', '-*'], ['^^^', '*'], ['+^^^', 'o'], ['x^^^', '-']],
                          2: [['o'], ['^^'], ['+^^', 'o*'], ['x^^', '-*'], ['^^^', '*'], ['+^^^', 'o']],
                          3: [['-*'], ['*'], ['x^'], ['^^'], ['+^^', 'o*'], ['x^^', '-*']],
                          4: [['o*'], ['-*'], ['*'], ['x^'], ['^^'], ['+^^', 'o*']],
                          5: [['-**', 'x^'], ['**'], ['o*'], ['-*'], ['+^'], ['x^']],
                          6: [['***', '^'], ['o**', '-**'], ['**'], ['o*'], ['^']],
                          7: [['o***', '+'], ['-***', 'x'], ['***', '^'], ['o**', '+^'], ['-**', 'x^'], ['**']]}
        self.ccc = None
        self.btcom = Button(self.cad, text='Commatisme', width=15, bg='ivory', command=self.comma)
        self.btcom.pack()
        self.comchr = []
        self.comgen = []
        self.co_tbgen = [], [], [], [], [], [], [], [], [], [], [], []  # Table des notes altérées
        self.co_tbval = [], [], [], [], [], [], [], [], [], [], [], []  # Table des valeurs tonales
        self.comfdb = [0]  # Ligne diatone, forme: dia ou/et com
        self.comfcb = [0]  # Ligne chrome, forme : com ou/et dia
        self.comfct = [0]  # -1: formulé chromatique total
        self.compy_ = [0]  # Les 2 niveaux chromatiques
        self.btcom3color = self.btcom4color = 'light grey'
        self.com2 = Commatique()
        self.scalair = 0  # Indice taux d'inversion

        # Mémoire fantomatique
        self.entfan = Entry(self)
        self.c_ii = ''

        # self.entfan.pack()
        self.entfan.pack_forget()  # Pantomime
        self.entfan.delete(0, END)
        self.entfan.insert(END, "IOI")

        # Groupe Octave RADIO
        etiqs = ["Octave -1", "Octave  0", "Octave +1"]
        valse = ["YOI", "IOI", "IOY"]
        self.variable = StringVar()
        self.rad = []
        for (variable, text, value, command) in (
                (self.variable, etiqs[2], valse[2], self.yoiioiioy),
                (self.variable, etiqs[1], valse[1], self.yoiioiioy),
                (self.variable, etiqs[0], valse[0], self.yoiioiioy),
        ):
            self.rad.append(Radiobutton(
                self.cad,
                variable=self.variable,
                text=text,
                value=value,
                command=command,
            ))
        for i in self.rad:
            i.pack()
        self.rad[1].select()

        # Bouton sélection diatonique
        self.preselect = [0]
        self.sel_bon = []
        self.select = []
        self.sel_yes = 0
        self.sel_myx = [0]
        # Tables gen* : Contient les indices des fréquences "tab_freqs"
        self.gen_b = [3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24, 26, 27, 29, 31, 32, 34, 36, 38]
        self.gen_n = [4, 6, -1, 9, 11, 13, -1, 16, 18, -1, 21, 23, 25, -1, 28, 30, -1, 33, 35, 37]
        # Tables gen**: Contient les indices des touches
        self.gen_bz = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24, 26, 28, 29, 31, 33, 35, 36, 38]
        self.gen_nz = [1, 3, -1, 6, 8, 10, -1, 13, 15, -1, 18, 20, 22, -1, 25, 27, -1, 30, 32, 34, -1, 37]
        self.sel_gam = [12, 14, 16, 17, 19, 21, 23]  # Positions relatives majeures
        self.btsel = Button(self.cad, text='Sélectif', width=15, bg='orange', command=lambda: self.actuac(8))
        self.btsel.pack()

        # Bouton des propriétés
        self.btsimi = Button(self.cad, text='Propriétés', bg='moccasin', width=15,
                             command=lambda: progam_simis.approprier())
        self.btsimi.pack()

        # Bouton quitter
        self.btquit = Button(self.cad, text='Quitter', bg='light grey', width=15, command=self.destroy)
        self.btquit.pack(side=BOTTOM)

        # Les notes cursives scalpha : Graduations gérées.
        self.sca = []
        for (label, color, f, t, command) in (
                ("C", "black", 0, 5, self.scanote1),
                ("D", "green", -1, 4, self.scanote2),
                ("E", "blue", -2, 3, self.scanote3),
                ("F", "grey", -2, 3, self.scanote4),
                ("G", "red", -3, 2, self.scanote5),
                ("A", "orange", -4, 1, self.scanote6),
                ("B", "yellow", -5, 0, self.scanote7),
                ("CDEFGAB", "ivory", -12, 12, self.scanote8),
        ):
            self.sca.append(Scale(
                self,
                length=300,
                orient=HORIZONTAL,
                label=label,
                troughcolor=color,
                sliderlength=20,
                from_=f,
                to=t,
                tickinterval=1,
                command=command,
            ))
        for x in self.sca:
            x.pack()

        # Case à cocher de conversion scanote8 (CDEFGAB) vers l'octave majeure
        # Car, la gamme de bCmaj (scanote8) = Bmaj à l'octave principale
        # Exemple : bC,bD,bE,bF,bG,bA,bB = B,#C,#D,E,#F,#G,#A
        self.fr_8 = [0, 0, 0, 0, 0, 0, 0]  # Les tableaux self.(fr/to/sc/_8)
        self.to_8 = [0, 0, 0, 0, 0, 0, 0]  # Sont utilisés à def self.scanote8(_8)
        self.sc_8 = [0, 0, 0, 0, 0, 0, 0]  # from_(fr), to(to), .set(sc)
        self.cb_chk = IntVar()
        self.cbchk8 = Checkbutton(self, text='Conversion Octave Majeure',
                                  variable=self.cb_chk, fg='black', command=self.convers)
        self.cbchk8.pack()
        self.cbchk8.deselect()

        # Bouton gamme_naturelle
        self.scolors = ['black', 'green', 'blue', 'grey', 'red', 'orange', 'yellow']
        self.fnotes = [0, -1, -2, -2, -3, -4, -5]  # Les from_'s majeurs
        self.tnotes = [+5, +4, +3, +3, +2, +1, 0]  # Les to's majeurs
        self.btzer = Button(self, text='Zéro', width=25, command=self.zero)
        self.btzer.pack()

        # Bouton gamme_calculée
        self.data = data_gam.copy()
        self.nordiese = []  #
        self.subemol = []
        self.cursifs = []
        self.gammescopie = []
        self.gamnomscopie = []
        self.decore = {}  # Base du zéro tonique des accords
        self.declare = {}  # Base (degrés - notes - altérations)
        self.dechire = {}  # Base avec l'indice adapté aux tableaux(b/#)
        self.btgama = Button(self, text='gamme', width=25, command=self.gama)
        self.btgama.pack_forget()  # Pantomime
        self.btgama.invoke()

    def fermeture(self, fff=None):
        """Fermeture des fenêtres() :
            comma[ccc], tetra[ttt], tabla[tur], chrome[chm], accords[acc]"""
        # print(' Quoi ?', fff)
        if fff == 'comma':
            # print('Fermeture fenêtre : chrome +', fff)
            self.ccc.destroy()
            self.chm.destroy()
            self.ccc, self.chm = None, None
        elif fff == 'tetra':
            # print('Fermeture fenêtre :', fff)
            self.ttt.destroy()
            self.ttt = None
        elif fff == 'tabla':
            # print('Fermeture fenêtre :', fff)
            self.tur.destroy()
            self.tur = None
        elif fff == 'chrome':
            # print('Fermeture fenêtre :', fff)
            self.chm.destroy()
            if self.ccc is not None:
                self.ccc.destroy()
            self.chm = None
        elif fff == 'accord':
            # print('Fermeture fenêtre :', fff)
            self.acc.destroy()
            self.acc = None
        elif fff == 'ferme':
            # print('Fermeture fenêtre : chrome + comma ', fff)
            self.ccc.destroy()
            self.chm.destroy()
            self.ccc, self.chm = None, None

    def typgam(self, typ):
        """Modification du type de gamme
            1 : Les noms habituels
            2 : Les modes légers
        Boutons(self) : btchr(chm), bttab(tur), btacc(acc), btcom(ccc), bttet(ttt) self.genre_chrome"""
        if typ == 1:  # Les gammes classiques (naturel)
            self.gamclas = True
            if self.gamcalc:
                self.gamcalc = None
        if typ == 2:  # Les gammes calculées (atonal)
            self.gamcalc = True
            if self.gamclas:
                self.gamclas = None
        self.btgama.invoke()
        if self.chm:
            try:  # Ouvert
                ('typgam.self.chm', self.chm, self.chm.state())
                self.btchr.invoke()
            except TclError:  # Fermé
                self.chm = None
        if self.tur:
            try:  # Ouvert
                ('typgam.self.tur', self.tur, self.tur.state())
                self.bttab.invoke()
            except TclError:  # Fermé
                self.tur = None
        if self.acc:
            try:  # Ouvert
                ('typgam.self.acc', self.acc, self.acc.state())
                self.btacc.invoke()
            except TclError:  # Fermé
                self.acc = None
        if self.ccc:
            try:  # Ouvert
                ('typgam.self.ccc', self.ccc, ' : ', self.ccc.state())
                self.btcom.invoke()
            except TclError:  # Fermé
                self.ccc = None
        if self.ttt:
            try:  # Ouvert
                ('typgam.self.ttt', self.ttt, ' : ', self.ttt.state())
                self.bttet.invoke()
            except TclError:  # Fermé
                self.ttt = None

    # Section com
    def comma(self):
        """ La fonction commatique dépend de la définition chromatique """
        # global c_deg0
        if self.ccc is not None:
            self.ccc.destroy()
        self.ccc = Toplevel(self)
        self.ccc.title('Entité Gammique : Chromatisme en %s' % self.c_ii)
        self.ccc.geometry('600x666+800+80')
        self.ccc.protocol("WM_DELETE_WINDOW", lambda: Gammique.fermeture(self, 'comma'))
        frcom_up = Frame(self.ccc, width=30, height=3)  # Partie haute
        frcom_up.pack()
        c_oo = []
        c_pp = []
        c_ii = []
        # Traitement d'accrochage de la gamme (nom et type)
        # self.tbdegre : Première note du mode tonique en cours
        # self.gamula = ['C','D','E','F','G','A','B']
        # self.sel_myx[0] : Est l'indice [i] en cours, dans self.gamnomscopie[i]
        c_gam = self.gamnomscopie[self.sel_myx[0]]  # c_gam = Rapport du Type
        if c_gam == '0':
            c_gam = "Majeur"
        c_deg = self.tbdegre[0]  # c_deg = Rapport du Degré
        c_not = self.gamula[c_deg]  # c_not = Rapport du Nom
        c_ide = c_not + ' ' + c_gam
        c_ii.append(c_ide)
        btcom_id = Button(frcom_up, text=c_ide, height=1, width=15, bg='light green')
        btcom_id.pack(side=RIGHT)
        btcom_up = Button(frcom_up, text='Commane', height=1, width=15, bg='pink',
                          command=lambda: self.com2.brnch_1(c_oo, c_pp, self.c_ii, self.scalair))
        btcom_up.pack(side=LEFT)
        frcom_gaup = Frame(self.ccc, width=30, height=3)  # Partie gauche
        frcom_gaup.place(x=20, y=10, anchor='nw')
        btcom_ga0up = Button(frcom_gaup, text='Console', height=1, width=15, bg='yellow')
        btcom_ga0up.pack()
        frcom_ga = Frame(self.ccc, width=30, height=3)  # Partie gauche
        frcom_ga.pack(side=LEFT)
        btcom_ga0 = Button(frcom_ga, text='Forme totale', height=1, width=15, bg='white',
                           command=lambda: compyac(0))
        btcom_ga0.pack()
        btcom_ga01 = Button(frcom_ga, text='Forme augmentée', height=1, width=18, bg='orange',
                            command=lambda: compyac(1))
        btcom_ga01.pack()
        btcom_ga02 = Button(frcom_ga, text='Forme diminuée', height=1, width=18, bg='light blue',
                            command=lambda: compyac(2))
        btcom_ga02.pack()
        btcom_ga03 = Button(frcom_ga, text='Chrome naturel', height=1, width=15, bg=self.btcom3color,
                            command=lambda: compyac(3))
        btcom_ga03.pack()
        btcom_ga04 = Button(frcom_ga, text='Chrome atonal', height=1, width=15, bg=self.btcom4color,
                            command=lambda: compyac(4))
        btcom_ga04.pack()

        def compyac(y):
            if y == 0:      # Forme totale
                self.compy_[0] = 0
            elif y == 1:    # Forme augmentée
                self.compy_[0] = 1
            elif y == 2:    # Forme diminuée
                self.compy_[0] = 2
            elif y == 3:    # Chrome naturel
                self.btchr.configure(text='Chrome naturel')
                self.btcom3color = 'ivory'
                self.btcom4color = 'light grey'
            elif y == 4:    # Chrome atonal
                self.btchr.configure(text='Chrome atonal')
                self.btcom3color = 'light grey'
                self.btcom4color = 'ivory'
            self.ccc.destroy()
            self.btcom.invoke()

        def scaler():
            while self.scalair > 12 or self.scalair in (0, ''):
                self.scalair = simpledialog.askinteger('Inversion', 'Entrez un nombre entier de 1 à 12' +
                                                       '. Pour le traitement commatique' + '\n' +
                                                       'Par défaut la dénivellation est fixée à 12')
                if self.scalair == 0:
                    self.scalair = 12
            btcom_dr0up.configure(text='Scalaire = ' + str(self.scalair))
            btcom_up.invoke()

        frcom_drup2 = Frame(self.ccc, width=20, height=3)  # Partie droite
        frcom_drup2.place(x=468, y=10, anchor='nw')
        sca_txt = 'Scalaire = ' + str(12)
        btcom_dr0up = Button(frcom_drup2, text=sca_txt, height=1, width=15, bg='yellow',
                             command=lambda: scaler())
        btcom_dr0up.pack()
        frcom_dr = Frame(self.ccc, width=30, height=3)  # Partie droite
        frcom_dr.pack(side=RIGHT)
        btcom_dr0 = Button(frcom_dr, text='Toutes les lignes', height=1, width=15, bg='white',
                           command=lambda: commuac(-1))
        btcom_dr0.pack()
        btcom_dr01 = Button(frcom_dr, text='Ligne diatone.diatone', height=1, width=18, bg='light grey',
                            command=lambda: commuac(1))
        btcom_dr01.pack()
        btcom_dr02 = Button(frcom_dr, text='Ligne diatone.chrome', height=1, width=18, bg='light grey',
                            command=lambda: commuac(2))
        btcom_dr02.pack()
        btcom_dr03 = Button(frcom_dr, text='Ligne chrome.chrome', height=1, width=18, bg='light grey',
                            command=lambda: commuac(3))
        btcom_dr03.pack()
        btcom_dr04 = Button(frcom_dr, text='Ligne chrome.diatone', height=1, width=18, bg='light grey',
                            command=lambda: commuac(4))
        btcom_dr04.pack()
        btcom_dr05 = Button(frcom_dr, text='Lignes diatones', height=1, width=15, bg='pink',
                            command=lambda: commuac(5))
        btcom_dr05.pack()
        btcom_dr06 = Button(frcom_dr, text='Lignes chromes', height=1, width=15, bg='light green',
                            command=lambda: commuac(6))
        btcom_dr06.pack()

        def commuac(c):
            self.comfct[0] = 0  # Toute. Ligne
            self.comfdb[0] = 0  # Ligne dia.dia et/ou com
            self.comfcb[0] = 0  # Ligne com.com et/ou dia
            if c == -1:
                self.comfct[0] = -1  # Toute. Ligne
            elif c == 0:
                pass
            elif c == 1:
                self.comfdb[0] = 1  # Ligne dia_dia
            elif c == 2:
                self.comfdb[0] = 2  # Ligne dia_com
            elif c == 3:
                self.comfcb[0] = 3  # Ligne com_com
            elif c == 4:
                self.comfcb[0] = 4  # Ligne com_dia
            elif c == 5:
                self.comfdb[0] = 5  # Ligne dia_dia/com
            elif c == 6:
                self.comfcb[0] = 6  # Ligne com_com/dia
            self.ccc.destroy()
            self.btcom.invoke()

        # (self.comfct[0],self.comfdb[0],self.comfcb[0])
        comcan_1 = Canvas(self.ccc, bg='ivory', height=600, width=300)
        comcan_1.place(x=150, y=30, anchor='nw')
        comcan_1.delete(ALL)
        frcom_bo = Frame(self.ccc, width=30, height=3)  # Partie basse
        frcom_bo.pack(side=BOTTOM)
        btcom_bo = Button(frcom_bo, text='Changer', height=1, width=15, bg='light grey',
                          command=lambda: Gammique.fermeture(self, 'ferme'))
        btcom_bo.pack()
        fontval = Font(family='Liberation Serif', size=8)
        fontchr = Font(family='Liberation Serif', size=7)
        fontcom = Font(family='Liberation Serif', size=9)
        # self.scolors = ['black','green','blue','grey','red','orange','yellow']# Couleurs usuelles
        # self.chrgen : Dictionnaire du premier mode chromatique en cours
        # self.comchr : Premier mode chromatique indexé
        commaj_gam = [0, 2, 4, 5, 7, 9, 11]  # Forme majeure
        # self.commaj_com = [1, 3, 6, 8, 10]  # Forme de l'indice chrome
        self.btchr.invoke()
        self.comchr = [], []
        self.comgen = [], [], [], [], [], [], [], [], [], [], [], []
        compro = [0]
        # Prélèvement des primitives chromatiques
        for ci in self.chrgen:
            change = self.chrgen[ci][7]
            if change[0] == 'n':
                cochr = 'gam', self.chrgen[ci][2], self.chrgen[ci][3]
                self.comchr[0].append(cochr)
            else:
                cochr = 'com', self.chrgen[ci][2], self.chrgen[ci][3], self.chrgen[ci][5], self.chrgen[ci][6]
                self.comchr[0].append(cochr)
        # print('comchr', self.comchr[0])
        compro[0] = self.comchr[0]
        # ('compro',compro[0])  # Forme d'écriture et de lecture
        # Composition du modèle chrome diatonique
        for ci in range(12):
            count, cow = ci, -1
            while cow < 11:
                cow += 1
                self.comgen[ci].append(compro[0][count])
                count += 1
                if count > 11:
                    count = 0
            # ('comgen', ci, self.comgen[ci])
        # écriture du modèle chrome diatonique
        # self.dechire[(deg,maj)] # Tableau des tonalités diatoniques
        # c_deg = indice de tonalité
        c_deg0 = 0
        co_d1 = -1
        co_tbnat = [1, 2, 3, 4, 5, 6, 7]
        self.co_tbgen = [], [], [], [], [], [], [], [], [], [], [], []  # Table des notes altérées
        self.co_tbval = [], [], [], [], [], [], [], [], [], [], [], []  # Table des valeurs tonales
        # self.nordiese(#) self.subemol(b) Rappel pour indices signatures
        # self.nordiese = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^',...]
        # self.subemol = [..., '****', 'o***', '-***', '***', 'o**', '-**', '**', 'o*', '-*', '*', 'o', '-']
        for ci in range(12):
            co_d2i = co_d2 = co_d3 = 0
            c_zer = [0]
            c_zof = 0
            co_tbmod = [], [], [], [], [], [], [], [], [], [], [], []  # Passe les notes altérées
            co_tbdif = [], [], [], [], [], [], [], [], [], [], [], []  # Passe les valeurs tonales modifiées
            co_tbdif0 = [], [], [], [], [], [], [], [], [], [], [], []  # Passe les valeurs tonales inchangées
            for co in range(12):
                compris = self.comgen[ci][co][0]
                if co == 0 and compris == 'gam':
                    co_c1 = 0
                    co_c0 = self.comgen[ci][co][2]
                    for c_ in self.gamula:
                        if c_ == co_c0[0][0]:
                            c_deg0 = co_c1
                            break
                        co_c1 += 1
                    co_d1 += 1
                    c_zer[0] = 'on'
                elif co == 0 and compris == 'com':
                    co_c1 = 0
                    co_c0 = self.comgen[ci][co][2]
                    for c_ in self.gamula:
                        if c_ == co_c0[0][0]:
                            c_deg0 = co_c1
                            break
                        co_c1 += 1
                    c_zof = 1
                    c_zer[0] = 'of'
                # ('compris', compris)
                if compris == 'gam':
                    co_sign0 = self.comgen[ci][co][1]
                    comcan_1.create_text(12 + co * 25, (30 + ci * 49) - 10, font=fontchr,
                                         text=co_sign0[0], fill='black')
                    co_note0 = self.comgen[ci][co][2]
                    comcan_1.create_text(12 + co * 25, 30 + ci * 49, font=fontcom,
                                         text=co_note0[0], fill='black')
                    # méthode 7 notes ("déchire")
                    if co_d2 < 7 and c_zer[0] == 'on':  # Ligne diatonique : dia
                        co_d2 += 1  # co_d2 = degré
                        co_d0 = self.dechire[(co_d1, co_d2)]  # co_d0 = signe (+/-)
                        if co_d0 >= 0:
                            co_d01 = "{0}{1}".format(self.nordiese[co_d0], co_d2)
                        else:
                            co_d01 = "{0}{1}".format(self.subemol[co_d0], co_d2)
                        # Selon l'activité demandée
                        if self.comfdb[0] == 2 or self.comfcb[0] != 0:
                            pass
                        else:
                            comcan_1.create_text(12 + co * 25, (30 + ci * 49) + 20,
                                                 font=fontval, text=co_d01, fill='magenta')
                            co_d012 = 'g', co, co_d01
                            co_tbdif[co].append(co_d012)
                            co_tbdif0[co].append(co_d012)
                            # print(538, 'CO', co, 'co_tbdif[co]', co_tbdif[co], 'co_tbdif0[co]', co_tbdif0[co])
                    elif co_d2i < 7 and c_zer[0] == 'of':  # Ligne chromatique : dia
                        co_d2i += 1  # co_d2i = degré
                        co_n0 = 0
                        for c_ in self.gamula:  # obtenir tonique
                            if c_ == co_note0[0][0]:
                                if c_deg0 == 0:
                                    c_dif = co_n0 + c_deg0
                                else:
                                    c_dif = co_n0 - c_deg0
                                c_ree = int(commaj_gam[co_tbnat[c_dif] - 1])
                                co_s2 = co - c_ree  # (+1/-1)
                                if co_s2 >= 0:
                                    co_res = self.nordiese[co_s2]
                                else:
                                    co_res = self.subemol[co_s2]
                                co_s1 = "{0}{1}".format(co_res, co_tbnat[c_dif])  # co_s1 = Signe + Numéric
                                co_s11 = co_s1
                                # str(co_tbnat[c_dif]) = Uniquement l'unité-degré
                                # Mise en œuvre des extensions
                                space = False
                                for kys in self.notespace.keys():
                                    kit = list(str(kys))
                                    if str(str(co_tbnat[c_dif])) == kit[0]:
                                        for x in range(len(self.notespace[kys])):
                                            compo = self.notespace[kys][x] + kit[0]
                                            if compo == co_s1:
                                                space = True
                                                break
                                self.notespace[888] = [co_res, str(co_tbnat[c_dif])]  # Mémo entier et unité
                                if not space:  # De compris = 'gam'
                                    for kys6 in self.notespec6[co_tbnat[c_dif]]:
                                        if co_res in kys6:
                                            if len(kys6) > 1:
                                                ext = str(co_tbnat[c_dif] + 7)
                                                if co_s2 > 0:
                                                    co_di = 12 - co_s2
                                                    co_di = co_di - (co_di + co_di)
                                                    co_ex = self.subemol[co_di]
                                                else:
                                                    co_di = 12 - abs(co_s2)
                                                    co_ex = self.nordiese[co_di]
                                                coin = co_ex + ext  # Correction kys6[1)
                                                co_s1 = coin
                                                (lineno(), 'co_res:', co_res, 'co_di:', co_di, 'co_s1:', co_s1)
                                                break
                                    # Suivre chrome numéric
                                    # (634, 'GAM|co_s1 ', co_s1, self.notespace[888], 'Space', space)
                                # Selon l'activité demandée
                                if self.comfdb[0] != 0 or self.comfcb[0] == 3:
                                    pass
                                else:
                                    comcan_1.create_text(12 + co * 25, (30 + ci * 49) + 22,
                                                         font=fontchr, text=co_s1, fill='magenta')
                                    co_s12 = 'c', co, co_s1  # c. co = Note analogic. co_s1 = Signe + Numéric
                                    co_s13 = 'c', co, co_s11  # c. co = Note analogic. co_s11 = Signe + Numéric
                                    co_tbdif[co].append(co_s12)
                                    co_tbdif0[co].append(co_s13)
                                    # print(645, 'co_s12 ', co_s12, )  # (co_s12) Voir ci-dessus
                            co_n0 += 1
                    co_tbgam = co_sign0[0], co_note0[0][0]
                    co_tbmod[co].append(co_tbgam)
                    # print(649, 'co_tbgam:', co_tbgam, ':', )
                if compris == 'com':  # Définition d'usage des grands volumes altérés
                    '''1. Degrés : +1 ~ ^^1, -2 ~ x^2, o3 ~ +^3, o4 ~ +^4, *5 ~ ^5, -*6 ~ x6, o*7 ~ +7 
                    2. Extensions : -8 ~ o*8
                        +^^^9 & **9 ~ o9, x^^10 ~ ^^^10 & -**10   -*10, +^^11 ~ ^^^11 & -**11 ~ o*11,
                        x^12 ~ x^^12 & o**12 ~ -**12, ^13 ~ +^^13 & ***13, +14 ~ ^^ 14
                    3. Volumes : ^^1 = **8
                        **9 = ^^2, **10 = ^^3, **11 = ^^4, ^^12 = **5, ^^13 = **6, ^^14 = **7'''
                    co_sign1 = self.comgen[ci][co][1]  # augmentation chromatique (signe)
                    co_note1 = self.comgen[ci][co][2]  # augmentation chromatique (note)
                    co_sign2 = self.comgen[ci][co][3:4]  # diminution chromatique (signe)
                    co_note2 = self.comgen[ci][co][4:]  # diminution chromatique (note)
                    if self.compy_[0] == 0 or self.compy_[0] == 1:
                        comcan_1.create_text(12 + co * 25, (30 + ci * 49) + 12, font=fontval,
                                             text=co_sign1[0], fill='red')
                        comcan_1.create_text(12 + co * 25, (30 + ci * 49) + 4, font=fontchr,
                                             text=co_note1[0][0], fill='red')
                    if self.compy_[0] == 0 or self.compy_[0] == 2:
                        comcan_1.create_text(12 + co * 25, (30 + ci * 49) - 15, font=fontval,
                                             text=co_sign2[0][0], fill='blue')
                        comcan_1.create_text(12 + co * 25, (30 + ci * 49) - 5, font=fontchr,
                                             text=co_note2[0][0][0], fill='blue')
                    if co_d3 < 5 and c_zer[0] == 'on' or c_zof == 1:  # degré chromatique diatonique
                        # commaj_gam = forme majeure
                        co_d3 += 1
                        co_n0 = c_sauf = 0
                        for c_ in self.gamula:  # obtenir tonique
                            if c_ == co_note1[0][0]:
                                if c_deg0 == 0:
                                    c_dif = co_n0 + c_deg0
                                else:
                                    c_dif = co_n0 - c_deg0
                                c_ree = int(commaj_gam[co_tbnat[c_dif] - 1])
                                co_s2 = co - c_ree  # (+1/-1)
                                if co_s2 >= 0:
                                    co_res = self.nordiese[co_s2]
                                else:
                                    co_res = self.subemol[co_s2]
                                co_s1 = "{}{}".format(co_res, co_tbnat[c_dif])
                                # Mise en œuvre des extensions
                                space = 0
                                for kys in self.notespace.keys():
                                    kit = list(str(kys))
                                    if str(str(co_tbnat[c_dif])) == kit[0]:
                                        for x in range(len(self.notespace[kys])):
                                            compo = self.notespace[kys][x] + kit[0]
                                            if compo == co_s1:
                                                space += 1
                                                break
                                self.notespace[888] = [co_res, str(co_tbnat[c_dif])]  # Mémo entier et unité
                                if not space:  # De compris = 'com'
                                    for kys6 in self.notespec6[co_tbnat[c_dif]]:
                                        if co_res in kys6:
                                            (lineno(), 'co_res:', co_res, 'kys6:', kys6)
                                            if len(kys6) > 1:
                                                ext = str(co_tbnat[c_dif] + 7)
                                                if co_s2 > 0:
                                                    co_di = 12 - co_s2
                                                    co_di = co_di - (co_di + co_di)
                                                    co_ex = self.subemol[co_di]
                                                else:
                                                    co_di = 12 - abs(co_s2)
                                                    co_ex = self.nordiese[co_di]
                                                coin = co_ex + ext  # Correction kys6[1)
                                                co_s1 = coin
                                                (lineno(), '** co_s1:', co_s1, 'co:', co)
                                                break
                                    # Suivre chrome numéric
                                    # print(499, 'GAM|co_s1 ', co_s1, self.notespace[888], 'Space', space)
                                # Selon l'activité demandée
                                if c_zer[0] == 'on' and self.comfct[0] == 0:
                                    if self.comfdb[0] == 1 or self.comfcb[0] != 0:
                                        c_sauf = -1
                                elif c_zof == 1 and self.comfct[0] == 0:
                                    if self.comfdb[0] != 0 or self.comfcb[0] == 4:
                                        c_sauf = -1
                                if c_sauf == 0:
                                    comcan_1.create_text(12 + co * 25, (30 + ci * 49) + 22,
                                                         font=fontchr, text=co_s1, fill='green')
                                    co_s12 = '', co, co_s1
                                    co_tbdif[co].append(co_s12)
                                    co_tbdif0[co].append(co_s12)
                                    # print(722, 'co_s12:', co_s12)
                            co_n0 += 1
                    co_tbplus = co_sign1[0], co_note1[0][0]
                    co_tbmoins = co_sign2[0][0], co_note2[0][0][0]
                    co_tbplns = co_tbplus, co_tbmoins
                    co_tbmod[co].append(co_tbplns)
                self.co_tbgen[ci].append(co_tbmod)
                self.co_tbval[ci].append(co_tbdif)
            # print('\n\n__co_tbgen', ci, self.co_tbgen[ci])
            # ('730\n\n__co_tbval', ci, self.co_tbval[ci])
        c_oo.append(self.co_tbgen)
        c_pp.append(self.co_tbval)
        # Fermeture de fenêtre inutile quand inutilisée
        if self.chm is not None:
            self.chm.destroy()
        # cob2 = self.co_tbval
        # Self.co_tbgen, self.co_tbval : Utilisation au rapport commatique
        # print('734 c_pp:', c_pp)  # Remplacer "#" par "print" pour la forme

    # Panoplie tétracordique
    def tetra(self):
        """ La fonction tétracordique et les forces heptatoniques """
        if self.ttt is not None:
            self.ttt.destroy()
        self.ttt = Toplevel(self)
        self.ttt.title('Entité Gammique : Tétracorde %s' % self.c_ii)
        self.ttt.geometry('600x666+1210+140')
        self.ttt.protocol("WM_DELETE_WINDOW", lambda: Gammique.fermeture(self, 'tetra'))
        fonttt = Font(size=7)
        frtet = Frame(self.ttt, width=30, height=3, bg='green')
        frtet.pack(side=RIGHT)
        bttet0 = Button(frtet, text='Intro', height=1, width=10, bg='orange', command=lambda: Gammique.tetra(self))
        bttet0.pack()
        bttet1 = Button(frtet, text='Tétras', height=1, width=10, bg='orange', command=lambda: ttractuac(1))
        bttet1.pack()
        bttet2 = Button(frtet, text='Utiles', height=1, width=10, bg='orange', command=lambda: ttractuac(2))
        bttet2.pack()
        bttet3 = Button(frtet, text='Autres', height=1, width=10, bg='orange', command=lambda: ttractuac(3))
        bttet3.pack()
        frtet_ = Frame(self.ttt, width=30, height=1)
        frtet_.pack(side=BOTTOM)
        bttet_ = Button(frtet_, text='Quitter', height=1, width=15, bg='lightgrey',
                        command=lambda: Gammique.fermeture(self, 'tetra'))
        bttet_.pack()
        tetcan = Canvas(self.ttt, bg='ivory', height=500, width=333)  # width=300
        tetcan.place(x=10, y=30, anchor='nw')  # x=30
        tetcan_ = Canvas(self.ttt, bg='pink', height=500, width=150)
        tetcan_.place(x=350, y=30, anchor='nw')
        tetcan.create_line(50, 30, 250, 30, fill='blue')
        txlgh = 45  # txlgh=50 : Début des 66 lignes
        txldh = 288  # txldh=250 : Fin des 66 lignes
        tylgh = tyldh = 60  # Axe horizontal
        tylgv = 50
        tyldv = 460
        txlgv = txldv = 46  # Axe vertical (txlgv=txldv=30)
        for i in range(66):  # Lignes horizontales
            tetcan.create_line(txlgh, tylgh + i * 6, txldh, tyldh + i * 6, fill='lightgrey')
        for i in range(13):  # Lignes verticales
            tetcan.create_line(txlgv + i * 20, tylgv, txldv + i * 20, tyldv, fill='lightgrey')
        # Le pas : (horizontal = *20)(vertical = *6)
        r1 = 3
        x1 = 150
        y1 = 15
        tetcan.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill='white')  # Titre décor
        r2 = 2
        x2 = 150
        y2 = 24
        tetcan.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill='white')  # Titre décor
        # Label(self.ttt, text="Tétra's", font='bold', fg='blue')
        tetcan.create_text(66, 15, text='Système tétracordique', fill='black')
        self.pretetutil = 0

        def ttractuac(t1):  # Actions des boutons (tétras, utiles, clones)
            """ Axe horizontal(x)/vertical(y)
                Bouton intro (Remise grille à vide. Affichage primitif).
                Bouton tétras (Dessine les tétras fondamentaux (classic ou calculé)
                Bouton utiles (tet_is:inf/sup/nom,tet_tt:ordre,tgam_util: clone)
                Bouton clones (ts_simil[0] = [('Inf', 'Inf', 0, '0'),])[Brouillon]"""
            tetcan.delete(ALL)
            tetcan.create_line(50, 30, 250, 30, fill='blue')  # Ligne de soulignement
            for i1 in range(66):
                tetcan.create_line(txlgh, tylgh + i1 * 6, txldh, tyldh + i1 * 6, fill='lightgrey')
            for i2 in range(13):
                tetcan.create_line(txlgv + i2 * 20, tylgv, txldv + i2 * 20, tyldv, fill='lightgrey')
            if self.pretetutil == 1:
                self.fr_sup.destroy()
                self.fr_inf.destroy()
                self.btpont.destroy()
            xh = 46  # Départ Axe vertical
            yh = 60  # Départ Axe horizontal
            if t1 == 0:
                pass
                '''Dessiner les tétras fondamentaux principaux. Choix 1'''
            elif t1 == 1:  # Bouton tétras (tgam_tet = [])
                # xh= 46; yh= 60        # Départ Axe horizontal(x)/vertical(y)
                tetcan.create_text(150, 15, text='Système tétracordique ordonné', fill='grey')
                tv = x_01i = 0
                for tt in tgam_tet:  # tgam_tet : Table tétra's fondamentaux
                    th = 0
                    t_is = self.gamnomscopie[tv]
                    tt_inf = tt[0]
                    tt_sup = tt[1]
                    td = 13 - len(tt_inf + tt_sup)
                    (lineno(), 'tt', tt, '\t tv:', tv, 't_is', t_is)
                    for tti in tt_inf:
                        if tti == 1:
                            tetcan.create_oval(xh + th * 20 - r1, yh + tv * 6 - r1,
                                               xh + th * 20 + r1, yh + tv * 6 + r1,
                                               fill='red')
                            th += 1
                        else:
                            tetcan.create_oval(xh + th * 20 - r2, yh + tv * 6 - r2,
                                               xh + th * 20 + r2, yh + tv * 6 + r2,
                                               fill='salmon')
                            th += 1
                    if td > 0:
                        th1, td_ = th, -1
                        while td_ < td - 1:
                            td_ += 1
                            # for td_ in range(td):
                            tetcan.create_oval(xh + th1 * 20 - r1, yh + tv * 6 - r1,
                                               xh + th1 * 20 + r1, yh + tv * 6 + r1,
                                               fill='white')
                            th1 += 1
                        th = th1
                    for tts in tt_sup:
                        if tts == 1:
                            tetcan.create_oval(xh + th * 20 - r1, yh + tv * 6 - r1,
                                               xh + th * 20 + r1, yh + tv * 6 + r1,
                                               fill='blue')
                            th += 1
                        else:
                            tetcan.create_oval(xh + th * 20 - r2, yh + tv * 6 - r2,
                                               xh + th * 20 + r2, yh + tv * 6 + r2,
                                               fill='skyblue')
                            th += 1
                    if x_01i == 1:
                        x10 = 13  # Marges de principe(x)
                        x_01i = 0
                    else:
                        x10 = 33  # Marges de principe(x)
                        x_01i = 1
                    tetcan.create_text(x10, yh + tv * 6, text=t_is, font=fonttt, fill='red')
                    tv += 1
                '''Bouton utiles (tet_is:inf/sup/nom,tet_tt:ordre,tgam_util:clone). Choix 2'''
            elif t1 == 2:  # Bouton utiles (tet_is:inf/sup/nom,tet_tt:ordre,tgam_util:clone)
                # xh= 46; yh= 60        # Départ Axe horizontal(x)/vertical(y)
                tetcan.create_text(150, 15, text='Système tétracordique utilisé', fill='grey')
                if self.pretetutil == 1:
                    self.fr_sup.destroy()
                    self.fr_inf.destroy()
                    self.btpont.destroy()
                self.btpont = Button(self.ttt, text='Pont', height=1, width=5, bg='ivory')
                self.btpont.pack(side=RIGHT)
                self.fr_sup = Frame(self.ttt, width=3, height=1, bg='blue')
                self.fr_sup.pack(side=RIGHT)
                self.fr_inf = Frame(self.ttt, width=3, height=1, bg='blue')
                self.fr_inf.pack(side=RIGHT)

                # actifbout = Activation d'un bouton
                def actifbout(actif):
                    actinf = None
                    for tgb in tgam_bin:
                        if actif in tgb:
                            actinf = ''.join(str(tgb0) for tgb0 in tgb[0]) + '.'
                            actinf += ''.join(str(tgb0) for tgb0 in tgb[1])
                            messagebox.showinfo('actinf', actinf + '\n' + 'Gamme = ' + tgb[3])
                            (lineno(), 'tgb', tgb, tgb[3])
                            break
                    (lineno(), 'actif:', actif, 'actinf', actinf)

                tu = tg = x_01i = x_01s = 0  # x_01: Jeux de marges du texte
                plus, u_inf, u_sup = False, [], []
                for tt in tgam_util:  # tt: clone(tt)=[1, 1, 1, 1] (classic ou calcul)
                    (lineno(), 'tt:', tt, '\t tu:', tu, 'tet_is[tu]:', tet_is[tu], 'tet_tt[tu]:', tet_tt[tu])
                    # 877 tt: [1, 0, 1, 0, 1, 1] 	 tu: 0 tet_is[tu]: ('Inf', 'Maj') tet_tt[tu]: 0 (classic ou calcul)
                    t_is = tet_is[tu]  # t_is: "inf/sup"/nom(tu):"L'horizontale(x)":=('Inf', '0')
                    t_tt = tet_tt[tu]  # t_tt: ordre(tu):La verticale(y):=zéro à 66
                    t_ut = tt
                    if t_ut == tin_f:
                        couleur0 = 'red'
                        couleur1 = 'salmon'
                    else:
                        couleur0 = 'blue'
                        couleur1 = 'skyblue'
                    (lineno(), 't_ut', t_ut, 'tin_f', tin_f, 'tsu_p', tsu_p)
                    th = 0
                    tis0i = tis0s = 0  # Compteurs des tétras(inf/sup)
                    if not plus:
                        ('*', lineno(), 't_is:', t_is, 't_tt:', t_tt, 't_ut:', t_ut)
                        # * 893 t_is: ('Inf', 'Maj') t_tt: 0 t_ut: [1, 0, 1, 0, 1, 1]
                        if t_is[0] == 'Inf':  # Texte du tétra inférieur
                            tis0i += 1
                            if x_01i == 1:
                                x10 = 13  # Marges de principe(x)
                                x_01i = 0
                            else:
                                x10 = 33  # Marges de principe(x)
                                x_01i = 1
                            # for t2 in t_ut = Inférieur : Création ovale(note) + texte(nom)
                            for t2 in t_ut:
                                if t2 == 1:
                                    tetcan.create_oval(xh + th * 20 - r1,
                                                       yh + tg * 6 - r1,
                                                       xh + th * 20 + r1,
                                                       yh + tg * 6 + r1, fill=couleur0)
                                else:
                                    tetcan.create_oval(xh + th * 20 - r2,
                                                       yh + tg * 6 - r2,
                                                       xh + th * 20 + r2,
                                                       yh + tg * 6 + r2, fill=couleur1)
                                th += 1
                            u_inf.append(t_is[1])
                            tetcan.create_text(x10, yh + tg * 6, text=t_is[1], font=fonttt, fill='red')
                            '''Button(self.fr_inf, text=t_is[1], height=1, width=5, bg='lightblue',
                                   command=lambda: print(lineno(), t_is[1])).pack()'''
                        elif t_is[0] == 'Sup':  # Texte du tétra supérieur
                            tis0s += 1
                            if x_01s == 1:
                                x290 = 303  # Marges de principe(x)
                                x_01s = 0
                            else:
                                x290 = 315  # Marges de principe(x)
                                x_01s = 1
                            t_len = 13 - len(tt)
                            th += t_len
                            # for t3 in t_ut = Supérieur : Création ovale(note) + texte(nom)
                            for t3 in t_ut:
                                if t3 == 1:
                                    tetcan.create_oval(xh + th * 20 - r1,
                                                       yh + tg * 6 - r1,
                                                       xh + th * 20 + r1,
                                                       yh + tg * 6 + r1, fill=couleur0)
                                else:
                                    tetcan.create_oval(xh + th * 20 - r2,
                                                       yh + tg * 6 - r2,
                                                       xh + th * 20 + r2,
                                                       yh + tg * 6 + r2, fill=couleur1)
                                th += 1
                            u_sup.append(t_is[1])
                            tetcan.create_text(x290, yh + tg * 6, text=t_is[1], font=fonttt, fill='blue')
                    if tu + 1 < len(tet_is) and tet_is[tu + 1][1] == tet_is[tu][1]:
                        plus = True
                        (lineno(), 'True t_is:', t_is, 'tet_is', tet_is[tu], tet_is[tu + 1])
                    else:
                        if tu + 1 < len(tet_is):
                            plus = False
                            (lineno(), 'False t_is:', t_is, 'tet_is', tet_is[tu], tet_is[tu + 1])
                    if tu + 1 < len(tet_tt) and tet_tt[tu + 1] != tet_tt[tu]:
                        tg += 1
                    tu += 1
                # u_inf[ix] et u_sup[yx] = Texte du bouton vers fonction : actifbout(m)
                for ix in range(len(u_inf)):
                    u_inf[ix] = Button(self.fr_inf, text=u_inf[ix], height=1, width=5, bg='lightblue',
                                       command=lambda m=u_inf[ix]: actifbout(m))
                    u_inf[ix].pack()
                for yx in range(len(u_sup)):
                    u_sup[yx] = Button(self.fr_sup, text=u_sup[yx], height=1, width=5, bg='pink',
                                       command=lambda m=u_sup[yx]: actifbout(m))
                    u_sup[yx].pack()
                self.pretetutil = 1
                '''Bouton clones (ts_simil[0] = [('Inf', 'Inf', 0, '0'),]). Choix3'''
            elif t1 == 3:  # Bouton clones (ts_simil = [])
                # ts_simil[0] = [('Inf', 'Inf', 0, '0'),]
                # tg_tra[0] = [([1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1])] gamme en cours
                # self.sel_myx[0] : Est l'indice [i] en cours, dans self.gamnomscopie[i]
                # xh= 46; yh= 60        # Départ Axe horizontal(x)/vertical(y)
                tetcan.create_text(150, 15, text='Système tétracordique cloné', fill='grey')
                if self.pretetutil == 1:
                    self.fr_sup.destroy()
                    self.fr_inf.destroy()
                    self.btpont.destroy()
                # te_pos = self.sel_myx[0]
                # tg_in = tgam_tet[te_pos][0]  # Gamme choisie eu départ
                # tg_su = tgam_tet[te_pos][1]  # Gamme choisie eu départ
                te_ts = 0
                te = -1
                x_01i = x_01s = 0
                t_colinf = [0]
                t_colsup = [0]
                (lineno(), 'tgam_nom[:10]:', tgam_nom[:10], len(tgam_nom))
                # 997 tgam_nom[:10]: ['Maj', 'Maj', 'Maj', 'Maj', '-2', '-2', '+2', '+2', '-3', '-3'] 38
                for te_ in tgam_tet:  # tgam_tet : Table tétra's fondamentaux
                    te += 1
                    th = te_one = 0
                    teg_in = []  # Tétra en écriture(ovale, texte)
                    teg_su = []  # Tétra en écriture(ovale, texte)
                    te_fix = 0
                    teg_inf = ''
                    teg_sup = ''
                    te_in = te_[0]  # Tétra inférieur(lecture)
                    te_su = te_[1]  # Tétra supérieur(lecture)
                    t_tt = te
                    if self.gamnomscopie[te] not in tgam_nom:
                        if te_in:  # Tétra inférieur(lecture)
                            te_one += 1  # Recherche diatonique
                            teg_in = te_in
                            teg_inf = 'inf'  # Le côté sortant (position)
                            t_colinf[0] = 'red'
                        if te_su:  # Tétra supérieur(lecture)
                            te_one += 1
                            teg_su = te_su
                            teg_sup = 'sup'  # Le côté sortant
                            t_colsup[0] = 'blue'
                        if 0 < te_one:
                            te_ts = self.gamnomscopie[te]
                            te_ninf = len(teg_in)
                            te_nsup = len(teg_su)
                            te_fix = te_ninf + te_nsup
                        if teg_inf == 'inf':
                            if x_01i == 1:
                                x10 = 13  # Marges de principe(x)
                                x_01i = 0
                            else:
                                x10 = 33  # Marges de principe(x)
                                x_01i = 1
                            for t4 in teg_in:
                                if t4 == 1:
                                    tetcan.create_oval(xh + th * 20 - r1,
                                                       yh + t_tt * 6 - r1,
                                                       xh + th * 20 + r1,
                                                       yh + t_tt * 6 + r1, fill=t_colinf[0])
                                else:
                                    tetcan.create_oval(xh + th * 20 - r2,
                                                       yh + t_tt * 6 - r2,
                                                       xh + th * 20 + r2,
                                                       yh + t_tt * 6 + r2, fill='yellow')
                                th += 1
                            tetcan.create_text(x10, yh + t_tt * 6, text=te_ts, font=fonttt, fill='red')
                        if teg_sup == 'sup':
                            # nel = 0
                            nel = 13 - te_fix
                            th += nel
                            if x_01s == 1:
                                x290 = 303  # Marges de principe(x)
                                x_01s = 0
                            else:
                                x290 = 323  # Marges de principe(x)
                                x_01s = 1
                            for t5 in teg_su:
                                if t5 == 1:
                                    tetcan.create_oval(xh + th * 20 - r1,
                                                       yh + t_tt * 6 - r1,
                                                       xh + th * 20 + r1,
                                                       yh + t_tt * 6 + r1, fill=t_colsup[0])
                                else:
                                    tetcan.create_oval(xh + th * 20 - r2,
                                                       yh + t_tt * 6 - r2,
                                                       xh + th * 20 + r2,
                                                       yh + t_tt * 6 + r2, fill='yellow')
                                th += 1
                            tetcan.create_text(x290, yh + t_tt * 6, text=te_ts, font=fonttt,
                                               fill='blue')

        ''' Choix 1 : Dessine tous les tétras fondamentaux (classic ou calcul)
            Choix 2 : Dessine tous les tétras utilisés communs (tgam_util) (classic ou calcul)
            Choix 3 : [Brouillon] Dessine tous les tétras inutilisés (classic ou calcul)'''
        # La gamme en cours comme élément - système de définition tétracordique
        # Développé tétra similaire diatonique : TETRA/CLONE/DIATONE
        # self.gamnomscopie[]:(noms[+2])gammes - signatures(int)
        # self.gammescopie[] :(valeurs[1,1,0,,,])gammes - intervalles(int)
        # self.accdiese[(de  0 à +6)]: Table des altérations/str(+)
        # self.accbemol[(de -1 à -6)]: Table des altérations/str(-)
        # self.sel_myx[0] : Est l'indice [i] en cours, dans self.gamnomscopie[i]
        # La transition modifie [1,1,0,1,1,1,0] en ([1,0,1,0,1,1],[1,0,1,0,1,1])
        tginf_tra = []  # Table transitive (inf)
        tgsup_tra = []  # Table transitive (sup)
        tgam_tet = []  # tgam_tet : Table tétra's complète
        tgam_nom = []  # tgam_nom : Table des noms[index] relatifs (tgam_tet[index])
        tgam_bin = []  # tgam_bin : Table des tétras couplés relatifs (tgam_tet[index])
        tg_tra = [0]  # tg_tra[0] : Table tétra en cours
        ts_simil = []  # Table des similaires
        in_sim = []  # N° gamme originale
        tgam_util = []  # Tables des utilités
        tginf_nbr = tgsup_nbr = 0
        t_gam = self.gammescopie[self.sel_myx[0]]
        tgam_inf = t_gam[:4]
        tgam_sup = t_gam[4:]
        in_sim.append(self.gammescopie.index(t_gam))  # Index gamme originale
        (lineno(), 'tgam_inf', tgam_inf, tgam_sup, 'T_GAM', t_gam, self.c_ii)
        # 1049 tgam_inf [1, 1, 0, 2] [0, 1, 0] T_GAM [1, 1, 0, 2, 0, 1, 0] C +5
        '''Transformer les parties (cumuls intervalles) en tétras binarisés'''
        for tg_i in tgam_inf:
            if tg_i > 0:
                for tg_ii in range(tg_i + 1):
                    if tg_ii == 0:
                        tginf_tra.append(1)
                        tginf_nbr += 1
                    elif tginf_nbr < 4:
                        tginf_tra.append(0)
            else:
                tginf_tra.append(1)
                tginf_nbr += 1
        for tg_s in tgam_sup:
            if tg_s > 0:
                for tg_ss in range(tg_s + 1):
                    if tg_ss == 0:
                        tgsup_tra.append(1)
                        tgsup_nbr += 1
                    elif tgsup_nbr < 4:
                        tgsup_tra.append(0)
                    if tgsup_nbr == 4:
                        tgsup_tra.append(1)
                        tgsup_nbr += 1
            if tg_s == 0:
                tgsup_tra.append(1)
                tgsup_nbr += 1
        tgsup_tra.append(1)
        tgsup_nbr += 1
        tg_tra[0] = tginf_tra, tgsup_tra  # Conception des deux tétracordes
        (lineno(), tg_tra, 'Gamme en cours:', self.c_ii)
        # 1079 [([1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1])] Gamme en cours: C +5
        # Bouton tétras : L'ensemble tétracordique
        t, w = 0, 0
        '''Les toniques fondamentales. self.gammescopie(Inf/Sup) (version cumul intervalles)
        Construction tgam_tet : Table tétra's fondamentaux (classic ou calcul)'''
        for t_ in self.gammescopie:  # Les toniques fondamentales (version cumul intervalles)
            tinf_tra = []
            tsup_tra = []
            tinf_nbr = tsup_nbr = 0
            t_tra = [0]
            t += 1
            t_inf = t_[:4]
            t_sup = t_[4:]
            for t_i in t_inf:
                if t_i > 0:
                    for t_ii in range(t_i + 1):
                        if t_ii == 0:
                            tinf_tra.append(1)
                            tinf_nbr += 1
                        elif tinf_nbr < 4:
                            tinf_tra.append(0)
                else:
                    tinf_tra.append(1)
                    tinf_nbr += 1
            for t_s in t_sup:
                if t_s > 0:
                    for t_ss in range(t_s + 1):
                        if t_ss == 0:
                            tsup_tra.append(1)
                            tsup_nbr += 1
                        elif tsup_nbr < 4:
                            tsup_tra.append(0)
                        if tsup_nbr == 4:
                            tsup_tra.append(1)
                            tsup_nbr += 1
                if t_s == 0:
                    tsup_tra.append(1)
                    tsup_nbr += 1
            tsup_tra.append(1)
            tsup_nbr += 1
            t_tra[0] = tinf_tra, tsup_tra
            (lineno(), 'tinf_tra:', tinf_tra, tsup_tra, 't_:', t_, 't_ = (version cumul intervalles)')
            tgam_tet.append(t_tra[0])  # tgam_tet : Table tétra's fondamentaux (classic ou calculé)
            (lineno(), 't_tra[0]:', t_tra[0], '\tN°:', w, 'Nom:', self.gamnomscopie[w])
            # 1123 t_tra[0]: ([1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1]) 	N°: 2 Nom: +2 (classic)
            # 1123 t_tra[0]: ([1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1]) 	    N°: 2 Nom: +5 (calculé)
            w += 1  # Utilisé pour obtenir chaque nom de gamme du tétracorde
        # Bouton clones : Les clones dans le système
        tin_f = tg_tra[0][0]  # Tétra inf Original
        tsu_p = tg_tra[0][1]  # Tétra sup Original
        (lineno(), 'Gam_origine', 'inf', tin_f, 'sup', tsu_p, 'c_ii:', self.c_ii, in_sim)
        # 1135 Gamme origine tin_f [1, 0, 1, 0, 1, 1] tsu_p [1, 1, 0, 1, 1] c_ii: C +5 [2]
        ts = ts_t = tn = 0  # ts = Quantité de similitudes
        '''Lecture parmi les fondamentales : ts_simil.append(tin_nom)'''
        for t_ in tgam_tet:  # tgam_tet : Table tétra's fondamentaux (classic ou calcul)
            ts_eti = t_[0]  # Tétra inf en lecture
            ts_ets = t_[1]  # Tétra sup en lecture
            tin_nom = None
            if tin_f == ts_eti:  # Inf = Inf
                tin_nom = ['Inf', 'Inf', ts_t, self.gamnomscopie[ts_t]]
                if ts_eti == tin_f and ts_ets == tsu_p:
                    ts_simil.insert(0, tin_nom)
                else:
                    ts_simil.append(tin_nom)
                ts += 1
            if tin_f == ts_ets:  # Inf = Sup
                tin_nom = ['Inf', 'Sup', ts_t, self.gamnomscopie[ts_t]]
                if ts_eti == tin_f and ts_ets == tsu_p:
                    ts_simil.insert(0, tin_nom)
                else:
                    ts_simil.append(tin_nom)
                ts += 1
            if tsu_p == ts_ets:  # Sup = Sup
                tin_nom = ['Sup', 'Sup', ts_t, self.gamnomscopie[ts_t]]
                if ts_eti == tin_f and ts_ets == tsu_p:
                    ts_simil.insert(0, tin_nom)
                else:
                    ts_simil.append(tin_nom)
                ts += 1
            if tsu_p == ts_eti:  # Sup = Inf
                tin_nom = ['Sup', 'Inf', ts_t, self.gamnomscopie[ts_t]]
                if ts_eti == tin_f and ts_ets == tsu_p:
                    ts_simil.insert(0, tin_nom)
                else:
                    ts_simil.append(tin_nom)
                ts += 1
            if tin_nom:
                tn += 1
                si10 = ts_eti, ts_ets, ts_t, self.gamnomscopie[ts_t]
                tgam_bin.append(si10)
                ('*', lineno(), 'infOr:', tin_f, 'supOr:', tsu_p, 'Nom', self.c_ii, tn)
                ('*', lineno(), 'infCo:', ts_eti, 'supCo:', ts_ets, 'N°', ts_t, 'No', self.gamnomscopie[ts_t], tn)
            ts_t += 1
        (lineno(), self.c_ii, in_sim, 'ts_simil[:2]:', ts_simil[:2], 'len', len(ts_simil))
        # 1208 C Maj [0] ts_simil[:2]: [['Sup', 'Inf', 0, 'Maj'], ['Sup', 'Sup', 0, 'Maj']] len 38
        # Boutons utiles : Sans les clones de l'ensemble tétracordique
        tgam_util, tet_is, tet_tt = [], [], []
        '''tgam_tet = Table tétras fondamentaux'''
        for si in ts_simil:
            tet_tt.append(si[2])
            tetis = si[1], si[3]
            tet_is.append(tetis)
            if si[1] == 'Sup':
                tgam_util.append(tgam_tet[si[2]][1])
                (lineno(), '..si[1]:', si[1], tgam_tet[si[2]][1], si[-1])
            else:
                tgam_util.append(tgam_tet[si[2]][0])
                (lineno(), '...si[1]:', si[1], tgam_tet[si[2]][0], si[-1])
            tgam_nom.append(si[-1])
            (lineno(), 'Si:', si, 'tgam_tet:', tgam_tet[si[2]])  # si[2] = indice gamme. tgam_tet[:6] = 66 unités
            # 1224 Si: ['Inf', 'Sup', 1, '-2'] tgam_tet: ([1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1])
        (lineno(), 'tet_is[:4]:', tet_is[:4], len(tet_is))
        ('     tet_tt[:16]:', tet_tt[:16], len(tet_tt))
        ('     tgam_nom[:10]:', tgam_nom[:10], len(tgam_nom))
        ('     tgam_bin[:1]:', tgam_bin[:1], len(tgam_bin))
        '''1226 tet_is[:4]: [('Inf', 'Maj'), ('Sup', 'Maj'), ('Sup', 'Maj'), ('Inf', 'Maj')] 38 
                tet_tt[:16]: [0, 0, 0, 0, 1, 1, 2, 2, 4, 4, 5, 5, 9, 9, 11, 11] 38 
                tgam_nom[:10]: ['Maj', 'Maj', 'Maj', 'Maj', '-2', '-2', '+2', '+2', '-3', '-3'] 38
                tgam_bin[:1]: [([1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1], 0, 'Maj')] 18'''

    # Version con
    def convers(self):
        con_chk = self.cb_chk.get()
        if con_chk == 1:
            # self.tablenotes : Conteneur diatonique | Calcul graphique horizontal
            del (self.sel_bon[:])
            for y in range(7):
                con_m = (self.tablenotes[y] // 10) - 28
                con_ = con_m
                if con_m < 12:
                    con_ += 12
                if con_m > 23:
                    con_ -= 12
                self.sel_bon.append(con_)
            self.sel_bon.sort()
            self.select = self.sel_bon
            for z in range(7):
                sel_z = self.select[z] - self.sel_gam[z]
                # (z,sel_z)              # Remplacer "#" par "print" pour la forme
                self.sca[z].configure(from_=self.fnotes[z], to=self.tnotes[z])
                self.sca[z].set(sel_z)
            self.sca[7].configure(from_=-12, to=12)
            self.sca[7].set(0)
        else:
            pass
        self.rad[1].invoke()  # Remise à l'octave zéro ou "ioi"

    # Sel de fonction
    def selection(self):
        # ('yes',self.select[0])                 # Remplacer "#" par "print" pour la forme
        for z in range(7):
            sel_z = self.select[z] - self.sel_gam[z]
            self.sca[z].configure(from_=self.fnotes[z], to=self.tnotes[z])
            self.sca[z].set(sel_z)
        self.sca[7].configure(from_=-12, to=12)
        self.sca[7].set(0)
        self.tur.destroy()
        self.rad[1].invoke()  # Remise à l'octave zéro ou "ioi"
        self.btgama.invoke()
        self.preselect[0] = 0  # def selec/Bouton sélection désactivé
        self.bttab.invoke()

    # Piano ou clavier visuel
    def tabla(self):
        if self.tur is not None:
            self.tur.destroy()
        del (self.sel_bon[:])  # Remise à zéro sélection
        # (min:max) ; Tonice(0). Tonale(1:3). Mélode(4:14). Médiane(15:18). Domine(19:42). Harmone(43:65)
        # self.gamnomscopie : exemple(self.gamnomscopie[tbltr] == (noms)gammes concernées par ce type)
        # self.gammescopie : exemple(self.gammescopie[tbltr] == (valeurs)gammes concernées par ce type)
        # self.sel_myx[0] : Contient l'indice de la table gammenoms[myx2] (gamme en cours)
        self.tur = Toplevel(self)
        self.tur.title('Entité Gammique : Tablature en %s' % self.c_ii)
        self.tur.geometry('710x300+500+565')
        self.tur.protocol("WM_DELETE_WINDOW", lambda: Gammique.fermeture(self, 'tabla'))
        # print(lineno(), 'sel_yes:', self.sel_yes, '|sel_yes[0]:', self.sel_yes[0], '|sel_yes[1]:', self.sel_yes[1])
        alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        s_yes = ''

        def assemble(messe):
            """Génération complément du nom de la gamme"""
            m_, bible = '', ''
            if messe[-1] == '0':
                m_ = messe[0] + ' maj'
            else:
                for me in messe:
                    if me in alfa:
                        pass
                    else:
                        bible += me
                m_ = messe[0] + ' ' + bible
            return m_

        if self.sel_yes[0] != '':  # sel_yes[0] = La note est altérée
            for s_ in self.sel_yes[0]:
                s_yes += s_
                # print('S_', s_yes, len(s_yes))
            r_ = assemble(self.sel_yes[1])
        else:  # sel_yes[1] = Partie nom de la gamme
            r_ = assemble(self.sel_yes[1])
        s_yes += r_
        if len(self.sel_yes) > 2:  # sel_yes = Nom déjà traité
            pass
        else:
            self.sel_yes = s_yes
        (lineno(), '|s_yes:', s_yes, '|sel_yes:', self.sel_yes, '\n')
        Label(self.tur, text=self.sel_yes, font='bold', fg='black').pack()
        # Cadre de visualisation : Tablatures
        frtur = Frame(self.tur, width=30, height=1)
        frtur.pack(side=BOTTOM)
        bttur_p = Button(frtur, text='Sélectif', height=1, width=30, bg='orange',
                         command=lambda: self.actuac(6))
        bttur_p.pack(side=LEFT)
        bttur_g = Button(frtur, text='Quitter', height=1, width=30, bg='light grey',
                         command=lambda: self.actuac(7))
        bttur_g.pack(side=RIGHT)
        btsel_ = Button(frtur, text='Invisible', command=self.selection)
        btsel_.pack_forget()
        fontsel = Font(family='Liberation Serif', size=8)
        f0 = 110
        tab_freqs = []
        for ai in range(39):  # Construction tableau TM
            freq = f0 * 2 ** (ai / 12)
            tab_freqs.append(freq)  # Tableau en écriture TM
        # (tab_freqs)            # Remplacer "#" par "print" pour la forme
        if self.preselect[0] == 1:
            Label(self.tur, text='Sélectionner 7 notes, puis une dernière pour rechercher la gamme',
                  font=fontsel, fg='red').place(x=30, y=250, anchor='nw')
        # Encadrement littéral de la gamme
        ind_ = ''  # Famille de la gamme(,, mélodique,,, harmonique,)
        sel_ind = self.sel_myx[0]
        if sel_ind == 0:
            ind_ = self.tbltr_nom[0]
        elif 0 < sel_ind < 4:
            ind_ = self.tbltr_nom[1]
        elif 3 < sel_ind < 15:
            ind_ = self.tbltr_nom[2]
        elif 14 < sel_ind < 19:
            ind_ = self.tbltr_nom[3]
        elif 18 < sel_ind < 43:
            ind_ = self.tbltr_nom[4]
        elif 42 < sel_ind < 66:
            ind_ = self.tbltr_nom[5]
        Label(self.tur, text=ind_, font='bold', fg='blue').place(x=30, y=3, anchor='nw')
        self.sel_nbr = -1
        self.sel_stp = 0

        def piano_b(m):
            i_ = 0
            self.sel_nbr += 1
            freqhtz = int(tab_freqs[self.gen_b[m]])
            nboctet = nbcanal = 1
            fech = 64000
            niveau = float(1 / 2)
            duree = float(1 / 6)
            nbech = int(duree * fech)
            manote = open(self.piano_wav[0], 'wb')
            param = (nbcanal, nboctet, fech, nbech, 'NONE', 'NONE')
            # noinspection PyTypeChecker
            manote.setparams(param)
            amp = 127.5 * niveau
            for i in range(0, nbech):
                val = pack('B', int(128.0 + amp * sin(2.0 * pi * freqhtz * i / fech)))
                manote.writeframes(val)
            manote.close()
            p = PyAudio()
            chunk = 2048
            wf = open(self.piano_wav[0], 'rb')
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(chunk)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(chunk)
            stream.stop_stream()
            stream.close()
            p.terminate()
            if self.preselect[0] == 1 and self.sel_stp == 0:
                if self.sel_nbr < 7:
                    mb = m
                    sg_b = self.gen_bz[m]
                    if sg_b < 12:
                        sg_b += 12
                        mb = m + 7
                    if sg_b > 23:
                        sg_b -= 12
                        mb = m - 7
                    self.sel_bon.sort()
                    if self.sel_nbr == 0:
                        pb = 0
                    else:
                        pb = len(self.sel_bon)
                    for i in range(pb):
                        if self.sel_bon[i] == self.gen_bz[mb]:
                            self.sel_nbr -= 1
                            i_ = 1
                    if i_ == 0:
                        self.sel_bon.append(sg_b)
                        bts[m].configure(bg="orange")
                        bts[mb].configure(bg="yellow")
                        # ('m',self.gen_bz[m])   # Blanches()
                else:
                    self.sel_stp = 1
                    self.sel_bon.sort()
                    self.select = self.sel_bon
                    btsel_.invoke()
                    # del(self.sel_bon[:])    # Remise à zéro sélection

        def piano_n(m):
            i_ = 0
            self.sel_nbr += 1
            freqhtz = int(tab_freqs[self.gen_n[m]])
            nboctet = nbcanal = 1
            fech = 64000
            niveau = float(1 / 2)
            duree = float(1 / 6)
            nbech = int(duree * fech)
            manote = open(self.piano_wav[1], 'wb')
            param = (nbcanal, nboctet, fech, nbech, 'NONE', 'NONE')
            # noinspection PyTypeChecker
            manote.setparams(param)
            amp = 127.5 * niveau
            for i in range(0, nbech):
                val = pack('B', int(128.0 + amp * sin(2.0 * pi * freqhtz * i / fech)))
                manote.writeframes(val)
            manote.close()
            p = PyAudio()
            chunk = 2048
            wf = open(self.piano_wav[1], 'rb')
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(chunk)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(chunk)
            stream.stop_stream()
            stream.close()
            p.terminate()
            if self.preselect[0] == 1 and self.sel_stp == 0:
                if self.sel_nbr < 7:
                    mn = m
                    sg_n = self.gen_nz[m]
                    # ('sgn',sg_n)
                    if sg_n < 12:
                        sg_n += 12
                        mn = m + 7
                    elif sg_n > 23:
                        sg_n -= 12
                        mn = m - 7
                    self.sel_bon.sort()
                    if self.sel_nbr == 0:
                        pb = 0
                    else:
                        pb = len(self.sel_bon)
                    for i in range(pb):
                        if self.sel_bon[i] == self.gen_nz[mn]:
                            self.sel_nbr -= 1
                            i_ = 1
                    if i_ == 0:
                        self.sel_bon.append(sg_n)
                        btns[m].configure(bg="orange")
                        btns[mn].configure(bg="yellow")
                        # ('m',self.gen_nz[m])   # Noires()
                else:
                    self.sel_stp = 1
                    self.sel_bon.sort()
                    self.select = self.sel_bon
                    btsel_.invoke()
                    # del(self.sel_bon[:])    # Remise à zéro sélection

        # Les touches blanches définition
        bts = []
        lbab_bs = []
        for x in range(21):
            bt = Button(self.tur, text='', height=10, width=3, bg='ivory',
                        command=lambda m=x: piano_b(m), relief="groove")
            bt.place(x=30 * x + 30, y=30, anchor='nw')
            bts.append(bt)
            lbab_b = Label(self.tur, text='', font=fontsel, fg='black')
            lbab_b.place(x=30 * x + 30, y=225, anchor='nw')
            lbab_bs.append(lbab_b)
        # Les touches noires : Attention aux absences indicées ! (les -1)
        btns = []
        lbab_ns = []
        o = btn = 0
        for x in range(21):
            if o == 2 or o == 6:
                pass
            else:
                btn = Button(self.tur, text='', height=5, width=2, bg='black',
                             command=lambda m=x: piano_n(m), relief="groove")
                btn.place(x=30 * x + 45, y=30, anchor='nw')
            o += 1
            if o > 6:
                o = 0
            btns.append(btn)
            lbab_n = Label(self.tur, text='', font=fontsel, fg='black')
            lbab_n.place(x=30 * x + 45, y=200, anchor='nw')
            lbab_ns.append(lbab_n)
        # self.tablenotes : Conteneur diatonique (x)
        s_deg = self.tbdegre[0]
        s_deg = 7 - s_deg
        s_bob, s_bon = '', ''
        for x in range(7):
            bon_ok = bob = bon = 0
            z = (self.tablenotes[x] // 10) - 28
            if s_deg > 6:
                s_deg = 0
            for bz in self.gen_bz:
                if z == bz and bon_ok == 0:
                    bts[bob].configure(bg="lightblue")
                    s_bob = self.decore[s_deg][1]
                    lbab_bs[bob].configure(text=s_bob)
                    bon_ok = 1
                    break
                else:
                    bob += 1
            for nz in self.gen_nz:
                if z == nz and bon_ok == 0:
                    btns[bon].configure(bg="lightblue")
                    for sbo in self.decore[s_deg]:
                        s_bon += sbo
                        # print('***', sbo)
                    # print(s_bon, len(s_bon), 'self.decore[s_deg]', self.decore[s_deg])
                    lbab_ns[bon].configure(text=s_bon)
                    # bon_ok = 1
                    break
                else:
                    bon += 1
            s_deg += 1
            # print(lineno(), 's_bob:', s_bob, 's_bon:', s_bon)

    # Actualité " actuac "
    def actuac(self, a):
        if a == 5:  # def accord/Bouton fermer
            Gammique.fermeture(self, 'accord')
        elif a == 3:  # def accord/Bouton actualiser
            self.acc.destroy()
            self.presaudio = 1
            self.btaud2.invoke()
            self.btacc.invoke()
        elif a == 1:  # def audio/Bouton audio
            self.presaudio = 0
            self.btaud2.invoke()
        elif a == 2:  # def chrome/Bouton C_n
            self.btchr.configure(text='Chrome naturel')
            self.chm.destroy()
            self.btchr.invoke()
        elif a == 4:  # def chrome/Bouton C_a
            self.btchr.configure(text='Chrome atonal')
            self.chm.destroy()
            self.btchr.invoke()
        elif a == 6:  # def tabla/Bouton sélection activé
            self.preselect[0] = 1
            self.bttab_2.invoke()
        elif a == 7:  # def tabla/Bouton quitter
            Gammique.fermeture(self, 'tabla')
        elif a == 8:  # def select/Bouton sélection activé
            self.preselect[0] = 1
            self.bttab_2.invoke()
        elif a == 9:  # def init/Bouton Tablature activé
            self.preselect[0] = 0
            self.bttab_2.invoke()

    # Prémices chromatiques
    def chrome(self):
        """root.protocol("WM_DELETE_WINDOW",lambda: print('clic fermeture root') )"""
        if self.chm is not None:
            self.chm.destroy()
        self.chm = Toplevel(self)
        self.chm.title('Entité Gammique : Chromatisme en %s' % self.c_ii)
        self.chm.geometry('700x600+800+40')
        self.chm.protocol("WM_DELETE_WINDOW", lambda: Gammique.fermeture(self, 'chrome'))
        # Sélection du mode chromatique (naturel) ou (atonal)
        frchm = Frame(self.chm, width=200, height=10)
        frchm.pack(side=BOTTOM)
        btchn = Button(frchm, text='Chrome naturel', width=30, bg='ivory',
                       command=lambda: self.actuac(2))
        btchn.pack(side=LEFT)
        btcha = Button(frchm, text='Chrome atonal', width=30, bg='ivory',
                       command=lambda: self.actuac(4))
        btcha.pack(side=RIGHT)
        frchm_ = Frame(self.chm, width=200, height=10)
        frchm_.pack(side=TOP)
        # Fenêtre écran_résultat
        chrcan = Canvas(self.chm, bg='white', height=666, width=777)
        chrcan.pack()
        Label(frchm_, text="Chromatismes", fg='red').pack()
        fontchr = Font(family='Liberation Serif', size=10)
        # Le pas graphique entre 2 notes = 10, en cotation horizontale
        # self.tablenotes : Conteneur diatonique | Calcul graphique horizontal
        # self.tablehaute : Conteneur diatonique | Calcul graphique vertical
        # self.tbdegre : Première note du mode tonique en cours
        # self.chrgen : Tableau graphique chromatique( note , signe ,,, )
        # self.dechire : Tableau des positions altérées
        chnat_aug = [1, 2, 4, 5, 6]
        chnat_min = [2, 3, 5, 6, 7]
        chr_trans = []
        chr_curs = []
        chr_lepas = 10
        cy_inter = 0
        chrselect = self.btchr.cget('text')
        # self.tablenotes : Conteneur diatonique | Calcul graphique horizontal
        cy_zer = self.tbdegre[0]  # Premier degré de la gamme
        for cy_ in range(7):
            if cy_ == 0:
                cy_inter = self.tablenotes[cy_zer] - 0
                # print('cy_', cy_inter)
            if self.tablenotes[cy_zer] < cy_inter:
                cy_trans = self.tablenotes[cy_zer] - cy_inter + 120
            else:
                cy_trans = self.tablenotes[cy_zer] - cy_inter
            # print('cy_2', cy_inter)
            chr_trans.append(cy_trans)  # Transformé élémentaire
            chr_curs.append(self.cursifs[cy_zer])
            cy_zer += 1
            if cy_zer > 6:
                cy_zer = 0
        # print('chr_trans', chr_trans) # Contenu graphique diatonique
        # Génération élémentaire du tableau chromatique
        #  Formation chromatique
        chr_chrom = []
        chr_bem = []
        chr_dies = []
        tra0 = 6
        maj1 = 1
        maj0 = 0
        coltyp1 = [0]
        coltyp2 = [0]
        for c in range(0, 120, 10):
            c0 = c
            if c == chr_trans[maj0]:
                c_tr1 = chr_trans[tra0]
                while c_tr1 == 110:
                    c_tr1 = -10
                if c0 - 10 is not c_tr1 and c_tr1 > -1:
                    for di in chnat_aug:
                        if di == maj0:
                            rg_dies = c0 - 10
                            rg_diesdeg = rg_dies, maj0
                            chr_dies.append(rg_diesdeg)
                maj1 += 1
                if maj1 > 7:
                    maj1 = 1
                maj0 = maj1 - 1
                tra0 += 1
                if tra0 > 6:
                    tra0 = 0
            else:
                c_tr1 = chr_trans[tra0]
                chr_chrom.append(c - (c * 2))
                if c0 - 10 == c_tr1:
                    for be in chnat_min:
                        if be == maj1:
                            rg_bemdeg = c, maj1
                            chr_bem.append(rg_bemdeg)
        (lineno(), ' chr_dies:', chr_dies, '\n chr_bem:', chr_bem)  # [(rangX, degréN)]
        # 1753  chr_dies: [(10, 1), (30, 2), (60, 4), (80, 5), (100, 6)]    chnat_aug = [1, 2, 4, 5, 6]
        #  chr_bem: [(10, 2), (30, 3), (60, 5), (80, 6), (100, 7)]          chnat_min = [2, 3, 5, 6, 7]

        def c_sign(c_dbs, axe):  # Altération des notes chromatiques
            cdb_, ret_ = c_dbs, 0
            if axe == 1:
                if c_dbs > -1:
                    c_sdb[0] = self.nordiese[cdb_]
                    coltyp1[0] = 'plum'
                else:
                    c_sdb[0] = self.subemol[cdb_]
                    coltyp2[0] = 'pink'
                (lineno(), 'GGVc/C_SIGN/db_:', cdb_, 'c_sdb[0]:', c_sdb[0], 'c_dbs:', c_dbs)
            elif axe == 2:  # axe = 2 = C'est la valeur numérique de l'altération qui est en paramètre
                if c_dbs > -1:
                    c_xyz = self.nordiese[cdb_]
                    i_xyz = self.nordiese.index(c_xyz)
                    ret_ = 'Diato_aug'
                else:
                    c_xyz = self.subemol[cdb_]
                    i_xyz = self.subemol.index(c_xyz) - len(self.subemol)
                    ret_ = 'Diato_dim'
                (lineno(), 'GGVc/C_SIGN/db_:', cdb_, 'c_xyz:', c_xyz, 'i_xyz:', i_xyz)
                return c_xyz, i_xyz, ret_
            elif axe == 3:  # axe = 3 = C'est l'altération qui est en paramètre
                (lineno(), '--------- Définition service/axe3 ---------')
                if cdb_ in self.nordiese:
                    j_xyz = self.nordiese.index(cdb_)
                    ret_ = 'Chrome_aug'
                    (lineno(), '---------GGVc/C_SIGN/db_:', cdb_, 'j_xyz:', j_xyz, 'ret_:', ret_)
                else:
                    j_xyz = self.subemol.index(cdb_) - len(self.subemol)
                    ret_ = 'Chrome_dim'
                    (lineno(), '---------GGVc/C_SIGN/db_:', cdb_, 'j_xyz:', j_xyz, 'ret_:', ret_)
                return cdb_, j_xyz, ret_

        def c_form(c_noes):
            cf_ = c_noes
            c_ie = len(self.nordiese)
            for cie in range(c_ie):
                eic = cie - (cie * 2)
                ce_aug = self.nordiese[cie]
                ce_min = self.subemol[eic]
                if ce_aug == cf_:
                    c_dbn[0] = cie
                if ce_min == cf_:
                    c_dbn[0] = eic
            (lineno(), 'GGV6/C_FORM/cf_:', cf_, 'c_dbn[0]:', c_dbn[0], 'c_noes:', c_noes)

        # Définitions données
        ch_chrdies = ['0', '0', '0', '0', '0']
        ch_chrbem = ['0', '0', '0', '0', '0']
        c_sdb = [0]
        c_dbn = [0]
        # c1_,c7_ = 'n',0
        for ch in chr_chrom:
            ch_o = ch - (ch * 2)
            c_ = 0
            # cz_ = ch_o
            for ch_d in chr_dies:
                ch_wd = ch_d[0]
                if ch_wd == ch_o:
                    ch_dx = ch_d[1]
                    for cb in range(5):
                        cb_o = chr_chrom[cb]
                        cbo = cb_o - (cb_o * 2)
                        if ch_wd == cbo:
                            c_ = cb
                    c_noe0 = self.decore[ch_dx - 1]
                    c_noe1 = c_noe0[1]
                    c_noe2 = c_noe0[0]
                    c_form(c_noe2)  # c_form initialise c_dbn[0]
                    ch_wdx2 = (ch_wd - chr_trans[ch_dx - 1]) // 10
                    ch_wdx = ch_wdx2 + c_dbn[0]
                    c_db = ch_wdx
                    c_sign(c_db, 1)  # c_sign initialise c_sdb[0]
                    c2_0 = c_sdb[0]
                    c3_0 = c_noe1
                    # c4_0 = c2_0
                    ch_chrdies[c_] = ch_o, ch_dx, c2_0, c3_0, 'plum', ch_wdx
            for ch_b in chr_bem:
                ch_yb = ch_b[0]
                if ch_yb == ch_o:
                    ch_bz = ch_b[1]
                    for cb in range(5):
                        cb_o = chr_chrom[cb]
                        cbo = cb_o - (cb_o * 2)
                        if ch_yb == cbo:
                            c_ = cb
                    c_noe0 = self.decore[ch_bz - 1]
                    c_noe2 = c_noe0[0]
                    c_noe1 = c_noe0[1]
                    c_form(c_noe2)
                    ch_ybz2 = (ch_yb - chr_trans[ch_bz - 1]) // 10
                    ch_ybz = ch_ybz2 + c_dbn[0]
                    c_db = ch_ybz
                    c_sign(c_db, 1)
                    c5_0 = c_sdb[0]
                    c6_0 = c_noe1
                    ch_chrbem[c_] = ch_o, ch_bz, c5_0, c6_0, 'pink', ch_ybz
        (lineno(), 'ch_chrdies:', ch_chrdies, '\n ch_chrbem:', ch_chrbem)  # Gamme naturelle
        # 1831 ch_chrdies: [(10, 1, '+', 'C', 'plum', 1), (30, 2, '+', 'D', 'plum', 1), (60, 4, '+', 'F', 'plum', 1),
        # (80, 5, '+', 'G', 'plum', 1), (100, 6, '+', 'A', 'plum', 1)]
        #  ch_chrbem: [(10, 2, '-', 'D', 'pink', -1), (30, 3, '-', 'E', 'pink', -1), (60, 5, '-', 'G', 'pink', -1),
        #  (80, 6, '-', 'A', 'pink', -1), (100, 7, '-', 'B', 'pink', -1)]
        c_aug = []
        for ci_ in ch_chrdies:
            if ci_ != '0':
                c_aug.append(ci_[1])
        c_aug.sort()
        c_min = []
        for ci_ in ch_chrbem:
            if ci_ != '0':
                c_min.append(ci_[1])
        c_min.sort()
        c2_aug = []
        c2_min = []
        # Définitions ajoutées
        for c in range(5):
            ch_c = chr_chrom[c]
            c_ch = ch_c - (ch_c * 2)
            if ch_chrdies[c] == '0':
                c20 = c2_o = -1
                for c_a2 in chnat_aug:
                    if c20 < 0:
                        c20 = 0
                        c2_o += 1
                        for c_a3 in c_aug:
                            if c_a2 == c_a3:
                                c20 = -1
                                break
                        for c_a4 in c2_aug:
                            if c_a2 == c_a4:
                                c20 = -1
                                break
                    if c20 == 0:
                        c2_aug.append(c_a2)
                        break
                c2 = c2_o
                c_a = chnat_aug[c2]
                c_a0 = c_a - 1
                c_noe0 = self.decore[c_a0]
                c_noe1 = c_noe0[1]
                c_noe2 = c_noe0[0]
                c_form(c_noe2)
                c_mj2 = (c_ch - chr_trans[c_a0]) // 10
                c_mj = c_mj2 + c_dbn[0]
                c_db = c_mj
                c_sign(c_db, 1)
                c2_0 = c_sdb[0]
                c3_0 = c_noe1
                # c4_0 = c_mj
                ch_chrdies[c] = c_ch, c_a, c2_0, c3_0, 'plum', c_mj
            if ch_chrbem[c] == '0':
                c20 = c2_o = -1
                for c_a2 in chnat_min:
                    if c20 < 0:
                        c20 = 0
                        c2_o += 1
                        for c_a3 in c_min:
                            if c_a2 == c_a3:
                                c20 = -1
                                break
                        for c_a4 in c2_min:
                            if c_a2 == c_a4:
                                c20 = -1
                                break
                    if c20 == 0:
                        c2_min.append(c_a2)
                        break
                c2 = c2_o
                c_a = chnat_min[c2]
                c_a0 = c_a - 1
                c_noe0 = self.decore[c_a0]
                c_noe1 = c_noe0[1]
                c_noe2 = c_noe0[0]
                c_form(c_noe2)
                c_mj2 = (c_ch - chr_trans[c_a0]) // 10
                c_mj = c_mj2 + c_dbn[0]
                c_db = c_mj
                c_sign(c_db, 1)
                c2_0 = c_sdb[0]
                c3_0 = c_noe1
                # c4_0 = c2_0
                ch_chrbem[c] = c_ch, c_a, c2_0, c3_0, 'pink', c_mj  # [(10, 2, '-', 'D', 'pink', -1),,, ]
        (lineno(), 'ch_chrdies:', ch_chrdies, '\n ch_chrbem:', ch_chrbem)  # Gamme naturelle
        '''# Ressemble à la précédente sauf pour l'initialisation des variables utilisées'''
        # 1916 ch_chrdies: [(10, 1, '+', 'C', 'plum', 1), (30, 2, '+', 'D', 'plum', 1), (60, 4, '+', 'F', 'plum', 1),
        # (80, 5, '+', 'G', 'plum', 1), (100, 6, '+', 'A', 'plum', 1)]
        #  ch_chrbem: [(10, 2, '-', 'D', 'pink', -1), (30, 3, '-', 'E', 'pink', -1), (60, 5, '-', 'G', 'pink', -1),
        #  (80, 6, '-', 'A', 'pink', -1), (100, 7, '-', 'B', 'pink', -1)]
        xcpos_ = 180
        ycpos_ = 234
        y_poste = []
        # c4_ = self.dechire[(0, cx_uu)]
        for v10_dec in range(1, 8):
            v_10 = ycpos_ - (self.dechire[0, v10_dec] * 30)
            y_poste.append(v_10)
            (lineno(), 'v10_dec:', v_10)
        print(lineno(), 'y_poste:', y_poste)
        c_chaug = [0]
        c_chmin = [0]
        c_doube = [0]
        cz_ = cx_tr = cn_ = 0
        cx_uu = 1
        chtop6 = chr_trans[6] // 10
        chposx = 0
        rb_ = 15
        chrcan.create_line(15, 234, 585, 234, fill='blue')
        for cx_ in range(12):
            c1_ = c2_ = c3_ = c4_ = c5_ = c6_ = c7_ = 'n'  # -1 = Emplacement chromatique
            c2_a1 = c2_m1 = c3_a = c3_m = c4_a = c4_a1 = c4_m = c4_m1 = comp = 0
            coltyp = 'light grey'  # Couleur des notes diatoniques
            if cx_ == 0:
                c1_ = chr_trans[cx_tr]  # Incrustation position diatonique
                c2_ = chr_curs[cx_tr]  # Hauteur altérative tonale
                if c2_ > -1:
                    c2_ = self.nordiese[c2_]
                else:
                    c2_ = self.subemol[c2_]
                c3_ = self.decore[cx_tr][1:]  # Note diatonique
                c4_ = self.dechire[(0, cx_uu)]  # Position tonale
                (lineno(), 'c3_:', c3_, 'c4_:', c4_, 'cx_uu:', cx_uu)  # c3_[0] = C
                # 1946 c3_: ('C',) c4_: 0
                cx_tr += 1
                cx_uu += 1
                chposx += 1
                chposyn = c4_
                xb_ = xcpos_ + (chposx * 30)
                ybn_ = ycpos_ - (chposyn * 30)
                chvow_n = "{}{}".format(c2_, c3_[0])
                chrcan.create_oval(xb_ - rb_, ybn_ - rb_, xb_ + rb_, ybn_ + rb_, fill=coltyp)  # Notes diatoniques
                chrcan.create_text(xb_, ybn_, text=chvow_n, font=fontchr, fill='black')
                (lineno(), '_\t GGV6/ybn_:', ybn_, chvow_n, 'chposyn:', chposyn, 'cx_uu:', cx_uu)  # Gamme C b3
            else:
                if chr_trans[cx_tr] == cx_ * 10:
                    c1_ = chr_trans[cx_tr]  # c1_ = Position de la note diatonique
                    c2_ = chr_curs[cx_tr]  # c2_ = Altération de la note diatonique
                    (lineno(), 'chr_trans:', chr_trans, 'chr_curs:', chr_curs)  # Pour diatonique[b3]
                    # 1960 chr_trans: [0, 20, 30, 50, 70, 90, 110] chr_curs: [0, 0, -1, 0, 0, 0, 0]
                    if c2_ > -1:
                        c2_ = self.nordiese[c2_]
                    else:
                        c2_ = self.subemol[c2_]
                    c3_ = self.decore[cx_tr][1:]  # c3_ = Note de la gamme* (7 notes)
                    c4_ = self.dechire[(0, cx_uu)]  # self.dechire = Dictionnaire des altérations diatoniques
                    cx_tr += 1
                    cx_uu += 1
                    chposx += 1
                    chposyn = c4_
                    xb_ = xcpos_ + (chposx * 30)
                    ybn_ = ycpos_ - (chposyn * 30)
                    chvow_n = "{}{}".format(c2_, c3_[0])  # chvow_n(entier réel) = Note diatonique[c3_[0]], signe[c2_]
                    chrcan.create_oval(xb_ - rb_, ybn_ - rb_, xb_ + rb_, ybn_ + rb_, fill=coltyp)  # Notes diatoniques
                    chrcan.create_text(xb_, ybn_, text=chvow_n, font=fontchr, fill='black')
                    (lineno(), '_\t GGV6/ybn_:', ybn_, chvow_n, 'chposyn:', chposyn, 'cx_uu:', cx_uu)
                else:
                    comp = -1
                    # Zone des futurs
                if comp == -1 and cn_ < 5:
                    if chrselect == 'Chrome atonal':
                        if chtop6 < cx_:
                            chpre = chr_trans[6] // 10  # chr_trans = Positions des notes diatoniques
                            chsui = chr_trans[0] // 10
                            c2_pre = chr_curs[6]  # chr_curs = Altérations des notes diatoniques
                            c2_sui = chr_curs[0]
                            c3_pre = self.decore[6][1:]
                            c3_sui = self.decore[0][1:]
                            c4_pre = self.dechire[(0, 7)]
                            c4_sui = self.dechire[(0, 1)]
                        else:
                            chpre = chr_trans[cx_tr - 1] // 10
                            chsui = chr_trans[cx_tr] // 10
                            c2_pre = chr_curs[cx_tr - 1]
                            c2_sui = chr_curs[cx_tr]
                            c3_pre = self.decore[cx_tr - 1][1:]
                            c3_sui = self.decore[cx_tr][1:]
                            c4_pre = self.dechire[(0, cx_tr)]
                            c4_sui = self.dechire[(0, cx_tr + 1)]
                        tg_pre = cx_ - chpre
                        tg_sui = cx_ - chsui
                        c2_ax = tg_pre + c2_pre
                        c_db = c2_ax
                        c_sign(c_db, 1)
                        c2_a1 = c_sdb[0]
                        c2_mx = tg_sui + c2_sui
                        c_db = c2_mx
                        c_sign(c_db, 1)
                        c2_m1 = c_sdb[0]
                        c3_a = c3_pre[0]
                        c3_m = c3_sui[0]
                        c4_a = c4_pre + tg_pre
                        c_db = c4_a
                        c_sign(c_db, 1)
                        c4_a1 = c_sdb[0]
                        c4_m = c4_sui + tg_sui
                        c_db = c4_m
                        c_sign(c_db, 1)
                        c4_m1 = c_sdb[0]
                        (lineno(), 'Nom atonal =', c4_a, c4_m)
                    if chrselect == 'Chrome naturel':  # Voir fiche R_problèmes.md
                        ''' *** c3_a et c3_m : Transportent les notes chromes/diatoniques,
                            les notes chromatiques relatives aux notes diatoniques.
                            *** c4_a et c4_m : Transportent les valeurs de positionnement,
                            seul le positionnement vertical est affecté et en cours de rectification.
                        Seuls, chr_trans, chr_curs et self.decore pour les références diatoniques.
                        # 1960 chr_trans: [0, 20, 30, 50, 70, 90, 110] chr_curs: [0, 0, -1, 0, 0, 0, 0]'''

                        def relatif(cas, signal, image):
                            """Fonction chargée de trouver le lien avec la gemme diatonique,
                            afin d'identifier les correspondances notes/altérations des positionnements
                            cas[Note chrome], signal[Altération chrome], image[Chrome aug/dim]"""
                            (lineno(), ' ---- cas:', cas, 'signal:', signal, 'image:', image)
                            sig_dia, sig_chr, pos_dia = (), (), []
                            chr_sup1 = chr_inf1 = k_doc = 0
                            if signal in self.nordiese:
                                sig_chr = self.nordiese.index(signal)
                            else:
                                sig_chr = self.subemol.index(signal) - len(self.subemol)
                            # Chercher dans le dictionnaire self_décore
                            for k_dec, v_dec in self.decore.items():
                                if cas in v_dec:
                                    pos_dia, val_dia = chr_trans[k_dec], chr_curs[k_dec]
                                    (lineno(), 'k_dec:', k_dec, 'y_poste[k_dec]:', y_poste[k_dec])
                                    if image == 'sup':
                                        sig_chr = c_sign(signal, 3), 'sup'
                                        sig_dia = c_sign(val_dia, 2)
                                    elif image == 'inf':
                                        sig_chr = c_sign(signal, 3), 'inf'
                                        sig_dia = c_sign(val_dia, 2)
                                    n_chr, n_dia = sig_chr[0][1], sig_dia[1]
                                    nn_cd = n_chr - n_dia
                                    if sig_chr[1] == 'sup':
                                        chr_sup1 = nn_cd
                                        (lineno(), 'chr_sup1:', chr_sup1, nn_cd)
                                    elif sig_chr[1] == 'inf':
                                        chr_inf1 = nn_cd
                                        (lineno(), 'chr_inf1:', chr_inf1, nn_cd)
                                    (lineno(), k_dec, 'n_chr:', n_chr, 'n_dia:', n_dia, '= nn_cd:', nn_cd)
                                    (lineno(), 'cas:', cas, sig_chr, sig_dia, 'pos_dia:', pos_dia)
                                    k_doc = k_dec
                                    break
                            (lineno(), 'return:', chr_sup1, chr_inf1, y_poste[k_doc])
                            return chr_sup1, chr_inf1, k_doc

                        c_chaug[0] = ch_chrdies[cn_]
                        c2_a1 = c_chaug[0][2]  # Altération sur la note chrome augmentée
                        c3_a = c_chaug[0][3]  # Note du chrome augmenté
                        '''Appel fonction pour retour donnée de positionnement augmenté'''
                        ycpos_1 = relatif(c3_a, c2_a1, 'sup')
                        ycpos_, chr_sup, chr_inf = y_poste[ycpos_1[2]], ycpos_1[0], ycpos_1[1]
                        (lineno(), 'chr_sup:', chr_sup, 'ycpos_1:', ycpos_1)
                        c4_a1 = c2_a1
                        c4_a = chr_sup  # Valeur numérique altérative chrome augmenté
                        coltyp1[0] = c_chaug[0][4]  # Couleur graphique augmentée
                        c_chmin[0] = ch_chrbem[cn_]
                        c2_m1 = c_chmin[0][2]  # Altération sur la note chrome diminuée
                        c3_m = c_chmin[0][3]  # Note diatonique du chrome diminué
                        '''Appel fonction pour retour donnée de positionnement diminué'''
                        ycpos_1 = relatif(c3_m, c2_m1, 'inf')
                        ycpos_, chr_sup, chr_inf = y_poste[ycpos_1[2]], ycpos_1[0], ycpos_1[1]
                        (lineno(), 'chr_inf:', chr_inf, 'ycpos_:', ycpos_)
                        c4_m1 = c2_m1
                        coltyp2[0] = c_chmin[0][4]  # Couleur graphique diminuée
                        c4_m = chr_inf  # Valeur numérique altérative chrome diminué
                        c_doube[0] = 0
                        if c3_a == c3_m:
                            c_doube[0] = 2
                        (lineno(), 'Nom naturel =', c4_a, c4_m, ch_chrdies[cn_], ch_chrbem[cn_], c3_m)
                        # 2036 Nom naturel = 1 -1 (10, 1, '+', 'C', 'plum', 1) (10, 2, '-', 'D', 'pink', -1)
                        # 1916 ch_chrdies: [(10, 1, '+', 'C', 'plum', 1), (30, 2, '+', 'D', 'plum', 1),
                        # (60, 4, '+', 'F', 'plum', 1), (80, 5, '+', 'G', 'plum', 1), (100, 6, '+', 'A', 'plum', 1)]
                        # ch_chrbem: [(10, 2, '-', 'D', 'pink', -1), (30, 3, '-', 'E', 'pink', -1),
                        # (60, 5, '-', 'G', 'pink', -1), (80, 6, '-', 'A', 'pink', -1), (100, 7, '-', 'B', 'pink', -1)]
                    cn_ += 1
                    chposx += 1
                    c2_ = c2_a1
                    ''' c3_a et c3_m : Transportent les notes chromes/diatoniques,
                        les notes chromatiques relatives aux notes diatoniques.'''
                    c3_ = c3_a  # c3_ = Note chromatique augmentée dans chvow_a
                    c4_ = c4_a1
                    c5_ = c2_m1  # Altération portée sur la note
                    c6_ = c3_m  # c6_ = Note chromatique diminuée dans chvow_m
                    c7_ = c4_m1
                    ''' c4_a et c4_m : Transportent les valeurs de positionnement,
                        seul le positionnement vertical est affecté et en cours de rectification.'''
                    chposya = c4_a  # Valeur numérique altérative chrome augmenté de c_chaug[0][5]
                    chposym = c4_m  # Valeur numérique altérative chrome diminué de c_chmin[0][5]
                    xb_ = xcpos_ + (chposx * 30)
                    yb1_ = ycpos_ - (chposya * 30)  # ycpos_ = Position naturelle horizontale[234].
                    chvow_a = "{}{}".format(c2_, c3_)
                    if c_doube[0] == 2:
                        coltyp1[0] = 'tan'
                        coltyp2[0] = 'tan'
                    chrcan.create_oval(xb_ - rb_, yb1_ - rb_, xb_ + rb_, yb1_ + rb_, fill=coltyp1[0])
                    chrcan.create_text(xb_, yb1_, text=chvow_a, font=fontchr, fill='black')
                    (lineno(), '*GGV6/yb1_:', yb1_, chvow_a, 'yc:', ycpos_, 'chposya:', chposya)
                    yb2_ = ycpos_ - (chposym * 30)
                    chvow_m = "{}{}".format(c5_, c6_)  # Les notes chromatiques
                    chrcan.create_oval(xb_ - rb_, yb2_ - rb_, xb_ + rb_, yb2_ + rb_, fill=coltyp2[0])
                    chrcan.create_text(xb_, yb2_, text=chvow_m, font=fontchr, fill='black')
                    (lineno(), '*GGV6/yb2_:', yb2_, chvow_m, 'yc:', ycpos_, 'chposym:', chposym)
            self.chrgen[cx_] = [cz_], [c1_], [c2_], [c3_], [c4_], [c5_], [c6_], [c7_]
            cz_ += chr_lepas
            (lineno(), 'self.decore:', self.decore)  # Les notes diatoniques rangées
            # 2066 self.decore: {0: ('', 'C'), 1: ('', 'D'), 2: ('-', 'E'), 3: ('', 'F'),
            # 4: ('', 'G'), 5: ('', 'A'), 6: ('', 'B')}
            (lineno(), '-----------------:Marquage cycle révision-tonalité:-----------------')

            # Génération analogique du tableau chromatique
            # chrcan = Canvas(height=300,width=600)
            chvow = "{}{}".format('Gamme chromatique :', chrselect)
            chrcan.create_line(5, 15, 5, 5, fill='black')
            chrcan.create_text(120, 10, text=chvow, fill='red')
        (lineno(), '---------------------------:Marquage cycle révision-diatonie:---------------------------')

    # Les accords acoustiques
    def wavacc(self, w):
        waplo = self.fichacc[w]
        monac = open(waplo, 'wb')
        nboctet = nbcanal = 1
        fech = 64000
        niveau = float(1)
        duree = float(1 / 2)
        nbech = int(duree * fech)
        param = (nbcanal, nboctet, fech, nbech, 'NONE', 'NONE')
        # noinspection PyTypeChecker
        monac.setparams(param)
        amp = 127.5 * niveau
        vacc = [0, 0, 0, 0]
        vacc_oct = 0
        ww = w
        for vv in range(4):
            if ww == 7:
                ww = 0
                vacc[vv] = self.framno[ww] * 2
                vacc_oct = 1
            elif ww == 8:
                ww = 1
                vacc[vv] = self.framno[ww] * 2
                vacc_oct = 1
            if vacc_oct == 0:
                vacc[vv] = self.framno[ww]
            else:
                vacc[vv] = self.framno[ww] * 2
            ww += 2
        freq1 = vacc[0] * 2
        freq2 = vacc[1] * 2
        freq3 = vacc[2] * 2
        freq4 = vacc[3] * 2
        for i in range(0, nbech):
            val1 = pack('B', int(128.0 + amp * sin(2.0 * pi * freq1 * i / fech)))
            val2 = pack('B', int(128.0 + amp * sin(2.0 * pi * freq2 * i / fech)))
            val3 = pack('B', int(128.0 + amp * sin(2.0 * pi * freq3 * i / fech)))
            val4 = pack('B', int(128.0 + amp * sin(2.0 * pi * freq4 * i / fech)))
            monac.writeframes(val1 + val2 + val3 + val4)
        monac.close()
        p = PyAudio()
        chunk = 2048
        wf = open(self.fichacc[w], 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(chunk)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()

    # L'harmonie des accords
    def accord(self):
        if self.acc is not None:
            self.acc.destroy()
            self.btaud2.invoke()
        self.acc = Toplevel(self)
        self.acc.title('Entité Gammique : Harmonie en %s' % self.c_ii)
        self.acc.geometry('600x300+800+90')
        self.acc.protocol("WM_DELETE_WINDOW", lambda: Gammique.fermeture(self, 'accord'))
        if self.presaudio == 0:
            self.presaudio = 1
        self.btaud2.invoke()
        # Définition du style d'écriture
        fotyp = Font(family='Liberation Serif', size=12)
        fofin = Font(family='Liberation Serif', size=8)
        fonot = Font(family='Liberation Serif', size=14)
        # Fenêtrage des widgets
        fra = Frame(self.acc, width=100, height=50)
        fra.pack(side=BOTTOM)
        fraleft = Frame(self.acc, width=30, height=30)
        fraleft.pack(side=LEFT)
        fraright = Frame(self.acc, width=30, height=30)
        fraright.pack(side=RIGHT)
        # Les accords 1357 de la gamme en cours (partie gauche(left))
        Button(fra, text='Actualiser', width=20, command=lambda: self.actuac(3)).pack(side=LEFT)
        Label(fraleft, text='Accords 1357', fg='red').pack()
        btaccleft = []
        for i in range(7):
            btaccleft.append(Button(fraleft, text='', bg='light blue', width=10,
                                    command=lambda w=i: self.wavacc(w)))
            btaccleft[i].pack()
        # Les autres accords de la gamme en cours (partie droite(right))
        btferm = Button(fra, text='Fermer', width=20, bg='light grey', command=lambda: self.actuac(5))
        btferm.pack(side=RIGHT)
        Label(fraright, text='Autre accord', fg='blue').pack()
        Button(fraright, text='inactif', bg='light blue', width=10).pack()
        # L'espace blanc central pour écrire l'accord
        caaacc = Canvas(self.acc, bg='white', height=300, width=300)
        caaacc.pack()
        caaacc.delete(ALL)
        # Types d'accords 1357 : chr(248) = ( ø )
        # Majeur_7ème(maj7). Mineur_7ème(7). Demi-diminué_7ème(ø7). Diminué_7ème(°7)
        accmaj7 = [0, 0, 0, 0]
        acc7 = [0, 0, 0, -1]
        accdd7 = [0, -1, -1, -1]
        accd7 = [0, -1, -1, -2]
        tbtxgd = ['1', '3', '5', '7']
        tbacc7 = []  # Tableau de l'accord forme(str)
        tbsign = []  # Tableau de l'accord forme(int)
        tbfine = []  # Tableau des accords forme fine
        tbgene = []  # Tableau des accords forme écriture
        tblect = []  # Tableau des accords forme lecture
        # self.decore[] = altération et note tonique de l'accord
        xcc, ycc = 120, 80
        xtt = 20
        ypos = 26
        for decdegre in range(7):
            accnote = self.decore[decdegre][1:]
            accsign = self.decore[decdegre][:1]
            # self.declare[] = altérations "3.5.7" en rang
            decnote = 1
            txga = txdr = ''
            ydd = ycc + (ypos * decdegre)
            xdd = xcc + 30
            xgg = xcc - 30
            while decnote < 8:  # Définition de l'accord modal(str)
                decalt = self.declare[(decdegre, decnote)]
                tbacc7.append(decalt)
                decnote += 2
            # Transcodage de l'accord de type original(str)
            for a_ in range(4):
                z_ = -1
                a_acc = tbacc7[a_]
                for b_ in range(7):  # Lecture et transformation
                    if a_acc == '':
                        b_alt = 0
                        tbsign.append(b_alt)
                        break
                    if a_acc == self.accdiese[b_]:
                        b_alt = b_
                        tbsign.append(b_alt)
                        break
                    if a_acc == self.accbemol[z_]:
                        b_alt = z_
                        tbsign.append(b_alt)
                        break
                    z_ += -1
            # Définition des accords de 7ᵉ
            if tbsign[3] == 0:
                # L'accord est majeur 7(maj7)
                for t_ in range(4):
                    txsg = ''
                    zone = 0
                    if accmaj7[t_] == tbsign[t_]:
                        t_fin = 0
                    else:
                        t_fin = tbsign[t_] - accmaj7[t_]
                    if t_ == 1 and t_fin != 0:
                        if t_fin < -1:  # Zone de droite
                            txsg = self.accbemol[t_fin] + tbtxgd[t_]
                            zone = 1
                        elif t_fin > -1:  # Zone de droite
                            txsg = self.accdiese[t_fin] + tbtxgd[t_]
                            zone = 1
                        else:  # Zone de gauche
                            txsg = self.accbemol[t_fin]
                            zone = -1
                    if t_ == 2 and t_fin != 0:
                        if t_fin < 0:  # Zone de droite
                            txsg = self.accbemol[t_fin] + tbtxgd[t_]
                            zone = 1
                        elif t_fin > 2:  # Zone de droite
                            txsg = self.accdiese[t_fin] + tbtxgd[t_]
                            zone = 1
                        else:  # Zone de gauche
                            txsg = self.accdiese[t_fin]
                            zone = -1
                    if t_ == 3 and t_fin != 0:  # Zone de droite
                        txsg = self.accbemol[t_fin] + tbtxgd[t_]
                        zone = 1
                    if zone == 1:  # Zone de droite
                        txdr += txsg
                        caaacc.create_text(xdd, ydd, text=txsg, font=fofin, fill='blue')
                        xdd += 20
                    if zone == -1:  # Zone de gauche
                        txga += txsg
                        caaacc.create_text(xgg, ydd, text=txsg, font=fofin, fill='blue')
                        xgg -= 20
                    tbfine.append(t_fin)
                txbadr = txga + 'maj7' + txdr
                btaccleft[decdegre].configure(text=txbadr)
                caaacc.create_text(xcc, ydd, text='maj7', font=fotyp, fill='black')
                caaacc.create_text(xtt, ydd, text=accsign, font=fofin, fill='blue')
                caaacc.create_text(xtt + 20, ydd, text=accnote, font=fonot, fill='black')
            if tbsign[3] == -1:
                if (tbsign[1] or tbsign[2] >= 0) or ((tbsign[1] or tbsign[2]) < 0):
                    if tbsign[1] and tbsign[2] < 0:
                        pass
                    else:
                        # L'accord est septième mineur (7).
                        for t_ in range(4):
                            txsg = ''
                            zone = 0
                            if acc7[t_] == tbsign[t_]:
                                t_fin = 0
                            else:
                                t_fin = tbsign[t_] - acc7[t_]
                            if t_ == 1 and t_fin != 0:
                                if t_fin < -1:  # Zone de droite
                                    txsg = self.accbemol[t_fin] + tbtxgd[t_]
                                    zone = 1
                                elif t_fin > -1:  # Zone de droite
                                    txsg = self.accdiese[t_fin] + tbtxgd[t_]
                                    zone = 1
                                else:  # Zone de gauche
                                    txsg = self.accbemol[t_fin]
                                    zone = -1
                            if t_ == 2 and t_fin != 0:
                                if t_fin < 0:  # Zone de droite
                                    txsg = self.accbemol[t_fin] + tbtxgd[t_]
                                    zone = 1
                                elif t_fin > 2:  # Zone de droite
                                    txsg = self.accdiese[t_fin] + tbtxgd[t_]
                                    zone = 1
                                else:  # Zone de gauche
                                    txsg = self.accdiese[t_fin]
                                    zone = -1
                            if t_ == 3 and t_fin != 0:  # Zone de droite
                                txsg = self.accbemol[t_fin] + tbtxgd[t_]
                                zone = 1
                            if zone == 1:  # Zone de droite
                                txdr += txsg
                                caaacc.create_text(xdd, ydd, text=txsg, font=fofin, fill='blue')
                                xdd += 20
                            if zone == -1:  # Zone de gauche
                                txga += txsg
                                caaacc.create_text(xgg, ydd, text=txsg, font=fofin, fill='blue')
                                xgg -= 20
                            tbfine.append(t_fin)
                        txbadr = txga + '7' + txdr
                        btaccleft[decdegre].configure(text=txbadr)
                        caaacc.create_text(xcc, ydd, text='7', font=fotyp, fill='black')
                        caaacc.create_text(xtt, ydd, text=accsign, font=fofin, fill='blue')
                        caaacc.create_text(xtt + 20, ydd, text=accnote, font=fonot, fill='black')
            if (tbsign[3] == -1) and (tbsign[1] and tbsign[2] < 0):
                # L'accord est demi-diminué 7(ø7)
                for t_ in range(4):
                    txsg = ''
                    zone = 0
                    if accdd7[t_] == tbsign[t_]:
                        t_fin = 0
                    else:
                        t_fin = tbsign[t_] - accdd7[t_]
                    if t_ == 1 and t_fin != 0:
                        if t_fin < -1:  # Zone de droite
                            txsg = self.accbemol[t_fin] + tbtxgd[t_]
                            zone = 1
                        elif t_fin > -1:  # Zone de droite
                            txsg = self.accdiese[t_fin] + tbtxgd[t_]
                            zone = 1
                        else:  # Zone de gauche
                            txsg = self.accbemol[t_fin]
                            zone = -1
                    if t_ == 2 and t_fin != 0:
                        if t_fin < 0:  # Zone de droite
                            txsg = self.accbemol[t_fin] + tbtxgd[t_]
                            zone = 1
                        elif t_fin > 2:  # Zone de droite
                            txsg = self.accdiese[t_fin] + tbtxgd[t_]
                            zone = 1
                        else:  # Zone de gauche
                            txsg = self.accdiese[t_fin]
                            zone = -1
                    if t_ == 3 and t_fin != 0:  # Zone de droite
                        txsg = self.accbemol[t_fin] + tbtxgd[t_]
                        zone = 1
                    if zone == 1:  # Zone de droite
                        txdr += txsg
                        caaacc.create_text(xdd, ydd, text=txsg, font=fofin, fill='blue')
                        xdd += 20
                    if zone == -1:  # Zone de gauche
                        txga += txsg
                        caaacc.create_text(xgg, ydd, text=txsg, font=fofin, fill='blue')
                        xgg -= 20
                    tbfine.append(t_fin)
                    txbadr = txga + 'ø7' + txdr
                    btaccleft[decdegre].configure(text=txbadr)
                    caaacc.create_text(xcc, ydd, text='ø7', font=fotyp, fill='black')
                    caaacc.create_text(xtt, ydd, text=accsign, font=fofin, fill='blue')
                    caaacc.create_text(xtt + 20, ydd, text=accnote, font=fonot,
                                       fill='black')
            if tbsign[3] < -1:
                # L'accord est diminué 7(°7).
                for t_ in range(4):
                    txsg = ''
                    zone = 0
                    if accd7[t_] == tbsign[t_]:
                        t_fin = 0
                    else:
                        t_fin = tbsign[t_] - accd7[t_]
                    if t_ == 1 and t_fin != 0:
                        if t_fin < -1:  # Zone de droite
                            txsg = self.accbemol[t_fin] + tbtxgd[t_]
                            zone = 1
                        elif t_fin > -1:  # Zone de droite
                            txsg = self.accdiese[t_fin] + tbtxgd[t_]
                            zone = 1
                        else:  # Zone de gauche
                            txsg = self.accbemol[t_fin]
                            zone = -1
                    if t_ == 2 and t_fin != 0:
                        if t_fin < 0:  # Zone de droite
                            txsg = self.accbemol[t_fin] + tbtxgd[t_]
                            zone = 1
                        elif t_fin > 2:  # Zone de droite
                            txsg = self.accdiese[t_fin] + tbtxgd[t_]
                            zone = 1
                        else:  # Zone de gauche
                            txsg = self.accdiese[t_fin]
                            zone = -1
                    if t_ == 3 and t_fin != 0:  # Zone de droite
                        txsg = self.accbemol[t_fin] + tbtxgd[t_]
                        zone = 1
                        xdd += 20
                    if zone == 1:  # Zone de droite
                        txdr += txsg
                        caaacc.create_text(xdd, ydd, text=txsg, font=fofin, fill='blue')
                        xdd += 20
                    if zone == -1:  # Zone de gauche
                        txga += txsg
                        caaacc.create_text(xgg, ydd, text=txsg, font=fofin, fill='blue')
                        xgg -= 20
                    tbfine.append(t_fin)
                txbadr = txga + '°7' + txdr
                btaccleft[decdegre].configure(text=txbadr)
                caaacc.create_text(xcc, ydd, text='°7', font=fotyp, fill='black')
                caaacc.create_text(xtt, ydd, text=accsign, font=fofin, fill='blue')
                caaacc.create_text(xtt + 20, ydd, text=accnote, font=fonot, fill='black')
            tblect.append(tbsign[:4])
            tbgene.append(tbfine[:4])
            del (tbsign[:])  # Remise à zéro de l'accord(int)
            del (tbacc7[:])  # Remise à zéro de l'accord(str)
            del (tbfine[:])  # Remise à zéro de l'accord écriture
        del (tblect[:])  # Remise à zéro forme lecture
        del (tbgene[:])  # Remise à zéro forme écriture

    # Premiers pixels acoustiques
    def radio(self):
        ay = '0'
        ayay = self.tbdegre[0]
        for n in range(7):
            freqhtz = self.tablenotes[ayay]
            if ay == '0':
                pass
            else:
                freqhtz += 120
            ayay += 1
            if ayay > 6:
                ayay = 0
                ay = '1'
            nboctet = nbcanal = 1
            fech = 64000
            niveau = float(1 / 2)
            duree = float(1 / 6)
            nbech = int(duree * fech)
            manote = open(self.fichnom[n], 'wb')
            param = (nbcanal, nboctet, fech, nbech, 'NONE', 'NONE')
            # noinspection PyTypeChecker
            manote.setparams(param)
            amp = 127.5 * niveau
            for i in range(0, nbech):
                val = pack('B', int(128.0 + amp * sin(2.0 * pi * freqhtz * i / fech)))
                manote.writeframes(val)
            manote.close()
            p = PyAudio()
            chunk = 2048
            wf = open(self.fichnom[n], 'rb')
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(chunk)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(chunk)
            stream.stop_stream()
            stream.close()
            p.terminate()

    # Premières notes acoustiques
    def audio(self):
        la440 = 440
        la2 = la440 / 2
        fabula = ['A', '_', 'B', 'C', '_', 'D', '_', 'E', 'F', '_', 'G', '_', 'A']
        # FC # Fréquences cursives (pixels)
        notula = []
        modula = []
        for az in range(7):  # Construction tableau FC
            notula.append(self.tablenotes[az])
            mula = notula[az] / 10 - 25  # Transition vers l'indice
            modula.append(mula)  # Indice du tableau "sequla[]"
        # TM # Tableau majeur
        tabula = []
        for ai in range(13):  # Construction tableau TM
            paula = la2 * 2 ** (ai / 12)  # Calcul fréquence
            tabula.append(paula)  # Tableau en écriture TM
        # TF # Table des fréquences (1/12)
        sequla = []
        nomula = []
        yula = nula = 0
        for ay in range(40):  # Construction tableau TF
            if ay < 12:  # Niveau -1: Octave basse
                yula = tabula[ay] / 2  # yula: TM/2
                nula = fabula[ay]  # nula: Notes naturelles
            elif 11 < ay < 24:  # Niveau 0: Octave naturelle
                yula = tabula[ay - 12]  # yula: Déviation de l'indice(ay)
                nula = fabula[ay - 12]
            elif 23 < ay < 37:  # Niveau 1 : Une octave haute
                yula = tabula[ay - 24] * 2  # yula: Déviation de l'indice(ay)+TM*2
                nula = fabula[ay - 24]
            elif 36 < ay < 41:  # Niveau 2: Octave relative
                yula = tabula[ay - 36] * 4  # yula: Déviation de l'indice(ay)+TM*4
                nula = fabula[ay - 36]
            sequla.append(yula)  # Tableau en écriture TF
            nomula.append(nula)  # Tableau en écriture TF
        # TR # Tableau des résultats (fréquences cursives)
        freula = []
        for ax in range(7):  # Construction tableau TR
            xula = int(modula[ax])  # xula: Lecture indice-entier FC
            qula = sequla[xula]  # qula: Lecture de fréquence TF
            freula.append(qula)  # Tableau en écriture TR
        aw2 = self.tbdegre[0]
        diato = []
        opoto = []
        ax, aw = '0', -1
        while aw < 6:  # Construction tableau TR-tonique
            aw += 1
            freqhtz = freula[aw2]
            if ax == '0':
                diato.append(freqhtz)
            else:
                diato.append(freqhtz * 2)
            opoto.append(self.gamula[aw2])
            aw2 += 1
            if aw2 > 6:
                aw2 = 0
                ax = '1'
        # Partie échantillonnage
        nboctet = nbcanal = 1
        fech = 64000
        niveau = float(1 / 2)
        duree = float(1 / 6)
        nbech = int(duree * fech)
        for fy in range(7):
            manote = open(self.fichnom[fy], 'wb')
            param = (nbcanal, nboctet, fech, nbech, 'NONE', 'NONE')
            # noinspection PyTypeChecker
            manote.setparams(param)
            freq = diato[fy]
            self.framno[fy] = freq
            amp = 127.5 * niveau
            for i in range(0, nbech):
                val = pack('B', int(128.0 + amp * sin(2.0 * pi * freq * i / fech)))
                manote.writeframes(val)
            manote.close()
            if self.presaudio == 0:
                p = PyAudio()
                chunk = 2048
                wf = open(self.fichnom[fy], 'rb')
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)
                data = wf.readframes(chunk)
                while len(data) > 0:
                    stream.write(data)
                    data = wf.readframes(chunk)
                stream.stop_stream()
                stream.close()
                p.terminate()
        del (modula[:])
        del (tabula[:])
        del (sequla[:])
        del (nomula[:])
        del (freula[:])
        del (diato[:])

    # Les octaves du groupe RADIO
    def yoiioiioy(self):
        xradfan = self.entfan.get()
        xrad = self.variable.get()
        mqdo = self.sca[0].get()
        mqsi = self.sca[6].get()
        yo = yoc = yod = yoe = yof = yog = yoa = yob = 0
        fyoc = fyod = fyoe = fyof = fyog = fyoa = fyob = 0
        tyoc = tyod = tyoe = tyof = tyog = tyoa = tyob = 0
        topgam = [yoc, yod, yoe, yof, yog, yoa, yob]
        topform = [fyoc, fyod, fyoe, fyof, fyog, fyoa, fyob]
        topto = [tyoc, tyod, tyoe, tyof, tyog, tyoa, tyob]
        mqdo1 = mqsi1 = 0
        while yo < 7:
            yotop = topgam[yo] = int(self.sca[yo].get())
            topf = topform[yo] = self.sca[yo].cget("from")
            topt = topto[yo] = self.sca[yo].cget("to")
            if xradfan == "IOI":
                if xrad == "YOI":
                    if (mqdo > -1) and (mqsi < 1):
                        yioiy = yotop
                    else:
                        yioiy = yotop + 12
                        topf += 12
                        topt += 12
                elif xrad == "IOY":
                    if (mqdo > -1) and (mqsi < 1):
                        yioiy = yotop
                    else:
                        yioiy = yotop - 12
                        topf -= 12
                        topt -= 12
                else:
                    yioiy = yotop
            elif xradfan == "YOI":
                if xrad == "IOI":
                    if (mqdo > -1) and (mqsi < 1):
                        yioiy = yotop
                    else:
                        yioiy = yotop - 12
                        topf -= 12
                        topt -= 12
                elif xrad == "IOY":
                    if (mqdo > -1) and (mqsi < 1):
                        yioiy = yotop
                    else:
                        yioiy = yotop - 24
                        topf -= 24
                        topt -= 24
                else:
                    yioiy = yotop
            else:
                if xrad == "YOI":
                    if (mqdo > -1) and (mqsi < 1):
                        yioiy = yotop
                    else:
                        yioiy = yotop + 24
                        topf += 24
                        topt += 24
                elif xrad == "IOI":
                    if (mqdo > -1) and (mqsi < 1):
                        yioiy = yotop
                    else:
                        yioiy = yotop + 12
                        topf += 12
                        topt += 12
                else:
                    yioiy = yotop
            if yo == 0:
                mqdo1 = yioiy
            if yo == 6:
                mqsi1 = yioiy
            self.sca[yo].configure(from_=topf, to=topt)
            self.sca[yo].set(yioiy)
            yo += 1
        if xrad == "YOI":
            self.sca[7].configure(from_=0 - mqdo1, to=24 - mqsi1)
        elif xrad == "IOI":
            self.sca[7].configure(from_=-12 - mqdo1, to=12 - mqsi1)
        elif xrad == "IOY":
            self.sca[7].configure(from_=-24 - mqdo1, to=0 - mqsi1)
        xradfan = xrad
        self.entfan.delete(0, END)
        self.entfan.insert(END, xradfan)
        self.btgama.invoke()

    # Moment self.gama
    def momentgama(self, event):
        if event != '':
            self.btgama.invoke()

    # Définition des curseurs
    def scanote1(self, xc):
        do = int(xc)
        xsi = self.sca[6].get()
        xre = self.sca[1].get()
        if do < xsi:
            self.sca[6].set(do)
        if do > xre + 1:
            self.sca[1].set(do - 1)
        # Initialise sca[7](from_)
        xxrad = self.variable.get()
        if xxrad == "YOI":
            self.sca[7].configure(from_=0 - do, to=24 - xsi)
        elif xxrad == "IOI":
            self.sca[7].configure(from_=-12 - do, to=12 - xsi)
        elif xxrad == "IOY":
            self.sca[7].configure(from_=-24 - do, to=0 - xsi)
        self.bind('<ButtonRelease-1>', self.momentgama)

    def scanote2(self, xd):
        ren = int(xd)
        xdo = self.sca[0].get()
        xmi = self.sca[2].get()
        if ren < xdo - 1:
            self.sca[0].set(ren + 1)
        if ren > xmi + 1:
            self.sca[2].set(ren - 1)
        self.bind('<ButtonRelease-1>', self.momentgama)

    def scanote3(self, xe):
        mi = int(xe)
        xre = self.sca[1].get()
        xfa = self.sca[3].get()
        if mi < xre - 1:
            self.sca[1].set(mi + 1)
        if mi > xfa:
            self.sca[3].set(mi)
        self.bind('<ButtonRelease-1>', self.momentgama)

    def scanote4(self, xf):
        fa = int(xf)
        xmi = self.sca[2].get()
        xsol = self.sca[4].get()
        if fa < xmi:
            self.sca[2].set(fa)
        if fa > xsol + 1:
            self.sca[4].set(fa - 1)
        self.bind('<ButtonRelease-1>', self.momentgama)

    def scanote5(self, xg):
        sol = int(xg)
        xfa = self.sca[3].get()
        xla = self.sca[5].get()
        if sol < xfa - 1:
            self.sca[3].set(sol + 1)
        if sol > xla + 1:
            self.sca[5].set(sol - 1)
        self.bind('<ButtonRelease-1>', self.momentgama)

    def scanote6(self, xa):
        la = int(xa)
        xsol = self.sca[4].get()
        xsi = self.sca[6].get()
        if la < xsol - 1:
            self.sca[4].set(la + 1)
        if la > xsi + 1:
            self.sca[6].set(la - 1)
        self.bind('<ButtonRelease-1>', self.momentgama)

    def scanote7(self, xb):
        si = int(xb)
        xla = self.sca[5].get()
        xdo = self.sca[0].get()
        if si < xla - 1:
            self.sca[5].set(si + 1)
        if si > xdo:
            self.sca[0].set(si)
        # Initialise sca[7](from_)
        xxxrad = self.variable.get()
        if xxxrad == "YOI":
            self.sca[7].configure(from_=0 - xdo, to=24 - si)
        elif xxxrad == "IOI":
            self.sca[7].configure(from_=-12 - xdo, to=12 - si)
        elif xxxrad == "IOY":
            self.sca[7].configure(from_=-24 - xdo, to=0 - si)
        self.bind('<ButtonRelease-1>', self.momentgama)

    def scanote8(self, xh):
        sch = int(xh)
        f_t = 0
        xsi = self.sca[6].get()
        t_si = self.sca[6].cget("to")
        if xsi + sch > t_si:
            f_t = -1
        xdo = self.sca[0].get()
        fromdo = f_do = self.sca[0].cget("from")
        todo = t_do = self.sca[0].cget("to")
        if (xdo + sch < f_do) or (f_t == -1):
            fromdo = f_do + sch
            todo = t_do + sch
            f_t = -1
        xre = self.sca[1].get()
        fromre = f_re = self.sca[1].cget("from")
        tore = t_re = self.sca[1].cget("to")
        if f_t == -1:
            fromre = f_re + sch
            tore = t_re + sch
        xmi = self.sca[2].get()
        frommi = f_mi = self.sca[2].cget("from")
        tomi = t_mi = self.sca[2].cget("to")
        if f_t == -1:
            frommi = f_mi + sch
            tomi = t_mi + sch
        xfa = self.sca[3].get()
        fromfa = f_fa = self.sca[3].cget("from")
        tofa = t_fa = self.sca[3].cget("to")
        if f_t == -1:
            fromfa = f_fa + sch
            tofa = t_fa + sch
        xsol = self.sca[4].get()
        fromsol = f_sol = self.sca[4].cget("from")
        tosol = t_sol = self.sca[4].cget("to")
        if f_t == -1:
            fromsol = f_sol + sch
            tosol = t_sol + sch
        xla = self.sca[5].get()
        fromla = f_la = self.sca[5].cget("from")
        tola = t_la = self.sca[5].cget("to")
        if f_t == -1:
            fromla = f_la + sch
            tola = t_la + sch
        xsi = self.sca[6].get()
        fromsi = f_si = self.sca[6].cget("from")
        tosi = t_si = self.sca[6].cget("to")
        if (xsi + sch > t_si) or (f_t == -1):
            fromsi = f_si + sch
            tosi = t_si + sch
        # Formation des données scanote8
        self.sc_8[0] = int(xdo)
        self.sc_8[1] = int(xre)
        self.sc_8[2] = int(xmi)
        self.sc_8[3] = int(xfa)
        self.sc_8[4] = int(xsol)
        self.sc_8[5] = int(xla)
        self.sc_8[6] = int(xsi)
        self.fr_8[0] = fromdo
        self.fr_8[1] = fromre
        self.fr_8[2] = frommi
        self.fr_8[3] = fromfa
        self.fr_8[4] = fromsol
        self.fr_8[5] = fromla
        self.fr_8[6] = fromsi
        self.to_8[0] = todo
        self.to_8[1] = tore
        self.to_8[2] = tomi
        self.to_8[3] = tofa
        self.to_8[4] = tosol
        self.to_8[5] = tola
        self.to_8[6] = tosi
        for i in range(7):
            self.sca[i].configure(from_=self.fr_8[i], to=self.to_8[i])
            self.sca[i].set(self.sc_8[i] + sch)
        cb_ = self.cb_chk.get()
        if cb_ == 1:
            self.cbchk8.invoke()
        self.bind('<ButtonRelease-1>', self.momentgama)

    # La gamme naturelle
    def zero(self):
        for z in range(7):
            self.sca[z].configure(from_=self.fnotes[z], to=self.tnotes[z])
            self.sca[z].set(0)
        self.sca[7].configure(from_=-12, to=12)
        self.sca[7].set(0)
        self.cbchk8.deselect()
        self.rad[1].invoke()  # Remise à l'octave zéro ou "ioi"
        if self.chm is not None:
            self.chm.destroy()
        self.btgama.invoke()

    # Motorisation Gammique
    def gama(self):
        (lineno(), 'GGV6 def gama : \n', self.data.keys())
        imod = None
        gammes, gamnoms = [], []
        self.decore.clear()  # Remise au zéro tonique des accords
        self.can.delete(ALL)
        # Tracé d'encadrement
        # Données de l'encadré : Axes(x,y)=365(x),220(y)
        self.can.create_line(10, 450, 740, 450, fill='blue')
        self.can.create_line(390, 220, 520, 220, fill='green')
        self.can.create_line(270, 340, 400, 340, fill='red')
        self.can.create_line(510, 100, 640, 100, fill='blue')
        if self.gamclas or not self.gamcalc and not self.gamclas:
            # Nombres d'intervalles des gammes et les diatoniques surnommées
            gammes = [[1, 1, 0, 1, 1, 1, 0], [0, 2, 0, 1, 1, 1, 0], [2, 0, 0, 1, 1, 1, 0], [4, 0, 0, 0, 0, 1, 0],
                      [1, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [1, 0, 3, 0, 0, 1, 0], [1, 2, 1, 0, 0, 1, 0],
                      [2, 2, 0, 0, 0, 1, 0], [0, 0, 1, 2, 1, 1, 0], [1, 3, 0, 0, 0, 1, 0], [0, 0, 2, 1, 1, 1, 0],
                      [1, 2, 2, 0, 0, 0, 0], [0, 0, 4, 0, 0, 1, 0], [1, 4, 0, 0, 0, 0, 0], [1, 0, 0, 2, 1, 1, 0],
                      [0, 1, 0, 2, 1, 1, 0], [1, 1, 3, 0, 0, 0, 0], [0, 0, 0, 3, 1, 1, 0], [1, 1, 0, 0, 2, 1, 0],
                      [0, 2, 0, 0, 2, 1, 0], [0, 2, 0, 2, 0, 1, 0], [2, 0, 0, 0, 2, 1, 0], [1, 0, 1, 0, 2, 1, 0],
                      [1, 0, 1, 2, 0, 1, 0], [1, 1, 1, 2, 0, 0, 0], [2, 0, 0, 3, 0, 0, 0], [0, 0, 2, 0, 2, 1, 0],
                      [1, 2, 0, 2, 0, 0, 0], [1, 0, 0, 3, 0, 1, 0], [1, 0, 0, 1, 2, 1, 0], [1, 1, 0, 3, 0, 0, 0],
                      [1, 1, 2, 1, 0, 0, 0], [0, 1, 0, 0, 3, 1, 0], [0, 0, 1, 0, 3, 1, 0], [0, 0, 0, 1, 3, 1, 0],
                      [0, 0, 0, 2, 2, 1, 0], [1, 0, 0, 0, 3, 1, 0], [0, 0, 2, 2, 0, 1, 0], [0, 0, 0, 0, 4, 1, 0],
                      [0, 0, 2, 3, 0, 0, 0], [1, 0, 0, 4, 0, 0, 0], [0, 0, 0, 5, 0, 0, 0], [1, 1, 0, 1, 0, 2, 0],
                      [1, 1, 0, 1, 2, 0, 0], [0, 2, 0, 1, 0, 2, 0], [0, 2, 0, 1, 2, 0, 0], [2, 0, 0, 1, 0, 2, 0],
                      [2, 0, 0, 1, 2, 0, 0], [1, 0, 1, 1, 0, 2, 0], [1, 0, 1, 1, 2, 0, 0], [1, 1, 0, 0, 1, 2, 0],
                      [1, 1, 0, 0, 3, 0, 0], [1, 1, 0, 2, 1, 0, 0], [1, 1, 2, 0, 1, 0, 0], [0, 2, 0, 0, 0, 3, 0],
                      [1, 0, 0, 2, 2, 0, 0], [1, 0, 0, 1, 0, 3, 0], [1, 3, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 3, 0],
                      [0, 0, 0, 3, 0, 2, 0], [0, 0, 2, 1, 2, 0, 0], [1, 0, 0, 0, 0, 4, 0], [0, 0, 0, 3, 2, 0, 0],
                      [1, 1, 0, 0, 0, 3, 0], [3, 0, 0, 0, 0, 2, 0]]
            # Tonice(0). Tonale(1:3). Mélode(4:14). Médiane(15:18). Domine(19:42). Harmone(43:65)
            gamnoms = ['Maj', '-2', '+2', '^2', '-3', '-32', 'x43-', '+34', 'x32+', '-43', 'x3', 'o3', '+34x',
                       'x43o', '^3', '-4', '-42', '^4', 'o4', '-5', '-52', '+52-', '+25-', '-53', '+53-',
                       'x54+', 'x52+', 'o35-', 'x53+', '+54-', '-54', 'x5', 'x45+', 'o52-', 'o53-', 'o54-',
                       'o45-', 'o5', '+53o', '*5', 'x53o', 'x54-', 'x54o', '-6', '+6', '-62', '+62-', '+26-',
                       '+26', '-63', '+63-', '-65', '+65-', '+56', 'x46+', 'o62-', '+64-', 'o64-', 'x36+',
                       'o65-', 'o46-', '+63o', '*6', '+64o', 'o6', 'x26-']
        if self.gamcalc:
            gammes = list(self.data[1].values())
            gamnoms = list(self.data[1].keys())
            # print(lineno(), gammes)
            # print(lineno(), 'GGV6 DATA 2 : \n', self.data[1])
        (lineno(), 'self.gamcalc', gamnoms)
        self.gammescopie = gammes.copy()
        self.gamnomscopie = gamnoms.copy()
        # dic_assemble = Rafraichir le dictionnaire transfert avec changement (classique, calculée)
        dic_assemble = {}
        for gg in range(len(gammes)):
            dic_assemble[gamnoms[gg]] = gammes[gg]
        (lineno(), 'GGV6/dic_assemble:', dic_assemble.keys())

        # Récupération des notes cursives
        xxx = 0
        xxrad0 = self.variable.get()
        if xxrad0 == "YOI":
            xxx = +120
        elif xxrad0 == "IOI":
            xxx = 0
        elif xxrad0 == "IOY":
            xxx = -120

        ydo = self.sca[0].get()
        xcpos_ = 400 - xxx
        ycpos_ = 220 + xxx
        xc_ = xcpos_ + (ydo * 10)
        yc_ = ycpos_ - (ydo * 10)
        rc_ = 5
        self.tablenotes[0] = int(xc_)
        self.tablehaute[0] = int(yc_)
        self.can.create_line(xc_, 350, xc_, 40, fill='black')
        self.can.create_oval(xc_ - rc_, yc_ - rc_, xc_ + rc_, yc_ + rc_, fill='black')
        yre = self.sca[1].get()
        xcpos_ = 420 - xxx
        ycpos_ = 220 + xxx
        xd_ = xcpos_ + (yre * 10)
        yd_ = ycpos_ - (yre * 10)
        rd_ = 5
        self.tablenotes[1] = int(xd_)
        self.tablehaute[1] = int(yd_)
        self.can.create_line(xd_, 360, xd_, 50, fill='green')
        self.can.create_oval(xd_ - rd_, yd_ - rd_, xd_ + rd_, yd_ + rd_, fill='green')
        ymi = self.sca[2].get()
        xcpos_ = 440 - xxx
        ycpos_ = 220 + xxx
        xe_ = xcpos_ + (ymi * 10)
        ye_ = ycpos_ - (ymi * 10)
        re_ = 5
        self.tablenotes[2] = int(xe_)
        self.tablehaute[2] = int(ye_)
        self.can.create_line(xe_, 370, xe_, 60, fill='blue')
        self.can.create_oval(xe_ - re_, ye_ - re_, xe_ + re_, ye_ + re_, fill='blue')
        yfa = self.sca[3].get()
        xcpos_ = 450 - xxx
        ycpos_ = 220 + xxx
        xf_ = xcpos_ + (yfa * 10)
        yf_ = ycpos_ - (yfa * 10)
        rf_ = 5
        self.tablenotes[3] = int(xf_)
        self.tablehaute[3] = int(yf_)
        self.can.create_line(xf_, 370, xf_, 60, fill='grey')
        self.can.create_oval(xf_ - rf_, yf_ - rf_, xf_ + rf_, yf_ + rf_, fill='grey')
        ysol = self.sca[4].get()
        xcpos_ = 470 - xxx
        ycpos_ = 220 + xxx
        xg_ = xcpos_ + (ysol * 10)
        yg_ = ycpos_ - (ysol * 10)
        rg_ = 5
        self.tablenotes[4] = int(xg_)
        self.tablehaute[4] = int(yg_)
        self.can.create_line(xg_, 380, xg_, 70, fill='red')
        self.can.create_oval(xg_ - rg_, yg_ - rg_, xg_ + rg_, yg_ + rg_, fill='red')
        yla = self.sca[5].get()
        xcpos_ = 490 - xxx
        ycpos_ = 220 + xxx
        xa_ = xcpos_ + (yla * 10)
        ya_ = ycpos_ - (yla * 10)
        ra_ = 5
        self.tablenotes[5] = int(xa_)
        self.tablehaute[5] = int(ya_)
        self.can.create_line(xa_, 390, xa_, 80, fill='orange')
        self.can.create_oval(xa_ - ra_, ya_ - ra_, xa_ + ra_, ya_ + ra_, fill='orange')
        ysi = self.sca[6].get()
        xcpos_ = 510 - xxx
        ycpos_ = 220 + xxx
        xb_ = xcpos_ + (ysi * 10)
        yb_ = ycpos_ - (ysi * 10)
        rb_ = 5
        self.tablenotes[6] = int(xb_)
        self.tablehaute[6] = int(yb_)
        self.can.create_line(xb_, 400, xb_, 90, fill='yellow')
        self.can.create_oval(xb_ - rb_, yb_ - rb_, xb_ + rb_, yb_ + rb_, fill='yellow')

        # Mesure de l'intervalle tempéré
        c1 = (yre + 1) - ydo
        d2 = (ymi + 1) - yre
        e3 = yfa - ymi
        f4 = (ysol + 1) - yfa
        g5 = (yla + 1) - ysol
        a6 = (ysi + 1) - yla
        b7 = i = cum_diat = x = 0
        diata = [c1, d2, e3, f4, g5, a6, b7]
        while i < 6:
            cum_diat += diata[i]
            i += 1
        diata[i] = 5 - cum_diat

        # Recherche diatonique par l'itération
        cc1 = dd2 = ee3 = ff4 = gg5 = aa6 = bb7 = degre = 0
        diata2 = [cc1, dd2, ee3, ff4, gg5, aa6, bb7]
        myx2 = 0
        while x < 7:
            m = x
            y = 0
            while y < 7:  # Une tonalité modale / tour
                diata2[y] = diata[m]
                y += 1
                m += 1
                if m > 6:
                    m = 0
            myx = myx2 = 0
            for my in gammes:  # Comparaison tonale / table gammes
                if diata2 == my:
                    degre = x
                    myx2 = myx
                    x = 7
                myx += 1
            x += 1
        # Ici : diata(original cursif).degre(tonique).my(gamme)

        # Définition diatonique
        # GMAJ= gammes[0]
        gmaj = [1, 1, 0, 1, 1, 1, 0]  # Forme majeure simplifiée
        # GNAT= Ordre cursif comme diata[]
        gnat = ['C', 'D', 'E', 'F', 'G', 'A', 'B']  # Forme alphabétique
        cnat = ['', '', '', '', '', '', '']
        # Niveaux d'altérations
        self.nordiese = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^',
                         '+^^^^', 'x^^^^', '^^^^^', '+^^^^^', 'x^^^^^', '^^^^^^', '+^^^^^^', 'x^^^^^^', '^^^^^^^',
                         '+^^^^^^^', 'x^^^^^^^', '^^^^^^^^', '25(#)', '26(#)', '27(#)', '28(#)', '29(#)', '30(#)',
                         '31(#)', '32(#)']
        self.subemol = ['', '32(b)', '31(b)', '30(b)', '29(b)', '28(b)', '27(b)', '26(b)', '25(b)', '********',
                        'o*******', '-*******', '*******', 'o******', '-******', '******', 'o*****', '-*****', '*****',
                        'o****', '-****', '****', 'o***', '-***', '***', 'o**', '-**', '**', 'o*', '-*', '*',
                        'o', '-']
        # Configuration modale
        gdeg = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
        # Définition du style d'écriture
        font100 = Font(family='Liberation Serif', size=9)
        font2 = Font(family='Liberation Serif', size=12)
        # Définition des notes cursives
        self.cursifs = [ydo, yre, ymi, yfa, ysol, yla, ysi]
        ynat = ymod = 0
        for ycurs in self.cursifs:
            ycurs = int(ycurs)
            if ycurs > 0:
                ymod = self.nordiese[ycurs]
            if ycurs < 0:
                ymod = self.subemol[ycurs]
            if ycurs == 0:
                ymod = self.subemol[ycurs]
            cnat[ynat] = ymod
            ynat += 1
        # (lineno(), 'cnat:', cnat)

        # Une tournée produit une tonalité modale de 7 notes
        nat2 = degre
        deg = nom = 0
        ynote = xgdeg = 30
        ytone = 50
        tt_deg, tt_gam, tt_nom, tt_ind = [], '', '', 0
        while deg < 7:
            nat = deg  # Degré tonal en question
            cri = gimj = maj = 0
            xdeg, cnom = 80, ''
            '''text0 = gdeg[deg]  # text0 = I, II, III, IV, V, VI, VII
            self.can.create_text(xgdeg + 25, ynote + 10, text=text0, font='bold', fill='black')'''
            while maj < 7:  # Tonalité modale du degré
                gmj = gmaj[maj]  # Forme majeure (1101110)
                imaj = diata2[nat]  # Forme modale (DIATA[DEGRE])
                ynt = cnat[nat2]  # Forme altérative des notes
                gnt = gnat[nat2]  # Forme tonale (CDEFGAB)
                cri += gimj  # Tonalité cumulée
                gimj = imaj - gmj  # Calcul tonal PAS/PAS
                cmod = gmod = cri
                if maj == 0:
                    yntgnt = ynt, gnt
                    self.decore[deg] = yntgnt
                    (lineno(), 'decore', deg, self.decore[deg])
                if gmod > 0:  # Forme altérative des tonalités
                    imod = self.nordiese[cmod]
                if gmod < 0:
                    imod = self.subemol[cmod]
                if gmod == 0:
                    imod = self.subemol[cmod]
                gmod += cri  # Transition tonale
                # Construction du nom de la gamme
                if nom == 0:  # Degré tonique de la gamme
                    ynom = ynt
                    gnom = gnt
                    tnom = "{}{}".format(gnom, gamnoms[myx2])
                    (lineno(), 'tnom:', tnom)
                    if ynom:  # Altération de la note
                        for yn in ynom:
                            cnom += yn
                        if tnom[-1:] == '0':  # En plus la gamme est majeure
                            cnom += tnom[:-1] + ' maj'
                        else:  # La note est altérée et elle n'est pas majeure
                            cnom += gnom + ' ' + gamnoms[myx2]
                    elif tnom[-1:] == '0':  # La gamme est majeure
                        cnom = tnom[:-1] + ' maj'
                    else:  # La note n'est pas altérée et la gamme n'est pas majeure
                        cnom = gnom + ' ' + gamnoms[myx2]
                    self.c_ii = cnom
                    self.sel_yes = ynom, tnom  # Report nom vers sélection
                    self.sel_myx[0] = myx2  # Report type vers sélection
                    # Décryptage du nom pour trouver les noms[entiers/décimaux] des modes diatoniques
                    if maj == deg == 0:
                        (lineno(), 'self.sel_yes:', self.sel_yes)
                        for tt in self.sel_yes[1]:
                            if tt not in self.gamula:
                                tt_nom += tt
                        tt_ind = 66 - self.gamnomscopie.index(tt_nom)  # Numéro de la gamme
                    (lineno(), 'Décrypte nom:', tt_nom, 'tt_ind:', tt_ind, ';')
                    self.can.create_text(40, 12, text=cnom, font=font2, fill='black')  # Nom de la gamme
                    (lineno(), 'Analise Général Texte', self.sel_yes, '|:', nom, ':Y|nom|T:', tnom)
                    # 3053 Analise Général Texte ('', 'CMaj') |: 0 :Y|nom|T: CMaj
                nat += 1
                nat2 += 1
                if nat > 6:
                    nat = 0
                if nat2 > 6:
                    nat2 = 0
                maj += 1
                text1 = gnt
                text2 = "{}{}".format(imod, maj)
                self.can.create_text(xdeg, ynote - 12, text=ynt, font=font100, fill='red')  # Altérations sur les notes
                self.can.create_text(xdeg, ynote, text=text1, font='bold')
                self.can.create_text(xdeg, ytone, text=text2, fill='blue')
                (lineno(), 'Analise Général Texte', self.sel_yes, imod, 'maj:', maj)
                xdeg += 30
                nom = 1
                self.declare[(deg, maj)] = imod
                self.dechire[(deg, maj)] = cmod  # Utilisation chromatique
            text0 = gdeg[deg]  # text0 = Degrés = I, II, III, IV, V, VI, VII
            if tt_ind == 0:
                tt_ind = 66
            nom_mode = self.data[7][tt_ind, text0]
            for nm in nom_mode:
                if nm:
                    text0 += ' ' + nm[1]
                (lineno(), 'nm:', nm[1])
                break
            (lineno(), ':', tt_ind, text0, ':', )  # self.data[7] [tt_ind, text0]
            self.can.create_text(xgdeg + 7, ynote + 10, text=text0, font=font100, fill='blue')
            (lineno(), 'declare imod ', self.declare)
            (lineno(), 'dechire cmod ', self.dechire)
            ynote += 60
            ytone += 60
            nat2 += 1
            if nat2 > 6:
                nat2 = 0
            deg += 1
        self.tbdegre[0] = degre
        ouvertes = [self.ccc, self.ttt, self.tur, self.chm, self.acc]
        boutons = [self.btcom, self.bttet, self.bttab,
                   self.btchr, self.btacc]
        for ouvert in ouvertes:
            if ouvert:
                b5 = boutons[ouvertes.index(ouvert)]
                b5.invoke()
        # print(lineno(), self.c_ii)
        (lineno(), 'GGV6/dic_assemble[Maj]:', dic_assemble['Maj'], dic_assemble.keys())
        # 3087 GGV6/dic_assemble[Maj]: [1, 1, 0, 1, 1, 1, 0] dict_keys(['Maj', '-2', '+2', '^2', '-3',
        # '-32', 'x43-', '+34', 'x32+', '-43', 'x3', 'o3', '+34x', 'x43o', '^3', '-4', '-42', '^4', 'o4',
        # '-5', '-52', '+52-', '+25-', '-53', '+53-', 'x54+', 'x52+', 'o35-', 'x53+', '+54-', '-54', 'x5',
        # 'x45+', 'o52-', 'o53-', 'o54-', 'o45-', 'o5', '+53o', '*5', 'x53o', 'x54-', 'x54o', '-6', '+6', '-62',
        # '+62-', '+26-', '+26', '-63', '+63-', '-65', '+65-', '+56', 'x46+', 'o62-', '+64-', 'o64-', 'x36+',
        # 'o65-', 'o46-', '+63o', '*6', '+64o', 'o6', 'x26-'])
        progam_simis.simili(dic_assemble, self.data, self.c_ii)

    gamme0 = {}
    globe0, galop, essor = [], {}, {}


class Commatique(Frame):
    """Branchement Commique"""

    def __init__(self):
        Frame.__init__(self)
        self.c_bb = []
        self.c_cc = []
        self.coo_gam = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.ctpier = self.ccnbase = self.ccn_bout = self.copier = self.cop_bout = None
        self.ctb_form = None  # Table originale
        self.f_bs = Font(family='Arial', size=8)
        self.f_bt = Font(family='Arial', size=7)
        self.f_bu = Font(family='Arial', size=8, weight='bold')
        self.f_bv = Font(family='Arial', size=6)
        # Dictionnarisation de l'ordre chromatique ascendant.
        self.normal = {}  # Dictionnaire des tonalités chromatiques en ordre ascendant(normal).

    def brnch_1(self, c_oo, c_pp, c_iii, s_cal):
        """Réception des gammes calculées :
            c_oo = Modes diatoniques calculés + Chromes analogues (sup/inf)
            c_pp = Modes diatoniques calculés + Chromes numériques (sup/inf)
            c_iii = Nom de la gamme 'Note + Valeur'
            s_cal = Taux de dénivellation des degrés pour commatisme"""
        (lineno(), '2665-brnch_1-c_oo', type(c_oo), c_oo[0][0][0], '\n')
        (lineno(), '2665-brnch_1-c_pp', type(c_pp), c_pp[0][0][0])
        (lineno(), '2665-brnch_1-c_iii', type(c_iii), c_iii, 'Long:', len(c_iii), 'SCA:', s_cal)
        if self.ctpier is not None:
            self.ctpier.destroy()
        self.ctpier = Toplevel(self)
        self.ctpier.title('Entités Commatiques du Chromatisme en  %s' % c_iii)
        self.ctpier.geometry('900x900+150+100')
        # Écriture chromatique de la gamme en cours (les formules (ana/num)
        self.ccnbase = Canvas(self.ctpier, bg='Ivory', height=800, width=600)
        self.ccnbase.pack(padx=13, side="left")  # ccnbase = Premier Canvas original (pack_forget ou pas)
        self.ccnbase.delete(ALL)
        # Empilement des boutons communs aux noms composés (notes non-couplées ou isolées)
        self.ccn_bout = Canvas(self.ctpier, bg='Ivory', height=800, width=100)
        self.ccn_bout.pack(expand=True)  # ccn_bout = Second Canvas original pour les boutons
        self.ccn_bout.delete(ALL)
        c_ii2 = "{}{}".format('Commatismes en cours : ', str(c_iii))
        self.ccnbase.create_text(112, 8, font=self.f_bt, text=c_ii2, fill='blue')
        if s_cal == 0:
            s_cal = 12
            (lineno(), 'Scalaire:', s_cal)
        #
        if isinstance(c_iii, str):
            '''Premier modèle des paramètres'''
            self.c_bb = []
            self.c_cc = []
            self.ctb_form = [], [], [], [], [], [], [], [], [], [], [], []
            for i in range(12):
                self.c_bb.append(c_oo[0][i][0][:12])  # Formes analogiques
                self.c_cc.append(c_pp[0][i][0][:12])  # Formes numériques
                (lineno(), 'self.c_bb[0]:', self.c_bb[0], 'Longueur =', len(self.c_bb[0]))
                (lineno(), 'c_cc:', c_pp[0][i][0][:12], 'Longueur =', len(c_pp[0][i][0][:12]))
            # Formation self.ctb_form pour self.normal
            self.ctb_form = [], [], [], [], [], [], [], [], [], [], [], []
            for i in range(12):
                c_rop = []
                for j in range(12):
                    c_rop2 = self.c_cc[i][j][0][2]  # Formule inter modale : ('', 1). ('+', 1)...
                    c_rop.append(c_rop2)
                self.ctb_form[i].append(c_rop)
                (lineno(), 'GGV6/ self.ctb_form[i]:', self.ctb_form[i])
            # Dictionnaire des tonalités chromatiques en ordre ascendant(self.normal).
            for i in range(12):
                self.normal[i] = self.ctb_form[i][0]
                (lineno(), 'i    \t:', i, self.ctb_form[i][0])  # , 'ctb_form[i]')
                '''3120 i    	: 0 ['1', '+1', '2', '+2', '3', '4', '+4', '5', '+5', '6', '+6', '7']/...'''
            clo_bb, clo_normal = self.c_bb[0], self.normal.copy()
        else:
            (lineno(), 'Paramètres déclarés à la fonction def brnch_1')
            clo_bb, clo_normal = c_oo, c_pp.copy()

        # Appel à la fonction de mise en forme commatique
        (lineno(), 'GGV6/', clo_bb, '\nc_iii:', c_iii, '\nclo_normal:', clo_normal, s_cal)
        topo_com = progam_chrom.chromatic(clo_bb, c_iii, clo_normal, s_cal)
        (lineno(), 'self.c_bb[0]:', self.c_bb[0], 'Longueur =', len(self.c_bb[0]))
        '''3127 self.c_bb[0]: ([('', 'C')], [(('+', 'C'), ('-', 'D'))], [('', 'D')], [(('+', 'D'), ('-', 'E'))], 
        [('', 'E')], [('', 'F')], [(('+', 'F'), ('-', 'G'))], [('', 'G')], [(('+', 'G'), ('-', 'A'))], [('', 'A')], 
        [(('+', 'A'), ('-', 'B'))], [('', 'B')]) Longueur = 12'''
        (lineno(), 'c_iii:', c_iii, 'Longueur =', len(c_iii))
        '''3131 c_iii: [[12, '-DG-A', ('C Maj', 1)]] Longueur = 1'''
        (lineno(), 'self.normal:', self.normal, 'Longueur =', len(self.normal))
        '''3133 self.normal: {0: ['1', '+1', '2', '+2', '3', '4', '+4', '5', '+5', '6', '+6', '7']/...'''
        print(lineno(), 'GGV6/topo_com0:', topo_com[0], '\n1:', topo_com[1], '\n2:', topo_com[2], '\n:', topo_com)
        '''Retour topo_com =
            topo_com[0] = Dictionnaire global des 12 premiers modes toniques commas.[dic_com]
                Tracer les premiers modes, car il s'agit de la première inspection (None).
            topo_com[1] = Dictionnaire des clefs sans doublons.[tab_nom]
            topo_com[2] = Dictionnaire des clefs qu'avec les doublons.[tab_cop]'''

        '''# Écriture sur canvas ccnbase'''
        tab_top, gam_top, cle_top0 = {}, ['C', 'D', 'E', 'F', 'G', 'A', 'B'], []
        c_rop7, c_rop9, c_rop10, pin_rop, est_rop = [], [], '', [], []
        '''####################################################"'''
        # c_rop7 = Clefs | c_rop9 = Index | est_rop = Noms
        # Détecter les modes commatiques en double
        for cle, d_k in topo_com[0].items():
            c_rop7.append(cle[1])
            (lineno(), 'd_k[0]:', d_k[0], cle, 'est_rop:', est_rop)
            if d_k[0] not in est_rop:
                est_rop.append(d_k[0])
                pin_rop.append(d_k[0])
                (lineno(), 'd_k:', d_k[0])
            else:
                c_rop9.append(cle[1])
                c_rop10 = 'DOUBLON : ' + d_k[0]
                pin_rop.append(c_rop10)
                (lineno(), 'DOUBLON c_rop10:', c_rop10, 'c_rop7:', c_rop7)
        (lineno(), pin_rop)
        '''####################################################"'''
        for i in range(12):
            tab_top[i] = []  # Un nouveau tableau à chaque fois
            # Trouver la correspondance avec 'i' parmi les clés de topo_com[0]
            for k_top in topo_com[0].keys():
                (lineno(), 'k_top:', k_top)
                if i in k_top:
                    cle_top0 = k_top
                    iso_top = topo_com[0][cle_top0][0]
                    itou = ''
                    for i_t in iso_top:
                        if i_t in gam_top:  # i_t = Note naturelle diatonique
                            itou += i_t
                            tab_top[i].append(itou)
                            itou = ''
                        else:
                            itou += i_t
                    (lineno(), 'i:', i, 'tab_top:', tab_top[i])
                    (lineno(), 'iso_top:', iso_top, 'cle_top0:', cle_top0)
                    break
            if i in c_rop7:
                (lineno(), 'i:', i, cle_top0, 'topo_com:', topo_com[0][cle_top0][0])
                c_i = i * 60
                c_x, c_y = 30, 60
                (lineno(), 'i:', i)
                for j in range(12):
                    c_j = j * 30
                    c_rop2 = topo_com[0][cle_top0][1][j]  # Valeur numérique de la tonalité supérieure
                    self.ccnbase.create_text(c_x + c_j, c_y + c_i - 20, font=self.f_bt, text=c_rop2, fill='olive')
                    (lineno(), 'C_Rop2:', c_rop2)  # c_rop2 = Valeur numérique de la tonalité
                    if topo_com[0][cle_top0][2][j] == topo_com[0][cle_top0][3][j]:
                        c_rip0 = topo_com[0][cle_top0][3][j]  # Signal augmenté : 0. ('+C')...
                        self.ccnbase.create_text(c_x + c_j, c_y + c_i, font=self.f_bu, text=c_rip0, fill='black')
                        (lineno(), 'C_Rip0:', c_rip0, tab_top[i], i)  # c_rip0 = Altération sur la note (gamme)
                    elif topo_com[0][cle_top0][2][j] != topo_com[0][cle_top0][3][j]:
                        c_rip1 = topo_com[0][cle_top0][2][j]  # Balance mineure : 0. ('-D')...
                        c_rip2 = topo_com[0][cle_top0][3][j]  # Signal augmenté : 0. ('+C')...
                        self.ccnbase.create_text(c_x + c_j, c_y + c_i - 5, font=self.f_bv, text=c_rip1, fill='red')
                        self.ccnbase.create_text(c_x + c_j, c_y + c_i + 5, font=self.f_bv, text=c_rip2, fill='blue')
                        (lineno(), 'C_Rip1:', c_rip1, i)  # Note chromatique du rang supérieur('-D')
                        (lineno(), 'C_Rip2:', c_rip2, i)  # Note chromatique du rang inférieur('+C')
                    c_rop2 = topo_com[0][cle_top0][4][j]   # Valeur numérique de la tonalité inférieure
                    self.ccnbase.create_text(c_x + c_j, c_y + c_i + 20, font=self.f_bt, text=c_rop2, fill='olive')
                    (lineno(), 'C_Rop2:', c_rop2)  # c_rop2 = Valeur numérique de la tonalité
                if i in c_rop9:
                    self.ccnbase.create_text(c_x + 450, c_y + c_i, font=self.f_bu, text=c_rop10, fill='red')
                    (lineno(), 'i:', i, topo_com[0][cle_top0])
                else:
                    self.ccnbase.create_text(c_x + 450, c_y + c_i, font=self.f_bu, text=topo_com[0][cle_top0][0],
                                             fill='black')

        '''Créer des boutons de développement diatonique des commas toniques, via la fonction commatic.'''
        for pr in range(len(pin_rop)):
            if 'DOUBLON' not in pin_rop[pr]:
                pin_rop[pr] = Button(self.ccn_bout, text=pin_rop[pr], height=1, width=60, bg='lightblue',
                                     command=lambda m=pin_rop[pr]:
                                     progam_micro.Comique.commatic(self, s_cal, topo_com, m))
                pin_rop[pr].pack(pady=6, padx=6)
        pin_rop.clear()
        (lineno(), topo_com[0], '\n ***', topo_com[1], '\n ***', topo_com[2])
        # Bien détailler les gammes (heptatoniques et chromatiques !)
        # self.c_bb[0] = Mode tonique en cours len(1)=hepta et len(2)=chroma
        # c_iii = Nom de la gamme en cours
        # self.normal = Tonalité numérique en cours
        (lineno(), 'Pied de page', 'self.c_bb[0]', self.c_bb[0], 'Scalaire:', s_cal)

# class Gammique
# Gammique().mainloop()


'''canvas.create_line((50, 50), (100, 100), width=4, fill='red')'''
