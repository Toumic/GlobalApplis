**GlobalApplis** _Mises à jour_
# Première main
#### Historique
Ce programme n'est pas le premier venu, puis c'est son niveau de maturité qui lui a valu sa déclaration :
* **Du 12/07/2015 progam.v1a via des assistances**  
[https://www.developpez.net/forums/.../.../python/](https://www.developpez.net/forums/f96/autres-langages/python/)
* **Du 07/08/2022 conversion en unité cumulative**  
[https://magviva.cabviva.fr/conversion-formule/](https://magviva.cabviva.fr/conversion-formule/)
* Les gammes calculées issues de GlobalApplis ont été transmises à GlobGamVers6 afin quelles puissent être utilisées.
* Du **24/08/2022 et 27/09/2022 gestion des Toplevel**   
[https://www.developpez.net/forums/.../.../tkinter/presence-frame-ouverte/#post11867692](https://www.developpez.net/forums/d2136918/autres-langages/python/gui/tkinter/presence-frame-ouverte/#post11867692)<br>
[https://www.developpez.net/forums/.../.../python/general-python/gestion-fenetres-window/](https://www.developpez.net/forums/d2138622/autres-langages/python/general-python/gestion-fenetres-window/)<br>
* **Du 28 septembre 2022 mise en forme du texte,** `aux notes affichées dans Gammique.chrome(self)`

### mercredi 28 septembre 2022
    Cas de poursuite des éléments concernés
Base Analise : Écriture nettoyée des parenthèses<br>
Fonction Gammique.chrome<br>
if chrselect == 'Chrome atonal':  	# Ligne 1779<br>
....c2_a1 = c_sdb[0]<br>
....c3_a = c3_pre[0]<br>
....c2_m1 = c_sdb[0]<br>
....c3_m = c3_sui[0]<br>
if chrselect == 'Chrome naturel':  	# Ligne 1819<br>
....c2_a1 = c_chaug[0][2]<br>
....c3_a = c_chaug[0][3]<br>
....c2_m1 = c_chmin[0][2]<br>
....c3_m = c_chmin[0][3]<br>
c2_ = c2_a1<br>
c3_ = c3_a<br>
c5_ = c2_m1<br>
c6_ = c3_m<br>
chvow_a = "{}{}".format(c3_, c2_)<br>
chvow_m = "{}{}".format(c6_, c5_)  # Les notes chromatiques<br>
chrcan.create_text(xb_, yb1_, text=chvow_a, font=fontchr, fill='black')<br>
chrcan.create_text(xb_, yb2_, text=chvow_m, font=fontchr, fill='black')<br>