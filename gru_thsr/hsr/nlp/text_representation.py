from hsr.nlp.text_representation_char_level import get_text_representation_char_level
from hsr.nlp.text_representation_word_level import get_text_representation_word_level
from hsr.nlp.config import TEXT_EMBEDDING


def get_text_representation(text):
    if TEXT_EMBEDDING == 'char_level':
        return get_text_representation_char_level(text)
    elif TEXT_EMBEDDING == 'word_level':
        return get_text_representation_word_level(text)
    else:
        print('Incorrect representation type.')
