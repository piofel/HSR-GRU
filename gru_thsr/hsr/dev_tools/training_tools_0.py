from hsr.config import TRAINING_SETS_MXNET_DIR, HS_DATABASE_DIR, NETWORK_PARAMETERS_DIR
from hsr.file_io.file_io_mxnet_params import save_params
from hsr.hsdb.db_reader import get_number_of_records
from hsr.hsdb.metadata import get_hs_db_name
from hsr.neural_networks_mxnet.config import NETWORK_PARAMETERS_FILENAME_EXTENSION
from hsr.neural_networks_mxnet.net import get_nn_for_training
from hsr.neural_networks_mxnet.training import train_0
from hsr.preprocessing.config import HS_DB_FILENAME_EXTENSION


def training_tool_1(countries_metadata, countries_indices):
    for i in countries_indices:
        training_tool_0(countries_metadata, i)


def training_tool_0(countries_metadata, country_index):
    nm = get_hs_db_name(countries_metadata, country_index)
    ts_dir = TRAINING_SETS_MXNET_DIR + nm + '/'
    db_fn = HS_DATABASE_DIR + nm + HS_DB_FILENAME_EXTENSION
    n = get_number_of_records(db_fn)
    net = get_nn_for_training(n)
    net = train_0(net, ts_dir)
    net_fn = NETWORK_PARAMETERS_DIR + nm + NETWORK_PARAMETERS_FILENAME_EXTENSION
    save_params(net, net_fn)
