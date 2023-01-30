#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Le vendredi 30 décembre 2022 (Commencement du script)
# GlobGamMicro : Construire les micro-intervalles sous-jacents à l'original[]

from tkinter import *
from tkinter.font import Font
import inspect
from typing import Callable

import GlobGamVers6
progam_vers6 = GlobGamVers6

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

tab_sup = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^', '+^^^^', 'x^^^^',
           '^^^^^', '+^^^^^', 'x^^^^^', '^^^^^^', '+^^^^^^', 'x^^^^^^', '^^^^^^^', '+^^^^^^^', 'x^^^^^^^', '^^^^^^^^']
tab_inf = ['', '-', 'o', '*', '-*', 'o*', '**', '-**', 'o**', '***', '-***', 'o***', '****', '-****', 'o****',
           '*****', '-*****', 'o*****', '******', '-******', 'o******', '*******', '-*******', 'o*******', '********']


class Comique(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.copier = self.cop_bout = None
        self.f_bt = Font(family='Arial', size=7)
        self.f_bu = Font(family='Arial', size=8, weight='bold')
        self.f_bv = Font(family='Arial', size=6)

    def commatic(self, scale, comic, choix):
        """Partie du développement diatonique de la gamme commatique.
            Scale... = Niveau d'inversion et suivi du traçage
            comic[0] = Dictionnaire global avec les formules (numériques, analogiques)
            comic[1] = Dictionnaire sans doublons (Clés pour dico global)
            comic[2] = Dictionnaire pour les doublons (Clés pour dico global)
            Choix... = Nom abrégé de l'ensemble des analogies isolées
        Cette fonction rassemble les éléments utiles à la création de nouveaux modes commatiques,
        ses paramètres nous indiquent qu'on a :
            2 modes analogiques chromatiques.
            2 modes numériques chromatiques.
                Il faut développer les douze modes diatoniques des 4 modes.
        Au sujet de la tonalité diatonique de la gamme commatique, il y a de nombreux cas de gammes
        qui ne comportent que deux notes isolées :
            Les notes isolées appartiennent à la gamme, car le couple est normalement chromatique.
            Mais on peut ajouter la tonique même s'il s'agit d'un couple.
            On peut aussi rajouter la septième majeure puisqu'elle est spécifique aux gammes fondamentales."""
        if self.copier is not None:
            self.copier.destroy()
        self.copier = Toplevel(self)
        self.copier.title('Entité Diatonique du Commatisme en  %s' % choix)
        self.copier.geometry('800x900+1060+100')
        self.cop_bout = Canvas(self.copier, bg='Ivory', height=800, width=500)
        self.cop_bout.pack(expand=True, padx=6)  # cop_bout = Second Canvas original pour les boutons
        self.cop_bout.delete(ALL)
        tracer, gamme, mode = [], ['C', 'D', 'E', 'F', 'G', 'A', 'B'], []
        (lineno(), 'comic1:', comic[1].values(), '\n0:', comic[0].values(), choix)
        mod_com, mod_ton1, mod_ton2, t_ion = [], '', '', ''  # mod_ton1.2 = Les toniques de la tonalité
        '''# Capter les formes tonales analogiques et numériques'''
        '''if 'DOUBLON' in choix:              # Choix du bouton appuyé qui détient la clé des formules
            for ion in comic[0].values():   # Aucun bouton avec le libellé DOUBLON n'a été programmé
                t_ion = tuple(ion[0])       # Voir GlobGamVers6 Ligne(3217): if 'DOUBLON' not in pin_rop[pr]:
                mod_com = comic[0][t_ion]
                mod_ton1 = mod_com[2][0]
                mod_ton2 = mod_com[3][0]
                print(lineno(), 't_ion DOUBLON:', mod_com, ', len:', len(mod_com), 't_ion:', t_ion)'''
        '''50 t_ion DOUBLON: ['CDEFGAB', ['1', '-2', '2', '-3', '3', '4', '-5', '5', '-6', '6', '-7', '7'], 
        ['C', '-D', 'D', '-E', 'E', 'F', '-G', 'G', '-A', 'A', '-B', 'B'], ['C', '+C', 'D', '+D', 'E', 'F', 
        '+F', 'G', '+G', 'A', '+A', 'B'], ['1', '+1', '2', '+2', '3', '4', '+4', '5', '+5', '6', '+6', '7']] , 
        len: 5 t_ion: ('C Maj', 5)'''
        for ion in comic[0].keys():
            if choix == comic[0][ion][0]:
                t_ion = ion
                mod_com = comic[0][t_ion]
                mod_ton1 = mod_com[2][0]
                mod_ton2 = mod_com[3][0]
                (lineno(), 'mod_com:', mod_com, ', len:', len(mod_com), 't_ion:', t_ion)
        '''80 mod_com: ['-DG-A', ['1', '*3', '*4', '-3', '*5', '4', '*6', 'o6', '*7', '*8', '-7', '*9'], 
        ['+B', '-D', 'oE', '+D', '-F', '+E', '-G', 'G', '-A', 'oB', '+A', '-C'], ['C', '-D', 'xC', '-E', 'xD', 'F', 
        '+F', 'G', '-A', 'xG', '-B', 'xA'], ['1', '-2', 'x1', '-3', 'x2', '4', '+4', '5', '-6', 'x5', '-7', 'x6']] , 
        len: 5 t_ion: ('C Maj', 1)'''
        (lineno(), 'mod_ton1:', mod_ton1, 'mod_ton2:', mod_ton2)
        '''85 mod_ton1: +B mod_ton2: C'''
        # Créer un tableau diatonique naturel transposé à la tonique [gamme]
        '''Utiliser : Gamme = ['C', 'D', 'E', 'F', 'G', 'A', 'B']'''
        ton1, ton2 = mod_ton1[len(mod_ton1)-1:], mod_ton2[len(mod_ton2)-1:]
        ind_ton1, ind_ton2 = gamme.index(ton1), gamme.index(ton2)  # ind_ton1.2 = Index dans gamme
        gam_ton1 = gamme[ind_ton1:] + gamme[:ind_ton1]  # Séquence reconstituée à la tonique
        gam_ton2 = gamme[ind_ton2:] + gamme[:ind_ton2]  # Séquence reconstituée à la tonique
        (lineno(), 'gam_ton1.2:', gam_ton1, '.', gam_ton2)
        '''81 gam_ton1.2: ['B', 'C', 'D', 'E', 'F', 'G', 'A'] . ['C', 'D', 'E', 'F', 'G', 'A', 'B']'''
        '''Permet de reconnaitre les notes isolées signées ou absolues'''
        # Créer un tableau avec les notes isolées
        cas = ''
        for no in choix:                            # Créer un tableau avec les notes isolées
            if no in gamme:
                cas += no
                mode.append(cas)
                cas = ''
            else:
                cas += no
        (lineno(), 'Mode des uniques:', mode)
        '''65 Mode des uniques: ['-D', 'G', '-A']'''
        # Créer un tableau permettant le traçage
        trace = [scale, choix, t_ion]               # Créer un tableau permettant le traçage
        tracer.append(trace)
        (lineno(), 'tracer:', tracer, 'Longueur = ', len(tracer))
        '''106 tracer: [[12, '-DG-A', ('C Maj', 1)]] Longueur =  1'''
        #
        '''Les éléments ci-dessous aux catégories numériques:
            0 = Formules numériques des chromes supérieurs
            1 = Formules analogiques des chromes supérieurs
            2 = Formules analogiques des chromes inférieurs
            3 = Formules numériques des chromes inférieurs
        #
        Formats d'enregistrement des données à respecter pour la fonction chromatic...
            La tonalité analogique du mode tonique premier 1er☺
             - Liste ( [('','')], [(('', ''), ('', ''))],,, )
        *** EXEMPLE en Do☺
        209 GGC/ A: ([('', 'C')], [(('+', 'C'), ('-', 'D'))], [('', 'D')], [(('+', 'D'), ('-', 'E'))], [('', 'E')], 
        [('', 'F')], [(('+', 'F'), ('-', 'G'))], [('', 'G')], [(('+', 'G'), ('-', 'A'))], [('', 'A')], [(('+', 'A'), 
        ('-', 'B'))], [('', 'B')])'''
        #
        '''Les douze modulations des tonalités diatoniques numériques☺
             - Dictionnaire { Clés de 0 à 11 : Liste [ str(Forme numérique en extension[de 8 à 14] ) ] }
        *** EXEMPLE en Do☺
        C: {0: ['1', '+1', '2', '+2', '3', '4', '+4', '5', '+5', '6', '+6', '7'], 1: ['1', '-2', '2', '-3', '-4', '4', 
        '-5', '5', '-6', '6', '-7', '-8'], 2: ['1', '+1', '2', '-3', '3', '4', '+4', '5', '+5', '6', '-7', '7'], 
        3: ['1', '-2', 'o3', '-3', '-4', '4', '-5', '5', '-6', 'o7', '-7', '-8'], 4: ['1', '-2', '2', '-3', '3', '4', 
        '+4', '5', '-6', '6', '-7', '7'], 5: ['1', '+1', '2', '+2', '3', '+3', '+4', '5', '+5', '6', '+6', '7'], 
        6: ['1', '-2', '2', '-3', '3', '4', '-5', '5', '-6', '6', '-7', '-8'], 7: ['1', '+1', '2', '+2', '3', '4', 
        '+4', '5', '+5', '6', '-7', '7'], 8: ['1', '-2', '2', '-3', '-4', '4', '-5', '5', '-6', 'o7', '-7', '-8'], 
        9: ['1', '+1', '2', '-3', '3', '4', '+4', '5', '-6', '6', '-7', '7'], 10: ['1', '-2', 'o3', '-3', '-4', '4', 
        '-5', 'o6', '-6', 'o7', '-7', '-8'], 11: ['1', '-2', '2', '-3', '3', '4', '-5', '5', '-6', '6', '-7', '7']} '''
        #
        # Construire les tables des notes diatoniques
        '''Format de réception : ['+B', '-D', 'oE', '+D', '-F', '+E', '-G', 'G', '-A', 'oB', '+A', '-C']
                                 ['C', '-D', 'xC', '-E', 'xD', 'F', '+F', 'G', '-A', 'xG', '-B', 'xA']'''
        # Formater les modes diatoniques - Analogies formatées
        '''Format d'expédition : - Liste ( [('','')], [(('', ''), ('', ''))],,, ). Uniquement le mode tonique.'''
        lst_dia = []
        for dia in range(12):                           # Formater les modes diatoniques - Analogies formatées
            not_dia2, not_dia3 = mod_com[2][dia], mod_com[3][dia]
            if not_dia2 in mode:
                sig_dia, deg_dia = not_dia2[:len(not_dia2)-1], not_dia2[len(not_dia2)-1:]
                trans = sig_dia, deg_dia
            else:
                sig_dia2, deg_dia2 = not_dia2[:len(not_dia2) - 1], not_dia2[len(not_dia2) - 1:]
                sig_dia3, deg_dia3 = not_dia3[:len(not_dia3) - 1], not_dia3[len(not_dia3) - 1:]
                trans = (sig_dia2, deg_dia2), (sig_dia3, deg_dia3)
            lst_dia.append([trans])
        lst_dia = tuple(lst_dia)
        (lineno(), 'lst_dia:', lst_dia)
        '''145 lst_dia: [[(('+', 'B'), ('', 'C'))], [('-', 'D')], [(('o', 'E'), ('x', 'C'))], [(('+', 'D'), 
        ('-', 'E'))], [(('-', 'F'), ('x', 'D'))], [(('+', 'E'), ('', 'F'))], [(('-', 'G'), ('+', 'F'))], [('', 'G')], 
        [('-', 'A')], [(('o', 'B'), ('x', 'G'))], [(('+', 'A'), ('-', 'B'))], [(('-', 'C'), ('x', 'A'))]]'''
        # Construire les modes diatoniques - Analogies
        '''Utilisations :
            65 Mode des uniques: ['-D', 'G', '-A'] + Toniques et septièmes'''
        mod_dia2, mod_dia3 = [], []
        for bio in range(12):                           # Construire les modes diatoniques - Analogies
            trans2 = mod_com[2][bio:] + mod_com[2][:bio]
            trans3 = mod_com[3][bio:] + mod_com[3][:bio]
            mod_dia2.append(trans2)
            mod_dia3.append(trans3)
        (lineno(), 'mod_dia2:', mod_dia2, '\n\nmod_dia3:', mod_dia3)
        #  Construire les modes diatoniques - Tonalité numérisée
        '''Format général : ['1', '-2', '2', '-3', '3', '4', '-5', '5', '-6', '6', '-7', '7']
        Format d'expédition : C: {0: ['1', '+1', '2', '+2', '3', '4', '+4', '5', '+5', '6', '+6', '7']
        Utilisations :
            76 gam_ton1.2: ['C', 'D', 'E', 'F', 'G', 'A', 'B'] . ['B', 'C', 'D', 'E', 'F', 'G', 'A']'''
        num_lie = {}  # Dictionnaire des modes numériques (de 0 à 11)
        maj_lie = [1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0, 7]  # Table des degrés majeurs
        deg_lie = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        # Déclarer les modes diatoniques de cette gamme commatique
        mdc_mod0, mdc_mod1, mdc_mod2, mdc_mod3 = {}, {}, {}, {}  # Dico primordial bitonic
        une_mod0, une_mod1, une_mod2, une_mod3 = {}, {}, {}, {}  # Dico première gamme
        sec_mod0, sec_mod1, sec_mod2, sec_mod3 = {}, {}, {}, {}  # Dico deuxième gamme
        tri_log = False
        for lie in range(12):                           # Construire les modes diatoniques - Tonalité numérisée
            # Détecter la tonique pour ranger les degrés
            tn2, tn3 = mod_dia2[lie][0], mod_dia3[lie][0]  # Les toniques des paramètres
            deg_tn2, deg_tn3 = tn2[len(tn2)-1:], tn3[len(tn3)-1:]  # Les notes toniques absolues
            ind_tn2, ind_tn3 = deg_lie.index(deg_tn2), deg_lie.index(deg_tn3)  # Index dans deg_lie
            gam_tn2 = deg_lie[ind_tn2:] + deg_lie[:ind_tn2]  # Les tables des degrés rangés
            gam_tn3 = deg_lie[ind_tn3:] + deg_lie[:ind_tn3]
            mdc_mod0[lie] = []  # Dictionnaire numérique sup
            mdc_mod1[lie] = []  # Dictionnaire analogue sup
            mdc_mod2[lie] = []  # Dictionnaire analogue inf
            mdc_mod3[lie] = []  # Dictionnaire numérique inf
            num_lie[lie] = []  # Dictionnaire général des numériques
            # Capter les degrés (emplacements naturels) et numériser avec les extensions
            '''Chaque degré note réelle, absolue, extension'''
            for que in range(12):  # que = L'emplacement du degré
                tone2, tone3 = mod_dia2[lie][que], mod_dia3[lie][que]  # Les toniques des paramètres
                deg_tone2, deg_tone3 = tone2[len(tone2)-1:], tone3[len(tone3)-1:]  # Les degrés naturels
                ind_tone2, ind_tone3 = gam_tn2.index(deg_tone2), gam_tn3.index(deg_tone3)  # Les degrés rangés
                ind_num2, ind_num3 = maj_lie.index(ind_tone2+1), maj_lie.index(ind_tone3+1)  # Les numériques rangés
                dif_tone2, dif_tone3 = que - ind_num2, que - ind_num3  # Produit le signe d'altération
                # Traiter les différences et les extensions
                if dif_tone2 > -1:
                    if abs(dif_tone2) > 6:
                        sig2 = 12 - abs(dif_tone2)
                        note2 = tab_inf[sig2] + str(ind_tone2 + 8)
                    else:
                        note2 = tab_sup[dif_tone2] + str(ind_tone2+1)
                    (lineno(), 'dif_tone2>-1:', dif_tone2, 'note2:', note2)
                else:
                    if abs(dif_tone2) > 6:
                        sig2 = 12 - abs(dif_tone2)
                        note2 = tab_sup[sig2] + str(ind_tone2 + 8)
                    else:
                        note2 = tab_inf[abs(dif_tone2)] + str(ind_tone2+1)
                    (lineno(), 'dif_tone2<0:', dif_tone2, 'note2:', note2)
                if dif_tone3 > -1:
                    if abs(dif_tone3) > 6:
                        sig3 = 12 - abs(dif_tone3)
                        note3 = tab_inf[sig3] + str(ind_tone3 + 8)
                    else:
                        note3 = tab_sup[dif_tone3] + str(ind_tone3+1)
                    (lineno(), 'dif_tone3>-1:', dif_tone3, 'note3:', note3)
                else:
                    if abs(dif_tone3) > 6:
                        sig3 = 12 - abs(dif_tone3)
                        note3 = tab_sup[sig3] + str(ind_tone3 + 8)
                    else:
                        note3 = tab_inf[abs(dif_tone3)] + str(ind_tone3+1)
                    (lineno(), 'dif_tone3<0:', dif_tone3, 'note3:', note3)
                (lineno(), 'dif_tone2.3:', dif_tone2, dif_tone3)
                mdc_mod0[lie].append(note2)
                mdc_mod1[lie].append(mod_dia2[lie][que])
                mdc_mod2[lie].append(mod_dia3[lie][que])
                mdc_mod3[lie].append(note3)
                num_lie[lie].append(note2)
                if que == 12:  # Pour activer cette section (que = 11)
                    print(lineno(), 'mdc_mod0[lie]:', lie, mdc_mod0[lie])
                    print(lineno(), 'mdc_mod1[lie]:', lie, mdc_mod1[lie])
                    # print(lineno(), 'mdc_mod2[lie]:', lie, mdc_mod2[lie])
                    # print(lineno(), 'mdc_mod3[lie]:', lie, mdc_mod3[lie])
                    print(lineno(), '***')
        (lineno(), 'num_lie.keys():', num_lie.keys())
        '''240 num_lie.keys(): dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])'''
        # Vérification des correspondances des tonalités ; Aux valeurs numériques sup/inf
        '''Quand la condition est vraie, elle indique qu'il s'agit d'une gamme standard :
            Gamme standard = Coïncidence modales à la forme numérique de la tonalité.
            Autrement, chaque tonalité est unique et n'a qu'une seule forme numérique.'''
        if mdc_mod0[1] == mdc_mod3[0]:  # Gamme originale
            tri_log = True
            (lineno(), 'Mod0 et Mod3 Correspondent:', mdc_mod0[0], mdc_mod3[1])
        else:  # Gamme bipartie et double-gamme
            # mdc_mod4, mdc_mod5 = Parties analogues pour une trilogie
            ''' mdc_mod4 : Analogie en duo avec mdc_mod1
                mdc_mod5 : Analogie en duo avec mdc_mod2
            En bref : Garder inf en créant sup, ou changer sur pour créer inf.'''
            une_mod0 = mdc_mod0.copy()  # Dictionnaire premier numérique sup des listes gardées
            une_mod1 = mdc_mod1.copy()  # Dictionnaire premier analogue sup des listes gardées
            (lineno(), une_mod1)
            #
            sec_mod2 = mdc_mod2.copy()  # Dictionnaire second analogue inf des listes gardées
            sec_mod3 = mdc_mod3.copy()  # Dictionnaire second numérique inf des listes gardées
            for cle0 in mdc_mod0.keys():
                une_mod2[cle0] = []  # Dictionnaire premier analogue inf des listes à compléter
                une_mod3[cle0] = []  # Dictionnaire premier numérique inf des listes à compléter
                #
                sec_mod0[cle0] = []  # Dictionnaire second numérique sup des listes à compléter
                sec_mod1[cle0] = []  # Dictionnaire second analogue sup des listes à compléter
                cle1 = cle0 + 1
                if cle1 == 12:
                    cle1 = 0
                if cle0 == 0:  # Initialisation des toniques des listes à compléter
                    une_mod2[cle0].append(mdc_mod2[cle0][0])
                    sec_mod1[cle0].append(mdc_mod1[cle0][0])
                    print(lineno(), 'GGM/Toniques premier:', une_mod2[cle0], ', et second:', sec_mod1[cle0])
                for hop in range(12):
                    # Partie de la première gamme
                    une_mod3[cle0].append(une_mod0[cle1][hop])  # Tonalité du mode suivant
                    # print(lineno(), 'cle0:', cle0, 'une_mod0:', une_mod0[cle0][:hop], 'hop:', hop)
                    # print(lineno(), 'cle0:', cle0, 'une_mod1:', une_mod1[cle0][:hop], 'hop:', hop)
                    # print(lineno(), 'cle0:', cle0, 'une_mod2:', une_mod2[cle0][:hop], 'hop:', hop)
                    # print(lineno(), 'cle0:', cle0, 'une_mod3:', une_mod3[cle0][:hop], 'hop:', hop)
                    # print(lineno(), '***')
                    #
                    # Partie de la seconde gamme
                    sec_mod0[cle0].append(sec_mod3[cle1][hop])
                    (lineno(), 'cle0:', cle0, 'sec_mod0:', sec_mod0[cle0][:hop], 'hop:', hop)
                    (lineno(), 'cle0:', cle0, 'sec_mod1:', sec_mod1[cle0][:hop], 'hop:', hop)
                    (lineno(), 'cle0:', cle0, 'sec_mod2:', sec_mod2[cle0][:hop], 'hop:', hop)
                    (lineno(), 'cle0:', cle0, 'sec_mod3:', sec_mod3[cle0][:hop], 'hop:', hop)
                    (lineno(), '***')
                    # break
                break  # Arrêt provisoire

        # Écriture sur Canvas
        tri = 20
        if tri_log:
            tri = 30
        c_ii2 = "{}{}".format('Commatismes en cours de traçage : ', tracer)
        self.cop_bout.create_text(180, 8, font=self.f_bt, text=c_ii2, fill='blue')
        for i in range(12):
            c_i = i * 60
            c_x, c_y = 30, 90
            (lineno(), 'GGM/i:', i)
            for j in range(12):
                c_j = j * 30
                c_ripmin = mdc_mod1[i][j]  # Balance mineure : 0. ('-D')...
                c_ripaug = mdc_mod2[i][j]  # Signal augmenté : 0. ('+C')...
                c_rop2 = mdc_mod0[i][j]  # Valeur numérique de la tonalité supérieure
                self.cop_bout.create_text(c_x + c_j, c_y + c_i - tri, font=self.f_bt, text=c_rop2, fill='olive')
                (lineno(), 'C_Rop2:', c_rop2)  # c_rop2 = Valeur numérique de la tonalité
                if c_ripaug in mode:  # Les notes de la gamme sont isolées
                    c_rip0 = c_ripaug  # Signal
                    self.cop_bout.create_text(c_x + c_j, c_y + c_i, font=self.f_bu, text=c_rip0, fill='black')
                    (lineno(), 'C_Rip0:', c_rip0)  # c_rip0 = Altération sur la note naturelle (gamme)
                else:  # Les notes chromatiques sont couplées
                    c_rip1 = c_ripmin
                    self.cop_bout.create_text(c_x + c_j, c_y + c_i - 10, font=self.f_bv, text=c_rip1, fill='red')
                    c_rip2 = c_ripaug
                    self.cop_bout.create_text(c_x + c_j, c_y + c_i + 10, font=self.f_bv, text=c_rip2, fill='blue')
                    (lineno(), 'C_Rip1:', c_rip1)  # Note chromatique du rang supérieur('-D')
                    (lineno(), 'C_Rip2:', c_rip2)  # Note chromatique du rang inférieur('+C')
                if tri_log and i == 11:  # Utiliser en cas de correspondance des tonalités sup/inf
                    c_rop2 = mdc_mod3[i][j]  # Valeur numérique de la tonalité inférieure
                    self.cop_bout.create_text(c_x + c_j, c_y + c_i + tri, font=self.f_bt, text=c_rop2, fill='olive')
                elif not tri_log:
                    c_rop2 = mdc_mod3[i][j]  # Valeur numérique de la tonalité inférieure
                    self.cop_bout.create_text(c_x + c_j, c_y + c_i + tri, font=self.f_bt, text=c_rop2, fill='olive')
                (lineno(), 'C_Rop2:', c_rop2)  # c_rop2 = Valeur numérique de la tonalité
        if not tri_log:
            but_cop = Button(self.copier, text='Commane', height=1, width=15, bg='pink',
                             command=lambda: progam_vers6.Commatique.brnch_1(self, lst_dia, num_lie, tracer, scale))
            but_cop.pack(side=BOTTOM, pady=6)


'''print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()'''
