from functools import partial

from hsr.config import HS_DATABASE_DIR, RESULTS_DIR, NETWORK_PARAMETERS_DIR
from hsr.file_io.file_io_pickles import load_dataframe_from_pickle_0
from hsr.hs_retrievers.config import RESULTS_FILENAME_EXTENSION
from hsr.hs_retrievers.hs_code_retriever_0 import hs_search_0
from hsr.hsdb.db_reader import get_number_of_records
from hsr.hsdb.metadata import get_hs_db_name, get_hs_db_characters_type
from hsr.neural_networks_mxnet.config import NETWORK_PARAMETERS_FILENAME_EXTENSION
from hsr.neural_networks_mxnet.net import get_nn_for_prediction
from hsr.prediction.predictor_mxnet import predictor_0
from hsr.preprocessing.config import HS_DB_FILENAME_EXTENSION


def hs_search(countries_metadata, query, country_index, return_results=False):
    dbn = get_hs_db_name(countries_metadata, country_index)
    db_tt = get_hs_db_characters_type(countries_metadata, country_index)
    db_fn = HS_DATABASE_DIR + dbn + HS_DB_FILENAME_EXTENSION
    n = get_number_of_records(db_fn)
    params_fn = NETWORK_PARAMETERS_DIR + dbn + NETWORK_PARAMETERS_FILENAME_EXTENSION
    net = get_nn_for_prediction(n, params_fn)
    pred = partial(predictor_0, net)
    res_fn = RESULTS_DIR + dbn + RESULTS_FILENAME_EXTENSION
    data = load_dataframe_from_pickle_0(db_fn)
    res = hs_search_0(data, pred, db_tt, query, res_fn, return_results)
    if return_results:
        return res
