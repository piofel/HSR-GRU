import pandas as pd

from hsr.file_io import file_io_json
from hsr.nlp.normalizers import normalize_1
from hsr.nlp.text_representation import get_text_representation
from hsr.preprocessing.config import HS_RESULTS_RELEVANCE_LABEL

RESULT_SHOWING_THRESHOLD = 0.0  # range 0 ... 1
MAX_NUM_RESULTS = 5


def hs_search_0(dataframe, predictor, hs_db_text_type, text, results_filename, return_results):
    text = normalize_1(hs_db_text_type, text)
    r = get_text_representation(text)
    outputs = predictor(r)
    res = interpret_outputs_0(dataframe, outputs, results_filename, return_results)
    if return_results:
        return res


def interpret_outputs_0(dataframe, outputs, results_filename, return_result):
    (_, n) = outputs.shape
    indexed_relevance = []
    for i in range(n):
        indexed_relevance.append((i, outputs[0, i]))
    results = result_records_from_indexed_relevance(dataframe, indexed_relevance)
    if return_result:
        return results
    else:
        file_io_json.save(results, results_filename)


# indexed relevance == (dataframe_index,relevance)
def result_records_from_indexed_relevance(dataframe, indexed_relevance):
    result_indices = select_result_indices_0(indexed_relevance)
    results = []
    relevance_list = []
    for (index, relevance) in result_indices:
        results.append(dataframe.iloc[[index]])
        relevance_list.append(relevance)
    if results:
        results = pd.concat(results, ignore_index=True)
    else:
        results = pd.DataFrame(columns=dataframe.columns)
    relevance = pd.Series(relevance_list, index=results.index)
    results[HS_RESULTS_RELEVANCE_LABEL] = relevance
    return results


def select_result_indices_0(indexed_relevance):
    indexed_relevance = sorted(indexed_relevance, key=lambda ir: ir[1])
    result_indices = []
    i = 0
    while (indexed_relevance != []) & (i < MAX_NUM_RESULTS):
        (_, relevance) = indexed_relevance[-1]
        if relevance >= RESULT_SHOWING_THRESHOLD:
            e = indexed_relevance.pop()
            result_indices.append(e)
            i += 1
        else:
            break
    return result_indices
