def save_params(network, filename):
    network.save_parameters(filename)


def load_params(network, filename):
    network.load_parameters(filename)
    return network
