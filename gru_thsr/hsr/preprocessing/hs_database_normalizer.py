import pandas as pd

import hsr.file_io.file_manager as fm
from hsr.config import VERBOSITY
from hsr.file_io.file_io_pickles import save_dataframe_to_pickle_0
from hsr.preprocessing.config import HS_DB_COLUMN_NAMES


def convert_raw_data_to_internal_db_0(raw_db_filename, new_db_filename, save_to_excel=False):
    hs_code_col_index = 0
    hs_desc_col_index = 1
    header_height = 4
    db = pd.read_excel(raw_db_filename, header=header_height, dtype="object")
    (n, _) = db.shape
    records = []
    for i in range(n):
        hs_code = db.iat[i, hs_code_col_index]
        hs_desc = db.iat[i, hs_desc_col_index]
        records.append([hs_code, hs_desc])
    df = pd.DataFrame(records, columns=HS_DB_COLUMN_NAMES)
    save_dataframe_to_pickle_0(new_db_filename, df)
    xlf = new_db_filename.split(".")[0] + ".xlsx"
    if save_to_excel:
        df.to_excel(xlf)
    else:
        fm.safely_remove_file(xlf)
    if VERBOSITY > 0:
        print('Internal database has been created.')
