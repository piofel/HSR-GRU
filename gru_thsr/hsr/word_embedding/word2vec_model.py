from multiprocessing import cpu_count

from gensim.models.word2vec import Word2Vec

from hsr.config import HG_HS_CORPUS_DIR, WORD_EMBEDDING_DIR, VERBOSITY
from hsr.homogenous_hs_corpus.config import CORPUS_FILENAME
from hsr.word_embedding.config import WORD_VECTOR_DIMENSIONALITY, WORD_EMBEDDING_FILENAME
from hsr.nlp.text_representation_word_level import reinint_word_embedding


def generate_model():
    cpf = HG_HS_CORPUS_DIR + CORPUS_FILENAME
    model = Word2Vec(corpus_file=cpf, size=WORD_VECTOR_DIMENSIONALITY, min_count=0, workers=cpu_count())
    model.save(WORD_EMBEDDING_DIR + WORD_EMBEDDING_FILENAME)
    reinint_word_embedding()
    if VERBOSITY > 0:
        print('Word2Vec model has been generated.')
