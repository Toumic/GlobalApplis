# -*- coding: utf-8 -*-
# vicenté quantic cabviva
#
# Nom de l'application = songammes.py
"""Ce programme consiste à donner une sonorité diatonique aux gammes.
Cette gamme est en Do et elle retrace les gammes fondamentales.
L’architecture de cet assemblage ressemble à cette image (images/ClassBooLsIII.png)."""
# https://cabviva.com/musicmp3/gamcop!s.mp3

import inspect
from tkinter import *
from tkinter.constants import *
from tkinter.font import *
from tkinter.messagebox import *
from tkinter import simpledialog
from typing import Callable

from PIL import ImageTk, Image
import time
import pyaudio
import numpy as np
import ctypes

# Les modules personnels.
import songammes.gammes_audio as gamma  # Faire sonner les gammes.

# lino() Pour consulter le programme grâce au suivi des print’s
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

(lineno(), "Gammes", dir(gamma))

("# Ces deux dictionnaires possèdent les caractéristiques des noms des gammes et de leurs modes binarisés."
 "Le _m_ veut dire venant du pôle 'Modes', le _g_ vient du pôle gammes. Aide dans le fichier 'READ notes_songammes.md'")
dic_m_analytic = {
    "dic_m_noms_ego": ['0', '-5', 'o45x', 'o46+', 'o46-', '-26o', '+25x', 'o35x', 'x26-', 'o45-', '*5', 'o4', 'o54-',
                       '-34', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', '-24',
                       '+35x', '+23x', 'o35+', 'o35-', 'o3', 'o36+', '-23', '+45x', 'x45+', 'x46+', '^4', 'x5', 'o6',
                       '+56', '-56', '-56+', '-25', '+25-', '-25+', '-46+', '-36', '-36+', '-26', '-26+', '+26-', '+26',
                       '-2', '+2', '-45+', '-34x', '+34', 'x3', '-45', 'o5', '-35+', '-35', '-4', '-3', '-6', '+6'],
    "dic_m_noms_ego_inv": ['o35-', '-24', '-23', '-25+', '-26+', '-46o', '-45', '-35+', '-3', '-35', '+56', '+6',
                           'x45+', 'x46+', '+35x', '+34', '+25x', '+26-', '+2', 'o45x', 'o46-', 'o4', 'o46+', 'o45-',
                           'o54-', '*5', '-34', 'o63-', 'o35x', 'o35+', 'o3', 'o36+', 'o34x', '-25o', '-45x', '-45+',
                           '*6', '-4', 'o65-', '-46+', 'o5', '-34x', 'x5', '-56+', '+45x', '^4', '+34x', 'x3', 'x36+',
                           '^3', '+25-', '+23x', 'x26-', '^2', '-36+', '-36', '-26', '-26o', '-6', 'o6', '-56', '+26',
                           '-2', '-25', '-5', '0'],
    "dic_m_noms_iso": ['o45x', 'o46-', 'o46+', 'o4', '*5', 'o45-', 'o35x', '+25x', 'x26-', 'o54-', '-34', 'o63-',
                       'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', 'o35+', 'o35-', 'o3',
                       'o36+', '-24', '+35x', '+23x', '-23', '+45x', '+25-', '-25+', '-26+', '-26', '-26o', '+26',
                       '-25', '-2', '+2', '-45+', '-34x', '+34', 'x3', '-46+', '+26-', '-4', '-45', 'o5', '-35+',
                       '-35', '-36', '-36+', '-3', 'x5', 'o6', '+56', '-56', '-56+', 'x45+', 'x46+', '^4', '-6', '+6',
                       '0', '-5'],
    "dic_m_noms_iso_inv": ['0', '-26', '-6', '-2', '-56', '-25', '+26', 'o35-', '-24', '-23', '-25+', '-26+', '-46o',
                           '-45', '-35+', '-36', '-3', '-35', '+56', '+6', 'x45+', 'x46+', '+35x', '+34', '+25x',
                           '+26-', '+2', 'o45x', 'o46-', 'o4', 'o46+', 'o45-', 'o54-', '*5', '-34', 'o63-', 'o35x',
                           'o35+', 'o3', 'o36+', 'o34x', '-25o', '-26o', '-45x', '-45+', '*6', '-4', 'o65-', '-46+',
                           'o5', '-36+', '-34x', 'x5', 'o6', '-5', '-56+', '+45x', '^4', '+34x', 'x3', 'x36+', '^3',
                           '+25-', '+23x', 'x26-', '^2'],
    "dic_m_noms_int": ['o45x', 'o35x', 'o46+', 'o46-', '-26o', '+25x', 'x26-', 'o45-', '*5', 'o35-', 'o54-', 'o63-',
                       'o35+', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+35x', '+34x', 'x36+', '^3', '+23x',
                       '^2', 'o36+', '-25', '+25-', '-25+', '-26', '-26+', '-46+', '+26-', '+26', '-45', 'o5',
                       '-45+', '-34x', '+34', 'x3', '-35+', '-35', 'x45+', 'x46+', '^4', '+45x', '-36+', 'o4',
                       '-34', 'o3', '-24', '-23', 'x5', 'o6', '+56', '-56', '-56+', '-2', '+2', '-36', '-5', '-4',
                       '-3', '-6', '+6', '0'],
    "dic_m_noms_int_inv": ['-2', '0', '-25', '-26', '-6', '-56', '+26', '-26o', 'o6', '-5', 'o45x', 'o46-', 'o4',
                           'o46+', 'o45-', 'o54-', '*5', '-34', 'o63-', 'o35x', 'o35+', 'o3', 'o36+', 'o35-',
                           'o34x', '-24', '-25o', '-23', '-25+', '-26+', '-45x', '-45+', '-46o', '*6', '-4', 'o65-',
                           '-46+', '-45', 'o5', '-35+', '-36', '-3', '-36+', '-35', '-34x', 'x5', '+56', '+6',
                           '-56+', '+45x', 'x45+', 'x46+', '^4', '+35x', '+34', '+34x', 'x3', 'x36+', '^3', '+25x',
                           '+26-', '+2', '+25-', '+23x', 'x26-', '^2'],
    "dic_m_bins_ego": ['1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1001000', '1111011',
                       '1100110', '1010111', '1000001', '1000000', '1000101', '1011000', '1011001', '1000100',
                       '1001001', '1010001', '1000011', '1100000', '1000111', '1111000', '1100001', '1000010',
                       '1010010', '1001011', '1010100', '1001111', '1110100', '1001101', '1100100', '1110001',
                       '1110010', '1100010', '1111001', '1011011', '1010101', '1011100', '1100101', '1001010',
                       '1010011', '1101101', '1110011', '1011101', '1011010', '1011111', '1110101', '1111010',
                       '1100011', '1000110', '1101001', '1101000', '1101011', '1010110', '1100111', '1001110',
                       '1111100', '1101111', '1110110', '1111101', '1101010', '1011110'],
    "dic_m_bins_ego_inv": ['1011110', '1101010', '1111101', '1110110', '1101111', '1111100', '1001110', '1100111',
                           '1010110', '1101011', '1101000', '1101001', '1000110', '1100011', '1111010', '1110101',
                           '1011111', '1011010', '1011101', '1110011', '1101101', '1010011', '1001010', '1100101',
                           '1011100', '1010101', '1011011', '1111001', '1100010', '1110010', '1110001', '1100100',
                           '1001101', '1110100', '1001111', '1010100', '1001011', '1010010', '1000010', '1100001',
                           '1111000', '1000111', '1100000', '1000011', '1010001', '1001001', '1000100', '1011001',
                           '1011000', '1000101', '1000000', '1000001', '1010111', '1100110', '1111011', '1001000',
                           '1101100', '1111110', '1110111', '1001100', '1101110', '1111111'],
    "dic_m_bins_iso": ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000', '1100000',
                       '1000011', '1001001', '1010001', '1000100', '1100001', '1000010', '1001011', '1010100',
                       '1001111', '1110100', '1001101', '1100100', '1010010', '1110001', '1110010', '1011011',
                       '1011100', '1010101', '1100101', '1001010', '1011101', '1011010', '1001000', '1011111',
                       '1001100', '1110101', '1111010', '1100011', '1000110', '1101001', '1100111', '1001110',
                       '1010011', '1111100', '1101000', '1101011', '1010110', '1101101', '1111011', '1100110',
                       '1010111', '1101111', '1110011', '1110110', '1111001', '1100010', '1111101', '1101010',
                       '1011110', '1111111', '1101110', '1110111', '1111110', '1101100'],
    "dic_m_bins_iso_inv": ['1101100', '1111110', '1110111', '1101110', '1111111', '1011110', '1101010', '1111101',
                           '1100010', '1111001', '1110110', '1110011', '1101111', '1010111', '1100110', '1111011',
                           '1101101', '1010110', '1101011', '1101000', '1111100', '1010011', '1001110', '1100111',
                           '1101001', '1000110', '1100011', '1111010', '1110101', '1001100', '1011111', '1001000',
                           '1011010', '1011101', '1001010', '1100101', '1010101', '1011100', '1011011', '1110010',
                           '1110001', '1010010', '1100100', '1001101', '1110100', '1001111', '1010100', '1001011',
                           '1000010', '1100001', '1000100', '1010001', '1001001', '1000011', '1100000', '1111000',
                           '1000111', '1011001', '1011000', '1000101', '1000000', '1000001'],
    "dic_m_bins_int": ['1000000', '1000001', '1000010', '1000011', '1000100', '1000101', '1000110', '1000111',
                       '1001000', '1001001', '1001010', '1001011', '1001100', '1001101', '1001110', '1001111',
                       '1010001', '1010010', '1010011', '1010100', '1010101', '1010110', '1010111', '1011000',
                       '1011001', '1011010', '1011011', '1011100', '1011101', '1011110', '1011111', '1100000',
                       '1100001', '1100010', '1100011', '1100100', '1100101', '1100110', '1100111', '1101000',
                       '1101001', '1101010', '1101011', '1101100', '1101101', '1101110', '1101111', '1110001',
                       '1110010', '1110011', '1110100', '1110101', '1110110', '1110111', '1111000', '1111001',
                       '1111010', '1111011', '1111100', '1111101', '1111110', '1111111'],
    "dic_m_bins_int_inv": ['1111111', '1111110', '1111101', '1111100', '1111011', '1111010', '1111001', '1111000',
                           '1110111', '1110110', '1110101', '1110100', '1110011', '1110010', '1110001', '1101111',
                           '1101110', '1101101', '1101100', '1101011', '1101010', '1101001', '1101000', '1100111',
                           '1100110', '1100101', '1100100', '1100011', '1100010', '1100001', '1100000', '1011111',
                           '1011110', '1011101', '1011100', '1011011', '1011010', '1011001', '1011000', '1010111',
                           '1010110', '1010101', '1010100', '1010011', '1010010', '1010001', '1001111', '1001110',
                           '1001101', '1001100', '1001011', '1001010', '1001001', '1001000', '1000111', '1000110',
                           '1000101', '1000100', '1000011', '1000010', '1000001', '1000000']}
lis_m_noms = [m for m in dic_m_analytic.keys() if "noms" in m]
lis_m_bins = [m for m in dic_m_analytic.keys() if "bins" in m]
dic_g_analytic = {
    "dic_g_noms_ego": ['0', '-5', 'o45x', 'o46+', 'o46-', '-26o', '+25x', 'o35x', 'x26-', 'o45-', '*5', 'o4', 'o54-',
                       '-34', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', '-24',
                       '+35x', '+23x', 'o35+', 'o35-', 'o3', 'o36+', '-23', '+45x', 'x45+', 'x46+', '^4', 'x5', 'o6',
                       '+56', '-56', '-56+', '-25', '+25-', '-25+', '-46+', '-36', '-36+', '-26', '-26+', '+26-', '+26',
                       '-2', '+2', '-45+', '-34x', '+34', 'x3', '-45', 'o5', '-35+', '-35', '-4', '-3', '-6',
                       '+6'],
    "dic_g_noms_ego_inv": ['+6', '-6', '-3', 'o45x', '-4', 'o5', '-35', '-45+', '-35+', '-34x', 'x3', 'o34x', '-45x',
                           '-46o', '*6', 'o65-', '-45', 'x36+', '^3', '^2', 'o54-', '*5', 'o63-', '-25o', '+34', '+2',
                           'o45-', 'o35x', 'o36+', '-2', 'o46+', '+34x', '-26+', '+26-', 'o46-', '-26o', '+25x', '+26',
                           'x26-', '-26', '-25', '+25-', '-25+', '-46+', '-36+', '-36', 'x5', 'o6', '-56+', '-56',
                           '+35x', '+23x', 'o35+', 'o35-', '+56', 'x45+', 'x46+', '^4', '+45x', 'o4', '-34', 'o3',
                           '-24', '-23', '-5', '0'],
    "dic_g_noms_iso": ['o45x', 'o46-', 'o46+', 'o4', '*5', 'o45-', 'o35x', '+25x', 'x26-', 'o54-', '-34', 'o63-',
                       'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', 'o35+', 'o35-', 'o3',
                       'o36+', '-24', '+35x', '+23x', '-23', '+45x', '+25-', '-25+', '-26+', '-26', '-26o', '+26',
                       '-25', '-2', '+2', '-45+', '-34x', '+34', 'x3', '-46+', '+26-', '-4', '-45', 'o5', '-35+',
                       '-35', '-36', '-36+', '-3', 'x5', 'o6', '+56', '-56', '-56+', 'x45+', 'x46+', '^4', '-6', '+6',
                       '0', '-5'],
    "dic_g_noms_iso_inv": ['o45x', 'o34x', '-45x', '-46o', '*6', 'o65-', 'x36+', '^3', '^2', 'o35x', '+25x', 'x26-',
                           'o46-', 'o46+', '+34x', '+35x', '+23x', 'o36+', '+25-', '-26+', '-26', '-26o', '+26', '+2',
                           '+26-', '-45+', '-34x', 'x3', 'o45-', 'o54-', '*5', 'o63-', '-25o', '+34', 'x45+', '^4',
                           'o35+', 'o35-', 'x46+', '+45x', 'x5', 'o6', '+56', '-56', '-56+', '-2', '-25', '-5', '-6',
                           '+6', '0', '-35+', '-45', 'o5', '-35', '-25+', '-46+', '-36', '-36+', '-4', '-3', 'o4',
                           '-34', 'o3', '-24', '-23'],
    "dic_g_noms_int": ['o45x', 'o34x', '-45x', '-46o', '*6', 'o65-', 'x36+', '^3', '^2', 'o35x', '+25x', 'x26-',
                       'o46-', 'o46+', '+34x', '+35x', '+23x', '-26+', '-26o', '+26', 'o36+', '+2', '+26-', '-26',
                       '+25-', '-45+', '-34x', 'x3', 'o45-', 'o54-', '*5', 'o63-', '-25o', '+34', 'x45+', '^4',
                       'o35+', 'o35-', 'x46+', '+45x', 'x5', 'o6', '+56', '-56', '-56+', '-6', '+6', '-2', '-25',
                       '0', '-5', '-35+', '-25+', '-46+', '-36', '-36+', '-4', '-45', 'o5', '-3', '-35', 'o4',
                       '-34', 'o3', '-24', '-23'],
    "dic_g_noms_int_inv": ['o45x', 'o54-', '*5', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', 'x36+',
                           '^3', '^2', 'o45-', 'o35x', 'o46+', '+34x', 'o46-', '+25x', 'x26-', 'o4', '-34', 'o35+',
                           'o35-', 'o3', 'o36+', '-24', '+35x', '+23x', '-23', '+45x', '-26o', '-25', '+25-',
                           '-26', '-26+', '+26', '-2', '+2', '-25+', '-45', 'o5', '-46+', '+26-', '-4', '-45+',
                           '-34x', '+34', 'x3', '-35+', '-35', '-36', '-36+', '-3', 'x5', 'o6', '+56', '-56',
                           '-56+', 'x45+', 'x46+', '^4', '-5', '-6', '+6', '0'],
    "dic_g_bins_ego": ['1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1001000', '1111011',
                       '1100110', '1010111', '1000001', '1000000', '1000101', '1011000', '1011001', '1000100',
                       '1001001', '1010001', '1000011', '1100000', '1000111', '1111000', '1100001', '1000010',
                       '1010010', '1001011', '1010100', '1001111', '1110100', '1001101', '1100100', '1110001',
                       '1110010', '1100010', '1111001', '1011011', '1010101', '1011100', '1100101', '1001010',
                       '1010011', '1101101', '1110011', '1011101', '1011010', '1011111', '1110101', '1111010',
                       '1100011', '1000110', '1101001', '1101000', '1101011', '1010110', '1100111', '1001110',
                       '1111100', '1101111', '1110110', '1111101', '1101010', '1011110'],
    "dic_g_bins_ego_inv": ['1111101', '1101010', '1000100', '1100111', '1011110', '1000000', '1001001', '1010011',
                           '1001000', '1101111', '1001110', '1110011', '1110110', '1111100', '1101000', '1000001',
                           '1101011', '1000110', '1100011', '1010110', '1000011', '1101001', '1000010', '1100001',
                           '1100000', '1011111', '1001101', '1110101', '1111010', '1100100', '1011000', '1010001',
                           '1001100', '1011101', '1000101', '1100101', '1011010', '1011001', '1010101', '1011011',
                           '1101101', '1001010', '1100110', '1011100', '1111011', '1010111', '1111001', '1100010',
                           '1000111', '1010010', '1010100', '1001011', '1110001', '1110010', '1001111', '1110100',
                           '1111000', '1101100', '1111111', '1101110', '1110111', '1111110'],
    "dic_g_bins_iso": ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000', '1100000',
                       '1000011', '1001001', '1010001', '1000100', '1100001', '1000010', '1001011', '1010100',
                       '1001111', '1110100', '1001101', '1100100', '1010010', '1110001', '1110010', '1011011',
                       '1011100', '1010101', '1100101', '1001010', '1011101', '1011010', '1001000', '1011111',
                       '1001100', '1110101', '1111010', '1100011', '1000110', '1101001', '1100111', '1001110',
                       '1010011', '1111100', '1101000', '1101011', '1010110', '1101101', '1111011', '1100110',
                       '1010111', '1101111', '1110011', '1110110', '1111001', '1100010', '1111101', '1101010',
                       '1011110', '1111111', '1101110', '1110111', '1111110', '1101100'],
    "dic_g_bins_iso_inv": ['1000011', '1000000', '1000001', '1100001', '1000010', '1000101', '1001001', '1011001',
                           '1010001', '1000100', '1011000', '1010010', '1011011', '1001101', '1010101', '1100100',
                           '1011101', '1100101', '1011010', '1001000', '1011111', '1110101', '1111010', '1010011',
                           '1100011', '1000110', '1101001', '1100000', '1110001', '1100010', '1010100', '1001011',
                           '1110010', '1111001', '1000111', '1111011', '1100110', '1001100', '1010111', '1101100',
                           '1111101', '1101010', '1100111', '1011110', '1111111', '1101110', '1110111', '1111110',
                           '1101011', '1010110', '1101000', '1101101', '1001010', '1110011', '1011100', '1101111',
                           '1001110', '1110110', '1111100', '1001111', '1110100', '1111000'],
    "dic_g_bins_int": ['1000011', '1000000', '1000001', '1100001', '1000010', '1000101', '1001001', '1011001',
                       '1010001', '1000100', '1011000', '1010010', '1011101', '1100101', '1011010', '1001000',
                       '1011111', '1001101', '1110101', '1111010', '1100100', '1010011', '1011011', '1010101',
                       '1100011', '1000110', '1101001', '1100000', '1110001', '1100010', '1010100', '1001011',
                       '1110010', '1111001', '1000111', '1111101', '1101010', '1100111', '1011110', '1111111',
                       '1101110', '1001100', '1110111', '1111110', '1101100', '1111011', '1100110', '1010111',
                       '1101011', '1010110', '1101101', '1001010', '1110011', '1011100', '1101111', '1001110',
                       '1110110', '1111100', '1101000', '1001111', '1110100', '1111000'],
    "dic_g_bins_int_inv": ['1000011', '1000001', '1100000', '1000000', '1100001', '1000010', '1001001', '1010001',
                           '1000100', '1000101', '1011000', '1011001', '1000111', '1111000', '1001011', '1010100',
                           '1001111', '1110100', '1001101', '1100100', '1010010', '1110001', '1110010', '1001000',
                           '1011011', '1001100', '1010101', '1011101', '1100101', '1011010', '1011111', '1110101',
                           '1111010', '1011100', '1001010', '1100011', '1000110', '1101000', '1100111', '1001110',
                           '1010011', '1111100', '1101001', '1101011', '1010110', '1101101', '1111011', '1100110',
                           '1010111', '1101111', '1110011', '1110110', '1111001', '1100010', '1101100', '1111101',
                           '1101010', '1011110', '1111111', '1101110', '1110111', '1111110']}
lis_g_noms = [g for g in dic_g_analytic.keys() if "noms" in g]
lis_g_bins = [g for g in dic_g_analytic.keys() if "bins" in g]
"# Traitement des données des 'dic__analytic' ou 'dic_g_analytic'."
# Connaitre les égalités avec et sans renversements. Dans un même dictionnaire.
"Dans un même dictionnaire : dic_m_analytic."
for mnb in [lis_m_noms, lis_m_bins, lis_g_noms, lis_g_bins]:
    for mn1 in mnb:
        if "_m_" in mn1:
            dma1 = dic_m_analytic[mn1]
        else:
            dma1 = dic_g_analytic[mn1]
        for mn2 in mnb:
            if "_m_" in mn1:
                dma2 = dic_m_analytic[mn2]
            else:
                dma2 = dic_g_analytic[mn2]

            # Comparaison des listes
            if dma1 == dma2 and mn1 != mn2:
                (lineno(), "\t mn1.2", mn1, mn2, "dma1.2", dma1[0], dma2[0])
            dma2.reverse()
            if dma1 == dma2 and mn1 != mn2:
                (lineno(), "\t mn1.2", mn1, mn2, "dma1.2", dma1[0], dma2[0])
"Comparaison entre les deux dictionnaires analytiques. Classe des noms."
for lmn in lis_m_noms:
    dma1 = dic_m_analytic[lmn]
    for lgn in lis_g_noms:
        dma2 = dic_g_analytic[lgn]
        if dma1 == dma2:
            (lineno(), "lmn_lgn", lmn, lgn, "\t\t Classic dma1=2", dma1[0], dma2[0])
        dma2.reverse()
        if dma1 == dma2:
            (lineno(), "lmn_lgn", lmn, lgn, "\t\t Reverse dma1.2", dma1[0], dma2[0])
"Comparaison entre les deux dictionnaires analytiques. Classe des binaires."
for lmb in lis_m_bins:
    dma1 = dic_m_analytic[lmb]
    for lgb in lis_g_bins:
        dma2 = dic_g_analytic[lgb]
        if dma1 == dma2:
            (lineno(), "lmb_lgb", lmb, lgb, "\t\t Classic dma1=2", dma1[0], dma2[0])
        dma2.reverse()
        if dma1 == dma2:
            (lineno(), "lmb_lgb", lmb, lgb, "\t\t Reverse dma1.2", dma1[0], dma2[0])
# Résultats obtenus :
# 244 lmn_lgn : dic_m_noms_ego dic_g_noms_ego 		 Classic dma1=2 +6 +6
# 244 lmn_lgn : dic_m_noms_iso dic_g_noms_iso 		 Classic dma1=2 o45x o45x
# 254 lmb_lgb : dic_m_bins_ego dic_g_bins_ego 		 Classic dma1=2 1011110 1011110
# 257 lmb_lgb : dic_m_bins_ego_inv dic_g_bins_ego 		 Reverse dma1.2 1011110 1011110
# 254 lmb_lgb : dic_m_bins_iso dic_g_bins_iso 		 Classic dma1=2 1000001 1000001
# 257 lmb_lgb : dic_m_bins_iso_inv dic_g_bins_iso 		 Reverse dma1.2 1000001 1000001


gam_classic = {
    "102034050607": ["0", 336], "120034050607": ["-2", 210], "100234050607": ["+2", 392],
    "102304050607": ["-3", 301], "102034500607": ["-5", 341], "102034056007": ["-6", 330],
    "102034050067": ["+6", 339], "120304050607": ["-23", 175], "120034500607": ["-25", 215],
    "120034005607": ["-25+", 201], "120034056007": ["-26", 204], "120034050067": ["-26+", 213],
    "100234500607": ["+25-", 397], "100234056007": ["+26-", 386], "100234050067": ["+26", 395],
    "102340050607": ["-4", 272], "102304500607": ["-35", 306], "102304005607": ["-35+", 292],
    "102304056007": ["-36", 295], "102304050067": ["-36+", 304], "102034506007": ["-56", 338],
    "102034500067": ["-56+", 342], "102034005067": ["+56", 333], "120340050607": ["-24", 146],
    "102030045067": ["x46+", 356], "102030400567": ["+45x", 343], "100234000567": ["+25x", 379],
    "123004500607": ["o35-", 110], "102003400567": ["+35x", 358], "120034560007": ["-26o", 206],
    "102340005607": ["-45+", 258], "102340050067": ["-46+", 278], "102300045607": ["-34x", 320],
    "102003045607": ["+34", 370], "102340500607": ["-45", 281], "102034000567": ["x5", 323],
    "102030040567": ["x45+", 353], "102340560007": ["-46o", 265], "100200345607": ["+23x", 431],
    "120345000607": ["-25o", 160], "102000345067": ["x36+", 376], "123040050607": ["-34", 76],
    "102000345607": ["x3", 375], "123045000607": ["o63-", 90], "123004050607": ["o3", 105],
    "102345060007": ["o65-", 277], "123405000607": ["o54-", 50], "102030004567": ["^4", 357],
    "102003004567": ["+34x", 372], "123400050607": ["o4", 27], "123400500607": ["o45-", 41],
    "123400056007": ["o46-", 12], "102345000607": ["o5", 286], "123004050067": ["o36+", 108],
    "123004005607": ["o35+", 96], "102345600007": ["*6", 267], "123400050067": ["o46+", 37],
    "123450000607": ["*5", 55], "123004000567": ["o35x", 92], "123000045607": ["o34x", 124],
    "102340000567": ["-45x", 253], "102034560007": ["o6", 332], "100023456007": ["x26-", 440],
    "100002345607": ["^2", 458], "102000034567": ["^3", 378], "123400000567": ["o45x", 1]
}
gam_physic = {
    "102034050607": ["0", 336], "120034050607": ["-2", 210], "100234050607": ["+2", 392],
    "102304050607": ["-3", 301], "102034500607": ["-5", 341], "102034056007": ["-6", 330],
    "102034050067": ["+6", 339], "120304050607": ["-23", 175], "120034500607": ["-25", 215],
    "120034005607": ["-25+", 201], "100234005607": ["+25", 383], "120034050067": ["-26+", 213],
    "100234500607": ["+25-", 397], "100234056007": ["+26-", 386], "100234050067": ["+26", 395],
    "102340050607": ["-4", 272], "102304500607": ["-35", 306], "102304005607": ["-35+", 292],
    "102034005607": ["+5", 327], "102304050067": ["-36+", 304], "102034506007": ["-56", 338],
    "102034500067": ["-56+", 342], "100203450607": ["+23", 422], "120340050607": ["-24", 146],
    "102030045067": ["x46+", 356], "102030400567": ["+45x", 343], "100023450067": ["x26+", 444],
    "123004500607": ["o35-", 110], "102003400567": ["+35x", 358], "100023400567": ["x25", 435],
    "102340005607": ["-45+", 258], "102340050067": ["-46+", 278], "102300045607": ["-34x", 320],
    "102003045607": ["+34", 370], "102340500607": ["-45", 281], "100023450607": ["x2", 443],
    "102030040567": ["x45+", 353], "100023045607": ["x24+", 447], "100200345607": ["+23x", 431],
    "120345000607": ["-25o", 160], "102000345067": ["x36+", 376], "123040050607": ["-34", 76],
    "102304000567": ["x53-", 288], "100020345607": ["x23+", 452], "123004050607": ["o3", 105],
    "102345060007": ["o65-", 277], "102000304567": ["x34+", 377], "102030004567": ["^4", 357],
    "102003004567": ["+34x", 372], "123400050607": ["o4", 27], "123400500607": ["o45-", 41],
    "100234560007": ["+26o", 388], "102345000607": ["o5", 286], "123004050067": ["o36+", 108],
    "102345006007": ["o56-", 283], "100002304567": ["^24+", 460], "100020034567": ["x23", 455],
    "100002034567": ["^23+", 461], "120030004567": ["^42-", 231], "102345000067": ["+65o", 287],
    "102340000567": ["-45x", 253], "102034560007": ["o6", 332], "100023456007": ["x26-", 440],
    "102300004567": ["^43-", 322], "102000034567": ["^3", 378], "100000234567": ["+^2", 462]
}
gam_maj = '102034050607'
dic_codage = {}  # Dictionnaire des gammes et de leurs modes. PRÉALABLE
dic_indice = {}  # Dictionnaire, clé = Nom de la gamme, valeur = Numéro de la gamme. PRÉALABLE
dic_binary = {}  # Dictionnaire, clé = binaire, valeur = zob (['o45x', 1], '1000001'), (1, 2, '1000001'). PRÉALABLE
dic_gammic = {}  # Dico, clé = Nom + valeur énumérée, valeur = Énumération binarisée + degrés binarisés. PRÉALABLE
dic_force = {}  # Dictionnaire, clé = binaire, valeur = dic_codage avec le même binaire. PRÉALABLE
dic_colon = [""]  # Liste, clés binaires liées aux choix de conversions.
code_ages = {}  # Dictionnaire, clé = Numéro, valeur = Modes diatoniques énumérés.
liste_keys = []

def func_ima(ami, ute):
    """Fonction de récupération des données de la fonction def clic image(), ami = Paramètre de clic_image,
    ami[0] = Type de conversion : item_id : (1=ego, 2=anti-ego, 3=iso, 3=anti-iso, 2=int, 3=bin, 3=anti-bin).

        Processes the input 'ami' and modifies the list of binaries, integrating changes by user requests in 'ute'.
        This function interacts with several dictionaries that represent different
        aspects of musical range coding, binary keys, index rankings, and binary forces to update a list
        of binaries.

        :param ami: A list that represents user-specified binary ranges and associated metadata.
        It
                    includes coding information, binary representations, indices, and force mappings
                    used by the application.
        :type ami: List
        :param ute: Additional data or instructions that refine the binary processing or user requests.
        :type ute: Any.

        :return: A tuple containing the newly updated list of binaries and user instructions.
        :rtype: Tuple.
        """
    (lineno(), "ami[0]", ami[0], list(dic_codage)[0], "\n")
    # 160 ami[0] 2 (1, '123400000567') dic_codage, dic_binary, dic_indice, dic_force, dic_colon
    (lineno(), "func_ima", ami[0])
    # Ok = dic_codage, dic_binary, dic_indice, dic_force, dic_colon
    '''"# 160 ami[0] 1 [1, {'type': 'Entiers libres', '1000001': 1000001, : ami"
        * Ami = Les binaires selon la demande utilisateur.
    "# 160 ami[0] 1 {(1, '123400000567'): [(['o45x', 1], '1000001'), (1, 2, '1000001'), : dic_codage"
        * Dic_codage = Les gammes utilisées par l'appli songammes.py, dans un ordre original.
            Clef=(1, '123400000567'): => Clef[0] = Rang. Clef[1] = Forme numéraire des gammes.
            Val=(1, 2, '1000001') => Val[0] = Nom gamme ou numéro de colonne. Val[1] = Numéro de ligne ou degré.
                                        Val[2] = Code du mode binaire.
    "# 160 ami[0] 1 {'1000001': [(66, 5, '1000001')], '1000000': [(66, 2, '1000000')], : dic_binary"
        * Dic_binary = Clefs binaires et gammes relatives selon l'ordre original.
            Clef=Binaire. Val=[(66, 2, '1000000')] => Val[0] = Numéro de gamme ou colonne. 
                                                        Val[1] = Numéro de ligne ou degré.
                                                        Val[2] = Code du mode binaire.
    "# 160 ami[0] 1 {'o45x': [1], 'o46-': [2], 'o4': [3], 'o46+': [4], 'o45-': [5], : dic_indice"
        * Dic_indice = Clefs composées des noms des gammes et leurs indices des rangs des gammes.
    "# 160 ami[0] 1 {'1000111': [(3, '123400050607'), (43, '102034005067'), : dic_force"
        * Dic_force = Clefs binaires aux valeurs égales aux clefs de dic_codage original.
            Val[0] = Numéro de la gamme. Val[1] = Valeur énumérée de la gamme.
    def func_ima(ami):
        relance_instance = Relance(di_code=ami)
    # Accéder à la fonction gammes_arp dans la classe Relance.
    relance_instance.gammes_arp()'''

    "# Consultation du paramètre 'ami'. Modification de la liste des binaires (appliquée dans gammes_arp())."
    for ai in ami:  # Dictionnaire dans lequel se range l'ordre du typage.
        if type(ai) is dict:  # Dictionnaire à partir du deuxième niveau.
            keys_ai = list(ai.keys())
            for kai in keys_ai:  # Kai = Clef Binaire de mise à jour de l'utilisateur.
                if len(str(kai)) == 7:
                    (lineno(), "kai", kai)
                    dic_colon.append(kai)
                    (lineno(), "kai", kai, "dic_force", dic_force[str(kai)])
    "'dic_colon' = Paramètre nouvelle liste binaire"
    (lineno(), "func_ima dic_colon = Nouveaux binaires", dic_colon[:12], "ute", ute)
    return dic_colon, ute

class Relance(Toplevel):
    """Elle permet de relancer l'affichage avec une nouvelle orientation"""

    # Relance(dic_codage, dic_binary, dic_indice, dic_force, dic_colon, dic_titres).mainloop()
    def __init__(self, di_code=None, di_ages=None, di_bine=None, di_indi=None, di_fort=None, di_colon=None,
                 di_gamme=None, di_ute=None, di_solo=None, di_mode=None, di_lec=None, di_son=None, di_gam=None,
                 di_com=None, di_sec=None):
        """ Initialisation du visuel, sous forme d'un tableur.
        Di_code = dic_codage = Dictionnaire des gammes et de leurs modes.
        Di_ages = dic_ages = Dictionnaire, clé = Numéro, valeur = Modes diatoniques.
        Di_bine = dic_binary = Dictionnaire, clé = binaire, valeur = zob (['o45x', 1], '1000001'), (1, 2, '1000001').
        Di_indi = dic_indice = Dictionnaire, clé = Nom de la gamme, valeur = Numéro de la gamme.
        Di_fort = dic_force = Dictionnaire, clé = binaire, valeur = dic_codage avec le même binaire.
        Di_colon = dic_colon = Liste, clés binaires liées aux choix de conversions.
        Di_gamme = dic_gammic = Dictionnaire, clé = Nom + Énuméré, valeur = Binarisation + Degrés binarisés.
        Di_ute = tri...
            Initializes the class with provided dictionaries for codification, age,
            binaries, indices, and others.
            Sets up the layout and UI components for
            the main window including decorative elements, grids, and various display
            tables to show information related to binary arrays and musical scales.

            :param di_code: Dictionary containing codification for various scales.
            :param di_ages: Dictionary with keys as numbers and values as listed diatonic inversions.
            :param di_bine: Dictionary mapping binary keys with associated zob.
            :param di_indi: Dictionary where the key is the name of the scale and the value is its number.
            :param di_fort: Dictionary with keys as binary values and corresponding original dic_codage key.
            :param di_colon: Additional dictionary related to columns of the UI.
            :param di_gamme: Dictionary specific to the scales and their modes.
            :param di_ute: Utility dictionary for supporting UI operations.
            :param di_solo: Dictionary aimed for solo mode functionalities.
            :param di_mode: Descriptive dictionary detailing the modes available in the UI.
            :param di_lec: Dictionary designed for reading and processing input data.
            :param di_son: Dictionary for handling sound related functionalities.
            :param di_gam: Secondary dictionary supporting scale functionalities.
        """
        super().__init__()
        self.title("Base illusion")
        self.geometry("1824x1025+30+10")
        # self.protocol("WM_DELETE_WINDOW", self.quit())  # Pose problème au déroulement souhaité.
        self.borne = {1: "       "}
        self.quitter("1111111")
        self.focus_force()  # Donnez l'intérêt à la fenêtre
        "# Assemblage, clé = binaire, valeur = dic_codage.keys() à même binaire."
        self.dic_force = di_fort  # Dictionnaire clé=Binaire valeur=Clé_dic_codage original
        self.dic_codage = di_code  # Dictionnaire des gammes et de leurs modes.
        (lineno(), "di_code", di_code)
        "# di_ages  # Dictionnaire, clé = Numéro, valeur = Renversements diatoniques énumérés."
        self.di_ages = di_ages  # Le dictionnaire des formes énumérées.
        self.dic_binary = di_bine  # Clé = binaire, valeur = zob (['o45x', 1], '1000001'), (1, 2, '1000001')
        self.dic_indice = di_indi  # Dictionnaire, clé = Nom de la gamme, valeur = Numéro de la gamme.
        self.font_coins = "Courrier 18 bold"
        self.table_x = Canvas(self, width=60, height=30)  # Coin (haut, gauche) pour l'image favicon.
        self.table_x.grid(row=1, column=1)
        self.table_b = Canvas(self, width=60, height=884, bg="white")  # Colonne dédiée aux boutons binaires.
        self.table_b.grid(row=2, column=1)
        self.frame_b = Frame(self.table_b)
        self.frame_b.grid()
        self.table_c = Canvas(self, width=60, height=60, bg="white")  # Coin (bas, gauche) pour commentaire d'état.
        self.table_c.grid(row=3, column=1)

        "# Affichage du mode sélectionné pour information dans le canvas du bas à gauche."
        self.comment_sta = []
        if di_com:
            self.comment_sta = di_com
            # Ajouter du texte au Canvas
            self.table_c.create_text(30, 20, text=self.comment_sta[0], anchor="center", font=("arial", 10, "bold"))
            self.table_c.create_text(30, 40, text=self.comment_sta[1], anchor="center", font=("arial", 10, "bold"))
            (lineno(), "di_com", di_com)
            # 606 di_com ['Gammes', 'TriEgo']
        else:
            self.comment_sta = ["Modes", "TriEgo"]
            self.table_c.create_text(30, 20, text=self.comment_sta[0], anchor="center", font=("arial", 10, "bold"))
            self.table_c.create_text(30, 40, text=self.comment_sta[1], anchor="center", font=("arial", 10, "bold"))

        self.table_y = Canvas(self, width=84, height=30, bg="thistle")  # Coin (haut, droite).
        self.table_y.grid(row=1, column=3)
        self.table_o = Canvas(self, width=84, height=884, bg="thistle")  # Colonne dédiée aux binaires ordonnés.
        self.table_o.grid(row=2, column=3)
        self.table_w = Canvas(self, width=1656, height=60, bg="lightgray")  # Colonne dédiée aux options d'affichage.
        self.table_w.grid(row=3, column=2)
        self.table_z = Canvas(self, width=84, height=60, bg="thistle")  # Coin (bas, droite).
        self.table_z.grid(row=3, column=3)
        self.table_g = Canvas(self, width=1656, height=30, bg="seashell")  # Colonne dédiée aux boutons gammes.
        self.table_g.grid(row=1, column=2)
        self.frame_g = Frame(self.table_g)
        self.frame_g.grid()

        "# Mise en forme des tables dans la grille"
        "72/2=36/2=18, 30/2=15, 54=18+36"
        tx1, tx2 = (18, 2), (54, 30)
        self.table_x.create_oval(tx1, tx2, fill="gold", width=0)  # Table décorative.
        self.table_x.create_text(36, 15, fill="white", text="X", font=self.font_coins)  # Table décorative. Lettre X.
        tx1, tx2 = (2, 2), (1656, 30)
        self.table_g.create_oval(tx1, tx2, fill="blanchedalmond", width=0)  # Colonne dédiée aux boutons gammes.
        self.table_y.create_text(44, 16, fill="white", text="Y", font=self.font_coins)  # Table décorative. Lettre Y.
        self.table_z.create_text(44, 31, fill="white", text="Z", font=self.font_coins)  # Table décorative. Lettre Y.
        self.tableau = Canvas(self, width=1656, height=884, bg="ivory")  # Affichage des (noms, binaires) liées.
        self.tableau.grid(row=2, column=2)
        self.tableau.config(borderwidth=3, relief=RAISED)

        "# Initialisation métrique de l'affichage."
        self.police1, self.police2 = "Courrier 8 bold", "Courrier 10 bold"
        '''Pour une colonne binaire de soixante-six éléments, un intervalle de treize = Hauteur (67*13 = 871).
        Ayant un nombre de colonnes égal aux gammes (66), pulsif une pour les binaires = Longueur (67*24 = 1608).'''
        long1, haut1, long2, haut2 = 1656, 884, 1608, 871
        self.deb_col, self.deb_lin = (long1 - long2) // 2, (haut1 - haut2) // 2
        self.col, self.lin = 24, 13  # Espace entre les colonnes_26 et espace entre les lignes_13.
        self.tot_col, self.tot_lin = 67 * 24, 67 * 13

        "# Tracer le quadrillage principal en bleu clair."
        self.fin_col, self.fin_lin = self.deb_col + self.tot_col, self.deb_lin + self.tot_lin
        self.deb_col0, self.deb_lin0 = self.deb_col, self.deb_lin
        (lineno(), "col, lin", self.col, self.lin)
        (lineno(), "fin_col, fin_lin", self.fin_col, self.fin_lin)
        (lineno(), "deb_col, deb_lin", self.deb_col, self.deb_lin)
        (lineno(), "deb_col0, deb_lin0", self.deb_col0, self.deb_lin0)
        self.tab_rec, bouc = [], "0"
        self.tab_lig, lino = [], ""
        for i in range(68):
            "# Les rectangles peuvent être colorisés."
            if self.deb_col0 > 48:
                bouc = self.tableau.create_rectangle(self.deb_col0 - 5, self.deb_lin, self.deb_col0 + 6,
                                                     self.fin_lin + 3,
                                                     fill="", width=0)
                self.tab_rec.append(bouc)
                (lineno(), "tab_rec", self.tab_rec, "long", len(self.tab_rec))
                # 262 tab_rec [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, ] long 66
                # For rec in self.tab_rec: self.tableau.itemconfig(rec, fill="red") : Change la couleur.
                # For rec in self.tab_rec: coords = self.tableau.coords(rec) : Donne les coordonnées.
            linge = self.tableau.create_line(self.deb_col, self.deb_lin0, self.fin_col, self.deb_lin0,
                                             fill="lightblue", dash=(1, 1))  # Lignes horizontales.
            self.tab_lig.append(linge)
            self.tableau.create_line(self.deb_col0, self.deb_lin, self.deb_col0, self.fin_lin,
                                     fill="hotpink", dash=(1, 1))  # Lignes verticales.
            self.deb_col0 += self.col
            self.deb_lin0 += self.lin
        (lineno(), "tab_rec", self.tab_rec, "\ntab_lig", self.tab_lig, "long", len(self.tab_lig))
        # 335 tab_rec [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62,
        # tab_lig [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, ] long 68

        "# Initialisation de la colonne binaire."
        (lineno(), "di_colon", di_colon)
        if di_colon == [""]:
            di_colon = []
        self.colonne_bin = di_colon  # Première colonne aux modes binaires uniques. L’index de l'élément = La ligne.
        self.colonne_gam = {}  # Colonnes contenant les gammes de 1 à 66. Première ligne = Noms.
        self.colonne_lis = {}  # Le dictionnaire clé=N°gamme, valeur=Ensemble degrés à même niveau.
        self.gammes_bin = {}  # Dictionnaire des gammes aux modes binaires existants.
        self.gam_nat = []
        self.tag_nat = False
        if not self.colonne_bin and di_ute is None:
            self.tag_nat = True
            (lineno(), "Validation unique")
        (lineno(), "self.colonne_bin", self.colonne_bin)
        (lineno(), "self.colonne_gam", self.colonne_gam)

        "# Exécution de la fonction qui sert à alimenter les boutons horizontaux et verticaux."
        if len(di_colon) == 0:
            "# self.gammes_arp()  # Fonction découvertes binaires absentes."
            self.gammes_arp()  # Fonction découvertes des gammes binarisées.
            # int([self.dic_codage[(44, '102034050607')][0][1]] [0])
            passe1 = [self.dic_codage[(44, '102034050607')][0][1]]
            self.borne[1] = int(passe1[0])
            ("self borne[1]", self.borne[1], type(self.borne[1]), "|", None, lineno())
            # self borne[1] 1111111 <class 'int'> | None 281.
        else:
            "# self.gammes_log()  # Fonction découvertes des binaires créées."
            self.gammes_log()  # Fonction découvertes des gammes binarisées.
            self.borne[1] = di_colon[0]
            ("self borne[1]", self.borne[1], type(self.borne[1]), "|", di_colon, lineno())
            # self borne[1] 1000001 <class 'int'> | 1000001 287.

        "# Mise en place des listes comparatives"
        self.test_bin1, self.test_bin2 = [], []

        # Clé = iso, valeur = (iso, int, bin, hex, oct)
        self.dic_ego, self.dic_iso, self.dic_int = {}, {}, {}
        self.dic_ego_inv, self.dic_iso_inv, self.dic_int_inv = {}, {}, {}
        self.mod_type = []
        self.dic_trans = {}
        self.table_bin = self.colonne_bin.copy()
        self.test_bin2 = self.colonne_bin.copy()
        (lineno(), "colonne_bin", self.colonne_bin, "\n colonne_gam", self.colonne_gam.keys())
        (lineno(), "Long colonne_bin", len(self.colonne_bin), "Long colonne_gam", len(self.colonne_gam.keys()))

        "# Visionner les modes binaires par l'écriture."
        if self.colonne_bin.count("") == 0:
            self.colonne_bin.insert(0, "")
            self.colonne_bin.insert(0, "")
        elif self.colonne_bin.count("") == 1:
            self.colonne_bin.insert(0, "")
        (lineno(), " colonne_bin", self.colonne_bin[:6])
        deb_col1, deb_lin1 = self.deb_col + 6, self.deb_lin + 26
        (lineno(), "deb_col1, deb_lin1", deb_col1, deb_lin1)
        for colin in range(len(self.colonne_bin)):
            self.tableau.create_text(deb_col1, deb_lin1, text=self.colonne_bin[colin], font=self.police1)
            deb_lin1 += self.lin
            self.test_bin1.append(self.colonne_bin[colin])
            (lineno(), " colonne_bin[colin]", self.colonne_bin[colin], "colin", colin)

        "# Mise en place des boutons binaires sur le panneau gauche."
        self.tri = di_ute
        (lineno(), "self.tri", self.tri)
        coq0 = 0
        poli0, poli1 = Font(size=5, weight="bold"), Font(size=7, weight="bold")
        for colin in range(len(self.table_bin)):
            if self.table_bin[colin]:  # Self.table_bin = self.colonne_bin.copy(). Avant l'ajout des ("","")
                nom0 = self.table_bin[colin]
                self.table_bin[colin] = Button(self.frame_b, font=poli0, text=nom0,
                                               command=lambda bab=self.table_bin[colin], ages=self.di_ages:
                                               self.bouton_bin(bab, ages))
                self.table_bin[colin].grid(pady=1)
                coq0 += 1

        "# Résultat des tests sur binaires."
        if len(self.test_bin1) != len(self.test_bin2):
            if self.test_bin1.count("") == 0:
                self.test_bin1.insert(0, "")
                self.test_bin1.insert(0, "")
            elif self.test_bin1.count("") == 1:
                self.test_bin1.insert(0, "")
            if self.test_bin2.count("") == 0:
                self.test_bin2.insert(0, "")
                self.test_bin2.insert(0, "")
            elif self.test_bin2.count("") == 1:
                self.test_bin2.insert(0, "")
        for stb in range(len(self.test_bin1)):
            if self.test_bin1[stb] == self.test_bin2[stb]:
                (lineno(), self.test_bin1[stb])  # Pour transfert sur le classeur Excel

        "# Repérer les gammes ayant deux ensembles de degrés séparés."
        multi, sage, passe = {}, 0, 0
        for k_bis in self.colonne_gam.keys():
            k_val = self.colonne_gam[k_bis]
            (lineno(), "k_bis", k_bis, "k_val", k_val)
            if k_bis[1] == 0:
                passe = 0
                sage = k_val[0]
                multi[sage] = []
                (lineno(), "k_val", k_val[0], type(k_val[0]), "k_bis", k_bis)
            if len(k_val) > 1:
                passe += 1
                multi[sage].append(passe)
            (lineno(), "k_bis", k_bis, "passe", passe, "multi[sage]", multi[sage])
        for k_sage in multi.keys():
            if len(multi[k_sage]) < 2:
                multi[k_sage] = {}

        "# Écriture des noms et les degrés des soixante-six gammes."
        #  gammes_bin = Les gammes aux modes binaires existants.
        # 342 self.gammes_bin {'x26-': 'Ok', '*5': 'Ok', '-34': 'Ok', 'o63-': 'Ok', 'o34x': 'Ok', '-25o': 'Ok',
        # '-45x': 'Ok', '-46o': 'Ok', '*6': 'Ok', 'o65-': 'Ok', '+34x': 'Ok', 'x36+': 'Ok', '^3': 'Ok', '^2': 'Ok',
        # '+35x': 'Ok', '+23x': 'Ok', 'o35-': 'Ok', '+45x': 'Ok', 'x46+': 'Ok', '^4': 'Ok', 'o6': 'Ok', '+56': 'Ok',
        # '-56': 'Ok', '-56+': 'Ok', '+25-': 'Ok', '-26+': 'Ok', '+26-': 'Ok', '+26': 'Ok', '+2': 'Ok', '-34x': 'Ok',
        # '+34': 'Ok', 'x3': 'Ok', 'o5': 'Ok', '-35': 'Ok', '+6': 'Ok'}
        (lineno(), "self.colonne_gam", self.colonne_gam, "")
        # 467 self.colonne_gam {(1, 0): ['0'], (1, 2): ['1'], (1, 3): ['2'], (1, 4): ['3'], (1, 5): ['4'],
        (lineno(), " *********************************************** ")
        coq2, t_noms = 1, []  # 't_noms' Liste les noms organisés
        color1, color2 = "black", "lavender"
        mul_bin = False  # Si la gamme en cours a plusieurs ensembles de degrés.
        col0, lin0 = self.deb_col + 24, self.deb_lin + 26
        recaler = True
        for k_col, v_lin in self.colonne_gam.items():
            col1, sig = (k_col[0] * self.col) + col0, 0
            (lineno(), "colonne_gam", self.colonne_gam[k_col], "mul_bin", mul_bin)
            for val in v_lin:
                if k_col[1] == 0:
                    if val in self.gammes_bin.keys():
                        color1 = "saddlebrown"
                        color2 = "pink"
                    else:
                        color1 = "black"
                        color2 = "lavender"
                    t_noms.append(self.colonne_gam[k_col][0])
                    (lineno(), self.colonne_gam[k_col][0])
                lin1 = (k_col[1] * self.lin) + lin0
                (lineno(), "___   col1", col1, "lin1", lin1, "v_lin", v_lin)
                (lineno(), "*** k_col", k_col[1], "val", type(val), len(val), val)
                if len(val) > 1:  # Le dictionnaire 'multi' informe sur les multilistes.
                    if val in multi.keys() and multi[val]:
                        mul_bin = True  # print("val", val, colonne_gam[k_col], "multi", multi[val])
                    else:
                        mul_bin = False
                if len(v_lin) == 1:  # Écriture des noms en quinconce pour une meilleure lisibilité.
                    coq2 += 1
                    if k_col[1] == 0:
                        if recaler:
                            sig = -12
                            row0 = 1
                            recaler = False
                        else:
                            row0 = 2
                            recaler = True
                        gam_bouton = Button(self.frame_g, font=poli1, text=str(val), bg=color2,
                                            command=lambda bag=str(val), ages=self.di_ages:
                                            self.bouton_bin(bag, ages))
                        gam_bouton.grid(row=row0, column=coq2)
                    if v_lin[0] == '1':
                        col3, lin3 = (col1 - 6, lin1 - 6), (col1 + 6, lin1 + 6)
                        self.tableau.create_rectangle(col3, lin3, fill="gold", width=0)
                    self.tableau.create_text(col1, lin1 + sig, text=str(val), font=self.police2, fill=color1)
                    (lineno(), "col1, lin1 + sig", col1, lin1 + sig)
                else:  # 'len(v_lin)'. Quand, plusieurs degrés correspondent à un même emplacement.
                    ce = len(v_lin)
                    col2, lin2 = (col1 - ce, lin1 - ce), (col1 + ce, lin1 + ce)
                    if mul_bin:
                        # print("multi=", mul_bin, "col_gam=", multi[colonne_gam[k_col[0], 0][0]],
                        # colonne_gam[k_col[0], 0][0])
                        # multi= True col_gam= [1, 2] o46-
                        cran = -6
                        for ici in v_lin:
                            if ici == '1':
                                col3, lin3 = (col1 - 12, lin1 - 6), (col1, lin1 + 6)
                                self.tableau.create_rectangle(col3, lin3, fill="gold", width=0)
                            self.tableau.create_text(col1 + cran, lin1, text=ici, font=self.police2, fill="maroon")
                            (lineno(), "col1 + cran, lin1", col1 + cran, lin1)
                            cran += 12
                            # print("Ici", ici, "col2, lin2", col2, lin2, val, "v_lin", v_lin,
                            # colonne_gam[k_col[0], 0][0])
                    else:
                        col3, lin3 = (col1 - 7, lin1 - 7), (col1 + 7, lin1 + 7)
                        if '1' in v_lin:
                            self.tableau.create_rectangle(col3, lin3, fill="gold", width=0)
                    self.tableau.create_oval(col2, lin2, fill="black", width=0)
                    # print("*** ELSE k_col", k_col, "col2", col2, "lin2", lin2, "\t len(v_lin)", v_lin, "val", val)
                    # print("", )
                    break
        (lineno(), "t_noms", t_noms, "[:6]", len(t_noms), "\n __________________________________________________")

        "# Alimentation du dictionnaire di_gamme. Correspondance simplifiée de 'self.dic_codage'"
        "# Di_gamme = dic_gammic = Dictionnaire, clé = Nom + Énuméré, valeur = Binarisation + Degrés binarisés."
        self.gammic = di_gamme  # Dictionnaire, clé = nom, énumérée, valeur = énumérée et modes binaires diatoniques.
        self.gam_gen = [int(gg[1]) for gg in self.gammic.keys()]  # Ne récupère que les formes énumérées des clefs.
        self.gam_iso, self.iso2 = self.gam_gen.copy(), {}
        (lineno(), "gammic", "self.gammic", "\ngam_gen", self.gam_gen)
        # 870 870 gammic {('o45x', '123400000567'): ['111100000111', '1000001', '1000001', '1000001', '1000001',
        # gam_gen [123400000567, 123400056007, 123400050607, 123400050067, 123400500607, 123405000607,
        #
        "# Code_âges est un dico-attribut de hors classe Relance (di_ages) : di_ages = self.di_ages."
        # 450 code_ages {44: ['102034050607', '102304050670', '120304056070', '102030450607', '102034050670',
        self.gam_con = {}  # Dico, clé = numéro de gamme, valeur = mode diatonique de type conteneur.
        self.age_con = {}  # Dico de liaison, clé = énuméré, valeur = conteneur.
        self.con_age = {}  # Dico de liaison, clé = conteneur, valeur = énuméré.
        # Se servir de code_ages pour transformer les énumérations en conteneurs.
        ("# self.di_ages = di_ages  # Le dictionnaire des formes énumérées."
         "# 908 Contient_self.di_ages ['100000234567', '123456700000', '123456000007', '123450000067'] 1ére Clé 1"
         "# 895 scg 1 cag 123450000067 gam_con ['000500', '005000', '050000', '500000', '000000', '000005', '000050']")
        for scg in self.di_ages.keys():
            self.gam_con[scg] = []
            for cag in self.di_ages[scg]:
                "# Compter le contenu des intervalles dans le mode cag."
                tour, vide, conte, c_vide = True, 0, "", 0
                for eag in cag:
                    if eag != "0":
                        if tour:
                            tour = False
                        else:
                            conte += str(vide)
                            vide = 0
                    else:
                        vide += 1
                    "# Il manque l'intervalle entre sept et l'octave."
                    if eag == "7":
                        ea1 = 0
                        for ea in conte:
                            if ea != "0":
                                ea1 += int(ea)
                        "# Si ea1 < 5 ; il manque l'intervalle entre sept et l'octave."
                        if ea1 <= 5:  # Le nombre d'intervalles complet est égal à cinq.
                            if ea1 < 5:
                                r_ea1 = 5 - ea1
                                conte += str(r_ea1)
                            elif ea1 == 5:
                                conte += "0"
                        (lineno(), cag, "eag", eag, "conte", conte, "ea1 =", ea1)
                self.gam_con[scg].append(conte)
                (lineno(), "scg", scg, "cag", cag, "conte", conte, "c_vide", c_vide)
            (lineno())
            (lineno(), "scg", scg, "cag", cag, "gam_con", self.gam_con[scg])
            # 895 scg 44 cag 120304506070 gam_con ['110111', '101110', '011101', '111011', '110110', '101101', '011011']

        "# Écriture sur le fichier 'gamme_majeure.txt' des 66 formes énumérées primordiales."
        self.gam_ego, self.ego2 = [], {}
        self.liste_iso1, self.liste_ego1 = [], []
        if self.tag_nat:
            pre_gamme = open('gamme_majeure.txt', 'w')
            for tn in t_noms:
                for sgg in self.gammic.keys():
                    if tn == sgg[0]:
                        pre_gamme.write(sgg[1] + "\n")
                        (lineno(), "sgg1", sgg[1])
            pre_gamme.close()

        "# Recopie des 66 formes énumérées primordiales dans le dictionnaire 'self.gam_ego'."
        with open('songammes\gamme_majeure.txt', 'r') as lec_gamme:
            for lg in lec_gamme:
                self.gam_ego.append(int(lg.strip()))
        (lineno(), "gam_ego", self.gam_ego, "Longueur", len(self.gam_ego))
        # 926 gam_ego ['102034050607', '102034500607', '123400000567', '123400050067', '123400056007',
        ("[EGO] = Organisation composée à partir de la gamme naturelle......... 'self.gam_ego'"
         "[ISO] = Organisation composée à partir du fichier `globdicTcoup.txt`. 'self.gam_iso'"
         "[INT] = Organisation croissante des éléments [ISO = EGO]............ 'self.gam_int'"
         "  Il y a trois dictionnaires pour deux ordonnances[EGO+ISO] :"
         "      Au démarrage de cette application, le type organisationnel est |MODES|,"
         "      RAPPEL ; chacune des organisations est composée des soixante-six gammes."
         "      |MODES66g|. [ORGANES] = mêmes gammes aux sept modulations diatoniques."
         "              La gamme aux sept notes (CDEFGAB), alias modes diatoniques binarisés."
         "              Les modes sont possiblement mis en ordre numérique d'état ou bien, croissant et décroissant")
        "Par défaut : "
        ("Valeur-MODES_BINARISÉS = Le mode tonique binarisé de chaque gamme, exp majeur[1111111]"
         " ♦ |MODES66gam462mog1386org|, gam_[Numéro de gamme], modes diatoniquement ordonnés (CDEFGAB)."
         " ♦    Au démarrage, seules les gammes toniques primordiales sont agencées. Elles font leurs suites"
         " ♦    diatoniques suivant les gammes. Sous la forme de sept modes binarisés à chaque fois."
         "Valeur-GAMMES_ÉNUMÉRÉES = La gamme est énumérée façon binaire, exp majeur[102034050607]"
         " ♦ Les gammes sont représentées numériquement[102034050607] et elles ont une signification numérique."
         " ♦ Les gammes sont celles qui supportent les tris [EGO+ISO+INT], ce ne sont pas elles qui vont être triées."
         " ♦ Chaque gamme possède sept modes qui en type 'Gammes', ils sont des valeurs énumérées à trier."
         "Valeur-CONTIENT_INTERVALLES = La gamme des intervalles, exp majeur[1101110], exp o3[1002110]"
         " ♦ Les gammes sont représentées numériquement[102034050607] et elles ont une signification numérique."
         " ♦ Les gammes sont celles qui supportent les tris [EGO+ISO+INT], ce ne sont pas elles qui vont être triées."
         " ♦ Chaque gamme possède sept modes qui en type 'Contient', ils sont des valeurs conteneurs à trier.")
        if di_gam == "Modes":  # Modes binarisés = Le mode tonique binarisé de chaque gamme.
            (lineno(), "di_gam Modes par défaut", self.gammic.keys(), "list(self.gammic.keys())[:2]")
            (lineno(), "dic_binary.keys()", list(self.dic_binary.keys())[:3])
            (lineno(), "Modes_self.di_age", self.di_ages[1][3:])
            # 937 di_gam Modes par défaut self.gammic.keys() [('o45x', '123400000567'), ('o46-', '123400056007')]
            # 937 self.gammic = {('o45x', '123400000567'): ['111100000111', '1000001', '1000001', '1000001', '1000001',
            #       '1000000', '1000001', '1000001'], ('o46-',
            # 938 dic_binary.keys() ['1000001', '1000000', '1000101']
            # 939 Modes_self.di_ages ['100000234567', '123456700000', '123456000007', '123450000067']
            ("Valeur-MODES_BINARISÉS = Le mode tonique binarisé de chaque gamme, exp majeur[1111111]"
             " ♦ |MODES66gam462mog1386org|, gam_[Numéro de gamme], modes diatoniquement ordonnés (CDEFGAB)."
             " ♦    Au démarrage, seules les gammes toniques primordiales sont agencées. Elles font leurs suites"
             " ♦    diatoniques suivant les gammes. Sous la forme de sept modes binarisés à chaque fois.")
        elif di_gam == "Gammes":  # Gammes énumérées = La gamme est énumérée façon binaire.
            (lineno(), "di_gam Gammes", "self.gammic.keys()", list(self.gammic.keys())[:2])
            (lineno(), "dic_binary.keys()", list(self.dic_binary.keys())[:3])
            (lineno(), "Gammes_self.di_age", self.di_ages[1][3:])
            # 894 di_gam Gammes self.gammic.keys() [('o45x', '123400000567'), ('o46-', '123400056007')]
            # 895 dic_binary.keys() ['1000001', '1000000', '1000101']
            # 896 Gammes_self.di_age ['100000234567', '123456700000', '123456000007', '123450000067']
            ("Valeur-GAMMES_ÉNUMÉRÉES = La gamme est énumérée façon binaire, exp majeur[102034050607]"
             " ♦ Les gammes sont représentées numériquement[102034050607] et elles ont une signification numérique."
             " ♦ Les gammes sont celles qui supportent les tris [EGO+ISO+INT], elles ne vont pas être triées."
             " ♦ Chaque gamme possède sept modes qui en type 'Gammes', ils sont des valeurs énumérées à trier.")
        elif di_gam == "Contient":  # Contient intervalles = La gamme des intervalles.
            (lineno(), "di_gam Contient", "self.gammic.keys()", list(self.gammic.keys())[:2])
            (lineno(), "dic_binary.keys()", list(self.dic_binary.keys())[:3])
            print(lineno(), "Contient_self.di_age", self.di_ages[1][3:], "1ére Clé", list(self.di_ages.keys())[0])
            # 906 di_gam Contient self.gammic.keys() [('o45x', '123400000567'), ('o46-', '123400056007')]
            # 907 dic_binary.keys() ['1000001', '1000000', '1000101']
            # 908 Contient_self.di_age ['100000234567', '123456700000', '123456000007', '123450000067'] 1ére Clé 1
            ("Valeur-CONTIENT_INTERVALLES = La gamme des intervalles, exp majeur[1101110], exp o3[1002110]"
             " ♦ Les gammes sont représentées numériquement[102034050607] et elles ont une signification numérique."
             " ♦ Les gammes sont celles qui supportent les tris [EGO+ISO+INT], elles ne vont pas être triées."
             " ♦ Chaque gamme possède sept modes qui en type 'Contient', ils sont des valeurs conteneurs à trier.")

        "# Oups !"
        if self.borne[1] != 1111111:
            (lineno(), "Borne", self.borne[1])
            self.protocol("WM_DELETE_WINDOW", self.quitter("0000000"))

        "# Traitement des images préalable."
        self.images_liste = ["songammes\BoutonTriEgo.png", "songammes\BoutonAntiEgo.png", "songammes\BoutonTriIso.png",
                             "songammes\BoutonAntiIso.png", "songammes\BoutonTriInt.png", "songammes\BoutonAntiInt.png"]
        self.images_references = []
        self.charger_image()

        "# Zone de l'interface aux actions dédiées à l'affichage des gammes."
        # self.table_w = Canvas(self, width=1656, height=60, bg="lightgray") # Colonne dédiée aux options d'affichage.
        "# Création des cadres destinés à recueillir les boutons-radio."
        largeur_cad, hauteur_cad = 1656 // 7, 100
        self.frame_lab = ["Toutes ou une seule gamme ?",
                          "En DO ou tonalité dynamique ?",
                          "Quel est votre ordonnance ?",
                          "Couper l'audio ?",
                          "Forme binarisée ?"]
        self.color_cad, rng = ["red", "orange", "yellow", "green", "skyblue", "mediumpurple", "violet"], 0
        self.table_cad = []
        for yes in range(7):
            frame = Frame(self.table_w, width=largeur_cad, height=hauteur_cad, bg=self.color_cad[yes], relief=GROOVE)
            frame.grid(row=1, column=yes, ipadx=1)
            frame.grid_propagate(False)
            self.table_cad.append(frame)
            # Ajout des labels dans les frames
            if yes < len(self.frame_lab):
                label = Label(frame, text=self.frame_lab[yes], bg=self.color_cad[yes])
                label.grid(row=1, column=1)

        (" Radio-bouton pour sélectionner le type de lecture."
         "# Conditionner sur une seule gamme est lue, ou sur toutes les gammes.")
        if not di_solo:
            self.zone_w0 = StringVar(self.table_cad[0], value="Poly")
        else:
            self.zone_w0 = StringVar(self.table_cad[0], value=di_solo)
        rad_bou0 = Radiobutton(self.table_cad[0], variable=self.zone_w0, value="Poly", text="Global",
                               bg=self.color_cad[rng])
        rad_bou0.grid(row=2, column=1)
        rad_bou01 = Radiobutton(self.table_cad[0], variable=self.zone_w0, value="Solo", text="Unique",
                                bg=self.color_cad[rng])
        rad_bou01.grid(row=3, column=1)

        ("# Radio-bouton pour sélectionner le type de développement diatonique entre (statique et dynamique)."
         "Le choix statique a toutes les gammes en DO. Le choix dynamique module les tonalités.")
        if not di_mode:
            self.zone_w1 = StringVar(self.table_cad[1], value="Sta")
        else:
            self.zone_w1 = StringVar(self.table_cad[1], value=di_mode)
        rng += 1
        rad_bou1 = Radiobutton(self.table_cad[1], variable=self.zone_w1, value="Sta", text="Statique",
                               bg=self.color_cad[rng])
        rad_bou1.grid(row=2, column=1)
        rad_bou2 = Radiobutton(self.table_cad[1], variable=self.zone_w1, value="Dyn", text="Dynamique",
                               bg=self.color_cad[rng])
        rad_bou2.grid(row=3, column=1)

        ("# Radio-bouton pour sélectionner le type de lecture à réaliser :"
         "  1. Ordre des groupes. Il est ce qui ressort en premier."
         "  2. Ordre diatonique. Il respecte la séquence des notes diatoniques."
         "  3. Ordre hertzien. Il suit les fréquences allant du grave à l'aigü.")
        if not di_lec:
            self.zone_w2 = StringVar(self.table_cad[2], value="Groupe")
        else:
            self.zone_w2 = StringVar(self.table_cad[2], value=di_lec)
        rng += 1
        rad_bou3 = Radiobutton(self.table_cad[2], variable=self.zone_w2, value="Groupe", text="Groupement",
                               bg=self.color_cad[rng])
        rad_bou3.grid(row=2, column=1)
        rad_bou4 = Radiobutton(self.table_cad[2], variable=self.zone_w2, value="Diatone", text="Diatonique",
                               bg=self.color_cad[rng])
        rad_bou4.grid(row=3, column=1)
        rad_bou5 = Radiobutton(self.table_cad[2], variable=self.zone_w2, value="Hertz", text="Hertzien",
                               bg=self.color_cad[rng])
        rad_bou5.grid(row=4, column=1)

        "# Radio-bouton pour ne pas effectuer l'écoute audio des gammes."
        if not di_son:
            self.zone_w3 = StringVar(self.table_cad[3], value="Inaudible")
        else:
            self.zone_w3 = StringVar(self.table_cad[3], value=di_son)
        rng += 1
        rad_bou6 = Radiobutton(self.table_cad[3], variable=self.zone_w3, value="Inaudible", text="Couper l'audio",
                               bg=self.color_cad[rng])
        rad_bou6.grid(row=2, column=1)
        rad_bou7 = Radiobutton(self.table_cad[3], variable=self.zone_w3, value="Audible", text="Entendre",
                               bg=self.color_cad[rng])
        rad_bou7.grid(row=3, column=1)

        ("# Radio-bouton pour sélectionner les binarisations à traiter. Les degrés modaux ou les gammes primordiales."
         "Valeur-Modes binarisés = Le mode tonique binarisé de chaque gamme, exp majeur[1111111]"
         "Valeur-Gammes énumérées = La gamme est énumérée façon binaire, exp majeur[102034050607]"
         "Valeur-Contient intervalles = La gamme des intervalles, exp majeur[1101110], exp o3[1002110]")
        if not di_gam:
            self.zone_w4 = StringVar(self.table_cad[4], value="Modes")
        else:
            self.zone_w4 = StringVar(self.table_cad[4], value=di_gam)
        rng += 1
        rad_bou8 = Radiobutton(self.table_cad[4], variable=self.zone_w4, value="Modes", text="Modes binarisés",
                               bg=self.color_cad[rng])
        rad_bou8.grid(row=2, column=1)
        rad_bou9 = Radiobutton(self.table_cad[4], variable=self.zone_w4, value="Gammes", text="Gammes énumérées",
                               bg=self.color_cad[rng])
        rad_bou9.grid(row=3, column=1)
        rad_bou10 = Radiobutton(self.table_cad[4], variable=self.zone_w4, value="Contient", text="Contient intervalles",
                                bg=self.color_cad[rng])
        rad_bou10.grid(row=4, column=1)

        "# Traitement de la sonorisation des gammes retournées du module 'gammes_audio.py'"
        self.gam_son, self.gam_son1 = None, None  # , 'self.gam_son1'. Afin d'ordonner les clefs.
        self.frequencies = []  # Liste [degré, fréquence].
        self.dic_donne = {}  # Dictionnaire, clé = nom de gamme + degré, valeur = numéro de gamme + ligne.
        self.all_rectangles = []  # Cela correspond aux fonds des notes diatoniques.
        self.all_textes = []  # Et ceci, à l'écriture des notes diatoniques.
        self.dic_multiples = {}  # Le dictionnaire qui rassemble les modes aux mêmes binaires.
        self.gam_diatonic = {}  # Le dictionnaire des notes diatoniques à la gamme.
        self.num_static = {}  # Dictionnaire, clé = Nom, valeur = Numéro.
        self.majeure = '102034050607'  # La gamme de référence.
        self.modaux = ["I", "II", "III", "IV", "V", "VI", "VII"]  # Liste des degrés modaux.
        self.message = []  # Tableau d'enregistrement des infos destinées à la 'messagebox'.
        self.tab_ind = []  # Tableau utilisé pour gérer la coloration des lignes des boutons binaires.

        "# Déclarations utiles à la contruction des tables de binarisations."
        self.age_dict, self.con_dict = {}, {}  # Clés = enumérée ou conteneur, valeurs = formes binaires.
        self.bin_age_ego, self.bin_age_iso, self.bin_con_ego, self.bin_con_iso = [], [], [], []
        self.bin_age_ego11, self.bin_age_iso11 = [], []  # Ampleur _age_ des sections à onze.
        self.bin_age_ego22, self.bin_age_iso22 = [], []  # Ampleur _age_ des sections à vingt-deux.
        self.bin_age_ego33, self.bin_age_iso33 = [], []  # Ampleur _age_ des sections à trente-trois.
        self.bin_con_ego11, self.bin_con_iso11 = [], []  # Ampleur _con_ des sections à onze.
        self.bin_con_ego22, self.bin_con_iso22 = [], []  # Ampleur _con_ des sections à vingt-deux.
        self.bin_con_ego33, self.bin_con_iso33 = [], []  # Ampleur _con_ des sections à trente-trois.
        self.bin_age_int_ego66, self.bin_age_int_iso66 = [], []  # Ampleur de section à soixante-six.
        self.bin_con_int_ego66, self.bin_con_int_iso66 = [], []  # Ampleur de section à soixante-six.
        self.age_pass11ego, self.age_pass22ego, self.age_pass33ego = [], [], []  # Par ici les secteurs age ego.
        self.age_pass11iso, self.age_pass22iso, self.age_pass33iso = [], [], []  # Par ici les secteurs age iso.
        self.con_pass11ego, self.con_pass22ego, self.con_pass33ego = [], [], []  # Par ici les secteurs con ego.
        self.con_pass11iso, self.con_pass22iso, self.con_pass33iso = [], [], []  # Par ici les secteurs con iso.
        ("Bin_age = Binaires énumérés. Bin_con = Binaires conteneurs. Bin_int = Binaires globaux."
         "Les binaires globaux viennent de la réunion des types age_con, qui contrairement aux types sités"
         "qui traitent les binaires par séquence diatonique. Les binaires globaux sont issus du traitement"
         "de toutes les énumérations toutes les diatoniques confondues de age_con.")
        self.transcript, self.transforme = {}, {}  # Dictionnaires des listes des multiplistes
        self.transcript, self.transforme = {}, {}  # Dictionnaires des listes des multiplistes

        "# Réception du message demandant le taux de séparation, soit 11 soit 22 soit 33 ou 66."
        (lineno(), "choix di_sec", di_sec)
        self.retour_bouton = 11
        if di_sec:
            self.choix_box = di_sec
        else:
            self.choix_box = self.retour_bouton
        (lineno(), "choix", self.choix_box, "retour_bouton", self.retour_bouton)  # 1141 choix 22 retour_bouton 11


    def k_num_fonc(self):
        """Traitement des sections"""
        k_num_fin = False
        if self.zone_w4.get() in ("Gammes", "Contient"):
            "# Création d'un dictionnaire trafiqué pour usage FONCTIO reforme_bin()."
            # "* ____________________________ MÉTHODES DES DICTIONNAIRES SELF.GAM_ISO ET EGO"
            ("On travaille avec {self.iso2} et {self.ego2}"
             "Les listes[ego_iso = primordiales énumérées], une clé pour deux indices (trié/non trié).")
            # "* ____________________________ RAPPEL DES NÉCESSITÉS
            ("      Self.gammic : dico[nom_gamme/tonique énumée] = 7 modes binaires 1 diatonie."
             "      Self.dic_indice[nom_gamme] = 1 numéro_gamme."
             "      Self.gam_con : dico[numéro_gamme] = 7 modes conteneurs 1 diatonie."
             "      Self.di_ages : dico[numéro_gamme] = 7 modes énumérés 1 diatonie]"
             "          Self.gam_ego : liste les 66 gammes énumérées dans un ordre majeur."
             "          Self.gam_iso : liste les 66 gammes énumérées dans un ordre premier.")
            # "* ____________________________ DÉBUT DU TRAITEMENT
            ("Commencer avec self.gammic, parce qu'il a une clef subjective ; un alias (nom_gamme/tonique énumée)."
             "L'alias a une tonique énumérée et sept modes binarisés. Le nom avec self.dic indice a un numéro de gamme."
             "(nom_gamme/tonique_énumée/numéro_gamme). Nous bâtissons un dictionnaire triple_clé[nom, énuméré, numéro]."
             "Et, pour chaque clé, il y a sept 'Contient' et sept 'Gammes'."
             "On va commencer par self.gam_iso/ego, car ils ont les énumérations ordonnées."
             "À chaque gamme énumérée correspond sept modes énumérés diatoniques qu'il faut ranger. Les énumérations"
             "captent les indices qui mènent à la bonne position dans la liste des modes binarisés de self.gammic.")
            # * "Le but est de concevoir un dico qui aurait tous les éléments nécessaires pour les traitements."
            # * "Afin de répondre aux demandes des différents ordres et construire une réponse binarisée."
            # * "Ce dico est créé en ligne 1170 :"
            # * "self.age_dict, self.con_dict = {}, {}  # Clés = enumérée ou conteneur, valeurs = formes binaires."
            clefs_triadic = []  # Liste des clés de gammic.keys + Numéros des gammes.
            gammic_keys = []  # Liste des clés de gammic.keys.
            'Self.di_ages[Numéro_gamme] = Les sept modes diatoniques énumérés.'         # Accès aux 7 modes diatoniqes
            'Self.gam_con[Numéro_gamme] = Les sept modes aux intervalles quantifiés.'   # liés à chacune des 66 gammes.
            # , di_ages et gam_con produisent les exactes positions modales des diatonies.
            "# Boucles 'for' d'initialisation de gammic_keys et clefs_triadic."
            for g_key in self.gammic.keys():
                gammic_keys.append(g_key)  # Liste des clés de gammic.keys_66, nom_gamme/tonique énumée.
                t_key = list(g_key) + [self.dic_indice[g_key[0]]]  # Donne la clé triadique_66, nom/énumation/numéro.
                clefs_triadic.append(t_key)  # t_key[:2] = list(g_key)  # Liste les clés triadiques_66.
                (lineno(), "_  g_key", g_key, "t_key", t_key)
                # 1130 _  g_key ('o45x', '123400000567') t_key ['o45x', '123400000567', 1]

            ("# Construction self.age_dict, self.con_dict. Évite la recherche des indices."
             "Création de deux listes de clefs :"
             "  1   Énumérée : les 66 clefs age sont triées séparemment............. self.enum_age"
             "  2   Conteneur : les 66 clefs con sont triées séparemment............ self.cont_con")
            zerf = 0
            for cle_t in clefs_triadic:
                cle_g = tuple(cle_t[:2])  # Préparation de la clé de self.gammic.
                (lineno(), "clef", cle_g, "\n ... gammic", self.gammic[cle_g])
                (lineno(), "age", self.di_ages[cle_t[2]], "\n ... con", self.gam_con[cle_t[2]])
                zero = 0
                "# Le dico self.age_dict[cle_t[2]]. Clé énumérée. Valeur définitivement binaire."
                for clef_c1 in self.di_ages[cle_t[2]]:  # La cle_t[2] est une énumération
                    zero += 1
                    self.age_dict[clef_c1] = self.gammic[cle_g][zero]
                    if zero == 1:  # Quand zéro = 1, c'est l'emplacement de la clef tonique.
                        zerf += 1
                        (lineno(), "clef_c1", clef_c1, "age_dict", self.age_dict[clef_c1], "\t\t zerf", zerf)
                        # 1197 clef_c1 123400000567 age_dict 1000001 		 zerf 1
                        self.age_con[cle_t[1]] = []  # Enregistrement du dico de liaison[énuméré/conteneur].
                        (lineno(), "cle_t", cle_t[1], "age_con", self.age_con[clef_c1])
                        # 1200 cle_t 123400000567 age_con []
                zero = 0
                for clef_c2 in self.gam_con[cle_t[2]]:  # La cle_t[2] est une énumération
                    zero += 1
                    self.con_dict[clef_c2] = self.gammic[cle_g][zero]
                    if zero == 1:  # Quand zéro = 1, c'est l'emplacement de la clef tonique.
                        zerf += 1
                        (lineno(), "clef_c2", clef_c2, "con_dict", self.con_dict[clef_c2], "\t\t zerf", zerf)
                        # 1208 clef_c2 0005000 con_dict 1000001 		 zerf 2
                        self.age_con[cle_t[1]] = clef_c2  # Enregistrement du dico de liaison[énuméré/conteneur].
                        self.con_age[clef_c2] = cle_t[1]  # Enregistrement du dico de liaison[conteneur/énuméré].
                        (lineno(), "cle_t", cle_t[1], "age_con", self.age_con[cle_t[1]])
                        # 1211 cle_t 123400000567 age_con 0005000

            "# Ces dicos ont les 462 modes binaires et 462 modes conteneurs."
            (lineno(), "age_dict", self.age_dict, "\n con_dict", self.con_dict)
            # 1192 age_dict {'123400000567': '1000001', '123000004567': '1000001', '120000034567': '1000001',
            # .... con_dict {'0005000': '1000001', '0050000': '1000001', '0500000': '1000001',

            def unit_indice(appel, genre, module):
                """Cette fonction produit une liste d'indices de contrôle. |module['indice', 'transcript_age_ego']|"""
                ("# La multiliste n'est pas triée et est composée de listes triées en ordre croissant"
                 "Il n'y a pas de multiliste, quand le choix soixante-six et sa liste est triée")
                (lineno(), "Fonction Unit_indice", list(appel), genre, module)
                if module == "indice":  # Produit les indices pour une vérification.
                    if genre == "EGO":
                        return [self.bin_age_ego11.index(x) for x in appel if x in self.bin_age_ego11]
                    elif genre == "ISO":
                        return [self.bin_age_iso11.index(x) for x in appel if x in self.bin_age_iso11]
                elif "transcript" in module:  # Données conteneur modifiées en données énumérées + transforme.
                    self.transcript[genre] = []
                    if len(appel) > 1:  # Multiliste
                        s_transcript = [item for sublist in appel for item in sublist]
                        for s_trans in s_transcript:
                            self.transcript[genre].append(self.con_age[s_trans])
                    else:  # Liste
                        for s_trans in appel[0]:
                            self.transcript[genre].append(self.con_age[s_trans])
                    (lineno(), "unit_indice/transcript[genre]", self.transcript, "[genre][:2]", genre, module)
                    # 1248 unit_indice/transcript[genre] ['123450000607', '123405000607'] CON_ISO transcript_con_iso
                    # 1248 unit_indice/transcript[genre] ['123450000607', '123400500607'] CON_EGO transcript_con_ego
                elif "transforme" in module:  # Modifie une multipliste en une simple liste.
                    if len(appel) > 1:  # Multiliste
                        self.transforme[genre] = [item for sublist in appel for item in sublist]
                    else:  # Liste
                        self.transforme[genre] = [item for item in appel[0]]
                    (lineno(), "unit_indice/transforme[genre]", self.transforme, "[genre][:2]", genre, module)
                    # 1256 unit_indice/transforme[genre] ['100023456007', '100234000567'] AGE_EGO transforme_age_ego
                    # 1256 unit_indice/transforme[genre] ['123004000567', '123004005607'] AGE_ISO transforme_age_iso

            ("# Produire les listes des binarisations."
             "Lire les deux ordres ego_iso, afin d'y traiter leurs énumérations."
             "Dans une approche des gammes fondamentales par les modes toniques."
             "Selon le choix de l'utilisateur, on peut choisir les binarisations à traiter."
             "De ce traitement, ne doivent ressortir que les modes binarisés :")
            "{ bin_age_ego11, bin_age_iso11, bin_age_ego33, bin_age_iso33 }."
            loc_bin_age_ego, loc_bin_age_iso = [], []  # Formatage de self.bin_age_ego11 en construction.
            loc_bin_con_ego, loc_bin_con_iso = [], []  # Formatage de self.bin_age_ego11 en construction.
            self.choix_box = self.retour_bouton
            (lineno(), "choix_box", self.choix_box, "retour_bouton", self.retour_bouton)
            ("# Il s'avère qu'à ce niveau, choix_box et retour_bouton sont différents."
             "Le paramètre di_sec, malgré le dialogue est à None ? ")
            for k_num in range(1, 67):  # Lecture des soixante-six possibilités.
                "# Les deux enum_ego/iso, elles ont les effets des odrdres sur les énumérations."
                enum_ego = str(self.gam_ego[k_num-1])  # Lecture de la liste des gammes énumérées. Ordre maj
                enum_iso = str(self.gam_iso[k_num-1])  # Lecture de la liste des gammes énumérées. Ordre org.
                cont_ego = self.age_con[enum_ego]  # Lecture de la liste des gammes énumérées. Ordre maj
                cont_iso = self.age_con[enum_iso]  # Lecture de la liste des gammes énumérées. Ordre org.
                (lineno(), "☺ \n", "*** \t enum_ego", enum_ego, "\t enum_iso", enum_iso)
                (lineno(), "*** \t cont_ego", cont_ego, "\t cont_iso", cont_iso)
                # 1241 ☺ *** 	 enum_ego 102034050607 	 enum_iso 123400000567
                # 1242 *** 	 cont_ego 1101110 	 cont_iso 0005000
                if enum_ego == enum_iso:
                    "# Les égalités sont des sous-formes rythmiques reliant énuméré et conteneur."
                    (lineno(), "enum_ego == enum_iso", enum_ego, enum_iso)

                if self.comment_sta[1] in ('TriInt', 'AntiInt'):  # if self.zone_w4.get() in ("Gammes", "Contient"):
                    # self.bin_age_int_ego66, self.bin_age_int_iso66 = [], []  # Ampleur de section à soixante-six.
                    # self.bin_con_int_ego66, self.bin_con_int_iso66 = [], []  # Ampleur de section à soixante-six.
                    self.bin_age_int_ego66.append(enum_ego)
                    self.bin_age_int_iso66.append(enum_iso)
                    self.bin_con_int_ego66.append(cont_ego)
                    self.bin_con_int_iso66.append(cont_iso)
                    (lineno(), "_sta", self.comment_sta[1], "bin_age_int_ego66", len(self.bin_age_int_ego66))
                    # 1269 comment_sta TriInt choix_box 66
                elif k_num != 0 and not k_num % self.choix_box:
                    "# C'est cette condition qui définit quand le secteur choix_box atteind sa limite."
                    if self.choix_box == 11:
                        self.age_pass11ego.append(enum_ego)
                        self.age_pass11iso.append(enum_iso)
                        self.con_pass11ego.append(cont_ego)
                        self.con_pass11iso.append(cont_iso)
                        (lineno(), k_num, "age_pass11ego", self.age_pass11ego, len(self.age_pass11ego))  # 11
                        (lineno(), "%-k_num", k_num, "bin_age_ego11", self.bin_age_ego11, len(self.bin_age_ego11))
                        # 1241 %-k_num 11 age_pass11ego ['123400050607']
                        # 1242 %-k_num 11 bin_age_ego11 ['102034050607', '102034500607', '123400000567',
                        self.bin_age_ego11 += self.age_pass11ego
                        self.bin_age_iso11 += self.age_pass11iso
                        self.bin_con_ego11 += self.con_pass11ego
                        self.bin_con_iso11 += self.con_pass11iso
                        self.age_pass11ego.clear()
                        self.age_pass11iso.clear()
                        self.con_pass11ego.clear()
                        self.con_pass11iso.clear()
                    elif self.choix_box == 22:
                        self.age_pass22ego.append(enum_ego)
                        self.age_pass22iso.append(enum_iso)
                        self.con_pass22ego.append(cont_ego)
                        self.con_pass22iso.append(cont_iso)
                        (lineno(), "k_num", k_num, "bin_age_ego22", self.bin_age_ego22, len(self.bin_age_ego22))
                        self.bin_age_ego22 += self.age_pass22ego
                        self.bin_age_iso22 += self.age_pass22iso
                        self.bin_con_ego22 += self.con_pass22ego
                        self.bin_con_iso22 += self.con_pass22iso
                        self.age_pass22ego.clear()
                        self.age_pass22iso.clear()
                        self.con_pass22ego.clear()
                        self.con_pass22iso.clear()
                    elif self.choix_box == 33:
                        self.age_pass33ego.append(enum_ego)
                        self.age_pass33iso.append(enum_iso)
                        self.con_pass33ego.append(cont_ego)
                        self.con_pass33iso.append(cont_iso)
                        self.bin_con_ego33 += self.con_pass33ego
                        self.bin_con_iso33 += self.con_pass33iso
                        (lineno(), "k_num", k_num, "bin_age_ego33", self.bin_age_ego33, len(self.bin_age_ego33))
                        self.bin_age_ego33 += self.age_pass33ego
                        self.bin_age_iso33 += self.age_pass33iso
                        self.bin_con_ego33 += self.con_pass33ego
                        self.bin_con_iso33 += self.con_pass33iso
                        self.age_pass33ego.clear()
                        self.age_pass33iso.clear()
                        self.con_pass33ego.clear()
                        self.con_pass33iso.clear()
                    (lineno(), "k_num", k_num, "bin_age_ego11", self.bin_age_ego11, len(self.bin_age_ego11))
                    (lineno(), "k_num", k_num, "bin_age_ego33", self.bin_age_ego33, len(self.bin_age_ego33))
                else:  # Et celle-ci, affecte les k_num intermédiaires.
                    if self.choix_box == 11:
                        self.age_pass11ego.append(enum_ego)
                        self.age_pass11iso.append(enum_iso)
                        self.con_pass11ego.append(cont_ego)
                        self.con_pass11iso.append(cont_iso)
                        (lineno(), "&-k_num", k_num, "age_pass11ego", self.age_pass11ego)  # 11
                        # 1259 &-k_num 0 age_pass11ego ['102034050607']
                    elif self.choix_box == 22:
                        self.age_pass22ego.append(enum_ego)
                        self.age_pass22iso.append(enum_iso)
                        self.con_pass22ego.append(cont_ego)
                        self.con_pass22iso.append(cont_iso)
                        (lineno(), "&-k_num", k_num, "age_pass22ego", self.age_pass22ego)  # 22
                    elif self.choix_box == 33:
                        self.age_pass33ego.append(enum_ego)
                        self.age_pass33iso.append(enum_iso)
                        self.con_pass33ego.append(cont_ego)
                        self.con_pass33iso.append(cont_iso)
                        (lineno(), "&-k_num", k_num, "age_pass33ego", self.age_pass33ego)  # 33
                        # 1274 &-k_num 0 age_pass33ego ['102034050607']
                    (lineno(), "k_num", k_num, "choix_box", self.choix_box)  # 1238 k_num 0 choix_box 11
                if k_num == 66:
                    if self.age_pass11ego and self.age_pass11iso:
                        self.bin_age_ego11 += self.age_pass11ego
                        self.bin_age_iso11 += self.age_pass11iso
                        self.bin_con_ego11 += self.con_pass11ego
                        self.bin_con_iso11 += self.con_pass11iso
                        self.age_pass11ego.clear()
                        self.age_pass11iso.clear()
                        self.con_pass11ego.clear()
                        self.con_pass11iso.clear()
                    if self.age_pass22ego and self.age_pass22iso:
                        self.bin_age_ego22 += self.age_pass22ego
                        self.bin_age_iso22 += self.age_pass22iso
                        self.bin_con_ego22 += self.con_pass22ego
                        self.bin_con_iso22 += self.con_pass22iso
                        self.age_pass22ego.clear()
                        self.age_pass22iso.clear()
                        self.con_pass22ego.clear()
                        self.con_pass22iso.clear()
                    if self.age_pass33ego and self.age_pass33iso:
                        self.bin_age_ego33 += self.age_pass33ego
                        self.bin_age_iso33 += self.age_pass33iso
                        self.bin_con_ego33 += self.con_pass33ego
                        self.bin_con_iso33 += self.con_pass33iso
                        self.age_pass33ego.clear()
                        self.age_pass33iso.clear()
                        self.con_pass33ego.clear()
                        self.con_pass33iso.clear()
                        # ...
                    (lineno(), "_sta", self.comment_sta[1], "bin_age_int_ego66", len(self.bin_age_int_ego66))
                    (lineno(), "k_num", k_num, "bin_age_ego11", self.bin_age_ego11[:4], len(self.bin_age_ego11))
                    (lineno(), "k_num", k_num, "bin_con_ego11", self.bin_con_ego11[:4], len(self.bin_con_ego11))
                    (lineno(), "k_num", k_num, "bin_age_ego33", self.bin_age_ego33, len(self.bin_age_ego33))
                    # 1401 _sta TriInt bin_age_int_ego66 66
                    # 1402 k_num 65 bin_age_ego11 ['102034050607', '102034500607', '123400000567',... ] 66
                    # 1403 k_num 66 bin_con_ego11 ['1101110', '1100210', '0005000', '0003200', '0003020',
                ("# C'est ici qu'on récupère les sections à traiter dans le cycle clefs_triadic."
                 "Recréation dans une liste par section, dans une vaiable locale par sujets au reformatage."
                 "{ bin_age_ego11, bin_age_iso11, bin_age_ego22, bin_age_iso22, bin_age_ego33, bin_age_iso33 }.")
                if (len(self.bin_age_ego11) > 1 or len(self.bin_age_ego22) > 1 or len(self.bin_age_ego33) > 1
                        and not k_num % self.choix_box or k_num == 66):
                    ("\n", lineno(), "k_num", k_num, "bin_age_ego11", self.bin_age_ego11, len(self.bin_age_ego11))
                    # Quand k_num vaut 11, la liste possède 12 éléments énumérés.
                    ("# Afin de résoudre ce problème de surnombre à cause de la comparaison de listes de strings,"
                     "qui une fois en désordre n'est plus comparable : ['1', '2', '3'] != ['3', '2', '1']... ")
                    ("###### ☺ \t", lineno())
                    # print(lineno(), "k_num", k_num, "Long bin_age_ego11", self.bin_age_ego11, len(self.bin_age_ego11))
                    # if k_num == self.choix_box:
                    if self.choix_box == 11 and not k_num % self.choix_box:
                        loc_age_ego = self.bin_age_ego11[- int(self.choix_box):].copy()
                        loc_age_iso = self.bin_age_iso11[- int(self.choix_box):].copy()
                        loc_con_ego = self.bin_con_ego11[- int(self.choix_box):].copy()
                        loc_con_iso = self.bin_con_iso11[- int(self.choix_box):].copy()
                        (lineno(), "self.bin_age_ego11", self.bin_age_ego11)
                        (lineno(), " * ", k_num, "loc_age_ego[- self.choix_box:]", loc_age_ego, len(loc_age_ego))
                    elif self.choix_box == 22:
                        loc_age_ego = self.bin_age_ego22[- self.choix_box:].copy()
                        loc_age_iso = self.bin_age_iso22[- self.choix_box:].copy()
                        loc_con_ego = self.bin_con_ego22[- int(self.choix_box):].copy()
                        loc_con_iso = self.bin_con_iso22[- int(self.choix_box):].copy()
                    elif self.choix_box == 33:
                        loc_age_ego = self.bin_age_ego33[- self.choix_box:].copy()
                        loc_age_iso = self.bin_age_iso33[- self.choix_box:].copy()
                        loc_con_ego = self.bin_con_ego33[- int(self.choix_box):].copy()
                        loc_con_iso = self.bin_con_iso33[- int(self.choix_box):].copy()
                    elif self.choix_box == 66:
                        loc_age_ego = self.bin_age_int_ego66.copy()  # [- self.choix_box:]
                        loc_age_iso = self.bin_age_int_iso66.copy()  # [- self.choix_box:]
                        loc_con_ego = self.bin_con_int_ego66.copy()  # [- int(self.choix_box):]
                        loc_con_iso = self.bin_con_int_iso66.copy()  # [- int(self.choix_box):]
                        (lineno(), "bin_age_int_ego66", len(self.bin_age_int_ego66))
                        # 1411 bin_age_int_ego66 66
                    retour_ind1 = unit_indice(loc_age_ego, "EGO", "indice")
                    retour_ind2 = unit_indice(loc_age_iso, "ISO", "indice")
                    retour_ind3 = unit_indice(loc_con_ego, "EGO", "indice")
                    retour_ind4 = unit_indice(loc_con_iso, "ISO", "indice")
                    loc_age_ego.sort()  #
                    loc_age_iso.sort()  # Chacune des listes de la multiliste est triée
                    loc_con_ego.sort()  # La multiliste n'est pas triée en ordre croissant
                    loc_con_iso.sort()  #
                    (lineno(), " * ", k_num, "loc_age_ego[:self.choix_box]", loc_age_ego, len(loc_age_ego))
                    if loc_age_ego not in loc_bin_age_ego:
                        loc_bin_age_ego.append(loc_age_ego)
                        (lineno(), k_num, "loc_bin_age_ego", loc_bin_age_ego[0][:3], len(loc_bin_age_ego))
                        # 1394 11 loc_bin_age_ego ['100023456007', '100234000567', '102034050607', ,... ]
                    if loc_age_iso not in loc_bin_age_iso:
                        loc_bin_age_iso.append(loc_age_iso)
                        (lineno(), k_num, "\t loc_bin_age_iso", loc_bin_age_iso[0][:3], len(loc_bin_age_iso))
                        # 1398 11 	 loc_bin_age_iso ['123004000567', '123004005607', '123040050607',,... ]
                    if loc_con_iso not in loc_bin_con_iso:
                        loc_bin_con_iso.append(loc_con_iso)
                        (lineno(), k_num, "loc_bin_con_iso", loc_bin_con_iso[0][:3], len(loc_bin_con_iso))
                        # 1402 11 loc_bin_con_iso [['0000410', '0001310', '0002210', '0003020',
                    if loc_con_ego not in loc_bin_con_ego:
                        loc_bin_con_ego.append(loc_con_ego)
                        (lineno(), k_num, "\t loc_bin_con_ego", loc_bin_con_ego[0][:3], len(loc_bin_con_ego))
                        # 1405 11 	 loc_bin_con_ego [['0000410', '0002210', '0003020', '0003200',

                ("Références choix de l'utilisateur self.comment_sta:"
                 "['TriEgo', 'AntiEgo', 'TriIso', 'AntiIso','TriInt', 'AntiInt']"
                 "Pour le secteur à traiter, on l'a en divisant 66 par self.choix_box."
                 "Quand 'TriInt' ou 'AntiInt' est sélectionné, le secteur correspond aux 66 gammes.")
                if k_num == 66:
                    (lineno(), "Choix utile / comment_sta", self.comment_sta, "choix_box", self.choix_box)
                    # 1421 Choix utile / comment_sta ['Gammes', 'TriEgo'] choix_box 11
                    (lineno(), k_num, "loc_bin_age_ego", loc_bin_age_ego, len(loc_bin_age_ego))
                    (lineno(), k_num, "loc_bin_age_iso", loc_bin_age_iso, len(loc_bin_age_iso))
                    (lineno(), k_num, "loc_bin_con_ego", loc_bin_con_ego, len(loc_bin_con_ego))
                    (lineno(), k_num, "loc_bin_con_iso", loc_bin_con_iso, len(loc_bin_con_iso))
                    # 1425 66 loc_bin_con_iso [['0000410', '0001310', '0002210',...]] 6
                    "# Transformer une multiliste en une simple liste."  # Gamme
                    unit_indice(loc_bin_age_ego, "AGE_EGO", "transforme_age_ego")
                    "# Transformer une multiliste en une simple liste."  # Gamme
                    unit_indice(loc_bin_age_iso, "AGE_ISO", "transforme_age_iso")
                    "# La suite du code traite des clés énumérées uniquement."  # Contient
                    unit_indice(loc_bin_con_iso, "CON_ISO", "transcript_con_iso")
                    "# La suite du code traite des clés énumérées uniquement."  # Contient
                    unit_indice(loc_bin_con_ego, "CON_EGO", "transcript_con_ego")
                    k_num_fin = True
                (lineno(), "k_num", k_num, "Long bin_age_ego11", self.bin_age_ego11, len(self.bin_age_ego11))
                (lineno(), "k_num", k_num + 1, "Long age_pass11ego", self.age_pass11ego, len(self.age_pass11ego))
                # 1272 k_num 66 Long bin_age_ego11 ['102034050607', '102034500607', '123400000567',
                # 1273 k_num 66 Long age_pass11ego ['102003045607', '102000345607', '102340500607',

        # À ce niveau toutes les gammes ont été traitées.
        ("Les boutons-images = ['TriEgo', 'AntiEgo', 'TriIso', 'AntiIso','TriInt', 'AntiInt']"
         "Pour la sélection 'Gammes' => self.transforme : dict_keys(['AGE_EGO', 'AGE_ISO'])"
         "Pour la sélection 'Contient' => self.transcript : dict_keys(['CON_ISO', 'CON_EGO'])")
        lis_enum_ego, lis_enum_iso = [], []  # Listes pour initialiser en boucle ; enum_ego et enum_iso.
        if k_num_fin:
            (lineno(), "comment_sta", self.comment_sta, "Le choix de l'utilisateur (bouton-image).")
            # 1490 comment_sta ['Gammes', 'TriEgo'] Le choix de l'utilisateur (bouton-image).
            if self.comment_sta[0] == 'Gammes':
                (lineno(), "Gammes/transforme['AGE_EGO' ou 'AGE_ISO']", len(self.transforme['AGE_EGO']))
                # 1492 Gammes/transforme['AGE_EGO'] 66
                lis_enum_ego = self.transforme['AGE_EGO'].copy()
                lis_enum_iso = self.transforme['AGE_ISO'].copy()
            elif self.comment_sta[0] == 'Contient':
                (lineno(), "Contient/transcript['CON_ISO' ou 'CON_EGO']", len(self.transcript['CON_ISO']))
                # 1495 Contient/transcript['CON_ISO'] 66
                lis_enum_iso = self.transcript['CON_ISO'].copy()
                lis_enum_ego = self.transcript['CON_EGO'].copy()
            (lineno(), "enum_ego", lis_enum_ego, "\n enum_iso", "lis_enum_iso")
            # 1514 enum_ego ['100023456007', '100234000567', '102034050607', '102034500607',

            ("Attribution des binarisations diatoniques pour chaque gamme"
             "# Début de bouclage itératif : sources (lis_enum_ego, lis_enum_iso)")
            for count_listes in range(66):
                enum_ego = lis_enum_ego[count_listes]
                enum_iso = lis_enum_iso[count_listes]
                "# Pour 'for tria in clefs_triadic', sont traités : enum_ego, enum_iso"
                tst = 0
                t_ego, t_iso = True, True
                for tria in clefs_triadic:  # À chaque fois, on cherche dans la clef_triadic les énumérations toniques.
                    "# Progression triadique traitant à trouver les indices des gammes."
                    if t_ego and tria[1] == enum_ego:  # Traitement enum_ego.
                        self.ego2[tria[2]] = {"age": [], "con": []}  # Clés = numéro_gamme[tria[2]] et age[] ou con[].

                        if self.comment_sta[0] == 'Gammes':
                            "# Conclusion diatonique énumérée."
                            self.ego2[tria[2]]["age"] = self.di_ages[tria[2]].copy()
                            ego_age = self.di_ages[tria[2]].copy()
                            (lineno(), "tria âge", tria, "ego_age.sort", ego_age)
                            t_ego_age = Relance.traite_ego_iso(self, ego_age, "ego_age")
                            (lineno(), "tria âge", tria, "t_ego_age", t_ego_age[0][:3])
                            # 1237 tria âge ['0', '102034050607', 44] t_ego_age ['1110111', '1111111', '1111110']
                            for tea in t_ego_age[0]:
                                if tea not in self.bin_age_ego:
                                    self.bin_age_ego.append(tea)  # Liste des binaires énumérés.
                            t_ego = False
                            tst += 1

                        if self.comment_sta[0] == 'Contient':
                            "# Conclusion diatonique conteneur."
                            self.ego2[tria[2]]["con"] = self.gam_con[tria[2]].copy()
                            ego_con = self.gam_con[tria[2]].copy()
                            t_ego_con = Relance.traite_ego_iso(self, ego_con, "ego_con")
                            (lineno(), "tria con", tria, "t_ego_con", t_ego_con[0][:3])
                            # 1244 tria con ['0', '102034050607', 44] t_ego_con ['1001000', '1001100', '1101100']
                            for tec in t_ego_con[0]:
                                if tec not in self.bin_con_ego:
                                    self.bin_con_ego.append(tec)  # Liste des binaires conteneurs.
                            (lineno(), "tria con", tria, "bin_con", self.bin_con_ego)
                            # 1245 tria con ['0', '102034050607', '1001000', '1001100', '1101100', '1101110', '1101111']
                            t_ego = False
                            tst += 1
                    if t_iso and tria[1] == enum_iso:  # Traitement enum_iso.
                        self.iso2[tria[2]] = {"age": [], "con": []}  # Clés = numéro_gamme[tria[2]] et age[] ou con[].

                        if self.comment_sta[0] == 'Contient':
                            "# Conclusion diatonique conteneur."
                            self.iso2[tria[2]]["con"] = self.gam_con[tria[2]].copy()
                            iso_con = self.gam_con[tria[2]].copy()
                            t_iso_con = Relance.traite_ego_iso(self, iso_con, "iso_con")
                            (lineno(), "tria con", tria, "t_iso_con", t_iso_con[0][:3])
                            # 1255 tria con ['o45x', '123400000567', 1] t_iso_con ['1000000', '1000001', '1000001']
                            for tic in t_iso_con[0]:
                                if tic not in self.bin_con_iso:
                                    self.bin_con_iso.append(tic)  # Liste des binaires conteneurs.
                            tst += 1
                            t_iso = False

                        if self.comment_sta[0] == 'Gammes':
                            "# Conclusion diatonique énumérée."
                            self.iso2[tria[2]]["age"] = self.di_ages[tria[2]].copy()
                            iso_age = self.di_ages[tria[2]].copy()
                            t_iso_age = Relance.traite_ego_iso(self, iso_age, "iso_age")
                            (lineno(), "tria âge", tria, "t_iso_age", t_iso_age[0][:3])
                            # 1262 tria âge ['o45x', '123400000567', 1] t_iso_age ['1000001', '1000001', '1000001']
                            for tia in t_iso_age[0]:
                                if tia not in self.bin_age_iso:
                                    self.bin_age_iso.append(tia)  # Liste des binaires énumérés.
                            tst += 1
                            t_iso = False
                    if tst == 2:
                        # En première utilisation cette boucle 'for' traite un seul enum_ego et un seul enum_iso.
                        (lineno(), "On a trouvé les deux énumérations.")
                        # 1551 On a trouvé les deux énumérations.
                        break
                (lineno(), "k_num", k_num, "tria", tria)
                (lineno(), "_ clefs_triadic", list(clefs_triadic)[:3], "\n.... _ gammic_keys", list(gammic_keys)[:3])
                # 1178 _ clefs_triadic [['o45x', '123400000567', 1], ['o46-', '123400056007', 2],
                # .... _ gammic_keys [('o45x', '123400000567'), ('o46-', '123400056007'), ('o4', '123400050607')]
            if self.comment_sta[0] == 'Gammes':
                (lineno(), "bin_age_ego", self.bin_age_ego, "")
                (lineno(), "bin_age_iso", self.bin_age_iso, "")
                return self.bin_age_ego, self.bin_age_iso, "Gammes"
            elif self.comment_sta[0] == 'Contient':
                (lineno(), "bin_con_ego", self.bin_con_ego, "")
                (lineno(), "bin_con_iso", self.bin_con_iso, "")
                return self.bin_con_ego, self.bin_con_iso, "Contient"

        ("# Création de la liste globale des binarisations pour self.bin_int."
         "Vont être utilisées les listes self.age_dict et self.con_dict.")
        '''print("\n", lineno(), "Distribution des clefs de ego2 et iso2 :\n",
              " [numéro_gamme]*66 gammes, pour une gamme, il y a ['age']*7 diatonies et ['con']*7 diatonies\n",
              " ['con'] = 7 modes conteneurs, ['age'] = 7 modes énumérés. 66 gammes * 14 degrés = 924 modèles.")
        print(lineno(), "ego2[num_gam]['age']['con'] # Ordre majeur", list(self.ego2.keys())[:13])
        print(lineno(), "iso2[num_gam]['age']['con'] # Ordre normal", list(self.iso2.keys())[:13])
        print(lineno(), "bin_int_ego66", self.bin_int_ego66, "\nbin_int_iso66", self.bin_int_iso66,
              "\n\nLes listes bin_age_iso_ego et bin_con_iso_ego ont les binaires finaux.",
             "\n\nbin_age_ego", self.bin_age_ego, "\nbin_age_iso", self.bin_age_iso,
             "\n\nbin_con_ego", self.bin_con_ego, "\nbin_con_iso", self.bin_con_iso)'''

    def charger_image(self):
        """
        Loads and displays a series of images onto a Canvas widget.

        This function loads a predefined list of images, creates PhotoImage objects
        from them, and displays them on a Canvas.
        It handles the positioning of each image on the Canvas and sets up event bindings to handle user clicks.

        :raises IOError: If an image file cannot be opened.
        :return: None
        """
        # table_o = Canvas(root, width=84, height=884, bg="thistle"), (row=2, column=3)
        self.table_o.delete("all")
        # self.images_references.clear()
        esp, deb, image_id, photo_image = 60, 48, None, 0
        """self.images_liste = ["BoutonTriEgo.png", "BoutonAntiEgo.png", "BoutonTriIso.png", "BoutonAntiIso.png",
                             "BoutonTriInt.png", "BoutonAntiInt.png"]"""
        for index, image in enumerate(self.images_liste):
            photo_image = ImageTk.PhotoImage(Image.open(image))
            self.images_references.append(photo_image)
            image_id = self.table_o.create_image(deb, esp, image=photo_image)
            self.table_o.tag_bind(image_id, "<Button-1>", self.clic_image)
            esp += 100
            (lineno(), "index", index, "image_id", image_id, "image", self.images_liste[image_id - 1])

    def quitter(self, tag):
        """Pour effectuer une transition en fenêtrage.
            Determines the current state with a real closure reference.
            This method evaluates various conditions based on the `tag` parameter and the internal
            state `self.borne[1]`, and performs actions such as clearing a collection or
            destroying the object accordingly.

            :param tag: A string representing the state or action that influences the
                        method’s behavior.
                        Valid values include "1111111", "0000000",
                        "clic_image", "Passer", and other possible strings.
            :return: None.
            """
        "# Connaitre l'état actuel avec un repère de fermeture réelle."
        (lineno(), "\t Quitter(tag)", tag)
        if self.borne[1] == 1111111 and tag in ("1111111", "0000000"):
            (lineno(), "Quitter/if borne", self.borne[1], "\t tag", tag)
            # 430 Quitter/if borne 1111111 	 tag clic_image
            self.destroy()
        elif tag == "clic_image":
            self.colonne_bin.clear()
            self.destroy()
            (lineno(), "Quitter/elif/clic_image borne", self.borne[1], "\t tag", tag)
            # 436 Quitter/elif/clic_image borne 1111111 	 tag clic_image
        elif tag == "Passer":
            # Gestion du clic de la souris perturbant.
            (lineno(), "Quitter/elif/\t tag", tag)
            pass
        else:  # 'self.borne[1] = "       " ou 1000001
            (lineno(), "Quitter/else borne", self.borne[1], "\t tag", tag)
            # 439 Quitter/else borne 1000001 tag 0000000

    def gammes_arp(self):
        """Cette fonction est destinée à trier les modèles binaires, en commençant par la gamme naturelle.
        Ça concerne l'initialisation des tables par la gamme naturelle exprimée en modulations (binaires et degrés)."""
        ("\t", lineno(), "**   Fonction gammes_arp ", "colonne_bin", list(self.colonne_bin))
        gammes_col = list(self.dic_codage.values())  # "dic_codage" = Les gammes issues de 'globdicTcoup.txt'
        (lineno(), "gammes_col", len(gammes_col))
        "# À chaque ligne, correspond un mode binaire. La ligne zéro, c'est pour les noms des gammes."
        # La ligne peut être donnée par l'index de l'élément de la liste des modes binaires présents.
        colon = 1  # À chaque colonne, correspond une gamme répertoriée. Une gamme a autant de modes que de lignes.

        "# Initialisation de la colonne binaire par les modulations binaires de la gamme naturelle."
        for gc in gammes_col[43]:
            if len(gc) == 2:
                self.colonne_bin.append("")
                self.colonne_bin.append("")
                self.colonne_bin.append(gc[-1])
                ligne = self.colonne_bin.index(gc[-1])
                self.colonne_gam[colon, 0] = [gc[0][0]]
                self.colonne_gam[colon, ligne] = []
                self.colonne_gam[colon, ligne].append('1')
                (lineno(), "colonne_bin[0]", self.colonne_bin, "ligne", ligne)
                (lineno(), "\t colonne_gam", self.colonne_gam[colon, ligne])
            else:
                self.colonne_bin.append(gc[-1])
                ligne = self.colonne_bin.index(gc[-1])
                self.colonne_gam[colon, ligne] = []
                self.colonne_gam[colon, ligne].append(str(gc[1]))
                (lineno(), "\t colonne_gam", self.colonne_gam[colon, ligne], "\n colonne_bin", self.colonne_bin)
            (lineno(), "Col:", colon, "Lig:", ligne, self.colonne_gam[colon, ligne], "gc", gc, len(gc), gc[-1])
            # 441 Col: 1 Lig: 1 ['1'] gc (['0', 336], '1111111') 2 1111111
            # 441 Col: 1 Lig: 2 ['2'] gc (44, 2, '1101110') 3 1101110/...
        gammes_col.pop(43)  # Effacement de la gamme majeure, afin de ne pas revenir dessus.

        "# Approvisionnement des tables binaires et modales."
        cumul_gam = {}  # Dictionnaire aux gammes comparées.
        (lineno(), "\n********** Marque Repère Répétition Hors While = (Pas de Répétition) *************\n")
        while 1:
            cumul_gam.clear()  # Dictionnaire aux gammes comparées.
            (lineno(), "\n********** Marque Repère Répétition Dans While *************\n")

            "# Poursuite du triage comparatif avec marquage lorsqu'elle y a un lien commun."
            # gammes_col = list(self.dic_codage.values())  # "dic_codage" = Les gammes issues de 'globdicTcoup.txt'
            for gam_col in gammes_col:
                ind_col = gammes_col.index(gam_col)  # 'ind_col' = Index de la gamme sélectionnée.
                cumul_gam[gam_col[0][0][0]] = [ind_col]
                (lineno(), "  cumul_gam", cumul_gam[gam_col[0][0][0]], "gam_col", gam_col)
                for mod_c in gam_col:  # 'gam_col' = Liste une gamme diatonique.
                    if mod_c[-1] in self.colonne_bin:  # 'mod_c[-1]' = Unième mode binaire.
                        ind_bin = self.colonne_bin.index(mod_c[-1])  # 'ind_bin' = Index correspondant au mode binaire.
                        cumul_gam[gam_col[0][0][0]].append(ind_bin)
                        ("_*", lineno(), "cumul_gam", cumul_gam[gam_col[0][0][0]], "mod_c", mod_c)
                ("_", lineno(), "cumul_gam", cumul_gam[gam_col[0][0][0]])
            ("\n", lineno(), "cumul_gam", cumul_gam)

            "# Les gammes qui ont des modes binaires communs existentiels."
            liste_sel = [va for va in cumul_gam.values() if len(va) > 1]  # Référence gamme.
            if liste_sel:
                liste_len = [len(va) for va in cumul_gam.values() if len(va) > 1]  # Les poids des modes binaires.
                max_liste = max(liste_len)  # Détecte le poids modal maximum.
                val_max = liste_sel[liste_len.index(max_liste)]  # Détecte la gamme aux modes binaires.
                (lineno(), "val_max", val_max[0], "\ngammes_col", gammes_col[val_max[0]])

                "# Mise à jour de la colonne binaire et celle des gammes."
                colon += 1
                n_gam = val_max[0]  # Index de la gamme sélectionnée à supprimer.
                lignes, nbr_bin = [], 0
                for gc in gammes_col[val_max[0]]:
                    # print("Gc", gc)
                    # Gc (47, 2, '1100110')
                    self.colonne_lis[str(gc[0])] = []
                    if len(gc) == 2:  # Première ligne dédiée au nom de la gamme.
                        self.colonne_gam[colon, 0] = []
                        self.colonne_gam[colon, 0] = [gc[0][0]]  # Mise à jour du nom de la gamme.
                        if gc[-1] in self.colonne_bin:
                            nbr_bin += 1
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            self.colonne_gam[colon, ligne].append('1')
                            # print("***2 col_bin0", gc, "index =", colonne_bin.index(gc[-1]))
                        else:
                            self.colonne_bin.append(gc[-1])
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            self.colonne_gam[colon, ligne].append('1')
                            # print("Not col_bin0 gc", gc, gc[-1])
                    else:
                        if gc[-1] in self.colonne_bin:
                            nbr_bin += 1
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            elif (colon, ligne) not in self.colonne_lis[str(gc[0])]:  # Ensembles à même figure binaire.
                                self.colonne_lis[str(gc[0])].append((colon, ligne))
                                # print("CORPS yes_bin not_lis", colonne_gam[colon, ligne], "\t col/lig", colon, ligne)
                                # CORPS yes_bin ['1', '2', '3', '4', '6'] 	 colon, ligne 3 11
                            self.colonne_gam[colon, ligne].append(str(gc[1]))
                            # print("*** col_bin0", gc, "index =", colonne_bin.index(gc[-1]))
                        else:
                            self.colonne_bin.append(gc[-1])
                            ligne = self.colonne_bin.index(gc[-1])
                            if ligne not in lignes:
                                self.colonne_gam[colon, ligne] = []
                                lignes.append(ligne)
                            self.colonne_gam[colon, ligne].append(str(gc[1]))
                            # print("___ Not col_bin0 gc", gc, gc[-1])
                    if nbr_bin > 6:
                        self.gammes_bin[self.colonne_gam[colon, 0][0]] = 'Ok'
                        (lineno(), "\t\tnbr_bin", nbr_bin, "colonne_gam[colon, 0]", self.colonne_gam[colon, 0][0])
                        (lineno(), "self.gammes_bin", self.gammes_bin[self.colonne_gam[colon, 0][0]],)
                    # print("Colon", colon, "Ligne", ligne, "gc", gc)
                    # print("Colon / Ligne", colon, ligne, "colonne_gam", colonne_gam[colon, ligne])
                gammes_col.pop(n_gam)  # Effacement de la gamme traitée, afin de ne pas revenir dessus.
                # print(lino(), "self.dic_force", list(self.dic_force.keys())[0], "||", len(self.dic_force.keys()))
            else:
                break
            (lineno(), ". len(gammes_col) =", len(gammes_col), "self.dic_force", self.dic_force)
            # 525 . len(gammes_col) = 64 self.dic_force {'1111001': [(48, '102034500067'), (43, '102034005067'),
            # print("max_liste", max_liste, "\n liste_sel", liste_sel, "\n", val_max, val_max[0][0])
        for k, v in self.colonne_gam.items():
            if len(v) > 1:
                (lineno(), "GAM_ARP self.colonne_gam", self.colonne_gam[k])
                # 578 GAM_ARP self.colonne_gam ['1', '2', '3', '4', '6', '7']
        (lineno(), "GAM_ARP self.colonne_gam", list(self.colonne_gam)[:3])
        (lineno(), "GAM_ARP self.dic_binary", self.dic_binary.keys(), "\n\nself.colonne_bin", self.colonne_bin)

    def gammes_log(self):
        """Fonction complémentaire au traitement original,
        elle traite le signal original comme des nombres entiers.
        Contrairement à la fonction
        du traitement original, qui découvrait les gammes selon les dispositions binaires.
        Elle compose l'intégralité des définitions binaires, qui de par celles-ci, va structurer
        la série des gammes fondamentales en fonction de leurs dispositions binaires.
        Soit,
        qu'elles sont les gammes qui contiennent le pulsif de binaires rapprochés, en rapport
        avec la liste intégrale des modes binaires."""
        ("\t", lineno(), "**   Fonction gammes_log, colonne_bin", list(self.colonne_bin)[:2])
        "# Définir les contenants par quantité des sept premiers binaires cumulatifs."
        gammes_loc = list(self.dic_codage.values())  # "dic_codage" = Les gammes issues de 'globdicTcoup.txt'
        (lineno(), "gammes_loc", len(gammes_loc), "dic_codage.keys", list(self.dic_codage.keys())[:3])
        # 839 gammes_loc 66 dic_codage.keys [(1, '123400000567'), (2, '123400056007'), (3, '123400050607')]
        (lineno(), "gammes_loc[0]", gammes_loc[0], "\n force", self.dic_force, "\n Clés", self.dic_force.keys())
        # 541 gammes_loc[0] [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
        # force {'1000001': [((1, '123400000567'), (['o45x', 1], '1000001')), (1, 2, '1000001'),
        # Clés dict_keys(['1000001', '1000000', '1000101', '1011000', '1011001', '1000111',

        "# Un dictionnaire ayant les clefs[Noms des gammes] et valeurs[Numéros des gammes]"
        # Accessible et enregistré dans le dictionnaire 'dic_titres'

        "# Faire une copie des clés 'dic_force', qui assemble les gammes aux mêmes clés."
        force_cop = self.colonne_bin  # 'force_cop' = Liste les clés de 'colonne bin'.
        force_gam = {}  # Dictionnaire, clés binaires et gammes relatives. Classe-gamme quantitative.
        liste_gam = []  # Liste les numéros des gammes sans répétition.

        "# Initialisation de l'assembleur des numéros des 66 gammes quantifiés."
        globe_num = {}  # Dictionnaire, clé = Numéro de gamme, valeur = Index + Quantité.
        val_vn2 = []  # Liste regroupant les gammes traitées.
        repos_num = []  # Liste des numéros anciens, afin d'éviter de refaire le traitement.
        colonne_cop = [""]
        cc, colon = 7, 1

        "# globe_num = Dictionnaire, clé = Numéro, value = Quantité"
        # for ss in range(1, 67):
        #   globe_num[ss] = 0 # Quand 'globe_num'[ss]>6= La gamme aux modes binaires est terminée.

        while cc <= len(force_cop):
            "# colonne_cop = Liste native des clés binaires utilisées."
            (lineno(), "_________________________________WHILE 1______ cc", cc)
            colonne_cop.clear()
            for cop_cc in force_cop[:cc]:  # 'force_cop' = Liste les clés de 'colonne bin'.
                colonne_cop.append(str(cop_cc))
                (lineno(), "cop_cc", type(cop_cc))
            col_count = colonne_cop.count("")  # Harmonisation des vides au début de la liste.
            if col_count == 0:
                colonne_cop.insert(0, "")
                colonne_cop.insert(1, "")
            if col_count == 1:
                colonne_cop.insert(0, "")
            (lineno(), " § colonne_cop", colonne_cop[:6], "long", len(colonne_cop), "col_count", col_count)
            # 878  § colonne_cop ['', '', '1011110', '1101010', '1111101', '1110110'] long 8 col_count 1
            # force_cop ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000']
            # colonne_cop ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000']

            "# Réajustement et réinitialisation de 'globe_num' à l'aide de 'repos_num'."
            if cc <= len(force_cop):
                globe_num.clear()
            for ss in range(1, 67):
                if ss not in repos_num:  # 'repos_num' = Gammes traitées.
                    globe_num[ss] = 0  # Quand 'globe_num'[ss] > 6 = La gamme aux modes binaires est terminée.
            (lineno(), "____________________________________________________________")
            (lineno(), " °°° Réajustement repos_num", repos_num, "Reste globe_num", globe_num)

            "# Tournée de tous les binaires de 'colonne_cop' en évolution. Et, rassembleur 'globe_num'"
            for cop in colonne_cop[2:]:
                liste_gam.clear()
                force_gam[cop] = []  # Liste les gammes et contrôle quantitatif.
                (lineno(), "colonne_cop", colonne_cop[2:], "cop", cop, type(cop))

                "# Lire le rassembleur 'self.dic_force[cop]', pour un mode binaire qui compte les 'globe_num'."
                for fc in self.dic_force[str(cop)]:
                    (lineno(), "-- for fc in self.dic_force[cop]-- FC", fc, fc[0])
                    if len(fc) < 3:
                        # Parfois 'flop' = Nom de gamme sans numéro de gamme.
                        flop = fc[0][0]
                        if isinstance(flop, str):
                            flop = self.dic_indice[flop]
                            (lineno(), "flop", flop)
                        (lineno(), "fc", fc, "flop", flop, type(flop))
                    else:
                        (lineno(), "fc", fc)
                        flop = fc[0]
                        (lineno(), "---ELSE---- fc", fc, " flop", flop)
                    if flop in globe_num.keys():
                        # Pointer les gammes aux mêmes binaires.
                        if len(fc) < 3:
                            ind_gam = fc[0][0]
                            if isinstance(ind_gam, str):
                                "# Capturer le numéro de la gamme avec le nom de la gamme."
                                indic = fc[0][0]
                                ind_gam = self.dic_indice[indic]
                                (lineno(), "\t if<3 str ind_gam", ind_gam, indic, "cop", cop,)
                            force_gam[cop].append(ind_gam)
                            (lineno(), "ind_gam", ind_gam, cop, "force_gam[cop]", force_gam[cop], "fc", fc)
                        else:
                            ind_gam = fc[0]
                            force_gam[cop].append(ind_gam)
                            (lineno(), "else ind_gam", ind_gam, cop, "fc", fc)
                        # Alimenter 'liste_gam',
                        if ind_gam not in liste_gam:
                            liste_gam.append(ind_gam)
                        globe_num[ind_gam] += 1
                        (lineno(), "cop", cop, "fc", fc, "ind_gam", ind_gam, "globe_num", globe_num[ind_gam])
                        (lineno(), "cop", cop, "fc", fc, " | gammes_loc", gammes_loc[ind_gam - 1])
                (lineno(), "cop", cop, "force_gam[cop]", force_gam[cop])
                # 645 cop 1111 000 force gam[cop] [3, 8, 12, 16, 18]. Liste les numéros de gammes aux mêmes binaires.

            "# Contrôler le nombre d'apparition des numéros des gammes dans le contexte 'colonne_cop'."
            "# Donner les valeurs aux emplacements via 'colonne_gam'. Clé[colonne, ligne], valeur[Noms. Degré]."
            (lineno(), "globe_num", globe_num)
            val_vn1 = [(ky, vl) for ky, vl in globe_num.items() if vl > 6]
            val_vn2.append(val_vn1)
            # Commencer à un (1) l'écriture en colonne des gammes.
            for gn, vn in globe_num.items():
                "# Contrôle des valeurs, si elles sont supérieures à six, c'est que la gamme est entière."
                if vn > 6 and gn not in repos_num:  # Trouver les gammes avec les numéros non-traités.
                    ("\n", lineno(), "=== if vn > 6 and gn not in repos_num: gn, vn", gn, vn, "val_vn2", val_vn2)
                    (lineno(), "globe_num", globe_num, "\ncolonne_cop", colonne_cop)
                    repos_num.append(gn)
                    ind_loc, halte0 = None, True
                    (lineno(), "gn", gn, "repos_num", repos_num)
                    "# Il peut y avoir quelques degrés avec un binaire, et le reste diatonique avec un autre binaire."
                    for cc1 in colonne_cop[2:]:  # 'colonne_cop' = Les binaires ou clefs 'dic force'.
                        force_g1 = self.dic_force[str(cc1)]  # 'dic_force' = Total, 'force_gam' = Numéros.
                        gl_index, fg2 = -1, None
                        (lineno(), " ****** Tous les modes aux cc1", cc1, "\n♦ force_g1[:3]", force_g1)
                        if halte0:
                            for fg1 in force_g1:  # 'force_g1' = Toutes les gammes aux 'cc1'
                                if len(fg1) < 3 and len(fg1[1]) < 3:
                                    fg2 = fg1[0]  # (lino(), "fg2", fg2)  # = 673 fg2 (['o45x', 1], '1000001')
                                    if gn in fg2:
                                        fg2 = fg1[1]
                                        (lineno(), "fg1", fg1[0], "fg2", fg2)
                                        halte0 = False
                                        break
                                elif len(fg1) == 3:
                                    fg2 = fg1
                                    if gn == fg2[0]:
                                        (lineno(), "fg1", fg1, "fg2", fg2)
                                        halte0 = False
                                        break
                                (lineno(), "---- fg1", fg1, "fg2", fg2)
                                # 691 fg1 ((1, '123400000567'), (['o45x', 1], '1000001')) fg2 (['o45x', 1], '1000001')
                        if fg2:
                            for gl in gammes_loc:  # "gammes_loc = dic_codage" = Les gammes de 'globdicTcoup.txt'
                                gl_index += 1
                                (lineno(), "gl[0]", gl, "gn", gn, "fg2", fg2)
                                if fg2 in gl:  # Le numéro de gamme[gn] est présent.
                                    ind_loc = gammes_loc[gl_index]
                                    (lineno(), "fg2", fg2, "gl", gl, "gn", gn, "\t ind_loc", ind_loc)
                                    # 704 gl [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
                                    break  # La gamme est trouvée, la recherche est finie.

                    (lineno(), "ind_loc", ind_loc)
                    # 688 ind_loc [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'), (1, 4, '1000001'
                    if ind_loc:  # Gamme intégrale aux sept degrés aux binaires parfois identiques.
                        (" ", lineno(), "ind_loc", list(ind_loc)[0], "\t globe_num", gn, globe_num[gn])
                        # 691 ind_loc [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
                        # (1, 4, '1000001'), (1, 5, '1000000'), (1, 6, '1000001'), (1, 7, '1000001')]
                        (lineno(), "colonne_cop", colonne_cop)
                        # 695 colonne_cop ['', '1000001', '1000000', '1000101', '1011000', '1011001', '1000111',
                        gl_count = 0
                        for gl_gam in ind_loc:
                            (lineno(), "gl_gam", gl_gam, type(gl_gam[-1]))
                            bin_gl = gl_gam[-1]
                            ligne = colonne_cop.index(bin_gl)
                            (lineno(), "colon", colon, "ligne", ligne, "bin_gl", bin_gl)
                            if gl_count == 0:
                                nom_gl = gl_gam[0][0]
                                deg_gl = 1
                                self.colonne_gam[colon, 0] = [nom_gl]
                                (lineno(), colon, ligne, "\t nom_gl", nom_gl, "deg_gl", deg_gl, bin_gl)
                                (lineno(), "colonne_gam", self.colonne_gam)
                            else:
                                deg_gl = gl_gam[1]
                                (lineno(), colon, ligne, "\t deg_gl", deg_gl, bin_gl)
                            if (colon, ligne) not in self.colonne_gam.keys():
                                self.colonne_gam[colon, ligne] = []
                            self.colonne_gam[colon, ligne].append(str(deg_gl))
                            gl_count = 1
                            (lineno(), "colonne_gam", self.colonne_gam[colon, ligne])
                            (lineno(), "colon", colon, "ligne", ligne, "bin_gl", bin_gl, "vn_nbr",)
                            (lineno(), "colonne_cop[ligne]", colonne_cop[ligne])
                        colon += 1

                    (lineno(), "colonne_cop", colonne_cop)
                    (lineno(), "colonne_gam", self.colonne_gam, "\n colon", colon)
                    (lineno(), "gn", gn, "vn", vn, "colonne_gam", self.colonne_gam)
                    (lineno(), "gammes_loc", "gammes_loc")
            (lineno(), "colonne_gam", self.colonne_gam.keys())

            cc += 1  # Nombre d'accompagnements des binaires dans la liste (en cours). Utile boucle 'while'

        "# colonne_gam = Clé (colonne, ligne). Valeur (Position zéro = Nom-gamme. Autres = Degrés numériques (1234567)"
        "# Intégrer 'self.gammes_bin' et repérer les gammes aux mêmes binaires (colorations)."
        # 342 self.gammes_bin {'x26-': 'Ok', '*5': 'Ok', '-34': 'Ok', 'o63-': 'Ok', 'o34x': 'Ok', '-25o': 'Ok'...
        "# Construction dictionnaire "
        dic_keys = {}
        for g_key in self.colonne_gam.keys():
            if g_key[1] == 0:
                dic_keys[g_key[0]] = []
            dic_keys[g_key[0]].append(g_key)
        (lineno(), "dic_keys", dic_keys.keys())
        (lineno(), "gammes_loc", len(gammes_loc), len(self.colonne_gam.keys()))

        "# Reconnaissance des binaires anciens, pour une coloration des degrés."
        key_lig = []  # Enregistre les nouvelles lignes.
        for c_col0 in range(0, 66):
            c_col = c_col0 + 1
            if c_col == 1:
                for dk in dic_keys[c_col]:
                    key_lig.append(dk[1])
            else:
                long_k, lo = len(dic_keys[c_col]), 0
                for dk in dic_keys[c_col]:
                    if dk[1] not in key_lig:  # Il provient des nouvelles lignes.
                        key_lig.append(dk[1])
                        (lineno(), "If c_col", c_col, "long_k", long_k)
                    else:  # dk[1] in key_lig
                        lo += 1
                        # print(lino(), "c_col", c_col, "lo", lo, "self.colonne_gam", self.colonne_gam[c_col, 0])
                if long_k == lo:
                    self.gammes_bin[self.colonne_gam[c_col, 0][0]] = "Ok"
                (lineno(), "long_k", long_k, "\n dic_keys", dic_keys[c_col], dic_keys)
            (lineno(), " **************************************************** ")
        (lineno(), "key_lig", key_lig, "\n dic_keys", "dic_keys")
        (lineno(), "self.gammes_bin", self.gammes_bin)

    def traite_ego_iso(self, forme, tip):
        """Traitement par redistribution des gammes EGO et ISO.
        Utile pour former les modes binaires et alimenter : self.age_dict, self.con_dict.
        Self.age_dict : clés énumérées, valeurs = modes binaires.
        Self.con_dict : clés conteneurs, valeurs = modes binaires.
        À l'aide de self.gammic qui a les modes binaires diatoniques."""
        (lineno(), "Fonction_T forme", forme[:3], "tip", tip)
        # 1993 Fonction_T forme ['102034050067', '102304005670', '120300456070'] tip ego_age
        # 1993 Fonction_T forme ['1101200', '1012001', '0120011'] tip ego_con
        # 1993 Fonction_T forme ['4000010', '0000104', '0001040'] tip iso_con
        # 1993 Fonction_T forme ['100002345607', '123450670000', '123405600007'] tip iso_age

        # self.age_dict, self.con_dict. Ont des éléments en ordre croissant.
        don_con, don_age = [], []
        if tip in ("iso_con", "ego_con"):
            for k_con in forme:
                don_con.append(self.con_dict[k_con])
                (lineno(), "forme", forme[:3], "EGO k_con", k_con, "don_con", don_con)
                # 1138 EGO k_con 0000500 don_con ['1000000', '1000001', '1000001']
            (lineno(), "DEF TRAITE CON", "k_con", k_con, don_con)  # 1133 CON 1000001
        elif tip in ("iso_age", "ego_age"):
            for k_age in forme:
                don_age.append(self.age_dict[k_age])
                (lineno(), "forme", forme[:3], "ISO k_age", k_age, "don_age", don_age)
                # 1144 ISO k_age 123000004567 don_age ['1000001', '1000001', '1000001']
            (lineno(), "DEF TRAITE AGE", "k_age", k_age, don_age)  # 1138 AGE 1000000
        if don_con:
            (lineno(), "DEF TRAITE CON", don_con)  # 1133 CON 1000001
            return don_con, "iso_con"
        if don_age:
            (lineno(), "DEF TRAITE AGE", don_age)  # 1138 AGE 1000000
            return don_age, "iso_age"

    def custom_dialog(self, event):
        if event == "00":
            dialog = Toplevel()
            dialog.title("Confirmation")
            dialog.geometry("250x120+1500+100")  # Définir une taille de fenêtre
            Label(dialog, text="Voulez-vous continuer ?").pack(pady=10)

            def action11():
                self.retour_bouton = 11
                ("Action 11", self.retour_bouton)
                dialog.destroy()

            def action22():
                self.retour_bouton = 22
                ("Action 22", self.retour_bouton)
                dialog.destroy()

            def action33():
                self.retour_bouton = 33
                ("Action 33", self.retour_bouton)
                dialog.destroy()

            def cancel_action():
                self.retour_bouton = 11
                ("Annulé", self.retour_bouton)
                dialog.destroy()

            button_frame = Frame(dialog)
            button_frame.pack(pady=10)
            textes = ["11", "22", "33", "Cancel"]
            actions = [action11, action22, action33, cancel_action]
            boutons = []  # Liste des boutons.
            for i in range(4):
                btn = Button(button_frame, text=textes[i], command=actions[i])
                btn.pack(side="left", padx=5)
                boutons.append(btn)
            # Mettre le gros plan sur le premier bouton et lier la touche "Return"
            boutons[0].focus_set()
            dialog.bind("<Return>", lambda event: boutons[0].invoke())
            dialog.transient(self)  # Garder la boîte de dialogue au-dessus de la fenêtre principale
            dialog.grab_set()  # Empêcher l'interaction avec la fenêtre principale tant que la boîte est ouverte
            self.wait_window(dialog)  # Attendre que la boîte soit fermée
            self.protocol("WM_DELETE_WINDOW", dialog.destroy())
        elif event == "66":
            self.retour_bouton = 66
        (lineno(), "Fonction dialog", event, "retour_bouton", self.retour_bouton)
        return self.retour_bouton

    def reforme_bin(self, lab, bin):
        """Cette fonction est chargée de récupérer les formes binaires à partir des formes énumérées.
        Les formes énumérées sont incluses dans les clefs du dictionnaire 'self.gammic'.
          # La fonction REFORME_BIN n'est pas appelée dans CLIC_IMAGE en type "MODES".
            Reforme_bin est appelée quand le type est "Gammes" ou "Contient" """
        table, tab_liste = [], []
        ("La variable table est le récipient dans lequel les données sont récoltées pour les redistribuer."
         "Il y a self.gam_iso = self.gam_gen | Ne récupère que les formes énumérées des clefs de self.gammic.keys()."
         "# 870 gam_iso :"
         "      [123400000567, 123400056007, 123400050607, 123400050067, 123400500607, 123405000607... Fig_1&2"
         "Et, self.gam_ego = écriture sur le fichier 'gamme_majeure.txt' des formes énumérées primordiales. Fig_3à6"
         "# # 926 gam_ego :"
         "      ['102034050607', '102034500607', '123400000567', '123400050067', '123400056007',"
         "Les types['Modes', 'Gammes'] sont déjà en cours, sauf le type['Contient']. Voir dico self.gam_con."
         "# 895 scg 44 cag 120304506070 gam_con :"
         "      ['110111', '101110', '011101', '111011', '110110', '101101', '011011']"
         "# 937 self.gammic = {('o45x', '123400000567'): ['111100000111', '1000001', '1000001', '1000001',"
         "Création d'un dictionnaire aux clés numéros des gammes et aux valeurs conteneurs. Ligne 877."
         "self.gam_con = {}  # Dico, clé = numéro de gamme, valeur = mode diatonique de type conteneur.")
        # "* ____________________________ LES FIGURES"
        ("Voici la liste des figures qui figurent sur le panneau droit de l'interface utilisateur :"
         "self.images_liste = ['BoutonTriEgo.png', 'BoutonAntiEgo.png', 'BoutonTriIso.png', 'BoutonAntiIso.png',"
         "                    'BoutonTriInt.png', 'BoutonAntiInt.png']"
         "self.images_liste[0] = 'BoutonTriEgo.png' étant la figure 1")
        # "* ____________________________ DISTRIBUTION DES BINARISATIONS"
        ""
        #
        (lineno(), "lab", lab)
        if lab == "gam_ego":  # "[EGO] = Organisation composée à partir de la gamme naturelle......... 'self.gam_ego'"
            table = bin.copy()     # Section lab[ego]
            (lineno(), "RÉFORME gam_ego_table", list(table), "[:6]")
        elif lab == "con_ego":  # "[EGO] = Organisation composée à partir de la gamme naturelle......... 'self.gam_ego'"
            table = bin.copy()     # Section lab[ego]
            (lineno(), "RÉFORME con_ego_table", list(table)[:6])
        elif lab == "gam_ego_inv":              # Section lab[ego_inv]
            ego_inv = bin.copy()
            ego_inv.reverse()
            table = ego_inv.copy()
            (lineno(), "RÉFORME gam_ego_inv_table", list(table)[:6])
        elif lab == "con_ego_inv":  # Section lab[ego_inv]
            ego_inv = bin.copy()
            ego_inv.reverse()
            table = ego_inv.copy()
            (lineno(), "RÉFORME con_ego_inv_table", list(table)[:6])
            # "* ____________________________ FIN EGO _
            #
        elif lab == "gam_iso":  # "[ISO] = Organisation énumérée à partir du fichier `globdicTcoup.txt`. 'self.gam_iso'"
            table = bin.copy()
            (lineno(), "RÉFORME gam_iso_table", list(table)[:6])
        elif lab == "con_iso":
            table = bin.copy()
            (lineno(), "RÉFORME con_iso_table", list(table)[:6])
            #
        elif lab == "gam_iso_inv":
            iso_inv = bin.copy()
            iso_inv.reverse()
            table = iso_inv.copy()
            (lineno(), "RÉFORME gam_iso_inv_table", list(table)[:6])
        elif lab == "con_iso_inv":
            iso_inv = bin.copy()
            iso_inv.reverse()
            table = iso_inv.copy()
            (lineno(), "RÉFORME con_iso_inv_table", list(table)[:6])
        elif lab == "gam_iso_int":
            iso_int = bin.copy()
            iso_int.sort()
            table = iso_int.copy()
            (lineno(), "RÉFORME gam_iso_int_table", list(table)[:6])
        elif lab == "con_iso_int":
            iso_int = bin.copy()
            iso_int.sort()
            table = iso_int.copy()
            (lineno(), "RÉFORME con_iso_int_table", list(table)[:6])
        elif lab == "gam_iso_int_inv":
            iso_int_inv = bin.copy()
            iso_int_inv.sort()
            iso_int_inv.reverse()
            table = iso_int_inv.copy()
            (lineno(), "RÉFORME gam_iso_int_inv_table", list(table)[:6])
        elif lab == "con_iso_int_inv":
            iso_int_inv = bin.copy()
            iso_int_inv.sort()
            iso_int_inv.reverse()
            table = iso_int_inv.copy()
            (lineno(), "RÉFORME con_iso_int_inv_table", list(table)[:6])
        (lineno(), "FONCTION_REFORME_BIN lab", lab, "table", table[:3], type(table), len(table))
        # 1584 FONCTION_REFORME_BIN lab ego table [102034050607, 102034500607, 123400000567] <class 'list'> 66
        return table

    def clic_image(self, event):
        """Cette fonction convertit les modes binaires. Appel à fonction self reforme_bin
            En changeant le type, on ne change pas son ordre croissant, sauf pour les entiers libres.
            'self.dic_codage.values()' = le dictionnaire original.
            'dic_indice' = un dictionnaire = Les clés sont les noms et les valeurs sont les numéros des gammes.
            Il faut modifier le dictionnaire original, afin d'établir une nouvelle correspondance."""
        # Relance(dic_codage, dic_binary, dic_indice, dic_force, dic_colon, dic_titres).mainloop()
        self.comment_sta.clear()
        self.mod_type.clear()
        ("# Les listes[_iso0 et _iso1] changent selon le choix[Modes ou Gammes]. 'self.zone_w4.get()'"
         "[EGO] = Organisation composée à partir de la gamme naturelle......... 'self.gam_ego'"
         "[ISO] = Organisation composée à partir du fichier `globdicTcoup.txt`. 'self.gam_iso'"
         "[INT] = Organisation croissante des éléments [ISO = EGO]............. 'self.gam_int'")

        (lineno(), "Listes vides avant clic_image... Iso0", self.liste_iso1, "\t Iso1", self.liste_ego1)
        # 1612 Listes vides avant clic_image... Iso0 [] 	 Iso1 []
        # , "codage_cop" = Transformé de "dic_codage"
        # print("dic_indice", "dic_indice", "dic_binary", "dic_binary", "\n liste_iso", liste_iso, len(liste_iso))
        """self.images_liste = ["BoutonTriEgo.png", "BoutonAntiEgo.png", "BoutonTriIso.png", "BoutonAntiIso.png",
                                     "BoutonTriInt.png", "BoutonAntiInt.png"]"""
        x, y = event.x, event.y
        item_id = self.table_o.find_closest(x, y)[0]  # Récupère l'ID de l'objet le plus proche
        # item_id : (1=iso[non trié], 2=int[trié])
        ("\n", lineno(), "Clic_image/item", item_id, "zone_w4", self.zone_w4.get())
        # 1482 Clic_image/item_id 1 (1er bouton image)


        (" Le bouton radio zone_w4, nous informe sur le choix du type de lecture des gammes."
         "En un premier temps, nous avions un choix binaire naturel[0=Non majeur, 1=Majeur]"
         "Ensuite, les gammes établissaient des définitions sous une forme énumérée suivant les degrés[1234567]"
         "Pour finir, les définitions ne donnaient que les quantités des intervalles entre les notes."
         "Ainsi, les définitions originelles[colonne_bin, dic_binary] sont à modifier, pour les cas[Modes. Contient].")

        ("# Selon, liste_ego1 et liste_iso1 : type 'Modes' par défaut"
         "La liste_ego1[colonne_bin/di_colon]"
         "Di_colon = dic_colon = Liste, clés binaires liées aux choix de conversions."
         "La liste_iso1[dic_binary.keys]"
         "")
        self.tri = self.images_liste[item_id - 1]  # Relever le type de tri qui organise les gammes.
        self.comment_sta.append(self.zone_w4.get())
        self.comment_sta.append(self.tri[6:-4])
        liste_ego3, liste_iso3, ref_mode = [], [], ""
        mission_ego, mission_iso = [], []

        if self.zone_w4.get() == "Modes":
            self.liste_ego1 = self.colonne_bin.copy()  # Liste selon self.colonne_bin.copy() MAJEUR[EGO]
            self.liste_iso1 = list(self.dic_binary.keys())  # Liste selon self.dic_binary.keys() INITIAL[ISO]
        else:
            if self.comment_sta[1] in ('TriInt', 'AntiInt'):
                "# En mode '66', ordres['EGO', 'ISO'], une fois triés en ordre croissant, ils deviennent égaux."
                # Pas besoin de questionner sur la grandeur des sections.
                self.retour_bouton = self.custom_dialog("66")
                retour_k = Relance.k_num_fonc(self)
                mission_ego, mission_iso = retour_k[0], retour_k[1]
                (lineno(), "retour fonction retour_k66", retour_k[0], retour_k[1], retour_k[2])
            else:
                "# Question de sélection d'envergure des sections, 11 par défaut ou bien 22 ou 33."
                self.retour_bouton = self.custom_dialog("00")
                (lineno(), "retour_bouton", self.retour_bouton, "comment_sta", self.comment_sta)
                # 2162 retour_bouton 11 comment_sta ['Gammes', 'TriEgo']
                retour_k = Relance.k_num_fonc(self)
                mission_ego, mission_iso = retour_k[0], retour_k[1]
                (lineno(), "retour fonction retour_k", retour_k[0], retour_k[1], retour_k[2])


        l0, l1 = self.liste_iso1, self.liste_ego1
        (lineno(), "_iso0[ISO]", list(l0)[:3], "_iso1[EGO]", list(l1)[:3], "len0_1 :", len(l0), len(l1))
        # 1937 _iso0[ISO] [] _iso1[EGO] [] len0_1 : 0 0

        ("# Série item_id : a de 1 à 6 onglets."
         "  Type 'Modes' = Traité ici (clic_image) et n'a pas d'appel à la fonction (reforme_bin)"
         "  Type 'Gammes' et 'Contient' > Appellent la fonction (reforme_bin)")
        if item_id == 1:  # Conversion des modes originaux en nombres entiers.
            "# 'liste_ego1' = Liste selon self.colonne_bin.copy()"
            ref_mode = "ego"
            if self.zone_w4.get() == "Modes":
                (lineno(), "MODES * ego")
                liste_ego3 = self.liste_ego1.copy()
            elif self.zone_w4.get() == "Gammes":  # mission_ego/gammes
                (lineno(), "GAMMES * ego")
                self.liste_ego1 = self.reforme_bin("gam_ego", mission_ego)  # 'liste_ego1' = Liste MAJEURE
                liste_ego3 = self.liste_ego1.copy()
            elif self.zone_w4.get() == "Contient":  # mission_ego/contient
                (lineno(), "CONTIENT * ego")
                self.liste_ego1 = self.reforme_bin("con_ego", mission_ego)  # 'liste_ego1' = Liste MAJEURE
                liste_ego3 = self.liste_ego1.copy()
            liste_ego = liste_ego3.copy()  # La liste_ego récupère finalement liste_ego3
            self.dic_ego["type"] = "Images libres"
            for ind in range(len(liste_ego)):
                self.dic_ego[liste_ego[ind]] = liste_ego[ind]
                (lineno(), "ind", ind, liste_ego[ind])
            self.dic_trans = self.dic_ego.copy()
            (lineno(), "dic_trans", self.dic_trans, "list(self.dic_trans.keys())[:6]")  # 1963 self.dic_trans ['type']
        elif item_id == 2:  # Inversion des modes originaux en nombres entiers.
            "# 'liste_ego1' = Liste selon self.colonne_bin.copy()"
            ref_mode = "ego_inv"
            if self.zone_w4.get() == "Modes":
                (lineno(), "MODES * ego_inv")
                liste_ego_inv = self.liste_ego1.copy()
                liste_ego_inv.reverse()
                liste_ego3 = liste_ego_inv.copy()
            elif self.zone_w4.get() == "Gammes":  # mission_ego/ego_inv/gammes
                (lineno(), "GAMMES * ego_inv")
                self.liste_ego1 = self.reforme_bin("gam_ego_inv", mission_ego)  # 'liste_ego1' = Liste MAJEURE
                liste_ego3 = self.liste_ego1.copy()
            elif self.zone_w4.get() == "Contient":  # mission_ego/contient
                (lineno(), "CONTIENT * ego_inv")
                self.liste_ego1 = self.reforme_bin("con_ego_inv", mission_ego)  # 'liste_ego1' = Liste MAJEURE
                liste_ego3 = self.liste_ego1.copy()
            liste_ego_inv = liste_ego3.copy()
            self.dic_ego_inv["type"] = "Images libres inversées"
            (lineno(), "liste_ego_inv", liste_ego_inv)
            for ind in range(len(liste_ego_inv)):
                self.dic_ego_inv[liste_ego_inv[ind]] = liste_ego_inv[ind]
                (lineno(), "ind", ind, liste_ego_inv[ind])
            self.dic_trans = self.dic_ego_inv.copy()
            (lineno(), "self.dic_trans", list(self.dic_trans.keys())[:6])
            # ______________________________________ FIN EGO _________________
        elif item_id == 3:  # Conversion des modes originaux en nombres entiers.
            "# 'liste_iso1' = Liste selon self.dic_binary.keys()"
            ref_mode = "iso"
            if self.zone_w4.get() == "Modes":
                (lineno(), "MODES * iso")
                liste_iso3 = [int(x) for x in self.liste_iso1 if x != '']
            elif self.zone_w4.get() == "Gammes":
                (lineno(), "GAMMES * iso")
                self.liste_iso1 = self.reforme_bin("gam_iso", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
            elif self.zone_w4.get() == "Contient":
                (lineno(), "CONTIENT * iso")
                self.liste_iso1 = self.reforme_bin("con_iso", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
            liste_iso = liste_iso3.copy()
            self.dic_iso["type"] = "Entiers libres"
            for ind in range(len(liste_iso)):
                self.dic_iso[str(liste_iso[ind])] = liste_iso[ind]
                (lineno(), "ind", ind, liste_iso[ind])
            self.dic_trans = self.dic_iso.copy()
            (lineno(), "self.dic_trans", list(self.dic_trans.keys())[:6])
        elif item_id == 4:  # Inversion des modes originaux en nombres entiers.
            "# 'liste_iso1' = Liste selon self.dic_binary.keys()"
            ref_mode = "iso_inv"
            if self.zone_w4.get() == "Modes":
                (lineno(), "*\t* MODES * iso_inv")
                liste_iso3 = self.liste_iso1.copy()
                liste_iso3.reverse()
            elif self.zone_w4.get() == "Gammes":
                (lineno(), "*\t* GAMMES * iso_inv")
                self.liste_iso1 = self.reforme_bin("gam_iso_inv", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
            elif self.zone_w4.get() == "Contient":
                (lineno(), "*\t* CONTIENT * iso_inv")
                self.liste_iso1 = self.reforme_bin("con_iso_inv", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
            liste_iso_inv = liste_iso3.copy()
            self.dic_iso_inv["type"] = "Entiers libres inversées"
            for ind in range(len(liste_iso_inv)):
                self.dic_iso_inv[liste_iso_inv[ind]] = liste_iso_inv[ind]
                (lineno(), "ind", ind, liste_iso_inv[ind])
            self.dic_trans = self.dic_iso_inv.copy()
            (lineno(), "self.dic_trans", list(self.dic_trans.keys())[:6])
        elif item_id == 5:  # Conversion des modes originaux en nombres entiers.
            "# 'liste_iso1' = Liste selon self.dic_binary.keys()"
            ref_mode = "iso_int"
            if self.zone_w4.get() == "Modes":
                liste_int1 = [int(x) for x in self.liste_iso1 if x != '']
                liste_int1.sort()
                liste_iso3 = liste_int1.copy()
                (lineno(), "*\t* MODES * iso_int")
            elif self.zone_w4.get() == "Gammes":
                self.liste_iso1 = self.reforme_bin("gam_iso_int", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
                (lineno(), "*\t* GAMMES * iso_int", "liste_iso3", list(liste_iso3)[:6])
            elif self.zone_w4.get() == "Contient":
                self.liste_iso1 = self.reforme_bin("con_iso_int", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
                (lineno(), "*\t* CONTIENT * iso_int", "liste_iso3", list(liste_iso3)[:6])
            liste_int = liste_iso3.copy()
            self.dic_int["type"] = "Entiers triés"
            for ind in range(len(self.liste_iso1)):
                self.dic_int[str(liste_int[ind])] = liste_int[ind]
                (lineno(), "ind", ind, liste_int[ind])
            self.dic_trans = self.dic_int.copy()
            (lineno(), "dic_trans", self.dic_trans, "\n list(self.dic_trans.keys())[:6]")
        elif item_id == 6:  # Inversion des modes originaux en nombres entiers.
            "# 'liste_iso1' = Liste selon self.dic_binary.keys()"
            ref_mode = "iso_int_inv"
            if self.zone_w4.get() == "Modes":
                liste_int_inv1 = [int(x) for x in self.liste_iso1 if x != '']
                liste_int_inv1.sort()
                liste_int_inv1.reverse()
                liste_iso3 = liste_int_inv1.copy()
                (lineno(), "MODES * iso_int_inv", "liste_iso3", list(liste_iso3)[:6])
            elif self.zone_w4.get() == "Gammes":
                self.liste_iso1 = self.reforme_bin("gam_iso_int_inv", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
                (lineno(), "GAMMES * iso_int_inv", "liste_iso3", list(liste_iso3)[:6])
            elif self.zone_w4.get() == "Contient":
                self.liste_iso1 = self.reforme_bin("con_iso_int_inv", mission_iso)  # 'liste_iso1' = Liste INITIAL
                liste_iso3 = self.liste_iso1.copy()
                (lineno(), "CONTIENT * iso_int_inv", "liste_iso3", list(liste_iso3)[:6])
            liste_int_inv = liste_iso3.copy()
            self.dic_int_inv["type"] = "Entiers triés inversées"
            for ind in range(len(self.liste_iso1)):
                self.dic_int_inv[str(liste_int_inv[ind])] = liste_int_inv[ind]
                (lineno(), "ind", ind, liste_int_inv[ind])
            self.dic_trans = self.dic_int_inv.copy()
            (lineno(), "self.dic_trans", list(self.dic_trans.keys())[:6])
            # 2083 liste_iso1[ISO] [], liste_ego1[EGO] []
        (lineno(), self.zone_w4.get(), "ref_mode", ref_mode)
        (lineno(), "self.dic_trans[clé égal valeur]", self.dic_trans.keys())

        (lineno(), "liste_iso1[ISO]", list(l0)[:6], "\n\tliste_ego1[EGO]", list(l1)[:6])
        ("PHASE DE SÉLECTION de l'item_id = self.images_liste = ['BoutonTriEgo.png', 'BoutonAntiEgo.png', "
         "'BoutonTriIso.png', 'BoutonAntiIso.png','BoutonTriInt.png', 'BoutonAntiInt.png']"
         "L'item_id = indice self.images_liste[0] = 'BoutonTriEgo' en (ref_mode = 'ego')")
        if item_id == 1 and self.zone_w4.get() == "Modes":  # Sélection de type "MODES"
            self.mod_type = ["Vide"]  # On intie self.mod_type vide par défaut =
            (lineno(), "self.dic_trans", self.dic_trans.keys())
        else:
            self.mod_type.append(item_id)  # Format self.mod_type [item_id, {self.dic_trans}]
            self.mod_type.append(self.dic_trans)
        #
        # self.tri = self.images_liste[item_id - 1]  # Relever le type de tri qui organise les gammes.
        if len(self.mod_type) < 2:
            (lineno(), "long mod_type", len(self.mod_type), type(self.mod_type))
            # 1694 long mod_type 1 <class 'list'>
            (lineno(), "item_id", item_id, "self.mod_type", self.mod_type, len(list(self.mod_type)))
            # 1696 item_id 1 self.mod_type ['Vide'] 1
        else:
            (lineno(), "item_id", item_id, "self.mod_type", list(self.mod_type[1])[:6], len(list(self.mod_type)))
            # 1698 item_id 3 self.mod_type ['type', '1000001', '1000000', '1000101', '1011000', '1011001'] 2
        (lineno(), "self.tri", self.tri)
        # self.comment_sta.append(self.zone_w4.get())
        # self.comment_sta.append(self.tri[6:-4])
        (lineno(), "self.comment_sta", self.comment_sta, " | | ", self.comment_sta[6:-4], "self.tri", self.tri)
        # 2300 self.comment_sta ['Gammes', 'TriEgo']  | |  [] self.tri BoutonTriEgo.png
        clic_tag = "clic_image"
        self.quitter(clic_tag)
        retour_func = func_ima(self.mod_type, self.tri)
        (lineno(), "clic_image retour_func", retour_func, len(retour_func))
        (lineno(), "\n _______________________________________________ \n")

        (lineno(), "dic_binary", self.dic_binary.keys())
        Relance(dic_codage, code_ages, dic_binary, dic_indice, dic_force, retour_func[0], dic_gammic, retour_func[1],
                self.zone_w0.get(), self.zone_w1.get(), self.zone_w2.get(), self.zone_w3.get(), self.zone_w4.get(),
                self.comment_sta, self.retour_bouton)

    def on_click(self, event):
        """Fonction chargée de la structuration des modèles diatoniques sous la forme de valeurs signées."""
        item = self.tableau.find_closest(event.x, event.y)
        co_y = event.y
        note = self.tableau.itemcget(item, 'text')
        tags = self.tableau.gettags(item[0])
        gamme = tags[0]  # Supposons que le deuxième tag soit le nom de la gamme
        ("# On commence par vérifier si l'utilisateur a choisi '☺' qui regroupe plusieurs degrés."
         "Ces regroupements sont dans le dictionnaire[self.dic_multiples[gamme]].")
        tab_notes = []
        if note == '☺':
            for dmg in self.dic_multiples[gamme]:
                if dmg[2] < co_y < dmg[3]:
                    tab_notes.append(dmg[0])
                    (lineno(), "\t dmg", dmg)
            (lineno(), "tab_notes", tab_notes)
            (lineno(), "dic_multiples", self.dic_multiples[gamme], "gamme", gamme, "note", note, "co_y", co_y)
            # 1090 dic_multiples [('C', '1', 209, 219), ('-D', '2', 209, 219), ('oE', '3', 183, 193),
            # ('oF', '4', 183, 193)] gamme o46- note ☺12 co_y 186
        else:
            tab_notes.append(note)

        "# Visiter les notes enregistrées dans la liste 'tab_notes'."
        self.message.clear()
        for note in tab_notes:
            self.num_static[note] = self.dic_indice[gamme]  # Dictionnaire, clé = Nom, valeur = Numéro.
            mod_diatonic = self.di_ages[self.num_static[note]]  # Le dictionnaire des formes énumérées.
            "# Prendre l'indice de la note diatonique sélectionnée...>"
            id_note = self.gam_diatonic[gamme].index(note)
            mode_id = mod_diatonic[id_note]
            "# >... Pour initialiser la tonalité énumérée."
            tone_id = {gamme: []}  # Le dictionnaire des énumérations diatoniques.
            for ti in range(1, 8):
                id1, id2 = mode_id.index(str(ti)), self.majeure.index(str(ti))
                diff_id = id1 - id2
                if diff_id > -1:
                    note_id = str(gamma.tab_sup[diff_id]) + str(ti)
                else:
                    note_id = str(gamma.tab_inf[diff_id]) + str(ti)
                tone_id[gamme].append(note_id)  # Insertion de l'énumération modale.
                ("*", lineno(), "diff_id", diff_id, note_id)
            deg = self.gam_diatonic[gamme]
            tab = deg[id_note:] + deg[:id_note]
            id_mode = self.modaux[id_note]

            "# La référence 'self_majeure', dans le module 'gammes_audio.py'."
            ("\n", lineno(), "Gamma majeure", gamma.dic_maj[self.gam_diatonic[gamme][0]])
            #  1124 Gamma majeure ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B']
            (f"{lineno()} Note {note} Gamme {gamme} Numéro {self.num_static[note]}"
             f" Mode {mod_diatonic[id_note]}\nGamme {self.gam_diatonic[gamme]}")
            # 1126 Note +A Gamme +6 Numéro 46 Mode 123040560700
            # Gamme ['C', 'D', 'E', 'F', 'G', '+A', 'B']
            # (f"{lineno()} Deg {id_mode} Énuméré {mode_id} Maj {self.majeure} \n Tab {tab} \nTone {tone_id[gamme]}")
            # 1113 Deg VI Énuméré 123040560700 Maj 102034050607
            #  Tab ['+A', 'B', 'C', 'D', 'E', 'F', 'G']
            # Tone ['1', '-2', 'o3', '-4', '-5', 'o6', 'o7']

            "# Afficher les informations relatives au choix de l'utilisateur."
            t_dia = "".join(map(str, self.gam_diatonic[gamme][0]))
            g_dia = ", ".join(map(str, self.gam_diatonic[gamme]))
            n_choix = t_dia + " " + gamme
            m_dia = ", ".join(map(str, tab))
            f_dia = ", ".join(map(str, tone_id[gamme]))
            enr_mess = (f"Le degré modal fondamental = {g_dia}\n"
                        f"La gamme choisie = {n_choix}\n"
                        f"Le modèle énuméré = {mode_id}\n"
                        f"Le degré diatonique = {id_mode}\n"
                        f"La note tonique = {note}\n"
                        f"Le mode diatonique choisi = {m_dia}\n"
                        f"La formule tonale choisie = {f_dia}")
            if note == tab_notes[-1] and self.zone_w2.get() != "Diatone":
                enr_mess += f"\n\n (LE BOUTON-RADIO DIATONIQUE ORDONNE LES DEGRÉS).\n"
            self.message.append(enr_mess)

        # Joindre tous les messages avec des sauts de ligne
        texte_complet = "\n---\n".join(self.message)
        showinfo("Informations", f"{texte_complet}")

    def bouton_bin(self, bb, cc):
        """Pratiquer les redirections des boutons d'en-tête[noms des gammes] et latéral gauche[binômes].
            Cette fonction est située après avoir initialisé les dictionnaires nécessaires. """
        '''Colonnes-gam {(1, 0) : ['0'], (1, 2) : ['1'], (1, 3) : ['2'], (1, 4) : ['3']}
        Tri None
        Dic-indice {'o45x' : 1, 'o46-' : 2, 'o4' : 3, 'o46+' : 4, 'o45-' : 5, 'o54-' : 6}
        Dic-codage {(1, '123400000567') : [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001')}
        Colonne-bin ['', '', '1111111', '1101110', '1001100', '1110111', '1111110', '1101100']
        Cc {1 : ['123400000567', '123000004567', '120000034567', '100000234567', '123456700000']}
        Bb x26- ou binaire
        Di_fort = dic_force. Dictionnaire, clé = binaire, valeur = dic_codage avec le même binaire.'''
        (lineno(), "**   Fonction bouton_bin bb ", bb, "\n cc", cc[1])
        (lineno(), "\nbb ", bb, "\ncc ", cc, "\ncolonne_gam ", self.colonne_gam, "\ncolonne_bin ",
         self.colonne_bin, "\ndic_indice ", self.dic_indice, "\ndic_codage ", self.dic_codage,
         "\nself.dic_force", self.dic_force, "\ntri ", self.tri)
        # Suivi de l'erreur 'o4' dans colonne_gam = (12, 0): ['o4'], (12, 22): ['1'], (12, 12): ['2', '3', '4'],
        # (12, 23): ['5'], (12, 21): ['6'], (12, 13): ['7']

        "# Production des listes des fréquences hertziennes de chacune des notes et des octaves."
        # Selon l'aptitude auditive humaine allant de 20 hz à 20 000 hz.
        ref = 440  # Au niveau de la clé de verrouillage du piano.
        notes = ["A", "", "B", "C", "", "D", "", "E", "F", "", "G", "", ]
        dic_notes = {}  # Dictionnaire, clé = note et valeur = fréquence hz
        octaves = [13.75, 27.5, 55, 110, 220, 440, 880, 1760, 3520, 7040, 14080, 28160]
        dic_octaves = {}  # Dictionnaire des octaves, clés = octave, valeur = fréquences hz
        lis_octaves = []
        y = 0  # Pour compter l'espace chromatique.
        (lineno(), ref, notes, dic_notes, octaves, dic_octaves, lis_octaves)
        for octa in octaves:  # Les octaves une par une.
            i = 0  # Pour compter l'espace chromatique.
            dic_octaves[octa] = []
            num_a = "A" + str(y)
            dic_notes[num_a] = []
            for x in range(1, 13):  # Les emplacements chromatiques.
                note_freq = octa * 2 ** ((x - 1) / 12)
                note_freq = round(note_freq, 2)
                dic_octaves[octa].append(note_freq)
                passe = ""
                if note_freq not in lis_octaves:
                    lis_octaves.append(note_freq)
                    note_y = notes[i] + str(y)
                    passe = [note_y, note_freq]  # Données modifiables en mode 'liste'.
                    dic_notes[num_a].append(passe)
                (lineno(), notes[y], "passe", passe, "i", i, "y", y)
                i += 1
                (lineno(), octa, "note_freq", note_freq, i)
            (lineno(), "\n dic_notes", dic_notes[num_a], "num_a", num_a)
            y += 1
        # Résultat sous la forme de dic_notes, clé = A numéroté, valeur = note et sa fréquence hz.
        (lineno(), "dic_octaves", dic_octaves.keys(), "\ndic_notes", dic_notes)

        "# Nettoyage des vides contenus dans la liste colonne-bin."
        vide = self.colonne_bin.count("")
        if vide:
            for v in range(vide):
                self.colonne_bin.remove("")

        "# Envoyer les données à la fonction respective, en attente de réponse."
        colis1 = bb, cc, self.colonne_gam, self.colonne_bin, self.dic_indice, self.dic_codage, self.dic_force, self.tri
        colis2 = dic_notes
        "Bb varie selon la sélection"
        # colis1[0] = bb  +34x
        "Cc est invariant."
        # ..1[1] = cc  {1: ['123400000567', '123000004567', '120000034567', '100000234567', '123456700000', '',
        "Colonne_gam et colonne_bin varient selon la sélection."
        # ..1[2] = colonne_gam  {(1, 0): ['0'], (1, 2): ['1'], (1, 3): ['2'], (1, 4): ['3'],
        # ..1[3] = colonne_bin  ['', '', '1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1001000',
        "Dic_indice, dic_codage, dic_force sont produits au début et sont invariants."
        # ..1[4] = dic_indice  {'o45x': 1, 'o46-': 2, 'o4': 3, 'o46+': 4, 'o45-': 5, 'o54-': 6, '*5': 7, '-34': 8,
        # ..1[5] = dic_codage  {(1, '123400000567'): [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
        # ..1[6] = self.dic_force {'1000001': [((1, '123400000567'), (['o45x', 1], '1000001')), (1, 2, '1000001'),
        "Le tri varie selon la sélection"
        # ..1[7] = tri  None
        # colis2 {'A0': [('A', 13.75), ('', 14.56761754744031), ('B', 15.433853164253879), ('C', 16.351597831287414)
        liste_gam = [colis1[2][x][0] for x in colis1[2] if x[1] == 0]  # Les noms des gammes, selon le tri.
        if len(str(bb)) < 7:
            "# Jonction module gammes_audio"
            self.gam_son = gamma.audio_gam(colis1, colis2, "Gammes", self.zone_w1.get(), self.zone_w2.get())
            (lineno(), "Gam *", self.zone_w1.get(), self.gam_son.keys())
            # 1100 Gam * fréquence {'+6' : [['C6', 1046.5], ['D7', 2349.32], ['E3', 164.81], ['F6', 1396.91],
            # ['G7', 3135.96], ['+A2', 58.27], ['B3', 123.47]]}
        else:
            ("# Jonction module binomes_audio"
             "Ordonner les clés est nécessaire dans cette lecture des modes binaires.")
            self.gam_son = {}  # Nouveau dictionnaire utile.
            self.gam_son1 = gamma.audio_gam(colis1, colis2, "Binomes", self.zone_w1.get(), self.zone_w2.get())
            for lg in liste_gam:
                for k_sgs, v_sgs in self.gam_son1.items():
                    if k_sgs == lg:
                        self.gam_son[k_sgs] = v_sgs
                        (lineno(), "kv_sgs", k_sgs, v_sgs)
            (lineno(), "Bin *", self.zone_w1.get(), self.gam_son.keys())
            # 1106 Bin * {'-3': [['C6', 1046.5], ['D6', 1174.66], ['-E5', 622.25], ['F6', 1396.91], ['G6', 1567.98],
            # ['A6', 880.0], ['B2', 61.74]]}

        "# Produire les structures nommées (notes, lignes), afin d'aider à l'écriture sur l'interface."
        tab_donne = list(self.gam_son.keys())
        (lineno(), "tab_donne", tab_donne, "dic_donne", self.dic_donne)
        # 1112 tab_donne ['+6'] dic_donne {}
        ("# Trouver la clé correspondante dans colis1[2] (dynamique)"
         "  # ..1[2] = colonne_gam  {(1, 0): ['0'], (1, 2): ['1'], (1, 3): ['2'], (1, 4): ['3'],")
        for clef in tab_donne:  # Passage en revue des clés enregistrées.
            (lineno(), "for clef in tab_donne : ======= \t", clef)
            # 1117 for clef in tab_donne : ======= 	 +6
            num_don, rng_don = None, 0
            for kco in colis1[2].keys():  # Chercher la clé dans le dictionnaire 'colis1[2]'.
                if clef in colis1[2][kco]:  # La gamme est localisée dans le dictionnaire.
                    num_don = kco[0]  # La clef est le nom qui n'est vu qu'en 'kco[1] = 0'.
                    (lineno(), "num_don", num_don, "Kco", kco, "colis1_kco", colis1[2][kco])
                    # 1260 num_don 12 Kco (12, 0) colis1_kco ['+6']
                elif num_don in kco:
                    ("# Construire la clef du dictionnaire 'dic_donne'."
                     "L'ordre des degrés n'est pas constant, le sixième peut paraitre avant le cinquième."
                     "Voir la gamme 'o46+'. Pour le moment, les degrés ont été traités différemment."
                     "Puisque les notes diatoniques n'ont pas encore été attribuées.")
                    if len(colis1[2][kco]) == 1:
                        if num_don == kco[0]:
                            clef_don = clef, colis1[2][kco][0]
                            self.dic_donne[clef_don] = kco
                            rng_don += 1  # Ce compte permet d'éviter des lectures inutiles.
                            (lineno(), "clef", clef_don, "dic", self.dic_donne[clef_don], "Kco", kco, rng_don)
                            # 1179 clef_don ('o45x', '5') dic_donne (3, 13)
                    else:
                        for ite in colis1[2][kco]:
                            if num_don == kco[0]:
                                clef_don = clef, ite
                                self.dic_donne[clef_don] = kco
                                rng_don += 1  # Ce compte permet d'éviter des lectures inutiles.
                                (lineno(), "clef", clef_don, "dic", self.dic_donne[clef_don], "Kco", kco, rng_don)
                                # 1185 clef_don ('o45x', '1') dic_donne (3, 12)
                                # 1185 clef_don ('o45x', '2') dic_donne (3, 12)
                                # 1185 clef_don ('o45x', '3') dic_donne (3, 12)
                                # 1185 clef_don ('o45x', '4') dic_donne (3, 12)
                                # 1185 clef_don ('o45x', '6') dic_donne (3, 12)
                                # 1185 clef_don ('o45x', '7') dic_donne (3, 12)
                if rng_don == 7:
                    (lineno(), "rng_don", rng_don)
                    break
            # break de vérification partielle, à cause des degrés aux mêmes binaires.

        def sine_tone(frequency, duration, sample_rate=18000):
            try:
                """# Calculer le nombre total d'échantillons"""
                # Initialiser PyAudio
                p = pyaudio.PyAudio()
                # Ouvrir un flux de sortie
                stream = p.open(format=pyaudio.paFloat32,  # 8 bits par échantillon
                                channels=1,  # mono
                                rate=sample_rate,  # fréquence d'échantillonnage
                                output=True)  # flux de sortie

                # Génération de l'onde sonore
                t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
                wave = 0.5 * np.sin(2 * np.pi * frequency * t)
                # Lecture de l'onde sonore
                stream.write(wave.astype(np.float32).tobytes())

                # Fermeture du flux audio
                stream.stop_stream()
                stream.close()
                time.sleep(0.1)

                # Fermeture de PyAudio
                p.terminate()
                (lineno(), "Sine_tone", frequency)
            except Exception as f:
                print(lineno(), "Erreur dans 'sine_tone'", f)

        # Empêcher la mise en veille de l'ordinateur
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

        # Gestion.
        self.tableau.bind("<Button-1>", self.quitter("Passer"))  # Du clic de la souris
        self.focus_force()  # De la fenêtre principale.

        "# Nettoyer le tableau pour un nouvel affichage."
        if self.all_rectangles:
            for item in self.all_rectangles:
                self.tableau.delete(item)
            self.all_rectangles.clear()
            for item in self.all_textes:
                self.tableau.delete(item)
            self.all_textes.clear()
        (lineno(), "Liste", self.all_rectangles)
        "# Générer les sons avec les fréquences et les notes de 'self.gam_son'."
        # liste_gam = [colis1[2][x][0] for x in colis1[2] if x[1] == 0]  # Les noms des gammes, selon le tri.
        # 328 tab_lig [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, ] long 68
        (lineno(), "tab_donne", tab_donne, "dic_donne", self.dic_donne, "\nliste_gam", liste_gam)
        # 1349 tab_donne ['+6'] dic_donne {('+6', '1'): (66, 61), ('+6', '2'): (66, 62), ('+6', '3'): (66, 17),
        # ('+6', '4'): (66, 56), ('+6', '5'): (66, 63), ('+6', '6'): (66, 13), ('+6', '7'): (66, 18)}
        # liste_gam ['-2', '0', '-25', '-26', '-6', '-56', '+26', '-26o', 'o6', '-5', 'o45x', 'o46-', 'o4',

        "# Comment obtenir les coordonnées des rectangles toute hauteur."
        # 262 tab_rec [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, ] long 66
        # liste_gam ['-2', '0', '-25', '-26', '-6', '-56', '+26', '-26o', 'o6', '-5', 'o45x', 'o46-', 'o4',
        riz = 0
        for rec in self.tab_rec:
            coords = self.tableau.coords(rec)  # Donne les coordonnées.
            (lineno(), "rec", rec, "coords", coords, self.tab_rec[riz])
            # 1352 rec 5 coords [67.0, 6.0, 78.0, 880.0] 5
            # 1352 rec 8 coords [91.0, 6.0, 102.0, 880.0] 8
            # 1352 rec 11 coords [115.0, 6.0, 126.0, 880.0] 11
            riz += 1

        ("# Il y a trois façons de séquencer les degrés modaux :"
         "      L'ordre initial interféré par les groupements des modes aux mêmes binaires."
         "      L'ordre original des degrés modaux selon 'CDEFGAB' :"
         "          Cette opération de tri est déjà réalisée dans le module 'gammes_audio.py'."
         "      L'ordre orgisationnel des fréquences hertziennes se fait maintenant, puisque le tri "
         "      réalisé dans le module 'gammes_audio.py' s'effectuait dans une fonction de remise en ordre"
         "      diatonique des notes. Et ne concernait pas toutes les gammes, contrairement à ces 'htz'.")
        "# La première boucle pour chaque gamme et ses modes diatoniques."
        for k2, v2 in self.gam_son.items():
            ind_gam = liste_gam.index(k2)
            if len(str(bb)) == 7:
                ind_bin = colis1[3].index(bb) + 4  # Liste des lignes 'self.tab_lig', 'fill="lightblue"'.
                self.tab_ind.append(ind_bin)
                (lineno(), "ind_gam", ind_gam, "ind_bin", bb, ind_bin, "k2", k2, "v2", v2)
                (lineno(), "tab_ind.1", self.tab_ind)
            (lineno(), "ind_gam", ind_gam, "k2", k2, "v2", v2)
            # 1376 ind_gam 0 k2 0 v2 [['C2', 65.41], ['D2', 73.42], ['E2', 82.41],
            # ['F2', 87.31], ['G2', 98.0], ['A3', 110.0], ['B3', 123.47]]
            self.frequencies.clear()
            self.dic_multiples[k2] = []  # L'enregistrement pour une utilisation ultérieure.
            k_dd = [vy for vy in self.dic_donne.values()]  # Liste des valeurs (colonnes, lignes).
            k_d2 = []
            self.gam_diatonic[k2] = [n_dia[0][:len(n_dia[0]) - 1] for n_dia in v2 if len(n_dia) == 2]
            (lineno(), "k_dd", k_dd, "Dans 'dic_donne.values()'.")
            # 1326 k_dd [(7, 16), (7, 16), (7, 17), (7, 14), (7, 14), (7, 13), (7, 18), (8, 18), (8, 19)
            for k_multi in k_dd:  # Détecter et enregistrer les mêmes binaires.
                if k_dd.count(k_multi) > 1:
                    if k_multi not in k_d2:
                        k_d2.append(k_multi)
                        (lineno(), "k_multi", k_multi, "Dans 'dic_donne.values()'.")
                        # 1332 k_d2 [(66, 62)] Dans 'dic_donne.values()'.

            if v2[-1] == "Hertz":  # Si le bouton-radio["Hertz"] est sélectionné.
                "# Réalisation du tri du dictionnaire en fonction de sa croissance hertzienne."
                tab_htz = []  # Enregistrer les fréquences, afin de les trier en ordre croissant.
                for v0 in v2:
                    if isinstance(v0[1], float):
                        tab_htz.append(v0[1])
                        (lineno(), "v0", v0, type(v0[1]), "k2", k2)
                tab_htz.sort()  # Tri croissant des fréquences hertziennes.
                (lineno(), "tab_htz", tab_htz, "k2", k2)
                for seq in tab_htz:
                    for v0 in v2:
                        if seq == v0[1]:
                            self.frequencies.append(v0)
                            (lineno(), "v0", v0, "k2", k2)
            else:  # L'enregistrement des fréquences des ordonnances[Diatonique et groupement].
                "# Une deuxième boucle pour un enregistrement diatonique[Fréquence. Modes binaires multiples.]."
                for v1 in v2:
                    self.frequencies.append(v1)
                    (lineno(), "v1", v1, "... \t", k2, "\t\t self.frequencies", self.frequencies)
                    # 1183 v1 ['B3', 123.47] ... 	 +6 		 self.frequencies [['C6', 1046.5], ['D7', 2349.32],
                    # ['E3', 164.81], ['F6', 1396.91], ['G7', 3135.96], ['+A2', 58.27], ['B3', 123.47]]
                    # ..1[1] = cc  {1: ['123400000567', '123000004567', '120000034567', '100000234567', '...',
                    ("# On a les notes diatoniques signées[self.frequencies] "
                     "et les degrés modaux[colis1[1]] diatoniques et statiques.")

            (lineno(), "frequencies", self.frequencies, "k2", k2)
            col_0, lig_0 = 24, 26  # Coordonnées d'origine.
            (lineno(), "col, lin", self.col, self.lin)  # 1216 col, lin 24 13
            for freq in self.frequencies:
                # Colorier les rectangles coordonnés aux gammes via 'tab_rec' (ligne-315).
                # For rec in tab_rec : self.tableau.itemconfig(rec, fill="red") : Change la couleur.
                # For rec in self.tab_rec : coords = self.tableau.coords(rec) : Donne les coordonnées.
                self.tableau.itemconfig(self.tab_rec[ind_gam - 1], fill="")
                self.tableau.itemconfig(self.tab_rec[ind_gam], fill="lightsteelblue")
                if len(str(bb)) == 7:
                    if len(self.tab_ind) == 2:
                        self.tableau.itemconfig(self.tab_lig[self.tab_ind[0]], fill="lightblue", width=1)
                        self.tab_ind.pop(0)
                        (lineno(), "len(str(bb)) == 7, tab_ind.2", self.tab_ind)
                    self.tableau.itemconfig(self.tab_lig[self.tab_ind[0]], fill="red", width=3)
                elif self.tab_ind:  # Pour effacer la ligne binaire précédente au changement de ligne nom de gamme.
                    self.tableau.itemconfig(self.tab_lig[self.tab_ind[0]], fill="lightblue", width=1)
                    (lineno(), "len(str(bb)) != 7, tab_ind.2", self.tab_ind)
                self.tableau.update_idletasks()  # Forcer la mise à jour de l'interface graphique.
                id_freq = self.frequencies.index(freq) + 1  # Rang actuel parmi les fréquences.
                "# Les clefs du dictionnaire dic_donne ont un nom de gamme et un rang diatonique."
                for key_don in self.dic_donne.keys():
                    if k2 in key_don and str(id_freq) in key_don:  # 'k2' est le nom de la gamme.
                        co_d, li_d = self.dic_donne[key_don][0] + 2, self.dic_donne[key_don][1] + 2
                        co0, li0 = self.col * co_d, self.lin * li_d
                        col0, lig0 = (co0 - 10, li0 + 1), (co0 + 10, li0 + 11)
                        (lineno(), "freq", freq, "key_don", key_don, "dic_donne", self.dic_donne[key_don])
                        (lineno(), "col0.1", col_0, lig_0, "co.li", co_d, li_d, "\tRectangle", col0, lig0)
                        # 1217 freq1['C6', 1046.5] key_don ('+6', '1') dic_donne (66, 61)
                        # 1221 col0.1 24 26 co.li 66 61 	co.li 1584 793
                        "# Dessiner les données correspondantes aux notes de la gamme sélectionnée."
                        # Les rectangles et fonds des notes diatoniques.
                        scr = self.tableau.create_rectangle(col0, lig0, fill="gold", width=0)
                        self.all_rectangles.append(scr)
                        # Le texte de chacune des notes diatoniques rassemblées.
                        if self.dic_donne[key_don] in k_d2:
                            pas_freq = (freq[0][:len(freq[0]) - 1], key_don[1], col0[1], lig0[1])
                            self.dic_multiples[k2].append(pas_freq)
                            nfq = "☺"
                            (lineno(), "n_all", self.dic_donne[key_don], "dic_multiples", self.dic_multiples[k2])
                            (lineno(), "co_d, li_d", co_d, li_d, "\t col0[1], lig0[1]", col0[1], lig0[1])
                            # 1391 n_all (5, 12) dic_multiples [('C', '1', 5, 14), ('-D', '2', 5, 14),
                            # ('oE', '3', 5, 12), ('oF', '4', 5, 12)]
                            # 1392 co_d, li_d 23 26 	 col0[1], lig0[1] 339 349
                        else:
                            nfq = freq[0][:len(freq[0]) - 1]
                        (lineno(), "Notes", freq[0][:len(freq[0]) - 1])
                        stt = self.tableau.create_text(co0, li0 + 6, text=nfq, font=self.police1,
                                                       fill="black", tags=(k2,))
                        self.all_textes.append(stt)
                        self.tableau.tag_bind(stt, "<Enter>", lambda event: self.tableau.config(cursor="hand2"))
                        self.tableau.tag_bind(stt, "<Leave>", lambda event: self.tableau.config(cursor=""))
                        self.tableau.tag_bind(stt, "<Button-1>", self.on_click)
                        break

                if self.zone_w3.get() == "Audible":
                    sine_tone(freq[1], 0.05)
                # break de vérification.

            self.tableau.itemconfig(self.tab_rec[ind_gam], fill="")

            if self.zone_w0.get() == "Solo":
                break

        (lineno(), self.colonne_gam)
        # , "gammes_copie" : Remplace : "gammes_col" par une autre demande utilisateur.

def primordial():
    pre_codage = open('songammes\globdicTcoup.txt', 'r')
    mod, cod1 = '', 1
    "# Lire un globdicTcoup.txt pour construire un dictionnaire de tous les modèles diatoniques = dic_codage"
    for pre_cod in pre_codage:
        mod_cod = pre_cod[:12]  # 'mod_cod' = Copie du mode tonique.
        (lineno(), "cod1", cod1, "mod_cod", mod_cod)
        if pre_cod[:12] in gam_classic.keys():
            cod2, clef0 = 0, ()
            dic_codage[cod1, mod_cod] = []
            code_ages[cod1] = [pre_cod[:12]]  # Enregistrer le mode tonique de chaque gamme.
            if mod_cod not in dic_gammic.keys():
                clef0 = gam_classic[mod_cod][0], mod_cod
                bin0 = "".join("1" if i != "0" else "0" for i in mod_cod)
                dic_gammic[clef0] = [bin0]
                (lineno(), "dic_gammic", dic_gammic[clef0], "clef", clef0, "bin", bin0)
                # 327 dic_gammic ['111100000111'] clef ('o45x', '123400000567') bin 111100000111
                # 327 dic_gammic ['111100011001'] clef ('o46-', '123400056007') bin 111100011001
            (lineno(), "clef", clef0, "code_ages", code_ages[cod1], cod1, "mod_cod", mod_cod)
            # 332 clef ('o45x', '123400000567') code_ages ['123400000567'] 1 mod_cod 123400000567
            # 332 clef ('o46-', '123400056007') code_ages ['123400056007'] 2 mod_cod 123400056007
            while cod2 < 12:
                cod2 += 1
                for p_c in mod_cod:
                    if p_c != '0':
                        ind_maj = gam_maj.index(p_c)
                        ind_cod = mod_cod.index(p_c)
                        if ind_maj == ind_cod:
                            mod += '1'
                        else:
                            mod += '0'
                "# C’est une section des premiers degrés, les noms et les numéros des gammes."
                if cod2 == 1:
                    zob = gam_classic[mod_cod], mod
                    "# self.dic_indice = Dictionnaire, clé = Nom_gamme, valeur = Rang_gamme."
                    dic_indice[gam_classic[mod_cod][0]] = cod1
                    (lineno(), "cod1", cod1, "dic_indice", dic_indice[gam_classic[mod_cod][0]])
                else:
                    zob = cod1, cod2, mod
                dic_codage[cod1, pre_cod[:12]].append(zob)
                dic_binary[zob[-1]] = []  # 'dic_mode01' = Clé Binaire, = Rang numérique.
                dic_binary[zob[-1]].append(zob)  # Ce dictionnaire a des binaires uniques
                dic_gammic[clef0].append(zob[-1])
                (lineno(), "zob", zob, "zob[-1]", zob[-1])
                # 358 zob (1, 2, '1000001') zob[-1] 1000001
                mod = ''
                "# Renversements diatoniques."
                mod_cod = mod_cod[1:] + mod_cod[:1]
                while mod_cod[0] == '0':
                    mod_cod = mod_cod[1:] + mod_cod[:1]
                mov, mut = 0, ''  # Renuméroter les degrés = 'mov'
                "# Binariser chaque mode."
                for m in mod_cod:
                    if m != '0':
                        mov += 1
                        mut += str(mov)
                    else:
                        mut += '0'
                mod_cod = mut
                (lineno(), "cod1", cod1, "pre_cod", pre_cod[:12], "mod_cod", mod_cod, "code_ages", code_ages[cod1])
                (lineno(), "dic_codage[cod1, pre_cod[:12]]", dic_codage[cod1, pre_cod[:12]])
                # 368 cod1 1 pre_cod 123400000567 mod_cod 123000004567 code_ages ['123400000567']
                # 126 dic_codage[cod1, pre_cod[:12]] [(['0', 336], '1111111'), (44, 2, '1101110'), (44, 3, '1001100'),
                # (44, 4, '1110111'), (44, 5, '1111110'), (44, 6, '1101100'), (44, 7, '1001000')]
                if mod_cod == pre_cod[:12]:
                    break
            (lineno(), "clef0", clef0, "dic_gammic", dic_gammic[clef0], "\n dic_codage", dic_codage[cod1, pre_cod[:12]])
            # 380 clef0 ('o45x', '123400000567')
            # dic_gammic ['111100000111', '1000001', '1000001', '1000001', '1000001', '1000000', '1000001', '1000001']
            #  dic_codage [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'), (1, 4, '1000001'),
            #  (1, 5, '1000000'), (1, 6, '1000001'), (1, 7, '1000001')]
            cod1 += 1  # ("dic_codage", dic codage, "Les gammes formatées.")
    doc_key_gam = [k[0] for k in dic_gammic.keys()]
    (lineno(), "doc_key_gam", doc_key_gam)
    # 385 doc_key_gam ['o45x', 'o46-', 'o4', 'o46+', 'o45-', 'o54-', '*5', '-34', 'o63-', 'o35x',
    pre_codage.close()

    ("# Construire un dictionnaire avec les modes énumérés ordonnés. Dans code_ages."
     "Ce dictionnaire va être réutilisé, afin de transcrire la donnée énumérée en donnée conteneur.")
    (lineno(), "code_ages", code_ages)  # dic_inter, doc_key_gam[Valeur énumérée ('123400056007')]
    # 390 code_ages {1 : ['123400000567'], 2 : ['123400056007'], 3 : ['1er Mode tonique'] (66 éléments)}
    for clef1 in code_ages.keys():  # La clef1 est la clef qui donne le numéro de gamme.
        clef2 = code_ages[clef1][0]  # La clef2
        num, age, iq = 0, clef2, 0
        (lineno(), "clef1", clef1, "code_ages", code_ages[clef1])  # Début de répétition à tonique comme seule donnée
        # 396 clef1 44 code_ages ['102034050607']
        for ia in age:
            pass
        if num == 0:
            (lineno(), "doc_key_gam", doc_key_gam[clef1 - 1], "age", age, "= clef0")
        (lineno(), "clef1", clef1, "clef2", clef2, "\t age", age, "num+1", num + 1)
        # 399 clef1 1 clef2 123400000567 	 age 123400000567 num+1 1 (Les énumérations toniques primordiales)
        ("399 clef1 1 clef2 123400000567 	 age 123400000567 num+1 1",  # Chaque ligne est une gamme différente,
         "399 clef1 2 clef2 123400056007 	 age 123400056007 num+1 1",
         # faisant partie des 66 tonalités fondamentales.
         "399 clef1 3 clef2 123400050607 	 age 123400050607 num+1 1",
         "399 clef1 4 clef2 123400050067 	 age 123400050067 num+1 1",
         "399 clef1 5 clef2 123400500607 	 age 123400500607 num+1 1",
         "399 clef1 6 clef2 123405000607 	 age 123405000607 num+1 1",
         "399 clef1 7 clef2 123450000607 	 age 123450000607 num+1 1",
         "399 clef1 8 clef2 123040050607 	 age 123040050607 num+1 1",
         "399 clef1 9 clef2 123045000607 	 age 123045000607 num+1 1")
        "# On sait que clef2 c'est le mode tonique de la unième gamme."
        for c in clef2:  # clef2 = 123400000567 (Suite des numérisations).
            "# Et qu'ensuite, la tonique "
            if num != 0 and clef2 == code_ages[clef1][0]:
                # Non utilisé pour construire un mode conteneur du dico dic_inter.
                (lineno(), "clef1", clef1, "clef2", clef2, "break")
                break
            elif clef2 not in code_ages[clef1]:  #
                age, num2 = "", 0
                for c2 in clef2:
                    if c2 != "0":  # Compter les degrés
                        num2 += 1  # Cumuler les degrés
                        age += str(num2)  # Construire le rang de l'âge
                    else:  # Copier les intervalles
                        age += "0"  # Construire le vide de l'âge
                    (lineno(), "clef1", clef1, "num2", num2, "age", age, "clef2", clef2)
                    " De ; 402 clef1 44 clef2 102034050607 	 age 102034050607 num+1 1"
                    # 426 clef1 44 num2 6 age 1203045060 clef2 710203405060
                    # 426 clef1 44 num2 7 age 12030450607 clef2 710203405060
                    # 426 clef1 44 num2 7 age 120304506070 clef2 710203405060
                code_ages[clef1].append(age)  # Enregistrement des âges.
                (lineno(), "clef1", clef1, "clef2", clef2, "\t age", age, "num+1", num + 1)
            num += 1
            (lineno(), "c", c, "clef1", clef1, "clef2", clef2)
            ("# 436 c 1 clef1 1 clef2 123400000567",
             "# 436 c 2 clef1 1 clef2 234000005671",
             "# 436 c 3 clef1 1 clef2 340000056712",
             "# 436 c 4 clef1 1 clef2 400000567123",
             "# 436 c 0 clef1 1 clef2 567123400000",
             "# 436 c 0 clef1 1 clef2 671234000005",
             "# 436 c 0 clef1 1 clef2 712340000056")
            "# Renversements diatoniques."
            clef2 = clef2[1:] + clef2[:1]
            while clef2[0] == '0':
                clef2 = clef2[1:] + clef2[:1]
        (lineno(), "clef1", clef1, "code_ages", code_ages[clef1], "\n")  # Modes énumérés des gammes.
        # 420 clef1 1 code_ages ['123400000567', '123000004567', '120000034567', '100000234567', '123456700000',
    (lineno(), "code_ages", code_ages)  # Copie du mode naturel '102034050607'
    # 450 code_ages {44: ['102034050607', '102304050670', '120304056070', '102030450607', '102034050670',
    # '102304056070', '120304506070'],
    "# dic_codage[cod1, pre_cod[:12]]"

    "# Construire un dictionnaire 'dic_force' avec les valeurs ayant les mêmes binaires, de dic_codage original."
    liste_keys, liste_copy = list(dic_codage.keys()), []  # Liste les clés de dic_codage original.
    for lk in liste_keys:
        (lineno(), "lk", lk, "dic_codage", dic_codage[lk])
        for dc in dic_codage[lk]:
            if dc[-1] not in liste_copy:
                liste_copy.append(dc[-1])
                pas_lk = lk, dc
                dic_force[dc[-1]] = []
                dic_force[dc[-1]].append(pas_lk)
                (lineno(), "IF pas_lk", dc[-1], dc, "*", pas_lk)
                (lineno(), "IF dic_force", dc[-1], dic_force[dc[-1]])
            else:
                dic_force[dc[-1]].append(dc)
                (lineno(), "ELSE dc", dc[-1], dc)
                (lineno(), "ELSE dic_force", dc[-1], dic_force[dc[-1]])
    (lineno(), "dic_force", list(dic_force)[0], dic_force[list(dic_force)[0]], len(dic_force.keys()))
    (lineno(), "dic_force", dic_force.keys())
    # 444 dic_force 1000001 [((1, '123400000567'), (['o45x', 1], '1000001')), (1, 2, '1000001'), (1, 3, '1000001'),
    # 445 dic_force dict_keys(['1000001', '1000000', '1000101', '1011000', '1011001', '1000111',

    (lineno(), "dic_codage", list(dic_codage)[0], "\ncode_ages", "code_ages")
    Relance(dic_codage, code_ages, dic_binary, dic_indice, dic_force, dic_colon, dic_gammic).mainloop()
