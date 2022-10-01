# Liste des problèmes rencontrés
Dans la fonction `def typgam(self, typ):`

~~Le comportement des fenêtres n'est pas toujours cohérent, quand une fenêtre est ouverte et que je fasse une transition des gammes classiques vers celles qui sont calculées. La mise à jour des fenêtres se fait correctement, mais parfois lorsque je ferme cette fenêtre elle s'ouvre lors d'une nouvelle transition, même si les conditions sont bonnes. `Voir lignes 231 à 308 de GlobGamVers6`~~<br>
- Problème des fenêtres (Toplevel) résolu

Dans les fonctions `def wavacc(self, w):`, `def accord(self):`, `def radio(self):`, `def audio(self):`.<br>
~~Des paramétrages audio étaient incorrects malgré qu'il soit 
fonctionnels. Les messages d'erreurs ont été résolus en ajoutant
cette ligne : `# noinspection PyTypeChecker`~~<br>
- Problème du paramétrage audio caché



