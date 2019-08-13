from random import shuffle

import pandas as pd

from hsr.file_io.file_io_json import save
from hsr.hsdb.db_reader import get_number_of_records, get_hs_code
from hsr.hsdb.metadata import get_database_filename, get_metadata

COUNTRY_INDEX = 37
NUMBER_OF_PAIRS = 1000


def select_hscodes():
    hsc = []
    m = get_metadata()
    dbn = get_database_filename(m, COUNTRY_INDEX)
    n = get_number_of_records(dbn)
    indices = [i for i in range(n)]
    shuffle(indices)
    indices = indices[0:NUMBER_OF_PAIRS]
    for i in indices:
        hsc.append(get_hs_code(dbn, i))
    df = pd.DataFrame(hsc)
    save(df, "~/Documents/hscodes_for_evaluation.json")

