from hsr.config import TRAINING_SETS_MXNET_DIR
from hsr.hsdb.metadata import get_hs_db_name, get_metadata
from hsr.neural_networks_mxnet.net import get_nn_for_training
from hsr.preprocessing.ts import load_features


def test_0():
    countries_metadata = get_metadata()
    nm = get_hs_db_name(countries_metadata, 161)
    ts_dir = TRAINING_SETS_MXNET_DIR + nm + '/'
    feat = load_features(ts_dir, 0)
    net = get_nn_for_training(1024)
    print('TEST: ' + str(net(feat).shape))
