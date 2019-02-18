def save(net_to_save, filename):
    with open(filename, 'wb') as output:
        pickle.dump(net_to_save, output, pickle.HIGHEST_PROTOCOL)


def load(filename):
    with open(filename, 'rb') as input:
        net_to_load = pickle.load(input)
    return net_to_load

