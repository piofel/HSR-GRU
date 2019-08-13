USERNAME = "td_laptop_0"
SOFTWARE_NAME = "TEGGS HS Retriever"
SOFTWARE_VERSION = "3.2.7"
RESOURCES_DIR = "hsr/resources/"
HS_DATABASE_DIR = RESOURCES_DIR + "hs_db/"
RESULTS_DIR = RESOURCES_DIR + "results/"
NETWORK_PARAMETERS_DIR = RESOURCES_DIR + "nets_params/"
EVALUATION_DIR = RESOURCES_DIR + "evaluation_sets/"
HG_HS_CORPUS_DIR = RESOURCES_DIR + "hg_hs_corpus/"
WORD_EMBEDDING_DIR = RESOURCES_DIR + "word_embedding/"
SAVE_HS_DATABASES_TO_EXCEL = True
VERBOSITY = 2
LENGTH_OF_HSCODES_COMMON_PART = 6
PICKLE_PROTOCOL = 2

if USERNAME == "shi_tianbao":
    RAW_HS_DATABASE_DIR = "your path here"
    TRAINING_SETS_MXNET_DIR = "your path here"
elif USERNAME == "tdhn_mjxu_1":
    RAW_HS_DATABASE_DIR = "/home/tdhn_mjxu_1/hs_codes/databases_1/"
    TRAINING_SETS_MXNET_DIR = "/home/tdhn_mjxu_1/training_sets_mxnet/"
elif USERNAME == "td_laptop_0":
    RAW_HS_DATABASE_DIR = "/home/piotr/main/dev/hs_databases/databases_1/"
    TRAINING_SETS_MXNET_DIR = "/home/piotr/Data/training_sets_mxnet/"
elif USERNAME == "piotrfelisiak":
    RAW_HS_DATABASE_DIR = "/home/piotrfelisiak/main/dev/hs_databases/databases_1/"
    TRAINING_SETS_MXNET_DIR = '/media/piotrfelisiak/Big Disc/training_sets_mxnet/'
else:
    print("Incorrect user name.")
