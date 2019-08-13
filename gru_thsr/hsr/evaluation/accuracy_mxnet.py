def calculate_accuracy_0(output, label):
    """

    :type label: (batch, ) int32 ndarray
    :type output: (batch, num_output) float32 ndarray
    """
    acc = (output.argmax(axis=1) == label.astype('float32')).mean().asscalar()
    return acc
