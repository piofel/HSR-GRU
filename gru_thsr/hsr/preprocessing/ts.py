from mxnet import nd

from hsr.file_io.file_io_txt import load_int
from hsr.preprocessing.config import NUM_BATCHES_FILENAME, FEATURES_FILENAME, MXNET_NDARRAY_FILENAME_EXTENSION, \
    TARGETS_FILENAME


def get_number_of_batches(training_set_dir):
    return load_int(training_set_dir + NUM_BATCHES_FILENAME)


def load_features(training_set_dir, batch_no):
    """

    :type training_set_dir: str
    :type batch_no: int
    """
    return nd.load(training_set_dir + FEATURES_FILENAME + str(batch_no) + MXNET_NDARRAY_FILENAME_EXTENSION)[0]


def load_targets(training_set_dir, batch_no):
    """

    :type training_set_dir: str
    :type batch_no: int
    """
    return nd.load(training_set_dir + TARGETS_FILENAME + str(batch_no) + MXNET_NDARRAY_FILENAME_EXTENSION)[0]


def save_features(training_set_dir, batch_no, numpy_ndarray):
    mxnet_array = nd.array(numpy_ndarray)
    nd.save(training_set_dir + FEATURES_FILENAME + str(batch_no) + MXNET_NDARRAY_FILENAME_EXTENSION, mxnet_array)


def save_target(training_set_dir, batch_no, category_no):
    mxnet_array = nd.array([[category_no]])
    nd.save(training_set_dir + TARGETS_FILENAME + str(batch_no) + MXNET_NDARRAY_FILENAME_EXTENSION, mxnet_array)


def load_whole_training_set(training_set_dir, data_loader):
    number_of_batches = get_number_of_batches(training_set_dir)
    al = []
    for i in range(number_of_batches):
        al.append(data_loader(training_set_dir, i))
    return al
