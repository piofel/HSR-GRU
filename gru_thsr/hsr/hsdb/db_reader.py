import pandas as pd

from hsr.preprocessing.config import HS_DB_CODE_COLUMN_INDEX
from hsr.preprocessing.config import HS_DB_DESCRIPTION_COLUMN_INDEX


def get_dataframe(database_filename):
    return pd.read_pickle(database_filename)


def get_hs_code(database_filename, index):
    data = get_dataframe(database_filename)
    return data.iat[index, HS_DB_CODE_COLUMN_INDEX]


def get_hs_description(database_filename, index):
    data = get_dataframe(database_filename)
    return data.iat[index, HS_DB_DESCRIPTION_COLUMN_INDEX]


def get_number_of_records(database_filename):
    data = get_dataframe(database_filename)
    (n, _) = data.shape
    return n
