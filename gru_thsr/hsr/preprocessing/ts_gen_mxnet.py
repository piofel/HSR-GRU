from hsr.config import TRAINING_SETS_MXNET_DIR, HS_DATABASE_DIR, VERBOSITY
from hsr.file_io.file_io_txt import save_int
from hsr.file_io.file_manager import refresh_dir
from hsr.hsdb.db_reader import get_number_of_records, get_hs_description
from hsr.hsdb.metadata import get_hs_db_characters_type, get_hs_db_name
from hsr.nlp.normalizers import normalize_1
from hsr.nlp.text_representation import get_text_representation
from hsr.preprocessing.config import HS_DB_FILENAME_EXTENSION, NUM_BATCHES_FILENAME, NUM_TRAINING_EXAMPLES_FILENAME
from hsr.preprocessing.hs_desc_replicator import replicate_hs_desc_0
from hsr.preprocessing.ts import save_features, save_target


def generate_training_set(countries_metadata, country_index):
    batch_no = 0
    example_no = 0
    text_type = get_hs_db_characters_type(countries_metadata, country_index)
    dbn = get_hs_db_name(countries_metadata, country_index)
    ts_dir = TRAINING_SETS_MXNET_DIR + dbn + '/'
    refresh_dir(ts_dir)
    db_fn = HS_DATABASE_DIR + dbn + HS_DB_FILENAME_EXTENSION
    n = get_number_of_records(db_fn)
    for k in range(n):
        desc = get_hs_description(db_fn, k)
        desc = normalize_1(text_type, desc)
        desc_list = replicate_hs_desc_0(desc)
        for d in desc_list:
            r = get_text_representation(d)
            save_features(ts_dir, batch_no, r)
            save_target(ts_dir, batch_no, k)
            batch_no += 1
            example_no += 1
    save_int(ts_dir + NUM_BATCHES_FILENAME, batch_no)
    save_int(ts_dir + NUM_TRAINING_EXAMPLES_FILENAME, example_no)
    if VERBOSITY > 0:
        print('Training set has been generated from "' + dbn + '" database.')
