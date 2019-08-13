from random import shuffle

import pandas as pd

from hsr.hsdb.db_reader import get_number_of_records, get_dataframe
from hsr.hsdb.metadata import get_database_filename, get_metadata

COUNTRY_INDEX = 161
NUMBER_OF_RECORDS = 100


def select_records():
    records = []
    m = get_metadata()
    db_fn = get_database_filename(m, COUNTRY_INDEX)
    sdf = get_dataframe(db_fn)
    n = get_number_of_records(db_fn)
    indices = [i for i in range(n)]
    shuffle(indices)
    indices = indices[0:NUMBER_OF_RECORDS]
    for i in indices:
        records.append(sdf.iloc[[i]])
    df = pd.concat(records, ignore_index=True)
    df.to_excel("~/Documents/experimental_database.xlsx")
