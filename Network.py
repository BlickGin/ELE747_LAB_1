import numpy as np
from Couches import *
from random import randint


class Network(object):
    def __init__(self):
        self.name = ""
        self.nb_unit_par_couche = []
        self.nb_couches = 0
        self.couches = []
        self.inputs = []
        self.outputs = []
        self.acti_type = ''
        self.error_count = []
        self.datafile = ""

    def setup(self):
        self.nb_couches = int(input("Nombre de couches : "))
        for i in range(self.nb_couches + 1):
            if i == 0:
                self.nb_unit_par_couche += [int(input("Nombre d'entrées : "))]
            else:
                if i is self.nb_couches:
                    self.nb_unit_par_couche += [int(input("Nombre d'unités à la couche " + str(i) + "(Sortie) : "))]
                else:
                    self.nb_unit_par_couche += [int(input("Nombre d'unités à la couche " + str(i) + " : "))]

    def init(self):
        # initialisation des couches
        for i in range(self.nb_couches):
            self.couches.append([])

        # Création des unités dans chaque couche
        for i in range(self.nb_couches):
            c = Couche(self.nb_unit_par_couche[i + 1], self.nb_unit_par_couche[i], self.acti_type)
            self.couches[i] += c.build()

        for i in range(self.nb_couches):  # Passe a chaque couche
            for j in range(self.nb_unit_par_couche[i + 1]):  # Passe par chaque unité de cette couche
                for k in range(self.nb_unit_par_couche[i] + 1):
                    weight_val = randint(-5, 5)
                    self.couches[i][j].weights[k] = float(weight_val)

    def predict(self):
        for j in range(self.nb_unit_par_couche[1]):  # Passe par chaque unité de la 1ere couche
            self.couches[0][j].predict(self.inputs)

        for i in range(self.nb_couches - 1):  # Passe par chaque couche en partant de la 2e
            out_prev_couche = []  # Liste pour stocker le valeurs des sorties précédentes
            for j in range(self.nb_unit_par_couche[i + 1]):
                out_prev_couche += [self.couches[i][j].acti]

            for k in range(self.nb_unit_par_couche[i + 2]):  # Passe par chaque unité de la couche
                self.couches[i + 1][k].predict(out_prev_couche)

    def train(self):
        for i in range(self.nb_couches):
            c = self.nb_couches - i
            delta = 0
            try:
                delta_next = np.zeros(self.nb_unit_par_couche[c + 1])
            except IndexError:
                delta_next = None

            prev_input = np.zeros(self.nb_unit_par_couche[c - 1])

            for j in range(self.nb_unit_par_couche[c]):
                if delta_next is not None:
                    weight_next = np.zeros(self.nb_unit_par_couche[c + 1])
                    for k in range(self.nb_unit_par_couche[c + 1]):
                        delta_next[k] = self.couches[c][k].delta
                        weight_next[k] = self.couches[c][k].weights[j + 1]

                else:
                    weight_next = None

                try:
                    desired_output = self.outputs[j]
                except IndexError:
                    desired_output = 0

                delta = self.couches[c-1][j].train(self.couches[c-1][j].acti, desired_output, delta_next, weight_next)

        for i in range(self.nb_couches):
            prev_input = [1]
            for j in range(self.nb_unit_par_couche[i + 1]):
                for k in range(self.nb_unit_par_couche[i]):
                    if i is 0:
                        prev_input.append(self.inputs[k])
                    else:
                        prev_input.append(self.couches[i - 1][k].acti)

                w = self.couches[i][j].update_weights(prev_input)

                # print("Poids couche " + str(i) + " / unité " + str(j) + " : " + str(w))
