# Python 3.9 UTF-8
# Mercredi 12 mai 2021 à 20h 32m (premières lignes)
#
# Conçu par Vicenté Llavata Abreu | Vicenté Quantic | Toumic
# Module GlobGamFonds.py

"""Réception liste binaire Tétra + Gamme
Priorité aux gammes heptatoniques:
    classement par le poids altéré du degré modal"""
action = ['', '+', 'x', '^', '^+', '^x', '°*', '-*', '*', '°', '-']
gamme = '1020340506078'  # Diatonisme majeur
gammic = {'maj': '1020340506078'}


def diatonic(tonic):
    coup = 0
    for ton in tonic:
        if len(ton) == 13:

            coup += 1
    print(f' Coup:{coup} Action:{action}')
    # print(f'Tonic:{tonic}')
