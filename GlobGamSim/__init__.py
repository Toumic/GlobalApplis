#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Le dimanche 12 février 2023 (Commencement du script)
# GlobGamSim : Pour présenter les propriétés de la gamme en cours

# lineno() Pour consulter le programme grâce au suivi des print's
import inspect
from typing import Callable

lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

# GGV6/2974(self.nordiese) 2978(self.subemol)
tab_sup = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^', '+^^^^', 'x^^^^',
           '^^^^^', '+^^^^^', 'x^^^^^', '^^^^^^', '+^^^^^^', 'x^^^^^^', '^^^^^^^', '+^^^^^^^', 'x^^^^^^^', '^^^^^^^^']
tab_inf = ['', '-', 'o', '*', '-*', 'o*', '**', '-**', 'o**', '***', '-***', 'o***', '****', '-****', 'o****',
           '*****', '-*****', 'o*****', '******', '-******', 'o******', '*******', '-*******', 'o*******', '********']
tab_abc = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def simili(sim, dat, nom):
    """Partie analytique liée à la gamme en cours et déclare les similitudes.
    Similitudes (sim = Selon les noms des gammes[classique ou calculée])
    Poids modaux : (
        (dat[1] = Dictionnaire. Clefs ('Maj', '-3',,,). Intervalles modaux genre cumulatif),
        (dat[2] = Liste. Format dictionnaire[('ISO', (((1, 'I'), '+^2'), ((1, 'III'), '-*6')))]),
        (dat[3] = Dictionnaire. Clefs (147, 266,,,). Groupe des gammes aux mêmes poids),
        (dat[4] = Dictionnaire. Clefs ('0352146', '1253046',,,). Groupe des gammes aux mêmes rangs),
        (dat[5] = Dictionnaire. Clefs (de 1 à 66). Groupe les noms entiers diatoniques),
        (dat[6] = Dictionnaire. Clefs ((66, 'I'), (66, 'II'),,,). Groupe poids modaux diatoniques))
    Le nom de la gamme en cours (attention aux compositions : Exemple = 'oF x54o')"""
    # Objectif mettre en forme les données reçues pour une meilleure gestion
    print(lineno(), 'GGS/sim:', sim['-2'], '\n', 'dat:', dat.keys(), type(dat), 'nom:', nom)
    # Formatage du nom de la gamme en cours : 'C Maj' devient 'C' et 'Maj'
    n0, max_n0 = 0, len(nom)
    n1 = ''
    sig_ava, sig_abc, sig_sui = [], [], []
    for no in nom:
        if n0 == 0 and no not in tab_abc:
            for ma in range(max_n0):
                if nom[ma] not in tab_abc:
                    n1 += nom[ma]
                    print(lineno(), 'N1 en construction:', n1)
                else:
                    if n1 in tab_sup:
                        print(lineno(), 'N1 tab_sup:', n1)
                    else:
                        print(lineno(), 'N1 tab_inf:', n1)
                    break
        elif no in tab_abc:
            print(lineno(), 'No tab_abc:', no)
        else:

            print(lineno(), 'No:', no)
        n0 += 1
        print(lineno(), 'Nom:', nom, 'No:', no, 'N0:', n0, 'max_n0:', max_n0)
