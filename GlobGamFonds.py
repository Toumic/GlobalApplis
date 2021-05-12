# Python 3.9 UTF-8
# Mercredi 12 mai 2021 à 20h 32m (premières lignes)
# Cabviva.fr Cab.Rich.Int.Music.Quant
# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# Module GlobGamFonds.py
"""Réception liste binaire Tétra + Gamme
Priorité aux gammes heptatoniques:
    classement par le poids altéré du degré modal"""

action = ['', '+', 'x', '^', '^+', '^x', '°*', '-*', '*', '°', '-']
gamme_majeure = '102034050607'  # Diatonisme naturel
gamme_signaux = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], }
gammic = {'maj': '102034050607'}
gamme_pesante = {1: [[0], [0]], 2: [['b3', 'b7'], [-4, -8]],
                 3: [['b2', 'b3', '6', 'b7'], [-3, -4, -7, -8]], 4: [['#4'], [+5]],
                 5: [['b7'], [-8]], 6: [['b3', 'b6', 'b7'], [-4, -7, -8]],
                 7: [['b2', 'b3', 'b5', 'b6', 'b7'], [-3, -4, -6, -7, -8]]}
poids_major = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
poids_modal = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
# longer = {4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 12: []}
for deg, kg in gamme_pesante.items():
    kgk = 0
    if len(kg[1]) == 1:
        poids_major[deg] = kg[1][0]
    else:
        for k in kg[1]:
            kgk += k
        poids_major[deg] = kgk
print(f' Poids maj:{poids_major}')


def diatonic(topic, top01):
    top00 = [0]  # :top00[0]=Premier mode majeur
    for top in topic:
        if gamme_majeure in top:
            top00[0] = topic.index(top)  # :top00[0]=Emplacement gamme dans topic
            print(f" \nTopic335i:{top[-1]} Index:{top00[0]} Top01:{top01[top00[0]]}")
            break
