# -*- coding: utf-8 -*-
# vicenté quantic cabviva
# Module : gammes_audio.py

import inspect
from typing import Callable

# lino() Pour consulter le programme grâce au suivi des print’s
lino: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno

"# dic_maj = Référence des tonalités majeures primaires à transposer"
dic_maj = {'C': ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B'],
           'D': ['D', '', 'E', '', '+F', 'G', '', 'A', '', 'B', '', '+C'],
           'E': ['E', '', '+F', '', '+G', 'A', '', 'B', '', '+C', '', '+D'],
           'F': ['F', '', 'G', '', 'A', '-B', '', 'C', '', 'D', '', 'E'],
           'G': ['G', '', 'A', '', 'B', 'C', '', 'D', '', 'E', '', '+F'],
           'A': ['A', '', 'B', '', '+C', 'D', '', 'E', '', '+F', '', '+G'],
           'B': ['B', '', '+C', '', '+D', 'E', '', '+F', '', '+G', '', '+A']}
tab_sup = ['', '+', 'x', '^', '+^', 'x^', '^^', '+^^', 'x^^', '^^^', '+^^^', 'x^^^', '^^^^', '+^^^^', 'x^^^^',
           '^^^^^', '+^^^^^', 'x^^^^^', '^^^^^^', '+^^^^^^', 'x^^^^^^', '^^^^^^^', '+^^^^^^^', 'x^^^^^^^', '^^^^^^^^']
tab_inf = ['********', 'o*******', '-*******', '*******', 'o******', '-******', '******', 'o*****', '-*****', '*****',
           'o****', '-****', '****', 'o***', '-***', '***', 'o**', '-**', '**', 'o*', '-*', '*', 'o', '-']
(lino(), "Inverser convenablement (12 * -1 = -12) tab_inf", tab_inf[::-1])


def initie(neo_maj=None, dico=None):
    """Recoder les infos[]. Nouvelle gamme majeure pour 'dic_maj' """
    "# Processus de reconnaissance de la signature tonique."
    if neo_maj:
        (lino(), "Neo", neo_maj)
        signe_nat, note_classic = "", "CDEFGAB"
        for sn in neo_maj:
            if sn not in note_classic:
                signe_nat += sn
        # Valeur numérique de 'sign_nat'.
        ind_signe = 0
        if signe_nat in tab_inf:
            ind_signe = tab_inf.index(signe_nat) - len(tab_inf)
            (lino(), "inf", signe_nat, len(tab_inf))
        elif signe_nat in tab_sup:
            ind_signe = tab_sup.index(signe_nat)
            (lino(), "sup", signe_nat)
        (lino(), "Valeur du signe entrant", ind_signe)
        note_nat = neo_maj[-1]
        (lino(), "Fonction initie neo_maj", neo_maj, "signe et note", signe_nat, note_nat)
        # 32 Fonction/initie neo_maj -E Le signe et la note - E

        "# Calcul de la nouvelle gamme majeure et enregistrement dans le dictionnaire 'dic_maj"
        if neo_maj not in dic_maj.keys():
            dic_maj[neo_maj] = []
            ind_signe2 = ind_signe3 = 0
            for nm in dic_maj[note_nat]:
                nm2, signe2, nm3, signe3 = "", "", "", 0
                if nm != "":
                    if len(nm) == 1:
                        nm2 += signe_nat + nm
                        (lino(), "Nm unique", nm, "nm2", nm2)
                    else:
                        note2 = nm[-1]
                        for sn2 in nm:
                            if sn2 not in note_classic:
                                signe2 += sn2
                        if signe2 in tab_inf:
                            ind_signe2 = tab_inf.index(signe2) - len(tab_inf)  # Signature majeure originale.
                            ind_signe3 = ind_signe + ind_signe2
                            if ind_signe3 > -1:
                                signe3 = tab_sup[ind_signe3]
                            else:
                                signe3 = tab_inf[ind_signe3]
                            nm3 = signe3 + note2
                            (lino(), "inf", signe2, len(tab_inf), signe3)
                        elif signe2 in tab_sup:
                            ind_signe2 = tab_sup.index(signe2)  # Signature avant modification.
                            ind_signe3 = ind_signe + ind_signe2
                            if ind_signe3 < 0:
                                signe3 = tab_inf[ind_signe3]
                            else:
                                signe3 = tab_sup[ind_signe3]
                            nm3 = signe3 + note2
                            (lino(), "sup", signe2, signe3)
                        nm2 = nm3
                        (lino(), "Nm pluriel", nm, "nm2", nm2, "signe2", signe2, "signe3", signe3)
                        (lino(), "ind_signe", ind_signe, "ind_signe2", ind_signe2, "ind_signe3", ind_signe3)
                    (lino(), "Nm", nm, "signe_nat", signe_nat)
                dic_maj[neo_maj].append(nm2)
        (lino(), "Fonction Majeure neo_maj", neo_maj, "dic_maj", dic_maj[neo_maj])
        # 82 Fonction Majeure neo_maj -E dic_maj ['-E', '', 'F', '', 'G', '-A', '', '-B', '', 'C', '', 'D']

    "# Processus de conception de la gamme relative à la demande du dico."
    retour_dico = {}
    nkd_maj, note_classic = '102034050607', "CDEFGAB"
    if dico:
        (lino(), "Dico", dico)
        for kdc, vdc in dico.items():
            # , vdc = Les notes recueillies correspondantes aux lignes couplées.
            for dc2 in vdc:  # Lire les notes toniques une par une.
                (lino(), kdc, "DC2", dc2, dic_maj[dc2])
                tonique = dc2  # Premier degré de la gamme à développer et à comparer.
                retour_dico[tonique] = []
                cdm = -1
                for dm in dic_maj[dc2]:  # Diatoniser les toniques pour comparaisons.
                    cdm += 1  # Donne les indices de la gamme à comparer.
                    nkd = kdc[cdm]  # Séquence la gamme à développer.
                    mkd = nkd_maj[cdm]  # Séquence la gamme majeure.
                    if nkd != "0":
                        ind_mkd = nkd_maj.index(nkd)  # Donne l'indice du degré majeur.
                        dif_dia = cdm - ind_mkd  # Donne la différence pour signer les notes à développer.
                        sig, ind_sig = "", None
                        for sdm in dic_maj[dc2][ind_mkd]:
                            if sdm not in note_classic:
                                sig += sdm
                        note0, deg_note = sig + dic_maj[dc2][ind_mkd][-1], ""
                        (lino(), note0, " sig", sig)

                        "# Première évaluation de la signature. Traitement de la note."
                        if sig in tab_inf:
                            ind_sig0 = tab_inf.index(sig) - len(tab_inf)
                            ind_sig0 += dif_dia
                            (lino(), note0, "IF ind_sig0", ind_sig0)
                        else:
                            ind_sig0 = tab_sup.index(sig)
                            ind_sig0 += dif_dia
                            (lino(), note0, "ELSE ind_sig0", ind_sig0)
                        (lino(), note0, "**1er** ind_sig0", ind_sig0, "dif_dia", dif_dia)

                        if ind_sig0 > -1:
                            sig = tab_sup[ind_sig0]
                            (lino(), note0, " sig", sig)
                        else:
                            # ind_sig2 = tab_inf.index(ind_sig0)
                            sig = tab_inf[ind_sig0]
                            (lino(), note0, " sig", sig)
                        (lino(), note0, "**2me** sig", sig, "dif_dia", dif_dia)

                        "# Deuxième évaluation de la signature."
                        if dif_dia == 0:  # La signature des notes est majeure.
                            deg_note = nkd, note0
                            (lino(), "deg_note", deg_note)
                        else:  # La signature est modifiée.
                            if sig in tab_inf:
                                ind_sig = tab_inf.index(sig) - len(tab_inf)
                                note1 = tab_inf[ind_sig] + dic_maj[dc2][ind_mkd][-1]
                                if dif_dia < 0:
                                    ind_deg = tab_inf[dif_dia]
                                else:
                                    ind_deg = tab_sup[dif_dia]
                                deg1 = ind_deg + nkd
                                deg_note = deg1, note1
                                (lino(), "INF note1", deg1, note1, "signe_note", ind_sig)
                            elif sig in tab_sup:
                                ind_sig = tab_sup.index(sig)
                                note1 = tab_sup[ind_sig] + dic_maj[dc2][ind_mkd][-1]
                                if dif_dia < 0:
                                    ind_deg = tab_inf[dif_dia]
                                else:
                                    ind_deg = tab_sup[dif_dia]
                                deg1 = ind_deg + nkd
                                deg_note = deg1, note1
                                (lino(), "SUP note1", deg1, note1, "signe_note", ind_sig)
                            (lino(), "signe", sig, "Majeure", note0, "dif_dia", dif_dia, "ind_sig", ind_sig)
                        retour_dico[tonique].append(deg_note)
                        (lino(), "dic_maj", dic_maj[dc2][ind_mkd], "deg_note", deg_note)
                        (lino(), "nkd", nkd, "ind_mkd", ind_mkd, dic_maj[dc2][ind_mkd])
                    (lino(), kdc, "DC2", dc2, "nkd", nkd, "mkd", mkd, dm, "\t cdm", cdm)
                (lino(), "retour_dico", retour_dico)
        return retour_dico


def audio_gam(gammic, pulsif, selon, mode, lecture):
    """Ce module[gammes_audio.py] est appliqué au traitement des gammes selon la méthode choisie
     par l'utilisateur. Puis, en retour, il retourne une séquence destinée à être traitée par le module pyaudio,
     afin d'entendre les sonorités des gammes sélectionnées. """
    colis1 = gammic  # Colis1
    colis2 = pulsif  # Colis2
    titre1 = selon  # Le titre est selon le type de données en entrée, soit gamme ou binôme.
    liste_gen = []  # Retour de la liste des gammes à lire.
    num_mem2 = {}  # Deuxième dictionnaire de passage.
    procession = mode  # Les gammes sont statiques en DO ou modulent dynamiquement.
    type_lec = lecture
    dic_htz = {}  # Le dictionnaire des htz-valeurs par nom-clef.
    dic_lig1 = {}  # La série des lignes et des octaves par nom-clef..
    (lino(), "colis1", list(colis1)[0], "colis2", list(colis2)[0], "titre1", titre1, "procession", procession)
    # 180 colis1 1111101 colis2 A0 titre1 Binomes procession Sta

    "Liste réservée aux testes des fréquences anormales situées dans ces gammes."
    liste_gam_anormales = ["-26o", "*6", "o6", "-36"]
    gamme_la = "ABCDEFG"  # La gamme en 'LA' pour assister la gestion des octaves dans la fonction 'invite'.
    dic_dia = [""]  # Il cumule les degrés, afin de mieux traiter les niveaux d'octaves dans la fonction 'invitation'.
    "Bb varie selon la sélection"
    # colis1[0] = bb  +34x
    "Cc est invariant."
    # ..1[1] = cc  {1: ['123400000567', '123000004567', '120000034567', '100000234567', '123456700000', '',
    "Colonne_gam et colonne_bin varient selon la sélection."
    # ..1[2] = colonne_gam  {(1, 0): ['0'], (1, 2): ['1'], (1, 3): ['2'], (1, 4): ['3'],
    # Ériger la liste des noms dynamiques.
    tab_nom = [colis1[2][x][0] for x in colis1[2] if x[1] == 0]
    (lino(), "tab_nom", tab_nom)
    # 190 key_n ['0', '-5', 'o45x', 'o46+', 'o46-', '-26o', '+25x', 'o35x', 'x26-',
    # Montrer un amalgame de degrés.
    for co in list(colis1[2].keys()):
        if 3 == co[0]:
            (lino(), "Colis1[2]", co, colis1[2][co])
            # 104 Colis1[2] (3, 0) ['o45x']
            # 104 Colis1[2] (3, 12) ['1', '2', '3', '4', '6', '7']
            # 104 Colis1[2] (3, 13) ['5']
    # ..1[3] = colonne_bin  ['', '', '1111111', '1101110', '1001100', '1110111', '1111110', '1101100', '1001000',
    "Dic_indice, dic_codage, dic_force sont produits au début et sont invariants."
    # ..1[4] = dic_indice  {'o45x': 1, 'o46-': 2, 'o4': 3, 'o46+': 4, 'o45-': 5, 'o54-': 6, '*5': 7, '-34': 8,
    # ..1[5] = dic_codage  {(1, '123400000567'): [(['o45x', 1], '1000001'), (1, 2, '1000001'), (1, 3, '1000001'),
    # ..1[6] = self.dic_force {'1000001': [((1, '123400000567'), (['o45x', 1], '1000001')), (1, 2, '1000001'),
    "Le tri varie selon la sélection"
    # ..1[7] = tri  None
    "La répartition des hertz sur douze octaves"
    # colis2 {'A0': [('A0', 13.75), ('0', 14.56761754744031), ('B0', 15.433853164253879), ('C0', 16.351597831287414),

    "# Liste des notes = Notes de musique."
    num_mem = {('0', 1): [('1', 'C'), ('2', 'D'), ('3', 'E'), ('4', 'F'), ('5', 'G'), ('6', 'A'), ('7', 'B')]}
    notes = [nm[1] for nm in num_mem['0', 1]]
    del num_mem['0', 1]
    notes_maj = notes.copy()
    gam_maj = '102034050607'
    (lino(), "Gammes. notes", notes, gam_maj)
    # 125 Gammes. notes ['C', 'D', 'E', 'F', 'G', 'A', 'B'] 102034050607

    if titre1 == "Gammes":
        """C’est une fonction de trouver la gamme sélectionnée et de séparer sa valeur invariable et variable. Le
        traitement se base sur les colonnes (bin ou gam), résumant l'ordre de lecture (selon le tri). """
        nom_gam = colis1[0]  # Procuration du nom de la gamme. … [0]. Variant.
        num_gam = colis1[4][nom_gam]  # Procuration du numéro de la gamme. ... [4]. Invariant.
        (lino(), "Variants nom", nom_gam, "num", num_gam)
        # Retrouver le numéro invariant de la gamme choisie avec colis1[5], dic_codage.
        for clef in colis1[5].keys():
            if nom_gam == colis1[5][clef][0][0][0]:  # Le numéro invariant correspondant.
                num_var = clef[0]  # Num_var donne le numéro invariant de la gamme. De 1 à 66.
                cod_var = clef[1]  # Cod_var donne la gamme énumérée. Ex : 102034050607.
                (lino(), "Invariant, clef", clef, nom_gam, cod_var, "num_var", num_var, "dans dic_codage.")
                # 51 Invariant, clef (41, '102034056007') -6 num_var 41 dans dic_codage.
                break
        # Retrouver la position variante de la gamme choisie avec colis1[2], colonne_gam.
        rng_gam = 0
        for g in colis1[2].keys():
            if g[1] == 0 and colis1[2][g][0] == nom_gam:  # La position variante correspondante.
                rng_gam = g[0]
                (lino(), "Variant, G", colis1[2][g], g, "rng_gam", rng_gam, ", dans colonne_gam.")
                # 58 Variant, G ['-6'] (64, 0) rng_gam 64 , dans colonne_gam.
                break
        "À ce moment, on a l'emplacement de la gamme dans les hiérarchies suivantes : constante/variante."
        "Ainsi, qu'un modèle de lecture audio relatif à la sélection."
        # Lire les gammes à partir du point 'rng_gam' correspondant à la gamme sélectionnée.
        liste_gen.clear()
        for g2 in colis1[2].keys():
            if g2[0] >= rng_gam:
                liste_gen.append(g2)
                (lino(), "colis1[2] G2", g2, colis1[2][g2], "liste_gen", liste_gen, len(liste_gen))
                # 249 colis1[2] G2 (3, 0) ['o45x']
                # 249 colis1[2] G2 (3, 12) ['1', '2', '3', '4', '6', '7']
                # 249 colis1[2] G2 (3, 13) ['5']

    elif titre1 == "Binomes":
        """C’est une fonction de trouver le binaire sélectionné et de séparer sa valeur invariable et variable. Le
        traitement se base sur les colonnes (bin ou gam), résumant l'ordre de lecture (selon le tri)."""
        nom_bin = colis1[0]  # Procuration du nom du binaire. … [0]. Variant.
        num_bin = colis1[3].index(nom_bin)  # Procuration de l'index du binaire. … [0]. Variant.
        (lino(), "Variants nom_bin", nom_bin, type(nom_bin), "num_bin", num_bin)
        # Retrouver les gammes qui correspondent à ce nom binaire par # ..1[6] = self.dic_force.
        "# Commencer par les gammes invariables, afin de retrouver les mêmes après le tri."
        bin_invariant, bina = set(), ""
        (lino(), "nom_bin", nom_bin, "colis1[6][nom_bin]", colis1[6].keys(), nom_bin, type(nom_bin))
        if isinstance(nom_bin, int):
            nom_bin = str(nom_bin)
        for key6 in colis1[6][nom_bin]:  # Cherche les noms des gammes ayant le binaire 'nom_bin' Invariant.
            if len(key6) < 3 and key6[0][0] not in bin_invariant:
                if isinstance(key6[0][0], str):
                    bina = key6[0][0]
                    (lino(), "key6<3 STR", key6[0][0], "bina", bina)
                elif isinstance(key6[0][0], int):
                    (lino(), "key6<3 INT", key6[0][0], "bina", bina)
                    # 89 key6<3 INT 2 bina
                    for di4 in colis1[4].keys():  # Clé = nom, valeur = numéro. Invariant.
                        if colis1[4][di4] == key6[0][0]:
                            bina = di4
                            (lino(), "2 key6", key6[1][0], "di4", di4, colis1[4][di4], "bina", bina)
                            break
                    (lino(), "key6(nom)", key6[0][0], "bina", bina)
            else:
                for di4 in colis1[4].keys():
                    if colis1[4][di4] == key6[0]:
                        bina = di4
                (lino(), "key6=3", key6[0], "bina", bina)
            if bina != "":
                bin_invariant.add(bina)
        (lino(), "bin_invariant =", bin_invariant, "Long =", len(bin_invariant))
        "# La liste des gammes d'origine invariable est complétée dans 'bin_invariant'."
        # Transformer la liste des numéros invariables, pour une compatibilité variante.
        liste_gen.clear()  # Liste des gammes ordonnées selon la sélection de tri de l'utilisateur.
        ok = None
        for bi in bin_invariant:
            for co2 in colis1[2].keys():  # ..1[2] = colonne_gam  {(1, 0): ['0'], (1, 2) : selon sélection.
                if co2[1] == 0 and colis1[2][co2][0] == bi:
                    ok = co2[0]
                if ok == co2[0] and co2 not in liste_gen:
                    liste_gen.append(co2)
                    (lino(), "co2", co2, colis1[2][co2])
        (lino(), "liste_gen", liste_gen)

    (lino(), "colis1[0]", colis1[0], "Liste_gen :", liste_gen, "max", max(liste_gen), "\n")
    # 197 colis1[0] -3 Liste_gen : [(64, 0), (64, 59), (64, 57), (64, 44), (64, 60)...] max (66, 63)
    ("# La liste 'liste_gen' contient des tuples ayant (numéro de colonne, numéro de ligne)."
     "Ces tuples ont été produits selon le bouton (nom ou binôme) sélectionné par l'utilisateur."
     "Maintenant, il faut situer chaque degré avec sa fréquence hz et ses notes diatoniques."
     "Situer les fréquences hz : grâce au dictionnaire 'colis2[0]'."
     "Situer les notes diatoniques : grâce au dictionnaire 'colis1[1]'.")

    "# Situation des fréquences hertziennes : grâce au dictionnaire 'colis2[0]'."
    (lino(), "colis2", colis2.keys())
    # 206 colis2 dict_keys(['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11'])
    ("Il y a douze octaves, la note LA 440hz est à la clef 'A5' et les limites d'audibilité sont de 'A1' à 'A9'."
     "En comptant les soixante-six gammes, elles peuvent s'étaler sur six octaves et la clef 440 est en 'A5'."
     "Pour connaitre le bon emplacement d'une gamme par rapport à la clef 'A5', il faut l'indice de la gamme."
     "L'indice de la gamme est détenu dans la liste 'colonne_gam' --> 'colis1[2]'.")

    "# Commencer par découvrir les tonalités diatoniques des gammes choisies, afin d'établir les bonnes octaves."
    # La première des gammes, qui est aussi celle choisie, commence en DO par défaut.
    # Ainsi, à partir du numéro de colonne, à la ligne zéro, on trouve le nom de la gamme.
    dic_dic, dic_deg = {}, {}  # Dictionnaire du dictionnaire aux degrés au même binaire.
    dic_log = {}  # Dictionnaire, clé = le nom de la gamme, valeurs = les données diatoniques[Notes réelles]
    for lg in liste_gen:
        if lg[1] == 0:
            nom_lg = colis1[2][lg][0]  # La donnée variable est insuffisante pour sa forme invariante. 'colonne_gam'.
            dic_log[lg[0]] = [nom_lg]
            num_lg = colis1[4][nom_lg]  # Donne le numéro de la gamme invariante. 'dic_indice'.
            (lino(), "nom_lg", nom_lg)  # Fourni les noms des gammes relatives.
            # 145 nom_lg x3. 145 nom_lg -45. ...
            "# Trouver les degrés au même binaire."
            for kd5 in colis1[5].keys():  # Gamme diatonique selon 'dic_codage' qui est invariant.
                if num_lg in kd5:
                    cop_kd5 = kd5  # Clef invariable (1, '123400000567')
                    dic_dic[colis1[0]] = dic_deg  # Le dico 'dic_dic', clé=nom, valeur=dictionnaire 'dic_deg'.
                    bin_inf = colis1[5][kd5][0][-1]
                    (lino(), "bin_inf", bin_inf, "1er binaire-clé")
                    dic_deg[(nom_lg, bin_inf)] = [cop_kd5[1], 1]
                    (lino(), "num_lg", num_lg, "cop_kd5", cop_kd5, "\n colis1[5]", colis1[5][cop_kd5])
                    # 154 num_lg 56 cop_kd5 (56, '102000345607')
                    #  colis1[5] [(['x3', 375], '1100011'), (56, 2, '1000110'), (56, 3, '1000000'),
                    for kc5 in colis1[5][cop_kd5]:  # Scruter les degrés aux binaires.
                        if len(kc5) > 2:
                            if (nom_lg, kc5[-1]) in dic_deg.keys():
                                dic_deg[(nom_lg, kc5[-1])].append(kc5[1])
                            else:
                                dic_deg[(nom_lg, kc5[-1])] = []
                                dic_deg[(nom_lg, kc5[-1])].append(kc5[1])
                            set(dic_deg[(nom_lg, kc5[-1])])
                        (lino(), "kc5", kc5)
                        # 164 kc5 (56, 2, '1000110')
                    (lino(), "\n dic_dic", dic_dic[colis1[0]], "\n dic_deg", dic_deg)
                    # dic_dic {('-4', '1100111'): [1], ('-4', '1001110'): [2], ('-4', '1010011'): [3]
            (lino(), "\n dic_dic", dic_dic[colis1[0]], "\n dic_deg", dic_deg)
            #  dic_deg {('-3', '1101111'): ['102304050607', 1], ('-3', '1001110'): [2], ('-3', '1110011'): [3]

    "# À ce niveau, le dictionnaire de dictionnaire a rangé les degrés dans leurs binaires respectifs."
    (lino(), "* dic_dic", dic_dic.keys(), "\n dic_deg", list(dic_deg.keys())[:5])
    # 251 * dic_dic dict_keys(['-3'])
    # dic_deg [('-3', '1101111'), ('-3', '1001110'), ('-3', '1110011'), ('-3', '1110110'), ('-3', '1111100')]

    "# Détailler la gamme sélectionnée diatoniquement à l'aide d'un dictionnaire à une seule clé."
    tab_gen, tab_ok = {}, True  # Dictionnaire, clef = nom gamme, valeur = numéro statique/dynamique.
    for ddc in dic_dic.keys():
        (lino(), "\n Premier_tour = Clé dictionnaire principal,", "ddc", ddc)
        # 266 premier_tour = Clé dictionnaire principal, ddc -3

        "# Nous avons besoin d'une mémorisation de la gamme précédente."
        mem0 = {}  # Dictionnaire (gammes, degrés, notes, lignes). Facilite le traitement (mem1, mem2).

        "# Le dictionnaire secondaire 'dic_deg' a la séquence des gammes suivantes."
        for ddg in dic_deg.keys():
            num_mem[ddg[0], 1] = []  # Le dictionnaire 'num_mem' et ses valeurs diatoniques en mode tonique.
            (lino(), "ddg[0]", ddg[0], "num_mem", num_mem)
            # 264 ddg[0] -3 num_mem {('-3', 1): []}
            if isinstance(dic_deg[ddg][0], str):  # Va de gamme en gamme
                num_dia = dic_deg[ddg][0]  # Donne la forme énumérée du mode diatonique.
                num_log = colis1[4][ddg[0]]  # Donne le numéro de la gamme invariante. 'dic_indice'.
                (lino(), "Forme énumérée num_dia", num_dia, "ddg", ddg, "num_log", num_log)
                # 269 Forme énumérée num_dia 102304050607 ddg ('-3', '1101111') num_log 36
                # 269 Forme énumérée num_dia 102034056007 ddg ('-6', '1111101') num_log 41
                # 269 Forme énumérée num_dia 102034050067 ddg ('+6', '1111101') num_log 46

                "# Trouver le numéro dynamique de la gamme dans la liste 'liste_gen'"
                if tab_ok:
                    for lg2 in liste_gen:
                        if lg2[1] == 0:
                            nom_dyn = colis1[2][lg2][0]
                            num_sto = colis1[4][nom_dyn]
                            for c15 in colis1[5].keys():
                                if num_sto in c15:
                                    tab_gen[nom_dyn] = c15 + lg2
                                    (lino(), "tab_gen2", tab_gen[nom_dyn])
                                    break
                    tab_ok = False
                    (lino(), ddg[0], "tab_gen", tab_gen)
                    # 298 -3 tab_gen {'-3': (36, '102304050607', 64, 0), '-6': (41, '102034056007', 65, 0),
                    # '+6': (46, '102034050067', 66, 0)}

                "# Lecture de la liste des formes énumérées (num_dia). Mode tonique uniquement."
                deg_note = deg_gam = 0
                for num in num_dia:  # Lecture de la tonique énumérée.
                    "# Partie correspondante à la première exécution ayant la note DO comme tonique par défaut."
                    num_note = ""  # num_note = tab_inf[val_num] + notes[deg_note]
                    deg_niv = ""  # deg_niv = tab_inf[val_num] + str(deg_gam)

                    "# Si la valeur de 'num' n'est pas un intervalle vide (= '0')"
                    if num != '0':
                        (lino(), ddg[0], num, "num_dia", num_dia, "____Lecture diatonique___deg_note ", deg_note)
                        # 294 -3 C1 102304050607 ____________Lecture diatonique____________________ 0
                        ind_num0 = num_dia.index(num)  # num_dia = 102304050607
                        ind_num1 = gam_maj.index(num)  # gam_maj = '102034050607'
                        val_num = ind_num0 - ind_num1
                        deg_gam += 1
                        (lino(), "ind_num0_1", ind_num0, ind_num1, "val_num", val_num, "num", num)
                        if val_num != 0:
                            if val_num < 0:
                                num_note = tab_inf[val_num] + notes_maj[deg_note]
                                deg_niv = tab_inf[val_num] + str(deg_gam)
                                (lino(), "\t*tab_inf", deg_niv, "num_note", num_note)
                            else:
                                num_note = tab_sup[val_num] + notes_maj[deg_note]
                                deg_niv = tab_sup[val_num] + str(deg_gam)
                                (lino(), "\t*tab_sup", deg_niv, "num_note", num_note)
                        else:
                            num_note = notes_maj[deg_note]
                            deg_niv = str(deg_gam)
                            (lino(), "\t* Naturelle", deg_niv, "num_note", num_note)
                        (lino(), deg_note, "*Origine", deg_niv, "num_note", num_note, "deg_gam", deg_gam)
                        # 317 0 *Note originale num_note C deg_gam 1
                        deg_note += 1

                    "# Élaboration du dictionnaire 'num_mem', qui comprend les degrés et les notes en tonalité de DO."
                    passage = deg_niv, num_note
                    (lino(), "passage", passage, "", deg_niv, num_note)
                    if passage != ('', ''):
                        if passage not in num_mem[ddg[0], 1]:
                            num_mem[ddg[0], 1].append(passage)
                            (lino(), "Clé [ddg[0], 1]", ddg[0], "num_mem", num_mem[ddg[0], 1])
                            # 325 Clé [ddc, niv] -3 1 num_mem {('-3', 1): [('1', 'C'), ('2', 'D'), ('-3', '-E'),
                            # ('4', 'F'), ('5', 'G'), ('6', 'A'), ('7', 'B')]}
                            if len(passage[1]) > 1:
                                if passage[1] not in dic_maj.keys():
                                    initie(passage[1], None)  # passage[1] (a servi de test pour les signatures).
                                    (lino(), "ddg[0], 1", ddg[0], 1, "passage", passage)
                notes.clear()
                notes = [nm[1] for nm in num_mem[ddg[0], 1]]
                (lino(), "Notes", notes, "ddg[0]", ddg[0])
                # 446 Notes ['C', 'D', 'E', 'F', 'G', 'A', 'B'] ddg[0] 0

            "# Lecture des gammes et seule la précédente compte pour le passage de la tonalité."
            # Les tests sélectionnant la gamme mélodique[-3] donnent deux gammes relatives qui
            # n'ont pas de points communs avec leurs origines. La première [-3] n'a pas de point commun
            # avec la seconde [-6] qui a plusieurs points communs avec la tierce [+6].
            # Dans ce cas, n'ayant aucun commun, la gamme repart en DO.
            for knm in num_mem.keys():
                if num_mem[knm]:
                    ("\n", lino(), "knm", knm, "num_mem[knm]", num_mem[knm], "\n ****************************")
                    # 359 knm ('-3', 1) num_mem[knm] [('1', 'C'), ('2', 'D'), ('-3', '-E'), ('4', 'F'), ('5', 'G'),
                    # ('6', 'A'), ('7', 'B')]
                    num_mem2[knm[0]] = num_mem[knm].copy()
                    ind_knm = tab_gen[knm[0]][-2]  # Le dico tab_gen a les numéros des gammes.
                    (lino(), "knm[0]", knm[0], "tab_gen[knm[0]][-2] = ind_knm", ind_knm)
                    # 362 knm[0] -3 tab_gen[knm[0]][-2] = ind_knm 64
                    if colis1[2][ind_knm, 0][0] == knm[0]:  # La clé [ind knm, 0] vérifie le nom de la gamme.
                        ("# Poursuite de la gamme concernée parmi les gammes dans 'colis1[2]. (colonne_gam)"
                         "Ce qui rend possible l'incrémentation des données de 'colis1[2]'.")
                        mem0[knm[0]] = []  # Déclaration d'une liste pour ce nom(knm[0]).
                        for c12 in range(1, len(colis1[3]) + 1):  # Nombre de lignes qui étalent les degrés modaux.
                            if (ind_knm, c12) in colis1[2].keys():  # Dans colonne_gam dynamique (colis1[2])
                                trans = (ind_knm, c12), colis1[2][ind_knm, c12]
                                mem0[knm[0]].append(trans)
                                (lino(), (ind_knm, c12), "colis1", colis1[2][ind_knm, c12], "c12", c12)
                                # 372 (60, 12) colis1 ['4', '5'] c12 12

            code_dg = dic_deg[ddg]
            (lino(), "code_dg", code_dg, "dic_deg", dic_deg[ddg])
            # 377 code_dg ['102304050607', 1] dic_deg ['102304050607', 1], 338 code_dg [2] dic_deg [2]
            # 377 code_dg [3] dic_deg [3], 338 code_dg [4] dic_deg [4], 338 code_dg [5] dic_deg [5]
            # 377 code_dg [6] dic_deg [6], 338 code_dg [7] dic_deg [7]

        "# Repères obtenus pour la production des tonalités."
        (lino(), "tab_gen", tab_gen)
        # 382 tab_gen {'-3': (36, '102304050607', 64, 0), '-6': (41, '102034056007', 65, 0),
        # '+6': (46, '102034050067', 66, 0)}
        (lino(), "num_mem2", num_mem2)
        # 382 num_mem2 {'-3': [('1', 'C'), ('2', 'D'), ('-3', '-E'), ('4', 'F'), ('5', 'G'), ('6', 'A'), ('7', 'B')],
        # '-6': [('1', 'C'), ('2', 'D'), ('3', 'E'), ('4', 'F'), ('5', 'G'), ('-6', '-A'), ('7', 'B')],
        # '+6': [('1', 'C'), ('2', 'D'), ('3', 'E'), ('4', 'F'), ('5', 'G'), ('+6', '+A'), ('7', 'B')]}
        "# ((Colonne = 60, Ligne = 12), Degrés = ['4', '5'])"
        (lino(), list(mem0)[0], "Mem0", mem0[list(mem0)[0]])
        # 381 o5 Mem0 [((60, 12), ['4', '5']), ((60, 13), ['7']), ((60, 20), ['3']), ((60, 50), ['1']),
        # ((60, 51), ['2']), ((60, 53), ['6'])]

        "# Commencement de la séquence des modulations dynamiques."
        if procession == "Dyn":
            mem0_key, len0_key, count_gam = list(mem0.keys()), len(mem0.keys()), 0
            for rng1 in range(len0_key):
                for rng2 in range(len0_key):
                    if rng1 == rng2 - 1:
                        count_gam += 1
                        "# Comparaison des deux gammes mémorisées."
                        un, u2 = mem0[mem0_key[rng1]], mem0_key[rng1]
                        de, d2 = mem0[mem0_key[rng2]], mem0_key[rng2]
                        (lino(), "__________________________________________", count_gam, "U2", u2, "D2", d2)
                        (lino(), "_________________________", "\n Un", u2, un, "\n De", d2, de)
                        # 402 _________________________
                        #  Un [((60, 12), ['4', '5']), ((60, 13), ['7']), ((60, 20), ['3']), ((60, 50), ['1']),
                        #  ((60, 51), ['2']), ((60, 53), ['6'])] o5
                        #  De [((61, 13), ['5']), ((61, 25), ['7']), ((61, 50), ['3']), ((61, 51), ['2']),
                        #  ((61, 52), ['6']), ((61, 54), ['1']), ((61, 55), ['4'])] -35+
                        lig, deg = 0, 0
                        tab_adn, tab_anm = [], []  # Tables de récupération.
                        for un2 in un:
                            for de2 in de:
                                "# Comparaison des lignes binaires."
                                if un2[0][1] == de2[0][1]:
                                    "# Condition requise pour une recherche de tonalité approximative."
                                    lig += 1
                                    (lino(), "Lig u2", u2, un2, un2[0][1], "d2", d2, de2, de2[0][1], "LIG", lig)
                                    # 414 Lig u2 -6 ((65, 17), ['3']) 17 d2 +6 ((66, 17), ['3']) 17 LIG 1
                                    ("# Des lignes binaires et les notes correspondantes de la gamme précédente"
                                     "sont utiles. Elles peuvent jouer un rôle pour tonifier la gamme suivante.")
                                    for nm1 in range(len(num_mem2[u2])):  # Comparaison des notes diatoniques.
                                        # adn1 = Instance pour les notes inégales, elle est la référence tonale.
                                        adn1, adn2 = num_mem2[u2][nm1], num_mem2[d2][nm1]
                                        "# La note précédente est vue, elle est différente de la suivante."
                                        if adn1[0] == un2[1][0] or un2[0][1] == de2[0][1]:
                                            if adn1 not in tab_adn:
                                                adn12 = u2, adn1, un2, d2, de2
                                                tab_adn.append(adn12)
                                            (lino(), "\t Inégaux adn1", u2, adn1, un2, "adn2", d2, adn2, de2)
                                            # 425 	 Inégaux adn1 o35x ('4', 'F') ((8, 17), ['4']) adn2 x26- ('+4', '+F')
                                            break
                                    "# Comparaison des degrés diatoniques aux mêmes lignes binaires."
                                    if un2[1][0] == de2[1][0]:
                                        "# Condition requise pour une recherche du degré approximatif."
                                        deg += 1
                                        (lino(), "Deg u2", u2, un2, un2[1][0], "d2", d2, de2, de2[1][0], "DEG", deg)
                                        # 432 Deg u2 -6 ((65, 17), ['3']) 3 d2 +6 ((66, 17), ['3']) 3 DEG 1
                                        ("# Plusieurs degrés sont semblables, ils enchainent "
                                         "une analyse ses notes diatoniques.")
                                        for nm2 in range(len(num_mem2[u2])):  # Comparaison des notes diatoniques.
                                            # anm1 = anm2 = Instances de référence des degrés aux notes égales.
                                            anm1, anm2 = num_mem2[u2][nm2], num_mem2[d2][nm2]
                                            if anm1[0][0] == anm2[0][0]:
                                                if anm1 not in tab_anm:
                                                    anm12 = u2, anm1, un2, d2, anm2, de2
                                                    tab_anm.append(anm12)
                                                (lino(), "\t Égaux anm1", u2, anm1, "\t anm2", d2, anm2)
                                                # 443 		 Égaux anm1 -6 ('3', 'E') 	 anm2 +6 ('3', 'E')
                                                break
                                    (lino(), u2, "* Un2", un2, "tab_gen", tab_gen[u2])
                                    (lino(), d2, "** De2", de2, "tab_gen", tab_gen[d2], "\n ______   ______")
                                    # 446 -6 * Un2 ((65, 61), ['1']) tab_gen (41, '102034056007', 65, 0)
                                    # 447 +6 ** De2 ((66, 61), ['1']) tab_gen (46, '102034050067', 66, 0)
                                    #  ______   ______

                        if 0 < lig >= deg > 0:
                            "# Le nombre de lignes est supérieur à zéro et il est égal à celui des degrés."
                            # print(lino(), "elif 0 < lig >= deg > 0: =================", lig, deg)
                            # print(lino(), "ADN num_mem2[u2]", u2, num_mem2[u2])
                            (lino(), "ANM num_mem2", d2, num_mem2[d2])
                            anm0, dico_anm = False, {}
                            dico_anm[tab_gen[d2][1]] = []
                            if tab_anm:
                                (lino(), " DEG", deg, "\n ANM", tab_anm, "Long", len(tab_anm))
                                for td_anm1 in num_mem2[u2]:
                                    for td_anm2 in num_mem2[d2]:
                                        "# Relevé des mêmes notes"
                                        (lino(), "td_anm1", td_anm1[-1], "|2", td_anm2[-1], tab_gen[d2][1])
                                        if td_anm1[-1] == td_anm2[-1] and td_anm1[-1] not in dico_anm[tab_gen[d2][1]]:
                                            dico_anm[tab_gen[d2][1]].append(td_anm1[-1])
                                            (lino(), "td_anm1", td_anm1[-1], td_anm2[-1], dico_anm[tab_gen[d2][1]])
                                "# Il y a six notes égales et une seule différence qui est la tonique."
                                if len(dico_anm[tab_gen[d2][1]]) == 6:
                                    dico_anm[tab_gen[d2][1]].clear()

                                for da in dico_anm[tab_gen[d2][1]]:
                                    if da not in dic_maj.keys():
                                        initie(da, dico=None)
                                        (lino(), "Initie Da", da)
                                (lino(), " dico_anm", dico_anm)

                            retour_init = initie("", dico_anm)
                            for ri_gam in retour_init.values():
                                "# Visionner le dictionnaire revenant de l'initiation."
                                (lino(), " retour_init", ri_gam, len(retour_init))
                                # 584  retour_init {'xG': [('1', 'xG'), ('2', 'xA'), ('3', 'xB'), ('x4', '+^C'),
                                # ('x5', '+^D'), ('+6', '^E'), ('7', '^F')]} 1
                            if retour_init:
                                (lino(), "tab_gen", d2, tab_gen[d2])
                                if len(retour_init) == 1:
                                    del num_mem2[d2]
                                    passe = retour_init.values()
                                    num_mem2[d2] = list(passe)[0]
                                    (lino(), "Une clé passe", list(passe)[0])
                                else:
                                    key_riz = list(retour_init.keys())
                                    dic_vrai, tab_vrai, nbr_vrai = {}, [], 0
                                    ton_u2 = num_mem2[u2][0][1]
                                    (lino(), "Key_riz", key_riz, "ton_u2", ton_u2, "\n num_mem2", num_mem2[u2])

                                    for varie in key_riz:  # Lecture par clés délivrées de la fonction[initie].
                                        dic_vrai[varie] = 0
                                        for rive in retour_init[varie]:  # Lecture de chacune des gammes à clés.
                                            (lino(), "Varie", varie, rive[1])
                                            for carie in num_mem2[u2]:
                                                if carie[1] == rive[1]:
                                                    nbr_vrai += 1
                                                    (lino(), "carie[1]", carie[1])
                                        dic_vrai[varie] = nbr_vrai
                                        tab_vrai.append(nbr_vrai)
                                        nbr_vrai = 0
                                        (lino(), "dic_vrai", varie, dic_vrai[varie])
                                    max_vrai = max(tab_vrai)
                                    # print(lino(), "dic_vrai", dic_vrai, "max_vrai", max_vrai, "ton_u2", ton_u2)
                                    if ton_u2 in dic_vrai.keys():
                                        if dic_vrai[ton_u2] == max_vrai:
                                            num_mem2[d2] = retour_init[ton_u2]
                                            (lino(), "[ton=max] num_mem2[d2]", d2, num_mem2[d2])
                                        else:
                                            "# Je laisse pour évaluer les apparitions."
                                            # print(lino(), "Else[ton=max]")
                                    else:
                                        for q_vrai in dic_vrai.keys():
                                            if dic_vrai[q_vrai] == max_vrai:
                                                num_mem2[d2] = retour_init[q_vrai]
                                                (lino(), "ton n'est pas une clé")
                                (lino(), "dico_anm", dico_anm)

                        elif 0 == lig == deg:
                            "# Le nombre de lignes et de degrés égaux est égal à zéro."
                            "# Quand le nombre de ligne/degré est nul, on ne fait rien, la gamme reste en DO[C]"
                            # print(lino(), "elif 0 == lig == deg: ================", lig, deg)
                            # print(lino(), lig, "ADN num_mem2[u2]", u2, num_mem2[u2])

                        else:
                            "# Les lignes vont de un à plus et les degrés sont toujours à zéro."
                            # print(lino(), "else: ================================", lig, deg)
                            adn0, dico_adn = True, {}
                            dico_adn[tab_gen[d2][1]] = []
                            (lino(), "LIG", lig, "ADN", tab_adn, "Long", len(tab_adn))
                            # print(lino(), lig, "ADN num_mem2[u2]", u2, num_mem2[u2])
                            (lino(), deg, "ANM num_mem2", d2, num_mem2[d2])
                            for tad in tab_adn:
                                for td in tad:
                                    if td == u2:
                                        if not adn0:  # Remise à True au second tour
                                            adn0 = True
                                        (lino(), "Nom 1", td, "len", len(td))
                                    elif td == d2:
                                        adn0 = False
                                        (lino(), "Nom 2", td)
                                    elif adn0:
                                        if isinstance(td[-1], str):
                                            (lino(), "elif (str) Nom 1", td, "len", len(td))
                                        else:
                                            for td_adn in num_mem2[u2]:
                                                if td_adn[0][-1] == td[-1][0]:
                                                    dico_adn[tab_gen[d2][1]].append(td_adn[-1])
                                                    (lino(), "elif Nom 1 td", u2, td, "td_adn", td_adn, tab_gen[d2])
                                    (lino(), "td", td)
                                (lino(), "tad", tad, "Len", len(tad))
                            for da in dico_adn.values():
                                for d in da:
                                    if d not in dic_maj.keys():
                                        initie(d, None)
                            retour_init = initie("", dico_adn)
                            "# Retourne les gammes demandées sous les toniques trouvées."
                            for k_rie, v_rie in retour_init.items():
                                (lino(), "retour_init", retour_init[k_rie], len(retour_init))
                            # 628 retour_init {'-G': [('1', '-G'), ('-2', 'oA'), ('o3', '*B'), ('o4', '*C'),
                            # ('5', '-D'), ('+6', 'E'), ('7', 'F')], '+D': [('1', '+D'), ('-2', 'E'), ('o3', 'F'),
                            # ('o4', '-G'), ('5', '+A'), ('+6', 'xB'), ('7', 'xC')]} 2
                            dic_rit, tab_rit, max_rit = {}, [], ""
                            for ri in retour_init.keys():
                                if lig == 1:  # Il n'y a qu'un seul choix pour la note tonique.
                                    del num_mem2[d2]
                                    num_mem2[d2] = retour_init[ri].copy()
                                else:
                                    tab_rit.clear()
                                    for kiri in retour_init.keys():
                                        dic_rit[kiri] = 0
                                        kr = 0
                                        for rire in retour_init[kiri]:
                                            # Compter le nombre de similitudes.
                                            for nmu2 in num_mem2[u2]:
                                                if rire[1] == nmu2[1]:
                                                    kr += 1
                                                    (lino(), "num_mem2", rire[1], nmu2[1])
                                        dic_rit[kiri] = kr
                                        tab_rit.append(kr)
                                    max_rit = max(tab_rit)
                                    for calor, rigolo in dic_rit.items():
                                        if max_rit == rigolo:
                                            del num_mem2[d2]
                                            num_mem2[d2] = retour_init[calor].copy()
                                            (lino(), "calor", calor, "rigolo", rigolo, "\n", retour_init[calor])
                                            break
                            "# Quand le nombre de comparaison est nul, on ne fait rien la gamme reste en DO[C]"
                            (lino(), "max_rit", max_rit)
                            # print(lino(), "dic_rit", dic_rit, "tab_rit", tab_rit, "lignes", lig)
                            (lino(), "dico_adn", dico_adn, "retour_init", retour_init)
                        # print(lino(), "ANM num_mem2[d2]", d2, num_mem2[d2])
                        break

    (lino(), dic_maj.keys())
    # 514 dict_keys(['C', 'D', 'E', 'F', 'G', 'A', 'B', '-G', '-D', 'oE', 'oF', 'xG', '+A', '-A', 'oA', '+D', 'xD',
    # '+E', '+F', '*G', 'oG', '-F', 'xF', '+G', '-E', '*A', '^F', 'xE', '^E', '^D'])

    # Distribution des lignes dans le répertoire des octaves.
    # Plage commence à la ligne deux et finit à la ligne soixante-trois.
    # 197 colis1[0] -3 Liste_gen : [(64, 0), (64, 59), (64, 57), (64, 44), (64, 60)...] max (66, 63)
    plages_lig = {f: [x for x in range(f, f+12)] for f in range(2, 87, 12)}
    tables_lig = list(plages_lig.keys())
    (lino(), "Lignes. Plages_lig", plages_lig, "\ntables_lig", tables_lig)
    # 719 Lignes. Plages_lig {2: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 14: [14, 15, 16, 17, 18, 19, 20, 21, 22,
    # 23, 24, 25], 26: [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], 38: [38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
    # 48, 49], 50: [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], 62: [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
    # 73], 74: [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], 86: [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]}
    # tables_lig [2, 14, 26, 38, 50, 62, 74, 86]

    ("\n", lino(), "ANM num_mem2", num_mem2, "\n liste_gen", liste_gen)

    ("# colis2 {'A0': [('A0', 13.75), ('0', 14.56761754744031), ('B0', 15.433853164253879), ... 'A11':."
     "Audibilité de A0 : ('E0', 20.60172230705437) Htz à A10 : ('#D10', 19912.12695821318) Htz.")
    "# Il faut déterminer où commence l'octave un et où finit l'octave six. L'octave va de DO à DO."
    octave_5, clef_oct = 440, 5  # Cette fréquence correspond à la clé de l'octave A5.
    oct_min, oct_max = clef_oct - 3, clef_oct + 5  # Calculer les octaves utiles par rapport à A5.
    clef_min, clef_max = "A" + str(oct_min), "A" + str(oct_max)  # Définir les clefs utiles.
    (lino(), "Octaves min et max", oct_min, oct_max, "\n colis2.keys()", colis2.keys())
    (lino(), "Clefs min et max", clef_min, clef_max)
    # 735 Octaves min et max 2 10
    # 736 Clefs min et max A2 A10
    panel, pan, stop = False, [], False
    for khz in colis2.keys():
        if clef_min[1] == khz[1]:
            panel = True
        else:
            val = int(khz[1:])
            if val >= int(clef_max[1:]):
                stop = True
        if panel:
            pan.append(khz)
        if stop:
            break
    (lino(), "Octaves. Pan", pan)
    # 752 Octaves. Pan ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']

    "# Création d'une liste contenant les octaves audibles issues du dictionnaire des fréquences."
    liste_htz = []  # La liste des fréquences notées du dictionnaire, sur une seule ligne.
    for k_htz in colis2.keys():
        if k_htz in pan:
            liste_htz.extend(colis2[k_htz])
    (lino(), "liste_htz", liste_htz)
    # 731 liste_htz [('A2', 55.0), ('2', 58.27047018976124), ('B2', 61.735412657015516), ('C2', 65.40... )

    def hertz(rang, note, ligne, nom):
        """Définir la fréquence hertzienne par rapport aux notes et à la liste des hertz."""
        (lino(), "******* ******* ******* Fonction HERTZ ******* ", nom)
        # 752 ******* ******* ******* Fonction HERTZ *******  0
        (lino(), "Fonction HERTZ", "rang", rang, "note", note, "ligne", ligne, "nom", nom)
        # 754 Fonction HERTZ rang 1 note C ligne 61


        def invitation(inf, sup):
            """Effectue une série de comparaisons récurrentes."""
            (lino(), "Inf", inf, "sup", sup)
            if len(sup) == 1:
                sup = sup[0]
            if len(dic_dia) == 7:
                dic_dia.clear()
            if nom_lgf not in dic_dia:
                dic_dia[0] += inf[0][-1]
                (lino(), "Inf", inf, "dic_dia", dic_dia)
                # 778 Inf ['C', 'A2', 2] dic_dia ['C']
            il, sl = inf[2], sup[2]  # Référentiel des lignes.
            io, so = int(inf[1][-1]), int(sup[1][-1])  # Référentiel des octaves[partie numérique].
            sa = sup[0][-1]  # Référentiel de la note 'LA'.
            ind_in, ind_sn = gamme_la.index(inf[0][-1]), gamme_la.index(sup[0][-1])

            "# La ligne 'sup' est supérieure."
            if il < sl:
                a0 = "(il<sl) :"
                "# La différence entre les lignes reste dans l'octave. Chaque clé est un 'LA'."
                # Octaves. Pan ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'].
                # 719 Lignes. Plages_lig {2: [2-13], 14: [14-25], 26: [26-37], 38: [38-49], 50: [50-73],
                # 62: [62-73], 74: [74-85], 86:[86-97]}
                # tables_lig [2, 14, 26, 38, 50, 62, 74, 86]
                # Gamme_la = "ABCDEFG"
                "# L'octave 'inf' est infer ou égale."
                if io <= so:
                    if sa != gamme_la[0]:  # 'gamme_la[0]' not note LA 'A'
                        if ind_in < ind_sn:
                            if sl - il < 8:  # Teste la différence entre les lignes sup et inf, à vérifier.
                                sup[1] = inf[1]  # Garder le cran de l'octave 'sup'.
                                (lino(), nom_lgf, a0, "(io<=so, != 'A') \t", inf, sup, note, "gamme_la", gamme_la)
                            else:
                                sup[1] = pan[sl//8]  # Garder le cran de l'octave 'sup'.
                                (lino(), nom_lgf, a0, "(io<=so, != 'A') \t", inf, sup, note, "gamme_la", gamme_la)
                        elif ind_in > ind_sn:
                            sup[1] = pan[ind_lig + 1]  # Augmenter d'un cran l'octave 'sup'.
                            (lino(), nom_lgf, a0, "(io<=so, != 'A') \t", inf, sup, note, "gamme_la", gamme_la)
                    elif sa == gamme_la[0]:  # La note est 'LA'.
                        if sl//8 + 1 < len(pan):
                            sup[1] = pan[sl // 8 + 1]  # Augmenter d'un cran l'octave 'sup'.
                            (lino(), nom_lgf, a0, "(io<=so, 'A', sl8<)  \t", inf, sup, note)
                        else:
                            sup[1] = pan[sl // 8]  # Augmenter d'un cran l'octave 'sup'.
                            (lino(), nom_lgf, a0, "(io<=so, 'A', sl8>)  \t", inf, sup, note)
                elif io > so:  # La ligne 'sup' est super, l'octave est infer.
                    sup[1] = pan[ind_lig + 1]  # Augmenter d'un cran l'octave 'sup'.
                    (lino(), nom_lgf, a0, "(io>so)         \t", inf, sup, note)
                else:
                    (lino(), nom_lgf, a0, "(Else)  \t\t\t", inf, sup, note)

            "# Les lignes 'inf' et 'sup' sont égales."
            if il == sl:
                b0 = "(il=sl) :"
                if sa == gamme_la[0]:
                    ind_pan = pan.index(sup[1])
                    sup[1] = pan[ind_pan + 1]  # Augmenter d'un cran l'octave 'sup'.
                    (lino(), nom_lgf, b0, "(A)  \t\t\t", inf, sup, note)
                elif io > so:
                    if ind_in < ind_sn:
                        sup[1] = inf[1]  # Garder le cran de l'octave 'sup'.
                        (lino(), nom_lgf, b0, "(io>so,ii<is)  \t\t\t", inf, sup, note)
                    elif ind_in > ind_sn:
                        ind_pan = pan.index(inf[1])
                        if ind_pan + 1 < len(pan):
                            sup[1] = pan[ind_pan + 1]  # Augmenter d'un cran l'octave 'sup'.
                            (lino(), nom_lgf, b0, "(io>so,ii>is)  \t\t\t", inf, sup, note)
                        else:
                            ind_pan = pan.index(inf[1])
                            sup[1] = pan[ind_pan]  # Augmenter d'un cran l'octave 'sup'.
                            (lino(), nom_lgf, b0, "(io>so,ii>is)  \t\t\t", inf, sup, note)
                elif io == so:
                    if ind_in < ind_sn:
                        sup[1] = inf[1]  # Garder le cran de l'octave 'sup'.
                        (lino(), nom_lgf, b0, "(io=so,ii<is)  \t\t\t", inf, sup, note)
                    elif ind_in > ind_sn:
                        ind_pan = pan.index(inf[1])
                        sup[1] = pan[ind_pan + 1]  # Augmenter d'un cran l'octave 'sup'.
                        (lino(), nom_lgf, b0, "(io=so,ii>is)  \t\t\t", inf, sup, note)
                elif io < so:  # Les lignes 'inf et sup' sont égales.
                    sup[1] = inf[1]  # Garder le cran de l'octave 'inf'.
                    (lino(), nom_lgf, b0, "(io<so)  \t\t\t", inf, sup, note)
                else:
                    (lino(), nom_lgf, b0, "(Else)  \t\t\t", inf, sup, note)

            "# La ligne 'inf' est supérieure."
            if il > sl:
                c0 = "(il>sl) :"
                ind_pan = sl//8
                sup[1] = pan[ind_pan]  # Régler le cran d'octave 'sup'.
                (lino(), nom_lgf, c0, "     \t\t\t\t", inf, sup, note)

            "# Utilisé pour une recherche des anomalies."
            if nom_lgf in liste_gam_anormales:  # ["-26o", "*6", "o6", "-36"]
                (lino(), nom_lgf, "Invitation", inf, sup)
                # 794 Invitation ['C', 'A2', 2] ['D', 'A2', 3]
            return inf, sup


        "# Recueillir l'octave correspondante à la ligne."
        "# En rapport avec la fonction 'invitation', dictionnaire valable 'dic_lig1[nom]'"
        cran = None  # Niveau de lecture de l'octave.
        if nom not in dic_lig1.keys():
            dic_lig1[nom] = []
            if nom in liste_gam_anormales:
                ("****", lino(), nom, "HERTZ", liste_gam_anormales)
        for lig_o in plages_lig.keys():
            "# Trouver à quelle plage se trouve la ligne."
            if ligne in plages_lig[lig_o]:
                ind_lig = list(plages_lig.keys()).index(lig_o)  # tables_lig [2, 14, 26, 38, 50, 62, 74, 86]
                cran = pan[ind_lig]  # Pan ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
                pass_lig = [note, cran, ligne]
                (lino(), "pass_lig", pass_lig)
                # 876 pass_lig ['C', 'A2', 2]
                "# Il faut incrémenter 'pass_lig' au bon emplacement."
                dic_lig1[nom].append(pass_lig)
                (lino(), "lig_o", lig_o, "ind_lig", ind_lig, "(la gamme zéro est la gamme naturellement majeure).")
                (lino(), "ligne", ligne, "plages", plages_lig[lig_o][0], "cran", cran, "(le cran est l'octave).")
                (lino(), "note", note, "nom", nom, "cran", cran, "dic_lig1", dic_lig1[nom][-1])
                # 808 lig_o 2 ind_lig 0 (la gamme zéro est la gamme naturellement majeure).
                # 809 ligne 2 plages 2 cran A2 (le cran est l'octave).
                # 810 note C nom 0 ligne 2 dic_lig1 ['C', 'A2', 2]

                ("# Arrangement des suites des octaves par rapport aux lignes."
                 "Cet arrangement peut s'appliquer au 'titre1 = Binomes'.")
                (lino(), "note", note, "nom", nom, "dic_lig1", dic_lig1.keys())
                ind_nom, inf0, sup0, bin_nom = "", "", "", ""
                if titre1 == 'Gammes':
                    ind_nom = tab_nom.index(nom)
                elif titre1 == 'Binomes':
                    tot_nom = [vn for vn in liste_gen if vn[1] == 0]
                    bin_nom = [colis1[2][bn][0] for bn in tot_nom]
                    ind_nom = bin_nom.index(nom)
                    (lino(), "tot_nom", tot_nom, "bin_nom", bin_nom)
                if len(dic_lig1.keys()) > 1:  # Le dictionnaire a plusieurs clefs.
                    if len(dic_lig1[nom]) == 1:  # La clef du nom n'a qu'un seul degré, ici.
                        ("# Cette partie permet l'analyse des passages entre les gammes."
                         "Afin de déterminer l'octave qui suit après les septième degré.")
                        if titre1 == 'Gammes':
                            inf0, sup0 = dic_lig1[tab_nom[ind_nom - 1]][-1], dic_lig1[nom]
                        elif titre1 == 'Binomes':
                            inf0, sup0 = dic_lig1[bin_nom[ind_nom - 1]][-1], dic_lig1[nom]
                        (lino(), "Avant", "inf0", inf0, "sup0", sup0)
                        retour_invite = invitation(inf0, sup0)
                        (lino(), nom, "Retour", retour_invite)
                        # 813 -5 Retour (['B', 'A3', 8], ['C', 'A3', 9])
                        (lino(), nom, " dic_lig1", dic_lig1[nom][-1])
                        (lino(), "Après", "inf0", inf0, "sup0", sup0)
                if len(dic_lig1[nom]) > 1:
                    (lino(), "dic_lig1", dic_lig1[nom])
                    ("# Informations des valeurs du dictionnaire (Note. Octave. Ligne)."
                     "Des derniers et avant-derniers degrés de la liste des valeurs du dictionnaire.")
                    inf0, sup0 = dic_lig1[nom][-2], dic_lig1[nom][-1]
                    (lino(), "Avant", "inf0", inf0, "sup0", sup0)
                    # 771 inf ['C', 'A2', 2] sup ['D', 'A3', 3]
                    "# Espace des comparaisons et des corrections."
                    retour_invite = invitation(inf0, sup0)
                    (lino(), nom, "Retour", retour_invite)
                    # 821 0 Retour (['C', 'A2', 2], ['D', 'A2', 3])
                    (lino(), nom, " dic_lig1", dic_lig1[nom][-1])
                    (lino(), "Après", "inf0", inf0, "sup0", sup0)
                ("# Le dictionnaire 'dic_lig1' comporte les bonnes gammes."
                 "Dont les définitions sup et inf ont été appliquées.")
                if len(dic_lig1[nom]) == 7:
                    (lino(), nom, "\ndic", dic_lig1[nom])
                    # 919 nom 0 dic [['C', 'A2', 2], ['D', 'A2', 3], ['E', 'A2', 4], ['F', 'A2', 5],
                    # ['G', 'A2', 6], ['A', 'A3', 7], ['B', 'A2', 8]]
                break

        ("# Trouver la note naturelle et indexer la note altérée."
         "# 720 Lignes. tables_lig [2, 14, 26, 38, 50, 62, 74, 86]"
         "# 747 Octaves. Pan ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']")
        for noe in dic_lig1[nom]:
            if noe[0] == note:
                cran = noe[1]
                (lino(), nom, "**** ** noe", noe, "note", note, "cran", cran)
                # 838 0 **** ** noe ['C', 'A2', 2] note C cran A2
                break
        signe_o, note_o, ind_car = None, None, 0
        if nom not in dic_htz.keys():
            dic_htz[nom] = []
        (lino(), "liste_htz", liste_htz)
        # 843 liste_htz [['A2', 55.0], ['2', 58.27], ['B2', 61.74], ['C2', 65.41], ['2', 69.3], ['D2', 73.42],
        # ['2', 77.78], ['E2', 82.41], ['F2', 87.31], ['2', 92.5], ['G2', 98.0], ['2', 103.83], ['A3', 110.0]
        for gen in liste_htz:
            (lino(), nom, "Fonction HERTZ", "____ Gen", gen, "note", note, "cran", cran)
            if gen[0] == cran:  # 743 ligne 61 plages 62 cran A7. Le cran a été arrangé précédemment.
                ind_cran = liste_htz.index(gen)  # Indice de l'octave A7 dans la liste des génériques.
                (lino(), nom, "Fonction HERTZ", "____ Gen", gen, "note", note, "cran", cran, "ind_cran", ind_cran)
                # 836 Fonction HERTZ _______ Gen ['A2', 55.0] note C cran A2.
                "# Traitement sur la note entrante signée."
                if len(note) > 1:
                    note_o = [n for n in 'CDEFGAB' if n == note[-1]][0]
                    signe_o = [n for n in note if n not in 'CDEFGAB'][0]
                    if signe_o in tab_sup:
                        ind_car = tab_sup.index(signe_o)
                    elif signe_o in tab_inf:
                        ind_car = tab_inf.index(signe_o) - len(tab_inf)
                    (lino(), "Fonction HERTZ", "ind_car", ind_car, "Valeur de l'altération.")
                    # 766 Fonction HERTZ ind_car 1 Valeur de l'altération.
                elif len(note) == 1:
                    note_o = note
                (lino(), "Fonction HERTZ", "signe_o", signe_o, "ind_car", ind_car, "note_o", note_o)
                # 768 Fonction HERTZ signe_o + ind_car 1 note_o A.
                (lino(), nom, "                       ____________________________            ind_cran", ind_cran)
                "# Aller à la rencontre de l'indice de la note dans la liste des génériques (htz)."
                for car in range(ind_cran, ind_cran+13):  # La valeur 'ind_cran' est son numéro d'octave.
                    (lino(), "*HERTZ* liste_htz[car]", liste_htz[car], "car", car, "nom", nom)
                    if liste_htz[car][0][0] == note[-1]:
                        (lino(), "*HERTZ* car", car, "ind_car", ind_car, "nom", nom, len(liste_htz), liste_htz[-1])
                        car += ind_car  # La variable 'car' est l'indice dans la liste des génériques.
                        (lino(), "*HERTZ* liste_htz[car]", liste_htz[car], note[-1], "note", note, "car", car)
                        (lino(), "len(liste_htz)", len(liste_htz), "ind_car", ind_car)
                        # 954 *HERTZ* liste_htz[car] ['C2', 65.41] C note C car 3
                        # 955 len(liste_htz) 96 ind_car 0
                        if liste_htz[car][0].isdigit():  # La valeur 'liste_htz' est numérique.
                            liste2 = liste_htz[car][0]
                            liste2 = [note + liste2[0], liste_htz[car][1]]
                            dic_htz[nom].append(liste2)
                            (lino(), "  Isdigit() liste2 2", liste2, "note", note, "car", car)
                            (lino(), nom, " Digit dic_htz", dic_htz[nom][-1], "note", note, "car", car)
                            (lino(), "Digit liste_htz dic_htz", liste_htz[car], dic_htz[nom], "note", note)
                        elif liste_htz[car][0].isalnum():  # La valeur 'liste_htz' est alphanumérique.
                            liste2 = liste_htz[car][0]
                            liste2 = [note + liste2[-1], liste_htz[car][1]]
                            dic_htz[nom].append(liste2)
                            (lino(), "\t\t Isalpha() liste2 2", liste2, "note", note, "car", car)
                            (lino(), nom, "\t\t Alpha dic_htz", dic_htz[nom][-1], note, "car", car)
                            (lino(), "Alpha liste_htz dic_htz", liste_htz[car], dic_htz[nom], "note", note)
                        else:
                            "# Quand la note est naturelle, la valeur 'liste_htz[car][0]' est naturelle."
                            (lino(), nom, "***** ELSE (Digit/Alpha)", "car", car, liste_htz[car], "note", note)
                        if len(dic_htz[nom]) == 7:
                            (lino(), nom, dic_htz[nom])
                        return dic_htz[nom]

    ("Fonction hertz juste au-dessus."
     "# Affectation des fréquences aux notes de 'liste_gen'. Avec appel fonction HERTZ."
     "En fin de ce traitement, est mis en évidence l'ordre de lecture des degrés diatoniques.")
    (lino(), "liste_htz", liste_htz, len(liste_htz)/12)
    # 731 liste_htz [('A2', 55.0), ('2', 58.27047018976124), ('B2', 61.735412657015516), ('C2', 65.40... )] 7
    # 747 Octaves. Pan ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
    # tables_lig [2, 14, 26, 38, 50, 62, 74, 86]


    def ordonnance(donne1, don2):
        """Mettre de l'ordre parmi les modèles modaux diatoniques.
        Les ordonnances sont là pour ordonner les degrés désordonnés du dictionnaire 'dic_lgf[gamme]'.
        Comme les gammes désordonnées sont réordonnées, celles qui ne le sont pas ne passent pas par là."""
        (lino(), "ordonnance donne1", donne1, cop1, cop2, "\n", dic_lgf[don2])
        # 908 ordonnance donne1 Diatone [1, 2, 3, 4, 6, 7, 5] [1, 2, 3, 4, 5, 6, 7]
        # [['C2', 65.41], ['-D2', 69.3], ['oE2', 73.42], ['oF2', 77.78], ['+A2', 58.27], ['B2', 61.74], ['xG3', 110.0]]
        ("Ordonnance", don2)
        if donne1 == "Diatone":
            "Traitement de remise en ordre des degrés diatoniques de la gamme en cours."
            rng_dld = 0
            tab_new = []
            for dld in dic_lgf[don2]:
                if cop1[rng_dld] != cop2[rng_dld]:
                    ind_cop = cop1.index(rng_dld+1)
                    tab_new.append(dic_lgf[don2][ind_cop])
                    (lino(), "\t cop1_2", cop1[rng_dld], cop2[rng_dld], "ind_cop1", dic_lgf[don2][ind_cop])
                else:
                    tab_new.append(dld)
                rng_dld += 1
            dic_lgf[don2] = tab_new
            (lino(), "Diatone", donne1, don2, "cop1", cop1, cop2, "\n", dic_lgf[don2])
        elif donne1 == "Hertz":
            ("L'ordonnance va agir sur l'ordre croissant des fréquences,"
             "elle n'est pas traitée ici, puisque seuls les degrés désordonnés y figurent."
             "Le rangement croissant des fréquences est dans le module principal 'songammes.py'.")
            (lino(), "Hertzien", donne1, don2, "cop1", cop1)
        elif donne1 == "Groupe":
            "L'ordonnance ajoute la liste désordonnée au dictionnaire 'dic_lgf[don2]'."
            dic_lgf[don2].append(cop1)
            (lino(), "Groupement", donne1, don2, "cop1", cop1)
            # 924 Groupement Groupe o45x cop1 [1, 2, 3, 4, 6, 7, 5]

    nom_lgf, dic_lgf, a_dnl = "", {}, 0.0
    tab_lgf = {}  # Dictionnaire des gammes aux degrés rangés.
    for lgf in liste_gen:
        doublons = []
        (lino(), "_______ for lgf in liste_gen:", nom_lgf, "lgf", lgf, "\n")
        # 906 _______ for lgf in liste_gen:  lgf (1, 0)
        if 0 in lgf:  # Cette clé mène à un nom de gamme.
            nom_lgf = colis1[2][lgf][0]
            dic_lgf[nom_lgf] = []
            tab_lgf[nom_lgf] = []
            (lino(), "Nom lgf", lgf, nom_lgf)
            # 746 Nom lgf (66, 0) +6
        else:  # Cette clé mène à une note diatonique de la gamme.
            deg_lgf = colis1[2][lgf]
            (lino(), "Introduction : deg_lgf", nom_lgf, deg_lgf)
            if len(deg_lgf) == 1:  # Ici, un degré binaire correspond avec une seule note diatonique.
                deg_lgf = colis1[2][lgf][0]
                for nm2_x in num_mem2[nom_lgf]:
                    if nm2_x[0][-1] == colis1[2][lgf][0][-1]:
                        degre_x, note_x, ligne_x, nom_x = nm2_x[0], nm2_x[1], lgf[1], nom_lgf
                        tab_lgf[nom_lgf].append(degre_x)
                        retour_htz = hertz(degre_x, note_x, ligne_x, nom_x)
                        (lino(), "degre_x", degre_x, "note_x", note_x, "ligne_x", ligne_x, "nom_x", nom_x)
                        (lino(), nom_lgf, "Note", note_x, "_______ retour_htz1", retour_htz, len(retour_htz))
                        # 925 degre_x 1 note_x C ligne_x 2 nom_x 0
                        if retour_htz[-1] not in dic_lgf[nom_lgf]:
                            dic_lgf[nom_lgf].append(retour_htz[-1])
                            (lino(), "** dic_lgf", dic_lgf[nom_lgf])
                            (lino(), nom_lgf, "deg_lgf", deg_lgf, "nm2_x", nm2_x, "lgf", lgf)
                            # 894 deg_lgf 1 nm2_x ('1', 'C') lgf (66, 61)
                            "# S'affiche à chaque fin de traitement de gamme."
                            if len(dic_lgf[nom_lgf]) == 7:
                                (lino(), nom_lgf, "** dic_lgf", dic_lgf[nom_lgf])
                                if type_lec == "Hertz":
                                    dic_lgf[nom_lgf].append("Hertz")
                                    (lino(), "Htz", nom_lgf, type_lec)
                                if nom_lgf in liste_gam_anormales:
                                    (lino(), nom_lgf, "\t\t IF dic_lgf", dic_lgf[nom_lgf])
                                    # 977 -26o 		 IF dic_lgf [['C3', 130.81], ['-D3', 138.59],
                                    # ['E3', 164.81], ['F3', 174.61], ['-G3', 185.0], ['oA8', 6271.93], ['B2', 61.74]]
                                cop1 = [int(x[-1]) for x in tab_lgf[nom_lgf]]
                                cop2 = cop1.copy()
                                cop2.sort()
                                if cop1 != cop2:
                                    ordonnance(type_lec, nom_lgf)
                                    (lino(), dic_lgf[nom_lgf], "\n", tab_lgf[nom_lgf], type_lec, "\n")
            else:  # Ce degré binaire a plusieurs notes diatoniques.
                # La liste des doublons aide à lire la liste 'deg_lgf'.
                for i_deg in deg_lgf:
                    deg_lgf2 = i_deg
                    (lino(), "deg_lgf", deg_lgf, "Note lgf", lgf, "deg_lgf2", deg_lgf2)
                    # 763 deg_lgf ['1', '2', '3', '4', '6', '7'] Note lgf (3, 12) deg_lgf2 1
                    for nm2_x in num_mem2[nom_lgf]:
                        if nm2_x[0][-1] in colis1[2][lgf]:
                            if nm2_x[0] not in doublons:
                                doublons.append(nm2_x[0])
                                (lino(), "nm2_x[0]", nm2_x[0][-1], "colis1[2][lgf]", colis1[2][lgf])
                                # 989 nm2_x[0] 1 colis1[2][lgf] ['1', '2', '3', '4', '6', '7']
                                degre_x, note_x, ligne_x, nom_x = nm2_x[0], nm2_x[1], lgf[1], nom_lgf
                                tab_lgf[nom_lgf].append(degre_x)
                                (lino(), "degre_x", degre_x, "note_x", note_x, "ligne_x", ligne_x, "nom_x", nom_x)
                                retour_htz = hertz(degre_x, note_x, ligne_x, nom_x)
                                (lino(), nom_lgf, "Liste", degre_x, "__ retour_htz2", retour_htz, len(retour_htz))
                                if retour_htz[-1] not in dic_lgf[nom_lgf]:
                                    dic_lgf[nom_lgf] += [retour_htz[-1]]
                                    (lino(), nom_lgf, "** dic_lgf", dic_lgf[nom_lgf])
                                    (lino(), nom_lgf, "deg_lgf2", deg_lgf2, "nm2_x", nm2_x, "lgf", lgf)
                                    # 916 deg_lgf2 1 nm2_x ('1', 'C') lgf (3, 12)
                                    "# S'affiche à chaque fin de traitement de gamme."
                                    if len(dic_lgf[nom_lgf]) == 7:
                                        (lino(), nom_lgf, "** dic_lgf", dic_lgf[nom_lgf])
                                        if type_lec == "Hertz":
                                            dic_lgf[nom_lgf].append("Hertz")
                                            (lino(), "Htz", nom_lgf, type_lec)
                                        if nom_lgf in liste_gam_anormales:
                                            (lino(), nom_lgf, "ELSE dic_lgf", dic_lgf[nom_lgf])
                                        cop1 = [int(x[-1]) for x in tab_lgf[nom_lgf]]
                                        cop2 = cop1.copy()
                                        cop2.sort()
                                        "# Jamais servi jusqu'à maintenant."
                                        if cop1 != cop2:
                                            (lino(), "\n", dic_lgf[nom_lgf], "\n", tab_lgf[nom_lgf], type_lec)

    (lino(), "Pied de page du code.", "dic_lgf", dic_lgf)
    # 837 Pied de page du code. dic_lgf {'+6' : [('C7', 2093.004522404789), ('D7', 2349.3181433392606), ('E4',
    # 329.6275569128699), ('F7', 2793.825851464031), ('G8', 6271.926975707988), ('+A3', 116.54094037952248),
    # ('B4', 246.94165062806206)]}

    return dic_lgf
