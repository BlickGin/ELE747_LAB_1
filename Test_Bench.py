from Network import Network
from Defines import *

Test_Net = Network()

Test_Net.setup()

Test_Net.init()
Test_Net.acti_type = ACTI_TYPE_SIGMOID
Test_Net.train()