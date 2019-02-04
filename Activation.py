import numpy as np
import math
from Defines import *


########################################################################################################################
# Fonction d'activation (Si un type d'acti  non défini est passé, utilise la Step)


def activate(type, input_sum):
    if type is ACTI_TYPE_SIGMOID:
        acti = 1 / (1 + np.exp(-input_sum))

    elif type is ACTI_TYPE_TANH:
        acti = np.tanh(input_sum)

    elif type is ACTI_TYPE_SIN:
        acti = np.sin(input_sum)

    elif type is ACTI_TYPE_STEP:
        if input_sum < 0:
            acti = 0
        else:
            acti = 1

    elif type is ACTI_TYPE_RAMP:
        acti = input_sum

    elif type is ACTI_TYPE_RELU:
        if input_sum < 0:
            acti = 0
        else:
            acti = input_sum

    elif type is ACTI_TYPE_GAUSS:
        acti = np.exp(-(input_sum ^ 2))

    else:
        if input_sum < 0:
            acti = 0
        else:
            acti = 1

    return acti


def prim_activate(type, input_sum):
    if type is ACTI_TYPE_SIGMOID:
        acti = activate(ACTI_TYPE_SIGMOID, input_sum) * (1 - activate(ACTI_TYPE_SIGMOID, input_sum))

    elif type is ACTI_TYPE_TANH:
        acti = 1 - (activate(ACTI_TYPE_TANH, input_sum) ^ 2)

    elif type is ACTI_TYPE_SIN:
        acti = np.cos(input_sum)

    elif type is ACTI_TYPE_STEP:
        acti = 0

    elif type is ACTI_TYPE_RAMP:
        acti = 1

    elif type is ACTI_TYPE_RELU:
        if input_sum < 0:
            acti = 0
        else:
            acti = 1

    elif type is ACTI_TYPE_GAUSS:
        acti = -2 * input_sum * np.exp(-(input_sum ^ 2))

    else:
        acti = 1

    return acti
