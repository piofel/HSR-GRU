from os import linesep

from hsr.hsdb.metadata import get_metadata, get_database_filename, get_number_of_countries, get_hs_db_characters_type
from hsr.hsdb.db_reader import get_number_of_records, get_hs_description
from hsr.file_io.file_io_txt import append_str_to_txt_file
from hsr.file_io.file_manager import safely_remove_file
from hsr.preprocessing.config import ENGLISH_TEXT_LABEL
from hsr.homogenous_hs_corpus.config import CORPUS_FILENAME
from hsr.config import HG_HS_CORPUS_DIR, VERBOSITY
from hsr.nlp.normalizers import normalize_1


def select_databases_for_corpus(countries_metadata):
    indices = []
    n = get_number_of_countries(countries_metadata)
    for i in range(n):
        if get_hs_db_characters_type(countries_metadata, i) == ENGLISH_TEXT_LABEL:
            indices.append(i)
    return indices


def create_corpus():
    md = get_metadata()
    countries_indices = select_databases_for_corpus(md)
    corp_pfn = HG_HS_CORPUS_DIR + CORPUS_FILENAME
    safely_remove_file(corp_pfn)
    for i in countries_indices:
        corp = linesep + get_corpus_single_db(md, i)
        append_str_to_txt_file(corp_pfn, corp)
    if VERBOSITY > 0:
        print('Corpus has been generated.')


def get_corpus_single_db(countries_metadata, country_index):
    corp = ''
    dbf = get_database_filename(countries_metadata, country_index)
    tt = get_hs_db_characters_type(countries_metadata, country_index)
    n = get_number_of_records(dbf)
    for i in range(n):
        desc = get_hs_description(dbf, i)
        desc = normalize_1(tt, desc)
        corp += desc + linesep
    return corp
