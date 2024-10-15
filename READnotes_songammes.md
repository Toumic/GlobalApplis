# BLOC NOTES songammes.py


## Défaut de lecture au type 'Anti iso'
    Une erreur se produit lorsque l'organisation des binaires est au type 'Anti iso'
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

    Il est tellement difficile d'atteindre la perfection !
