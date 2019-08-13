import pandas as pd

from hsr.config import PICKLE_PROTOCOL


def load_dataframe_from_pickle_0(pickle_filename):
    data = pd.read_pickle(pickle_filename)
    return data


def save_dataframe_to_pickle_0(pickle_filename, dataframe):
    dataframe.to_pickle(pickle_filename, protocol=PICKLE_PROTOCOL)
