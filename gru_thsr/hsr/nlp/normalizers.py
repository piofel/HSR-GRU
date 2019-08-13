import pypinyin
import unicodedata

from hsr.config import VERBOSITY
from hsr.preprocessing.config import CHINESE_TEXT_LABEL
from hsr.preprocessing.config import ENGLISH_TEXT_LABEL
from hsr.preprocessing.config import ROMAN_TEXT_LABEL


def normalize_1(text_type, text):
    if (text_type == ROMAN_TEXT_LABEL) | (text_type == ENGLISH_TEXT_LABEL):
        text = roman_text_normalization(text)
    elif text_type == CHINESE_TEXT_LABEL:
        text = chinese_text_normalization(text)
    else:
        if VERBOSITY > 0:
            print("Incorrect text type.")
    return text


def roman_text_normalization(text):
    text = unicode_to_ascii(text)
    text = text.lower()
    return text


def chinese_text_normalization(text):
    pt = pypinyin.pinyin(text, style=pypinyin.Style.TONE2)
    pt = [i[0] for i in pt]
    text = " ".join(pt)
    return text


def unicode_to_ascii(unicode_string):
    return "".join(
        c for c in unicodedata.normalize("NFD", unicode_string)
        if unicodedata.category(c) != "Mn"
    )
