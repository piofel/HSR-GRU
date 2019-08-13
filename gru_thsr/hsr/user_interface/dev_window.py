from functools import partial

from PyQt5.QtWidgets import QDialog, QPushButton, QLabel

from hsr.config import SOFTWARE_NAME, SOFTWARE_VERSION
from hsr.dev_tools.training_tools_0 import training_tool_0
from hsr.evaluation.evaluator_0 import evaluate_0, alpha_score, epsilon_score
from hsr.hsdb.metadata import get_metadata, \
    countries_names
from hsr.preprocessing.preprocessors import preprocess_step_0, preprocess_step_1
from hsr.user_interface.data_formatting import float_to_percent_str
from hsr.user_interface.shared import country_selector_0, grid_group_0, grid_layout_0, teggs_logo_0
from hsr.homogenous_hs_corpus.corpus import create_corpus
from hsr.word_embedding.word2vec_model import generate_model


def developer_window_0():
    qd = QDialog()
    qd.setWindowTitle(SOFTWARE_NAME + ' ' + SOFTWARE_VERSION + ' Developer tools')
    qd.countries_metadata = get_metadata()
    cn = countries_names(qd.countries_metadata)
    cs = country_selector_1(cn, 161)
    qd.countries_combo = cs[1][0]
    qd.country_index_label = cs[2][0]
    csp = grid_group_0(cs, 'Country selector')
    dt = dev_tools_0()
    qd.import_db_button = dt[0][0]
    qd.gen_ts_button = dt[0][1]
    qd.train_button = dt[0][2]
    dtp = grid_group_0(dt, 'Development tools for single database')
    et = eval_tools()
    qd.eval_button_alpha = et[0][0]
    qd.eval_label_alpha = et[0][1]
    qd.eval_button_epsilon = et[1][0]
    qd.eval_label_epsilon = et[1][1]
    etp = grid_group_0(et, 'Evaluation tools')
    wet = word_embedding_tools()
    qd.gen_corpus_button = wet[0][0]
    qd.gen_word_emb_button = wet[0][1]
    wetp = grid_group_0(wet, 'Word embedding tools')
    widgets = [[teggs_logo_0()],
               [csp],
               [dtp],
               [etp],
               [wetp]]
    layout = grid_layout_0(widgets)
    qd.setLayout(layout)
    qd.import_db_button.clicked.connect(partial(import_db, qd))
    qd.gen_ts_button.clicked.connect(partial(gen_ts, qd))
    qd.train_button.clicked.connect(partial(train, qd))
    qd.eval_button_alpha.clicked.connect(partial(evaluate_alpha, qd))
    qd.eval_button_epsilon.clicked.connect(partial(evaluate_epsilon, qd))
    qd.countries_combo.currentIndexChanged.connect(partial(set_country_index_label, qd))
    qd.gen_corpus_button.clicked.connect(create_corpus)
    qd.gen_word_emb_button.clicked.connect(generate_model)
    return qd


def country_selector_1(items, init_index, country_label='Please select a database:'):
    cs = country_selector_0(items, country_label, init_index)
    index_label = QLabel('Country index: ' + str(init_index))
    cs.append([index_label])
    return cs


def dev_tools_0():
    import_db_button = QPushButton('Import database')
    gen_ts_button = QPushButton('Generate training set')
    train_button = QPushButton('Train the network')
    return [[import_db_button, gen_ts_button, train_button]]


def eval_tools():
    eval_button_alpha = QPushButton('Evaluate \u03B1-score')
    eval_label_alpha = QLabel('')
    eval_button_epsilon = QPushButton('Evaluate \u03B5-score')
    eval_label_epsilon = QLabel('')
    return [[eval_button_alpha, eval_label_alpha],
            [eval_button_epsilon, eval_label_epsilon]]


def word_embedding_tools():
    gen_corpus_button = QPushButton('Generate HGHS corpus')
    gen_word_emb_button = QPushButton('Generate word embedding')
    return [[gen_corpus_button, gen_word_emb_button]]


def import_db(user_window):
    country_index = user_window.countries_combo.currentIndex()
    preprocess_step_0(user_window.countries_metadata, country_index)


def gen_ts(user_window):
    country_index = user_window.countries_combo.currentIndex()
    preprocess_step_1(user_window.countries_metadata, country_index)


def train(user_window):
    country_index = user_window.countries_combo.currentIndex()
    training_tool_0(user_window.countries_metadata, country_index)


def evaluate_alpha(user_window):
    country_index = user_window.countries_combo.currentIndex()
    user_window.eval_label_alpha.setText('\u03B1-score: ' +
                                         float_to_percent_str(evaluate_0(country_index, alpha_score)) + "%")


def evaluate_epsilon(user_window):
    country_index = user_window.countries_combo.currentIndex()
    user_window.eval_label_epsilon.setText('\u03B5-score: ' +
                                           float_to_percent_str(evaluate_0(country_index, epsilon_score)) + "%")


def set_country_index_label(user_window):
    country_index = user_window.countries_combo.currentIndex()
    user_window.country_index_label.setText('Country index: ' + str(country_index))
