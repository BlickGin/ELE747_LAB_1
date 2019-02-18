from src.Activation import *


class Unit(object):
    nb_unit = 0

    def __init__(self, nb_input, couche, acti_type, learning_rate=0.5):
        self.nb_input = nb_input
        self.couche = couche
        self.acti_type = acti_type
        self.learning_rate = learning_rate
        self.weights = np.zeros(nb_input + 1)
        self.summation = 0
        self.delta = 0
        self.acti = 0

        Unit.nb_unit += 1

    def unit_info(self):
        print("Appartient à la couche : ", self.couche)
        print("nb d'entrées : ", self.nb_input)
        print("poids : ", self.weights)

    def predict(self, inputs):
        self.summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Multiplie les entrées avec le poids corresp.
        activation = activate(self.acti_type, self.summation)
        self.acti = activation

        return activation

    def train(self, real_output, desired_output, delta_next, weight_next):
        acti_prim = prim_activate(self.acti_type, self.summation)

        if delta_next is None:
            self.delta = (desired_output - real_output) * acti_prim
        else:
            self.delta = acti_prim * np.sum(np.multiply(delta_next, weight_next))

        return self.delta

    def update_weights(self, prev_input):
        for i in range(len(self.weights)):
            delta_weight = (self.learning_rate * self.delta * prev_input[i])
            self.weights[i] = self.weights[i] + delta_weight

        return self.weights
