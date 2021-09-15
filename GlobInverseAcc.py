# Python utf8
# En construction
# Mercredi 8 septembre 2021 2021

# Conçu par Vicenté Llavata Abreu|Vicenté Quantic|Toumic
# GlobInverseAcc
# Parodie à double sens & accords 1357

gam_nat = "102034050607"
gam_not = "1234567"
gam_oblic = {}


def inv_acc(pc):
    """Traitement dictionnaire pc clone fichier binaire
    Synchronisation des modes diatoniques Formes classic et leurs inverses"""
    print(f' GlobInverseAcc  signatures')
    """GlobEnModes > dic_analyse"""
    for ikey1, aval1 in pc.items():
        gam_oblic[ikey1] = []
        lava = list(aval1[0][0])
        lava.reverse()
        aval = ''.join(s for s in lava)
        for ikey2, aval2 in pc.items():
            for aa in aval2[0]:
                iso = ''
                if aval == aa:
                    if ikey2 < ikey1 or ikey2 == ikey1:
                        if ikey2 == ikey1:
                            iso = 'X'
                        gam_oblic[ikey1].append(ikey2)
                        print(aa, ikey1, 'ikey1   ', iso, '   ikey2', ikey2, aval)
                    else:
                        gam_oblic.pop(ikey1)
    # break

    print(gam_oblic, "Nombre d'éléments", len(gam_oblic))


if __name__ == '__main__':
    print(f' GEM Quelle seption !')
    inv_acc({})
