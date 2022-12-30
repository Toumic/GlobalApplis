#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# Le vendredi 30 décembre 2022 (Commencement du script)
# GlobGamMicro : Construire les micro-intervalles sous-jacents à l'original[]

import inspect
from typing import Callable

# lineno() Pour consulter le programme grâce au suivi des print's
lineno: Callable[[], int] = lambda: inspect.currentframe().f_back.f_lineno


def commatic(comma):
    print(lineno(), 'comma:', comma)
