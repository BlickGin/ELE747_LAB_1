import numpy as np
from Network import *
from Defines import *
from Dataset import *
from random import shuffle


def save(net_to_save):
    with open('network_data.pkl', 'wb') as output:
        pickle.dump(net_to_save, output, pickle.HIGHEST_PROTOCOL)


def load():
    with open('company_data.pkl', 'rb') as input:
        net_to_load = pickle.load(input)
    return net_to_load

