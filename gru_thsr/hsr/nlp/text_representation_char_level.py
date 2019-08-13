import numpy as np

from hsr.config import VERBOSITY
from hsr.nlp.config import CHAR_LEXICON

characters_without_representation = []


def get_text_representation_char_level(text):
    tl = len(text)
    nc = len(CHAR_LEXICON)
    r = np.zeros(shape=(tl, 1, nc))
    for i in range(tl):
        not_found = True
        for j in range(nc):
            if text[i] == CHAR_LEXICON[j]:
                r[i, 0, j] = 1.0
                not_found = False
                break
        if not_found & (VERBOSITY > 0):
            no_representation_msg(text[i])
    return r


def no_representation_msg(char):
    global characters_without_representation
    if char not in characters_without_representation:
        characters_without_representation.append(char)
        print('Warning: the character "%s" has no numerical representation.' % char)
