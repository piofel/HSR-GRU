from mxnet.gluon import nn, rnn

from hsr.file_io.file_io_mxnet_params import load_params

HIDDEN_SIZE = 256
RNN_DROPOUT = 0.5
NUM_RECURRENT_LAYERS = 1
RNN_TYPE = rnn.GRU


def get_nn_for_prediction(num_out_channels, network_params_filename):
    net = get_bare_nn(num_out_channels)
    return load_params(net, network_params_filename)


def get_nn_for_training(num_out_channels):
    net = get_bare_nn(num_out_channels)
    net.initialize()
    return net


def get_bare_nn(num_out_channels):
    net = nn.Sequential()
    net.add(
        RNN_TYPE(HIDDEN_SIZE, NUM_RECURRENT_LAYERS, dropout=RNN_DROPOUT),
        nn.Lambda(lambda x: x[-1, :, :]),
        nn.Dense(num_out_channels)
    )
    return net
