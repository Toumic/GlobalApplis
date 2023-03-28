""" # La masse de la gamme naturelle
# Composée des seption notes majeures: C, D, E, F, G, A, B.
# Harmonisée des seption degrés majeurs:
#		(CDEFGAB) = 0
#		(DEFGABC) = b3, b7 = -4-8 = -12
#		(EFGABCD) = b2, b3, b6, b7 = -3-4-7-8 = -22
#		(FGABCDE) = #4 = +5 = +5
#		(GABCDEF) = b7 = -8 = -8
#		(ABCDEFG) = b3, b6, b7 = -4-7-8 = -19
#		(BCDEFGA) = b2, b3, b5, b6, b7 = -3-4-6-7-8 = -28"""
"""(" Chaque degré porte une valeur altérative binôme(b,#).\n"
 "	En opérant les valeurs de la signature (Signature/Masse)...\n"
 "	En ordonnant la séquence:		F, C, G, D, A, E, B\n"
 "			#4, 0, b7, b3b7, b3b6b7, b2b3b6b7, b2b3b5b6b7\n"
 "	... (Signature/Masse):\n"
 "			F(#4) 4ème degré plus 1 dièse = 4 + 1 = +5\n"
 "			A(b3b6b7) 	{\n"
 "				3ème degré moins 1 bémol = -3 - 1 = -4\n"
 "				6ème degré moins 1 bémol = -6 - 1 = -7\n"
 "				7ème degré moins 1 bémol = -7 - 1 = -8\n"
 "						}\n"
 "				Masse pesante totale = -4-7-8 = -19\n")"""

z = [0]


def func(x):
    print(x)
    z[0] = 8
    return z


func(4)
print('z', z[0])
