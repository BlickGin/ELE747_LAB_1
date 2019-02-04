import numpy as np
import math
from Unit import Unit


class Couche(object):
    nb_couche = 0

    def __init__(self, nb_unit, nb_unit_couche_prec, acti_type):
        self.nb_unit = nb_unit
        self.couche_id = Couche.nb_couche
        self.nb_unit_couche_prec = nb_unit_couche_prec
        self.acti_type = acti_type
        
        Couche.nb_couche += 1

    def couche_info(self):
        print("")

    def build(self):
        c = []
        for _ in range(self.nb_unit):
            c += [Unit(self.nb_unit_couche_prec, self.couche_id, self.acti_type)]

        return c
