from hsr.dev_tools.training_tools_0 import training_tool_1
from hsr.evaluation.evaluator_0 import evaluate_1, alpha_score, epsilon_score
from hsr.hsdb.metadata import get_metadata
from hsr.preprocessing.preprocessors import batch_preprocess_step_0, \
    batch_preprocess_step_1
from hsr.user_interface.data_formatting import float_to_percent_str

# COUNTRIES_INDICES = [37, 144, 161, 188]  # [China, Poland, Singapore, USA]
COUNTRIES_INDICES = [161]  # [Singapore]
PREPROCESSING_STEP_0 = 0
PREPROCESSING_STEP_1 = 0
TRAINING = 1

countries_metadata = get_metadata()

if PREPROCESSING_STEP_0:
    batch_preprocess_step_0(countries_metadata, COUNTRIES_INDICES)
if PREPROCESSING_STEP_1:
    batch_preprocess_step_1(countries_metadata, COUNTRIES_INDICES)
if TRAINING:
    training_tool_1(countries_metadata, COUNTRIES_INDICES)
alpha = float_to_percent_str(evaluate_1(COUNTRIES_INDICES, alpha_score))
epsilon = float_to_percent_str(evaluate_1(COUNTRIES_INDICES, epsilon_score))
print("alpha-score: " + alpha + "%")
print("epsilon-score: " + epsilon + "%")
