from mxnet import nd


def predictor_0(neural_network, features_npy, use_softmax=False):
    fmx = nd.array(features_npy)
    outputs = neural_network(fmx)
    if use_softmax:
        outputs = nd.softmax(outputs)
    outputs = outputs.asnumpy()
    return outputs
