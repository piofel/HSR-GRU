from hsr.hs_retrievers.hs_code_retriever_1 import hs_search
from hsr.hsdb.metadata import get_metadata


def search_hs_codes(query, country_index):
    hs_search(get_metadata(), query, country_index)
