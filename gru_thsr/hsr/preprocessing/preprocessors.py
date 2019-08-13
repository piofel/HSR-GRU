from hsr.config import HS_DATABASE_DIR
from hsr.config import RAW_HS_DATABASE_DIR
from hsr.config import SAVE_HS_DATABASES_TO_EXCEL
from hsr.hsdb.metadata import get_hs_db_name
from hsr.preprocessing.config import HS_DB_FILENAME_EXTENSION
from hsr.preprocessing.config import RAW_HS_DB_FILENAME_EXTENSION
from hsr.preprocessing.hs_database_normalizer import convert_raw_data_to_internal_db_0
from hsr.preprocessing.ts_gen_mxnet import generate_training_set


def batch_preprocess(countries_metadata, countries_indices):
    batch_preprocess_step_0(countries_metadata, countries_indices)
    batch_preprocess_step_1(countries_metadata, countries_indices)


def preprocess_step_0(countries_metadata, country_index):  # for a single country
    dbn = get_hs_db_name(countries_metadata, country_index)
    raw_db_fn = RAW_HS_DATABASE_DIR + dbn + RAW_HS_DB_FILENAME_EXTENSION
    new_db_fn = HS_DATABASE_DIR + dbn + HS_DB_FILENAME_EXTENSION
    convert_raw_data_to_internal_db_0(raw_db_fn, new_db_fn, SAVE_HS_DATABASES_TO_EXCEL)


def preprocess_step_1(countries_metadata, country_index):
    generate_training_set(countries_metadata, country_index)


def batch_preprocess_step_0(countries_metadata, countries_indices):  # for selected countries
    for i in countries_indices:
        preprocess_step_0(countries_metadata, i)


def batch_preprocess_step_1(countries_metadata, countries_indices):  # for selected countries
    for i in countries_indices:
        preprocess_step_1(countries_metadata, i)
