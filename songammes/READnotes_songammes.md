# BLOC NOTES songammes.py


## Défaut de lecture au type 'Anti iso'
    Une erreur se produit lorsque l'organisation des binaires est au type 'Anti iso'
**Solution :** <br>
L'erreur n'apparait plus
## Vérification des fréquences.
    Seulement à corriger si besoin.
Le problème vient à cause du manque de précision du rapport (ligne/octave). Par exemple : <br>
* 1212 freq1 ['E3', 164.81] key_don ('+6', '3') dic_donne (66, 17)
* 1212 freq1 ['B3', 123.47] key_don ('+6', '7') dic_donne (66, 18) <br>
Où la note MI ayant une `ligne inférieure` avec une fréquence plus élevée que la note SI. <br>
Y a besoin de calibrer les octaves à l'aide des notes réelles signées.


    Les fréquences hertziennes anormalement élevées, dans cette série de gammes.
Cette liste a des fréquences anormales [-26o, *6, o6, -36].

**Solution :** <br>
Se corrige avec l'amélioration du code.

## Dissociation des analyses intermodales
    Les réparations intermodales ne sont pas réalisées en mode de lecture binaire.
À la ligne 889 du module `gammes_audio.py` l'instruction `if titre1 == 'Gammes':` est arbitraire. <br>
En effet, les modes terminaux binaires pouvant recevoir cette analyse, n'y sont pas traités.

**Solution :** <br>
L'arrangement a été produit grâce à la création, d'une nouvelle liste située à `if titre1 == 'Binomes':`.


## Problématique liée aux mêmes modes binaires
    Le dictionnaire 'self.dic_multiples' ne distingue pas les différents rassemblements.
Voici deux choix d'une même gamme ayant deux assemblages distincts.
* 1089 self.dic_multiples [('C', '1'), ('+D', '3'), ('E', '4'), ('+A', '7')] gamme +25x note ☺
* 1089 self.dic_multiples [('C', '1'), ('+D', '3'), ('E', '4'), ('+A', '7')] gamme +25x note ☺
* Chacune des lignes correspond à un mode binaire dissemblable.<br>

**Solution :** <br>
Modifier les valeurs du dictionnaire, en leur ajoutant les coordonnées des rectangles d'arrière-plan. <br>
1. [ ] col0[1], lig0[1]. Où, col0 = coin haut-gauche[x, y] et lig0 = coin bas-droit[x, y].


    Lors de la sélection d'un bouton binaire, la lecture se comporte anormalement.
Les gammes ne sont pas lues selon l'ordre apparaissant dans l'interface de l'utilisateur. <br>
Le rectangle toute hauteur, "celui qui signale le niveau de lecture sonore", ne s'affiche pas. <br>
**Le problème ne vient pas de :**
* Le dictionnaire self.colonne_gam, le changement après le tri a bien eu lieu. (Ligne 428) <br>

**Solution :** <br>
A changé l'identification du rectangle, par un indice équivalant ici : `ind_gam = liste_gam.index(k2)` <br>


## Constitution des paramètres.
    Interfaçage des sonorités (volume, tempo, audio ou pas)
    Paramétrer les fréquences aux positions réelles, quand (ligne//8 = Octave)
    -   Il y a soixante-trois lignes liées aux modes binaires et huit octaves pan['A2'...'A9']

## Contrôler la lecture sonore.
    En ajoutant des boutons[marche, arrêt, pause, enregistrement]
Un bouton radio a été ajouté offrant le choix d'entendre ou pas les gammes lors de la sélection.

## Utilisation des gammes fantômes.
    ???

## Création de nouvelles ressources.
Au départ, les degrés modaux étaient binarisés et seulement eux. Maintenant, les formes énumérées des gammes fondamentales vont avoir une signification binaire. <br>
La manière de trier en ordre croissant les modes binarisés ne se reporte pas aux formes énumérées, puisqu'à elles seules, elles ont un même rapport de croissance. Selon le déroulement de la forme commençant et finissant toujours par (1 et 7) respectivement. <br>
`dic_gammic = {}  # Dico, clé = Nom + valeur énumérée, valeur = Énumération binarisée + degrés binarisés.` <br>

Ceci produit un dico ayant au 1er indice la valeur énumérée['123400000567'] binarisée['111100000111']. Suivi aux sept indices modaux des sept degrés binarisés tels qu'on les connait. Ce dictionnaire est construit au commencement du programme, dans la boucle `for pre_cod in pre_codage:`. Il est noté que le dictionnaire `dic_codage`, quoique plus complexe, a les mêmes données que `dic_gammic`. <br>
`dic_gammic ['111100000111', '1000001', '1000001', '1000001', '1000001', '1000000', '1000001', '1000001']` <br>

En triant les valeurs énumérées, on change l'ordre des modulations diatoniques binaires. <br>
De ce fait, ce nouvel ordre des modes binarisés n'est pas forcément ordonné. Donc, avec le tri des formules gammales binaires, on crée un désordre organisé. Ce qui et par conséquence, pourrait engendrer une quelconque familiarité relative aux tris réalisés sur les modes binarisés. Et des nouvelles organisations d'apparences binaires.

Les modèles modaux des gammes ont été vus jusqu'à présent à travers une conception binarisante. <br>
Les modes toniques peuvent être conceptualisés d'une autre façon. En invoquant les modèles énumérés ressemblants à ceci[102034050607] et d'en estimant la mesure d'intervalle de chacune des tonalités. Ainsi en comptant les intervalles[102034050607], devient[1101110]. Quand il n'y a pas d'intervalle entre deux tonalités, le résultat vaut zéro et s'il y en a, on a juste à compter le nombre d'intervalles vides. <br>
Faisons par exemple la conversion de cet exemple[1203040050607], équivalant à la gamme `b23`, le devenir de cet exemple est[0112110] (numériquement[112110]).

_Une première tentative de traitement a donné le même résultat que celui produit par le tri sur les modes._ <br>
À cause d'une ordonnance ne variant pas l'ordre des toniques, qui même en ayant trié les modèles [102034050607] et [1101110], l'ordre des binarisations était inchangé. <br>
Afin d'éviter cette redondance et paraitre créateur d'inutilité absolue. La méthode de traitement des modèles en modes `GAMME et CONTIENT`, sont traité différemment, en affectant une sectorisation. C'est en suivant la hiérarchie des ordres et des appels de type de traitement, que s'accomplissent les grandeurs des sections. <br>
Les grandeurs se basent sur la quantité des gammes primordiales et le nombre d'organisations : il y a soixante-six gammes et trois modèles de progression. <br>
Alors, les sections sont au nombre de trois grandeurs entières {11, 33, 66}, pour modifier du premier résultat.
* 11 : c'est la quantité de gammes incluses par secteur, il y a 6 secteurs de 11 gammes.
  * Chaque secteur voit ses 11 gammes triées en ordre croissant et les binarisations ont un ordre différent.
* 33 : il y a trente-trois gammes par section et il y a 2 secteurs de 33 gammes.
  * Chaque secteur voit ses 33 gammes triées en ordre croissant et les binarisations ont un ordre encore différent.
* 66 : il y a soixante-six gammes dans une section et il y a 1 secteur de 66 gammes.
  * Ce secteur englobe toutes les gammes, c'est ici que les formes énumérées et les conteneurs sont ordonnés.


### Consistance des formes binarisées :
Les consultations des modes binaires composées de sept chiffres, ont trois pôles[EGO, ISO, INT]. <br>
Et, celles des gammes binaires composées de douze chiffres, ont les mêmes pôles. <br>
[EGO] = Organisation composée à partir de la gamme naturelle. ......... **'self.gam_ego'** <br>
[ISO] = Organisation composée à partir du fichier `globdicTcoup.txt`. . **'self.gam_iso'** <br>
[INT] = Organisation croissante des éléments [ISO = EGO]. ............ **'self.gam_int'** <br>
Les binaires : `[ISO]=[EGO]=[INT]`. Ce `dictionnaire[E/I][102034050607] = (Binaires)` <br>

### Commentaires sur les résultats
    Au sujet du tri naturel de la gamme
Nous avons créé trois versions de transformation numérique des gammes. Nous avons remarqué que dans un premier temps, seuls les noms des gammes et les modes binarisés ont été traités. <br>
Ce premier traitement dévoile la constance des résultats obtenus par les pôles[EGO, ISO], car le changement de l'ordre de la séquence intervient uniquement au pôle[INT]. L'ordre ne change pas à cause de l'originalité statique des listes produites préalablement. <br>
_Le pôle[INT] modifie l'ordre de la séquence sans modifier les noms des gammes._ <br>

Puisque les ressources ont produit trois formes[binaires, énumérées, conteneurs], on devine clairement, que les modes diatoniques ont été modifiés. Entrainant d'autres éléments de triages et d'autres organisations. <br>

`self.zone_w4.get() == "Modes" ou "Gammes" ou "Contient"` : <br>
L'ordre des noms des gammes varient selon que les pôles sont traités en modes `"Modes"` ou `"Gammes"` ou `Contient`.
#### Dictionnaires des résultats
Ils ont la tâche de rassembler les résultats selon `self.zone_w4.get() == "Modes" ou "Gammes"` : <br>
Ainsi, que chacun de ces deux modes produisent, soit des modes binaires ou des gammes énumérées. <br>
##### Dictionnaire dic_m_noms["Modes"]
`dic_m_noms_ego = ['0', '-5', 'o45x', 'o46+', 'o46-', '-26o', '+25x', 'o35x', 'x26-', 'o45-', '*5', 'o4', 'o54-', '-34', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', '-24', '+35x', '+23x', 'o35+', 'o35-', 'o3', 'o36+', '-23', '+45x', 'x45+', 'x46+', '^4', 'x5', 'o6', '+56', '-56', '-56+', '-25', '+25-', '-25+', '-46+', '-36', '-36+', '-26', '-26+', '+26-', '+26', '-2', '+2', '-45+', '-34x', '+34', 'x3', '-45', 'o5', '-35+', '-35', '-4', '-3', '-6', '+6']` <br>
`dic_m_noms_ego_inv = ['o35-', '-24', '-23', '-25+', '-26+', '-46o', '-45', '-35+', '-3', '-35', '+56', '+6', 'x45+', 'x46+', '+35x', '+34', '+25x', '+26-', '+2', 'o45x', 'o46-', 'o4', 'o46+', 'o45-', 'o54-', '*5', '-34', 'o63-', 'o35x', 'o35+', 'o3', 'o36+', 'o34x', '-25o', '-45x', '-45+', '*6', '-4', 'o65-', '-46+', 'o5', '-34x', 'x5', '-56+', '+45x', '^4', '+34x', 'x3', 'x36+', '^3', '+25-', '+23x', 'x26-', '^2', '-36+', '-36', '-26', '-26o', '-6', 'o6', '-56', '+26', '-2', '-25', '-5', '0']` <br>
`dic_m_noms_iso = ['o45x', 'o46-', 'o46+', 'o4', '*5', 'o45-', 'o35x', '+25x', 'x26-', 'o54-', '-34', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', 'o35+', 'o35-', 'o3', 'o36+', '-24', '+35x', '+23x', '-23', '+45x', '+25-', '-25+', '-26+', '-26', '-26o', '+26', '-25', '-2', '+2', '-45+', '-34x', '+34', 'x3', '-46+', '+26-', '-4', '-45', 'o5', '-35+', '-35', '-36', '-36+', '-3', 'x5', 'o6', '+56', '-56', '-56+', 'x45+', 'x46+', '^4', '-6', '+6', '0', '-5']` <br>
`dic_m_noms_iso_inv = ['0', '-26', '-6', '-2', '-56', '-25', '+26', 'o35-', '-24', '-23', '-25+', '-26+', '-46o', '-45', '-35+', '-36', '-3', '-35', '+56', '+6', 'x45+', 'x46+', '+35x', '+34', '+25x', '+26-', '+2', 'o45x', 'o46-', 'o4', 'o46+', 'o45-', 'o54-', '*5', '-34', 'o63-', 'o35x', 'o35+', 'o3', 'o36+', 'o34x', '-25o', '-26o', '-45x', '-45+', '*6', '-4', 'o65-', '-46+', 'o5', '-36+', '-34x', 'x5', 'o6', '-5', '-56+', '+45x', '^4', '+34x', 'x3', 'x36+', '^3', '+25-', '+23x', 'x26-', '^2']` <br>
`dic_m_noms_int = ['o45x', 'o35x', 'o46+', 'o46-', '-26o', '+25x', 'x26-', 'o45-', '*5', 'o35-', 'o54-', 'o63-', 'o35+', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+35x', '+34x', 'x36+', '^3', '+23x', '^2', 'o36+', '-25', '+25-', '-25+', '-26', '-26+', '-46+', '+26-', '+26', '-45', 'o5', '-45+', '-34x', '+34', 'x3', '-35+', '-35', 'x45+', 'x46+', '^4', '+45x', '-36+', 'o4', '-34', 'o3', '-24', '-23', 'x5', 'o6', '+56', '-56', '-56+', '-2', '+2', '-36', '-5', '-4', '-3', '-6', '+6', '0']` <br>
`dic_m_noms_int_inv = ['-2', '0', '-25', '-26', '-6', '-56', '+26', '-26o', 'o6', '-5', 'o45x', 'o46-', 'o4', 'o46+', 'o45-', 'o54-', '*5', '-34', 'o63-', 'o35x', 'o35+', 'o3', 'o36+', 'o35-', 'o34x', '-24', '-25o', '-23', '-25+', '-26+', '-45x', '-45+', '-46o', '*6', '-4', 'o65-', '-46+', '-45', 'o5', '-35+', '-36', '-3', '-36+', '-35', '-34x', 'x5', '+56', '+6', '-56+', '+45x', 'x45+', 'x46+', '^4', '+35x', '+34', '+34x', 'x3', 'x36+', '^3', '+25x', '+26-', '+2', '+25-', '+23x', 'x26-', '^2']` <br>
#### Dictionnaire dic_m_bins["Modes"]
`dic_m_bins_ego = ['1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1001000', '1111011', '1100110', '1010111', '1000001', '1000000', '1000101', '1011000', '1011001', '1000100', '1001001', '1010001', '1000011', '1100000', '1000111', '1111000', '1100001', '1000010', '1010010', '1001011', '1010100', '1001111', '1110100', '1001101', '1100100', '1110001', '1110010', '1100010', '1111001', '1011011', '1010101', '1011100', '1100101', '1001010', '1010011', '1101101', '1110011', '1011101', '1011010', '1011111', '1110101', '1111010', '1100011', '1000110', '1101001', '1101000', '1101011', '1010110', '1100111', '1001110', '1111100', '1101111', '1110110', '1111101', '1101010', '1011110']` <br>
`dic_m_bins_ego_inv = ['1011110', '1101010', '1111101', '1110110', '1101111', '1111100', '1001110', '1100111', '1010110', '1101011', '1101000', '1101001', '1000110', '1100011', '1111010', '1110101', '1011111', '1011010', '1011101', '1110011', '1101101', '1010011', '1001010', '1100101', '1011100', '1010101', '1011011', '1111001', '1100010', '1110010', '1110001', '1100100', '1001101', '1110100', '1001111', '1010100', '1001011', '1010010', '1000010', '1100001', '1111000', '1000111', '1100000', '1000011', '1010001', '1001001', '1000100', '1011001', '1011000', '1000101', '1000000', '1000001', '1010111', '1100110', '1111011', '1001000', '1101100', '1111110', '1110111', '1001100', '1101110', '1111111']` <br>
`dic_m_bins_iso = ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000', '1100000', '1000011', '1001001', '1010001', '1000100', '1100001', '1000010', '1001011', '1010100', '1001111', '1110100', '1001101', '1100100', '1010010', '1110001', '1110010', '1011011', '1011100', '1010101', '1100101', '1001010', '1011101', '1011010', '1001000', '1011111', '1001100', '1110101', '1111010', '1100011', '1000110', '1101001', '1100111', '1001110', '1010011', '1111100', '1101000', '1101011', '1010110', '1101101', '1111011', '1100110', '1010111', '1101111', '1110011', '1110110', '1111001', '1100010', '1111101', '1101010', '1011110', '1111111', '1101110', '1110111', '1111110', '1101100']` <br>
`dic_m_bins_iso_inv = ['1101100', '1111110', '1110111', '1101110', '1111111', '1011110', '1101010', '1111101', '1100010', '1111001', '1110110', '1110011', '1101111', '1010111', '1100110', '1111011', '1101101', '1010110', '1101011', '1101000', '1111100', '1010011', '1001110', '1100111', '1101001', '1000110', '1100011', '1111010', '1110101', '1001100', '1011111', '1001000', '1011010', '1011101', '1001010', '1100101', '1010101', '1011100', '1011011', '1110010', '1110001', '1010010', '1100100', '1001101', '1110100', '1001111', '1010100', '1001011', '1000010', '1100001', '1000100', '1010001', '1001001', '1000011', '1100000', '1111000', '1000111', '1011001', '1011000', '1000101', '1000000', '1000001']` <br>
`dic_m_bins_int = ['1000000', '1000001', '1000010', '1000011', '1000100', '1000101', '1000110', '1000111', '1001000', '1001001', '1001010', '1001011', '1001100', '1001101', '1001110', '1001111', '1010001', '1010010', '1010011', '1010100', '1010101', '1010110', '1010111', '1011000', '1011001', '1011010', '1011011', '1011100', '1011101', '1011110', '1011111', '1100000', '1100001', '1100010', '1100011', '1100100', '1100101', '1100110', '1100111', '1101000', '1101001', '1101010', '1101011', '1101100', '1101101', '1101110', '1101111', '1110001', '1110010', '1110011', '1110100', '1110101', '1110110', '1110111', '1111000', '1111001', '1111010', '1111011', '1111100', '1111101', '1111110', '1111111']]` <br>
`dic_m_bins_int_inv = ['1111111', '1111110', '1111101', '1111100', '1111011', '1111010', '1111001', '1111000', '1110111', '1110110', '1110101', '1110100', '1110011', '1110010', '1110001', '1101111', '1101110', '1101101', '1101100', '1101011', '1101010', '1101001', '1101000', '1100111', '1100110', '1100101', '1100100', '1100011', '1100010', '1100001', '1100000', '1011111', '1011110', '1011101', '1011100', '1011011', '1011010', '1011001', '1011000', '1010111', '1010110', '1010101', '1010100', '1010011', '1010010', '1010001', '1001111', '1001110', '1001101', '1001100', '1001011', '1001010', '1001001', '1001000', '1000111', '1000110', '1000101', '1000100', '1000011', '1000010', '1000001', '1000000']` <br>
##### Dictionnaire dic_g_noms["Gammes"]
`dic_g_noms_ego = ['0', '-5', 'o45x', 'o46+', 'o46-', '-26o', '+25x', 'o35x', 'x26-', 'o45-', '*5', 'o4', 'o54-', '-34', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', '-24', '+35x', '+23x', 'o35+', 'o35-', 'o3', 'o36+', '-23', '+45x', 'x45+', 'x46+', '^4', 'x5', 'o6', '+56', '-56', '-56+', '-25', '+25-', '-25+', '-46+', '-36', '-36+', '-26', '-26+', '+26-', '+26', '-2', '+2', '-45+', '-34x', '+34', 'x3', '-45', 'o5', '-35+', '-35', '-4', '-3', '-6', '+6']` <br>
`dic_g_noms_ego_inv = ['+6', '-6', '-3', 'o45x', '-4', 'o5', '-35', '-45+', '-35+', '-34x', 'x3', 'o34x', '-45x', '-46o', '*6', 'o65-', '-45', 'x36+', '^3', '^2', 'o54-', '*5', 'o63-', '-25o', '+34', '+2', 'o45-', 'o35x', 'o36+', '-2', 'o46+', '+34x', '-26+', '+26-', 'o46-', '-26o', '+25x', '+26', 'x26-', '-26', '-25', '+25-', '-25+', '-46+', '-36+', '-36', 'x5', 'o6', '-56+', '-56', '+35x', '+23x', 'o35+', 'o35-', '+56', 'x45+', 'x46+', '^4', '+45x', 'o4', '-34', 'o3', '-24', '-23', '-5', '0']` <br>
`dic_g_noms_iso = ['o45x', 'o46-', 'o46+', 'o4', '*5', 'o45-', 'o35x', '+25x', 'x26-', 'o54-', '-34', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', '+34x', 'x36+', '^3', '^2', 'o35+', 'o35-', 'o3', 'o36+', '-24', '+35x', '+23x', '-23', '+45x', '+25-', '-25+', '-26+', '-26', '-26o', '+26', '-25', '-2', '+2', '-45+', '-34x', '+34', 'x3', '-46+', '+26-', '-4', '-45', 'o5', '-35+', '-35', '-36', '-36+', '-3', 'x5', 'o6', '+56', '-56', '-56+', 'x45+', 'x46+', '^4', '-6', '+6', '0', '-5']` <br>
`dic_g_noms_iso_inv = ['o45x', 'o34x', '-45x', '-46o', '*6', 'o65-', 'x36+', '^3', '^2', 'o35x', '+25x', 'x26-', 'o46-', 'o46+', '+34x', '+35x', '+23x', 'o36+', '+25-', '-26+', '-26', '-26o', '+26', '+2', '+26-', '-45+', '-34x', 'x3', 'o45-', 'o54-', '*5', 'o63-', '-25o', '+34', 'x45+', '^4', 'o35+', 'o35-', 'x46+', '+45x', 'x5', 'o6', '+56', '-56', '-56+', '-2', '-25', '-5', '-6', '+6', '0', '-35+', '-45', 'o5', '-35', '-25+', '-46+', '-36', '-36+', '-4', '-3', 'o4', '-34', 'o3', '-24', '-23']` <br>
`dic_g_noms_int = ['o45x', 'o34x', '-45x', '-46o', '*6', 'o65-', 'x36+', '^3', '^2', 'o35x', '+25x', 'x26-', 'o46-', 'o46+', '+34x', '+35x', '+23x', '-26+', '-26o', '+26', 'o36+', '+2', '+26-', '-26', '+25-', '-45+', '-34x', 'x3', 'o45-', 'o54-', '*5', 'o63-', '-25o', '+34', 'x45+', '^4', 'o35+', 'o35-', 'x46+', '+45x', 'x5', 'o6', '+56', '-56', '-56+', '-6', '+6', '-2', '-25', '0', '-5', '-35+', '-25+', '-46+', '-36', '-36+', '-4', '-45', 'o5', '-3', '-35', 'o4', '-34', 'o3', '-24', '-23']` <br>
`dic_g_noms_int_inv = ['o45x', 'o54-', '*5', 'o63-', 'o34x', '-25o', '-45x', '-46o', '*6', 'o65-', 'x36+', '^3', '^2', 'o45-', 'o35x', 'o46+', '+34x', 'o46-', '+25x', 'x26-', 'o4', '-34', 'o35+', 'o35-', 'o3', 'o36+', '-24', '+35x', '+23x', '-23', '+45x', '-26o', '-25', '+25-', '-26', '-26+', '+26', '-2', '+2', '-25+', '-45', 'o5', '-46+', '+26-', '-4', '-45+', '-34x', '+34', 'x3', '-35+', '-35', '-36', '-36+', '-3', 'x5', 'o6', '+56', '-56', '-56+', 'x45+', 'x46+', '^4', '-5', '-6', '+6', '0']` <br>
##### Dictionnaire dic_g_bins["Gammes"]
`dic_g_bins_ego = ['1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1001000', '1111011', '1100110', '1010111', '1000001', '1000000', '1000101', '1011000', '1011001', '1000100', '1001001', '1010001', '1000011', '1100000', '1000111', '1111000', '1100001', '1000010', '1010010', '1001011', '1010100', '1001111', '1110100', '1001101', '1100100', '1110001', '1110010', '1100010', '1111001', '1011011', '1010101', '1011100', '1100101', '1001010', '1010011', '1101101', '1110011', '1011101', '1011010', '1011111', '1110101', '1111010', '1100011', '1000110', '1101001', '1101000', '1101011', '1010110', '1100111', '1001110', '1111100', '1101111', '1110110', '1111101', '1101010', '1011110']` <br>
`dic_g_bins_ego_inv = ['1111101', '1101010', '1000100', '1100111', '1011110', '1000000', '1001001', '1010011', '1001000', '1101111', '1001110', '1110011', '1110110', '1111100', '1101000', '1000001', '1101011', '1000110', '1100011', '1010110', '1000011', '1101001', '1000010', '1100001', '1100000', '1011111', '1001101', '1110101', '1111010', '1100100', '1011000', '1010001', '1001100', '1011101', '1000101', '1100101', '1011010', '1011001', '1010101', '1011011', '1101101', '1001010', '1100110', '1011100', '1111011', '1010111', '1111001', '1100010', '1000111', '1010010', '1010100', '1001011', '1110001', '1110010', '1001111', '1110100', '1111000', '1101100', '1111111', '1101110', '1110111', '1111110']` <br>
`dic_g_bins_iso = ['1000001', '1000000', '1000101', '1011000', '1011001', '1000111', '1111000', '1100000', '1000011', '1001001', '1010001', '1000100', '1100001', '1000010', '1001011', '1010100', '1001111', '1110100', '1001101', '1100100', '1010010', '1110001', '1110010', '1011011', '1011100', '1010101', '1100101', '1001010', '1011101', '1011010', '1001000', '1011111', '1001100', '1110101', '1111010', '1100011', '1000110', '1101001', '1100111', '1001110', '1010011', '1111100', '1101000', '1101011', '1010110', '1101101', '1111011', '1100110', '1010111', '1101111', '1110011', '1110110', '1111001', '1100010', '1111101', '1101010', '1011110', '1111111', '1101110', '1110111', '1111110', '1101100']` <br>
`dic_g_bins_iso_inv = ['1000011', '1000000', '1000001', '1100001', '1000010', '1000101', '1001001', '1011001', '1010001', '1000100', '1011000', '1010010', '1011011', '1001101', '1010101', '1100100', '1011101', '1100101', '1011010', '1001000', '1011111', '1110101', '1111010', '1010011', '1100011', '1000110', '1101001', '1100000', '1110001', '1100010', '1010100', '1001011', '1110010', '1111001', '1000111', '1111011', '1100110', '1001100', '1010111', '1101100', '1111101', '1101010', '1100111', '1011110', '1111111', '1101110', '1110111', '1111110', '1101011', '1010110', '1101000', '1101101', '1001010', '1110011', '1011100', '1101111', '1001110', '1110110', '1111100', '1001111', '1110100', '1111000']` <br>
`dic_g_bins_int = ['1000011', '1000000', '1000001', '1100001', '1000010', '1000101', '1001001', '1011001', '1010001', '1000100', '1011000', '1010010', '1011101', '1100101', '1011010', '1001000', '1011111', '1001101', '1110101', '1111010', '1100100', '1010011', '1011011', '1010101', '1100011', '1000110', '1101001', '1100000', '1110001', '1100010', '1010100', '1001011', '1110010', '1111001', '1000111', '1111101', '1101010', '1100111', '1011110', '1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1111011', '1100110', '1010111', '1101011', '1010110', '1101101', '1001010', '1110011', '1011100', '1101111', '1001110', '1110110', '1111100', '1101000', '1001111', '1110100', '1111000']` <br>
`dic_g_bins_int_inv = ['1000011', '1000001', '1100000', '1000000', '1100001', '1000010', '1001001', '1010001', '1000100', '1000101', '1011000', '1011001', '1000111', '1111000', '1001011', '1010100', '1001111', '1110100', '1001101', '1100100', '1010010', '1110001', '1110010', '1001000', '1011011', '1001100', '1010101', '1011101', '1100101', '1011010', '1011111', '1110101', '1111010', '1011100', '1001010', '1100011', '1000110', '1101000', '1100111', '1001110', '1010011', '1111100', '1101001', '1101011', '1010110', '1101101', '1111011', '1100110', '1010111', '1101111', '1110011', '1110110', '1111001', '1100010', '1101100', '1111101', '1101010', '1011110', '1111111', '1101110', '1110111', '1111110']` <br>


_____________________________________________________________________________________________

## Historique des versions capturées.
### Version v0.7 = 
La précédente version a été arrangée, car la dernière gamme n'était pas colorée en rouge, <br>
bien que ses degrés avaient déjà été listés. <br>
### Version v0.8 =
**Ouverture des sonorités** <br>

Le programme a un niveau de préparation des données correct. <br>

Ce premier pas vers les sonorités commence sereinement. <br>
Toutes les données sont présentes pour réaliser tous les traitements nécessaires à l'édition des sons audio. <br>

La prochaine étape se fera avec l'organisation des données utiles. <br>
Elle sera suivie de la création de plusieurs options relatives à la lecture audio sélectionnée. <br>
### Version v0.9
Cette version connait une redirection importante puisqu'elle s'est allégée du module (binôme_audio.py). Le code qui devait être sur le module effacé s'est retrouvé dans le module existant (gammes_audio.py), qui ont tous deux créé une liste respectant les gammes issues du choix de l'utilisateur.

La liste créée contient des tuples (numéro de la colonne et numéro de la ligne) de chaque degré diatonique. Elle sera chargée de modifier avec exactitude les éléments graphiques liés aux gammes sélectionnées, ainsi qu'elle est la base qui finalisera les fréquences hertziennes et les degrés diatoniques respectifs.

    Quand l'utilisateur choisi un bouton (binôme ou gamme), des gammes lui sont attribuées...
### Propreté
**La version v0.9.1**

Les modulations dynamiques sont obtenues avec succès, elles fonctionnent aussi bien pour les boutons des sélections des modes binarisés que pour ceux des gammes nommées.

Je vais faire en sorte que les modulations dynamiques n'interviennent que sur la demande de l'utilisateur. Autrement, toutes les gammes ont la même note tonique qui est la note DO.

    En avant toute !
### Version 0.9.2
C'est avec plaisir que s'est réalisée la construction de cette application. Elle a le mérite de se perfectionner par l'augmentation des utilisations. Bien qu'elle ne soit pas parfaite, elle parvient à assurer une bonne cohabitation, faisant l'union des erreurs de certaines fréquences hertziennes et de l'algorithme chargé de conjuguer les gammes selon la volonté de l'utilisateur.

    On peut tout faire et rester réaliste.
### Message d'informations
**La version v09.3** <br>
**Message box infos** <br>
Cette version fait le point sur les informations relatives aux gammes sélectionnées par l'utilisateur. <br>
Plusieurs options de lecture ont été mises en place, tout en respectant les options précédentes. <br>

**Nouveautés**

**Lecture d'une seule ou de toutes les gammes.** <br>
**Les gammes restent en DO ou bien, elles font de la modulation successive.** <br>
**La lecture varie selon les choix :** <br>
– En respectant les groupements. <br>
– En suivant l'ordre diatonique. <br>
– En s'accordant sur la croissance des fréquences hertziennes. <br>

    Notes du bas de page. <br>
    Quelques fréquences inattendues à vérifier.
### Comme un château de sable
**La version v09.4** <br>
**Partie après partie**

L'architecture prend forme au fur et à mesure que les prévisions se réalisent. <br>
La version n'est pas définitive étant donné qu'il manque quelques parties essentielles : <br>

    Vérification des fréquences.
    Réglages de l'audio.
### Version v10
**Normalement fonctionnel.**

De nombreuses erreurs ont été corrigées et maintenant, le code devrait fonctionner sans erreurs fatales. <br>
Il se pourrait que je me trompe, mais les seules erreurs que j'aurais pu ne pas voir, sont celles des notes diatoniques.
### Version 10.1
**La version v10.1** <br>

Correctif de la version 10.

Quelques erreurs rectifiées aux niveaux de la sélection du bouton binaire et du type de lecture lié au triage des binaires.
### Version 10.2 corrigée
**Version 10.2 corrigée.**

### Version 10.3
**Nouvelle énumération**

Nouvelles matrices relatives aux gammes énumérées, qui du point de vue du traitement, ont été faciles. <br>
Puis c'est avec joie que la partie sensée de l'affichage et à la tonification, n'ont pas eu besoin d'être modifiée. <br>
Il ne reste plus qu'à mettre à jour les pages web : https://www.cabviva.fr/armsph_2.html.


    Il est tellement difficile d'atteindre la perfection !
