import pandas as pd

from hsr.config import RESOURCES_DIR, LENGTH_OF_HSCODES_COMMON_PART
from hsr.hs_retrievers.hs_code_retriever_1 import hs_search
from hsr.hsdb.metadata import get_metadata

EVAL_SET_FILENAME = RESOURCES_DIR + "evaluation_sets/eval_set_Belarus_China.xlsx"
EVAL_SET_HEADER = 0


def evaluate_1(countries_indices, evaluation_function):
    nc = len(countries_indices)
    mean_score = sum(map(lambda i: evaluate_0(i, evaluation_function), countries_indices)) / nc
    return mean_score


def evaluate_0(country_index, evaluation_function):
    (nr, _) = EVAL_SET.shape
    return sum(scores(country_index, evaluation_function)) / nr


def read_eval_set():
    return pd.read_excel(EVAL_SET_FILENAME, header=EVAL_SET_HEADER, dtype='object')


EVAL_SET = read_eval_set()
METADATA = get_metadata()


def hs_search_e(query, country_index):
    return hs_search(METADATA, query, country_index, return_results=True)


def search_results(eval_set_record_index, country_index):
    return hs_search_e(EVAL_SET.iat[eval_set_record_index, 0], country_index)


def hs_compare(x, y):
    x = x[0:LENGTH_OF_HSCODES_COMMON_PART]
    y = y[0:LENGTH_OF_HSCODES_COMMON_PART]
    return x == y


def get_correct_hscode(eval_set_record_index):
    return str(EVAL_SET.iat[eval_set_record_index, 1])


def alpha_score(eval_set_record_index, country_index):
    correct = get_correct_hscode(eval_set_record_index)
    res = search_results(eval_set_record_index, country_index)
    (nr, _) = res.shape
    match = nr
    for i in range(nr):
        if hs_compare(res.iat[i, 0], correct):
            match = i
            break
    if match < 5:
        return 1.0 - 0.2 * match
    else:
        return 0.0


def epsilon_score(eval_set_record_index, country_index):
    correct = get_correct_hscode(eval_set_record_index)
    res = search_results(eval_set_record_index, country_index)
    (nr, _) = res.shape
    for i in range(nr):
        if hs_compare(res.iat[i, 0], correct):
            return 1.0
    return 0.0


def scores(country_index, evaluation_function):
    (nr, _) = EVAL_SET.shape
    scr = []
    for i in range(nr):
        scr.append(evaluation_function(i, country_index))
    return scr
