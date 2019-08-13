from hsr.hsdb.metadata import get_metadata, get_database_filename
from hsr.hsdb.db_reader import get_hs_description


def test(rec_index):
    country_index = 37
    md = get_metadata()
    dbf = get_database_filename(md, country_index)
    desc = get_hs_description(dbf, rec_index)
    print(desc)
