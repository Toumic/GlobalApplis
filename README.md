{ GlobalApplis `Cette application`}

README.md

# GlobalApplis
_Est une application qui rassemble plusieurs instruments de mesure._
 
## Résumé gammologique :
    La gammologie est une science qui consiste à étudier les gammes musicales
La gamme musicale est naturelle et elle comporte 12 ½ tons chromatiques, dont sept tonalités majeures. Le fait de comprendre que les intervalles forment une ressource et une voie de développement, nous oriente dans une bonne direction. Celle du déploiement des possibilités gammales :
###     _C'est bien connu ! Il y a 462 modulations diatoniques_
    _Les 66 gammes fondamentales & Uniques diatoniques toniques. & leurs 396 modes diatoniques_
Les gammes sont développées grâce aux altérations bémol et dièse. Elles servent à la découverte des modèles fondamentaux et de leurs tonalités, et elles commencent le développement par la gamme naturellement majeure et non altérée. La nature non signée des notes est une indication de départ, si bien que cette gamme a des degrés modaux faisant partie d'une seule diatonie.
 
###    _C'est naturellement que la gamme comporte 7 tonalités différentes_
    _Tout un rassemblement diatonique aux tonalités qui se suivent sans se répéter_
La simplicité de cette gamme (**CDEFGAB**). Et la calculabilité des tonalités et la légèreté des modes toniques fondamentaux. Un ensemble d'informations aisément transmissibles à un quelconque algorithme. On notera que la notion de poids prend son pied avec la gamme, la charge diatonique répartie sur les tares modales associées, pouvant à terme être démultiplié au facteur 7.
 
### _Comment cette appli agit pour "calculer" la gamme naturelle._
    _La gamme naturelle comporte deux tétracordes et sept modulations diatoniques_
Normalement chaque nouvelle gamme fondamentale créée possède sept qualités modales majeures, si bien qu'à ce niveau la gamme de Do majeure et celle de Ré majeure ont les mêmes qualités tonales. Car elles sont égales du point de vue des intervalles. La gamme a sept notes & cinq intervalles qui déterminent sa tonalité, et en particulier la valeur naturelle de la tonalité. Comme il a été dit le tétracorde en fait partie en tant qu'objet, le mode tonique majeur de toutes les tonalités représentent une forme qualitative identique. Parmi les fondements ; il y a **°45x**, & ces notes : **[Do, bRé, bbMi, bbFa, ##Sol, #La, Si]**.
Les tétras majeurs occupent l'octave de Do à Do : Do, _, Ré, _, Mi, Fa et Sol, _, La, _, Si, Do. Ils ont une forme similaire : **"OoOoOO" = "OoOoOO" = ~~FAUX~~**. Puis le cas "°45x" donne l'aperçu d'un tétra minimal aussi appelé cluster : **OOOOoooooOOOO**
`Le développement clusterien initialiser systémique`
 
###Pour parler un peu du système tétra = Développer cluster
    _Le milieu tétra n'est pas limité à la gamme naturelle_
Et si cette limite faisait l'occasion à l'apprentissage d'une organisation clustérienne, de voir dans cet infini de combinaisons un systémisme gammique clustérien. En ce qui me concerne, le tétracorde a été vu pendant le développement des tonalités fondamentales. Il a été aussi perçu comme un système à part, selon le modèle cluster. Qui configure une série hiérarchique en croissance d'intervalles, ceci dans un espace donné de 12 notes(~~Octave~~). Le cluster inférieur débute à 1 et le supérieur prend fin à 13 ; En termes mathématiques : **Cluster = 4 notes** et :**Gamme = 2 clusters**, lorsque les 2 clusters sont limités aux extrémités `| La tonique(inf) / la quarte(sup) |`. Ils sont exponentiellement limités, `Voir GlobalApplis.py ligne 38.` Le cluster inférieur peut s'étendre à 9 notes :**= Octave - Cluster**. Au point de développement initial, il y a cinq intervalles vides : `OOOOoooooOOOO`; `Exemple extension : OOOoooooOOOOO, ici = °34^`.
#### §§§_& Le visuel mécanique & L'expansion méthodologique & `L'idéologie gammique`
    Le verbe idéal a l'empreinte des différents aspects des gammes fondamentales.
        `GlobalApplis Ligne 44 & 45`: Les notes 'CDEFGAB'
        Les altérations : ['', '+', 'x', '^', '^+', '^x', '°*', '-*', '*', '°', '-']
    Musicologiquement l'`Exemple : Mélodique. Dominante`. Soit : Modèles diatoniques altérés.
#### §§__& Le visuel mécanique & `L'expansion méthodologique` & L'idéologie gammique
    Une série d'incrémentations conditionnelles aux extrêmes ordonnés.
        `GlobalApplis Ligne 145 `: Zone Active Points
    Le couple tétra est Divisible. L'économie du désaccouplement & Une seule unité tétra.
#### §___& `Le visuel mécanique` & L'expansion méthodologique & L'idéologie gammique
    La scène de l'évolution ordonnée est animée en précisions | Film imaginaire
        `GlobalApplis. GlobModelGammy. GlobGamFonds. GlobEnModes.`: Modules Fabriques
    Au commencement et depuis, l'évolution est relative a un assemblage algorithmique.
# µ`UNITÉ`
## Détailler les fonctions des codes sources
_L'application a des modules sobres en fonction_
#### `GlobalApplis.GlobModelGammy.GlobGamFonds.GlobEnModes.`
### _GlobalApplis ***_
**Le module des initiales,** 'GA' est chargé de transformer le cluster en une entité recevable. Modifier par la voie des incrémentations dans un jeu de priorités rangées aux extrémités libres. C'est dire que lorsque l'extrémité parvient à l'extrême, l'élément clustérien précédant l'extrémité incrémentée avance d'un cran en rappelant l'extrémité à son côté. L'unité clustérienne propage son extrémité jusqu'à l'extrême, puis avance l'unité inférieure et Relance l'extrémisme. Selon que les libertés des unités inférieures ne soient limitées, l'avancée intérieure avance à chaque relance à une aide orientée vers le bas pour le cas.
#### Glob Apply `Édition Fichiers [(Tétras.µ)(Tétras.µ©)(Tétras.Qµ)]`µ: 1234. µ©: 1234. .5678. Q©: 1,b2, .,7,8.
### _GlobModelGammy ***_
**Le module des premiers,** 'GMG' service de triage des modèles (Tetra/Couple). Obtention des modèles uniques débarrassés de leurs modes diatoniques. Modélisations parfaites protagonistes du rôle fondamental : `Réductions Analytiques`. Une gamme a plusieurs descriptions, un exemple lettré "**123045670000**", et sa binarisation "**111011110000**". Binariser les notes à une finalité de comparaison entre modèles, methode de calcul se dispensant des degrés chiffrés.
#### Glob Gammy `Édition Tableaux [(Tétras)(Gammes)(Lettres/Chiffres/Binaires)]`
### _GlobGamFonds ***_
**Le module des pesées,** 'GGF' a pour fonction de donner un poids aux éléments modaux, ainsi chaque mode diatonique a sa propre charge. Cette réponse est nécessaire à l'appréciation du choix fondamental, puisque la gamme naturelle est de poids zéro car elle ne comporte pas de signature. Autrement les degrés qui lui sont diatoniques ont chacun un poids `calcul_tare_gam Ligne 13 & 14 Séquence: F, C, G, D, A, E, B || #4, 0, b7, b3b7, b3b6b7, b2b3b6b7, b2b3b5b6b7`. Mais les résultats sont nombreux, et ils ne répondent pas tous au critère de légèreté des signes. C'est aussi dire que l'algorithme ne répond pas à nos attentes, et que cette partie est à rehausser. Création du fichier `globdicTgams.txt` contenant ce premier résultat. Transmission du dictionnaire `mode_maj7` conteneur des modes diatoniques ayants les septièmes majeures.
#### Glob Fondy `Sort Léger [(GlobGamFonds Ligne 117)(glob_en.seption(modes_modal))]`
### _GlobEnModes ***_
**Le module des précis.** 'GEM' Dans ce module arrivent les gammes légères envoyées par `GlobGamFonds`. Elles deviennent opérationnelles avec le modèle majeur naturel, comme ceci : Chaque mode léger est opérationnel à tous les niveaux diatoniques, finalement chaque mode a sa définition de masse. En un 1er temps les modes sont représentés par des nombres assez conséquents, qui peuvent être rendus plus faciles à comprendre. Ainsi chaque donnée modale va être démultipliée par un facteur 7, jusqu'à zéro. Le résultat est absolu malgré qu'il soit décimal, certains affichent des valeurs entières à 1.

`def seption(mode_poids, k1, pc1, gm1): Réception des poids modaux basiques à augmenter & Création 'globdic_Dana.txt'`

`def dana_fonc(dana, gam1): Les dictionnaires {dan/ego/maj}: Enregistrer. Répertorier. Référencer.`

`def maj7_fonc(unic, fondre): Réception simple(unic), abscon(fondre). Trie les gammes.`

`def fond_gam(mode, fol): A la charge signer les gammes(notes et signes)+ Modes diatoniques.`


###### Brièvement ; Augmenter les mesures entrantes. Capter les septièmes majeures. Trier les gammes selon leurs masses : Mêmes poids signifient également mêmes rangs. Mêmes rangs possibilité de poids différents. Préciser les différentes natures gammales, soit que l'issue fonctionnelle produise un ensemble fondamental basé sur la légèreté des gammes à noms entiers.

Les gammes fondamentales sont les 1ers modes diatoniques, ces modes fondamentaux ont leurs importances et aussi leurs exactitudes est primordiale. En un premier temps, nous avons déterminé selon deux vecteurs : Les poids modaux. Les noms entiers. Et dans une deuxième mesure pouvant être décisive, nous avons décidé de réaliser une seconde expertise avec la même méthode que celle appliquée dans le développement diatonique. Et ainsi saisir l'occasion de valider ou pas la 1ʳᵉ déduction fondamentale :

Le premier degré modal naturel est majeur à toutes les tonalités, ainsi que tous les autres modes diatoniques.
Afin la lecture s'améliore sans les mots inutiles, et en scriptant l'écriture explicative : 
`I. Mode tonique. Tonalité modale/majeure. 
|. II. Mode tonal. Tonalité (b3, b7) plus la valeur du mode tonique. 
|. III. Mode mélodique. Tonalité (b2, b3, b6, b7) plus la valeur du mode tonique. 
|. IV. Mode médian. (#4)... |. Mode dominant. (b7)... |. Mode harmonique. (b3, b6, b7)... 
|. Mode sensible. (b2, b3, b5, b6, b7)... |`. 
Chaque modulation diatonique a sa propre définition, elle est chargée de s'appliquer au modèle fondamental. 
Si, `I. Tonique harmonique. Tonie(b6). |. II. (b3, b7)+(b5). |. III. (b3, b6, b7)+(b4). |. IV. (#4)+(b3). 
|. V. (b7)+(b2). |. VI. (b3, b6, b7)+(b1). |. VII. VII. (b2, b3, b5, b6, b7)+(b7).`. 
À bonne lecture bon entendeur, il y a une présence modale qui présente une improbable qualité modale : 
`|. VI. (b3, b6, b7)+(b1). |`

#### Glob Modely `Program Test & Actif [(Test.Précis)(Acte.Effet)]`

### _GlobInverseAcc ***_
**Le module des inverses.**'GIA' Le but est qu'à chacun des modèles modaux on puisse y trouver son inverse, 
soit que le modèle inversé ressemble en tout les points au modèle original comme à son image devant un miroir. 
Il est évident, que chacune des révélations soient renseignées par le nom de la gamme ainsi que celui du degré diatonique.

`Pour plus de détails voir : Ligne 48 -Notions basiques du module GlobInverseAcc`

### _GlobGamChrom ***_
**Le module des chromatismes.** 'GGC' les gammes chromatiques sont aussi importantes que les gammes diatoniques, 
puisque chaque gamme a sa définition chromatique. La gamme chromatique fait l'usage d'une trilogie, car elle est composée de la gamme originale et de deux chromatismes altérés. Alors, et selon la mise en place du chromatisme augmenté ou diminué, le développement diatonique produit un cycle ouvert ou fermé.
* Lorsque le cycle est ouvert : Les modes voisins n'ont pas les mêmes formules numériques
* Et quand le cycle est fermé : Les modes voisins ont les mêmes formules numériques<br>

Ce module est consacré à la mise en forme du dictionnaire à l'aide des tables reçues de GlobGamVers6. 
Le dictionnaire est donc renvoyé, sa forme est simplifiée par rapport aux tables reçues.


### _GlobGamMicro ***_
**Le module des commatismes.** 'GGM'

### _progamV6encore ***_
**Le module interface.** 'pv6e' Rassemble le résumé gammologique et est destiné à approfondir les systèmes tétras et commatiques.
