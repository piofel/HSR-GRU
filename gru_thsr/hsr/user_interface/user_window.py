from functools import partial

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, \
    QTableWidget, QTableWidgetItem, QGridLayout

from hsr.config import RESULTS_DIR
from hsr.config import SOFTWARE_NAME
from hsr.config import SOFTWARE_VERSION
from hsr.file_io import file_io_json
from hsr.hs_retrievers.config import RESULTS_FILENAME_EXTENSION
from hsr.hs_retrievers.hs_code_retriever_1 import hs_search
from hsr.hsdb.metadata import get_metadata, countries_names, get_hs_db_name
from hsr.preprocessing.config import HS_RESULTS_RELEVANCE_LABEL
from hsr.user_interface.shared import country_selector_0, teggs_logo_0, grid_group_0

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768


def user_window_0():
    qd = QDialog()
    qd.setWindowTitle(SOFTWARE_NAME + ' ' + SOFTWARE_VERSION)
    qd.setGeometry(10, 10, WINDOW_WIDTH, WINDOW_HEIGHT)
    qd.countries_metadata = get_metadata()
    cn = countries_names(qd.countries_metadata)
    cs = country_selector_0(cn, init_index=161)
    qd.countries_combo = cs[1][0]
    csp = grid_group_0(cs, 'Country selector')
    dp = description_panel_0()
    qd.query_edit = dp[1][0]
    dpp = grid_group_0(dp, 'Commodity description')
    sp = search_panel_0()
    qd.search_button = sp[0][0]
    qd.clear_query_button = sp[0][1]
    qd.clear_results_button = sp[0][2]
    spp = grid_group_0(sp, 'Search tools')
    rp = result_panel_0()
    qd.results_label = rp[0][0]
    qd.table = rp[1][0]
    rpp = grid_group_0(rp, 'Results')
    widgets_0 = [[csp, teggs_logo_0()], [dpp], [spp]]
    group_0 = grid_group_0(widgets_0)
    layout = QGridLayout()
    layout.addWidget(group_0, 0, 0)
    layout.addWidget(rpp, 1, 0)
    qd.setLayout(layout)
    qd.query_edit.setFocus()
    qd.search_button.clicked.connect(partial(search_0, qd))
    qd.clear_query_button.clicked.connect(partial(clear_description, qd))
    qd.clear_results_button.clicked.connect(partial(clear_results, qd))
    return qd


def search_0(user_window):
    text = user_window.query_edit.text()
    if text == '':
        user_window.results_label.setText('<font color=red>Please enter the description.</font>')
    else:
        ci = user_window.countries_combo.currentIndex()
        hs_search(user_window.countries_metadata, text, ci)
        cid = get_hs_db_name(user_window.countries_metadata, ci)
        results = file_io_json.load(RESULTS_DIR + cid + RESULTS_FILENAME_EXTENSION)
        (nr, nc) = results.shape
        user_window.table.setRowCount(nr)
        user_window.table.setColumnCount(nc)
        cols = results.columns.values
        if nr > 1:
            user_window.results_label.setText('<font color=red>There is more than one result. '
                                              'Please provide more details for disambiguation.</font>')
        elif nr == 0:
            user_window.results_label.setText('<font color=red>No results.</font>')
        else:
            user_window.results_label.setText('The result:')
        for j in range(nc):
            head_item = QTableWidgetItem(cols[j])
            user_window.table.setHorizontalHeaderItem(j, head_item)
        for i in range(nr):
            for j in range(nc):
                # r = unicode(results.iat[i, j]) for Python 2 only
                if cols[j] == HS_RESULTS_RELEVANCE_LABEL:
                    r = str("%.2f" % results.iat[i, j])
                else:
                    r = str(results.iat[i, j])
                item = QTableWidgetItem(r)
                user_window.table.setItem(i, j, item)
        user_window.table.setColumnWidth(0, WINDOW_WIDTH - 250)
        for j in range(1, nc):
            user_window.table.resizeColumnToContents(j)
        for i in range(nr):
            user_window.table.resizeRowToContents(i)


def clear_results(user_window):
    user_window.table.clear()
    user_window.results_label.setText('')


def clear_description(user_window):
    user_window.query_edit.setText('')
    user_window.query_edit.setFocus()


def description_panel_0():
    label = QLabel('Please provide a commodity description:')
    edit = QLineEdit()
    return [[label], [edit]]


def search_panel_0():
    space_size = 40
    space = ''
    for i in range(space_size):
        space += ' '
    space_label = QLabel(space)
    search_button = QPushButton('Search')
    clear_results_button = QPushButton('Clear results')
    clear_desc_button = QPushButton('Clear description')
    search_tools = [[search_button, clear_desc_button, clear_results_button, space_label]]
    return search_tools


def result_panel_0():
    results_label = QLabel('')
    table = QTableWidget()
    return [[results_label], [table]]
