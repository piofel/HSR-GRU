import pandas as pd


ORIENT = 'index'


def load(filename):
    return pd.read_json(filename, orient=ORIENT, dtype=False)


def save(dataframe, filename):
    dataframe.to_json(filename, orient=ORIENT)
