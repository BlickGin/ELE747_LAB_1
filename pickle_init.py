from Network import *
from Gui import  *
from save_load import *
from Defines import *
import pickle

dict_of_networks = {}
name = "Test Network"
net = Network()
net.nb_unit_par_couche = [2, 2, 1]
net.nb_couches = 2
net.acti_type = ACTI_TYPE_SIGMOID
net.name = name

net.init()

fname = "Network_1.pkl"
dict_of_networks[fname] = name
save(net, fname)
save(dict_of_networks, 'Network_List.pkl')