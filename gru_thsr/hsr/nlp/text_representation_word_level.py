import numpy as np
from gensim.models.word2vec import Word2Vec

from hsr.config import WORD_EMBEDDING_DIR, VERBOSITY
from hsr.word_embedding.config import WORD_EMBEDDING_FILENAME, WORD_VECTOR_DIMENSIONALITY

word_vectors = Word2Vec.load(WORD_EMBEDDING_DIR + WORD_EMBEDDING_FILENAME).wv
tokens_without_representation = []


def get_text_representation_word_level(text):
    text = text.split()
    num_tokens = len(text)
    rep = np.zeros(shape=(num_tokens, 1, WORD_VECTOR_DIMENSIONALITY))
    index = 0
    for token in text:
        if token in word_vectors.vocab:
            npy_vec = word_vectors[token]
            rep[index, 0, :] = npy_vec
        else:
            if VERBOSITY > 0:
                no_representation_msg(token)
        pass
        index += 1
    return rep


def no_representation_msg(token):
    global tokens_without_representation
    if token not in tokens_without_representation:
        tokens_without_representation.append(token)
        print('The token "%s" has no vector representation.' % token)


def reinint_word_embedding():
    global word_vectors
    word_vectors = Word2Vec.load(WORD_EMBEDDING_DIR + WORD_EMBEDDING_FILENAME).wv
