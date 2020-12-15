from enum import Enum

import numpy as np

# run mode
class RUN_MODE(Enum):
    TRAIN   = "train"
    PREDICT = "predict"


# training/prediction model seletion
class MODEL(Enum):
    KNN = "knn"
    SVM = "svm"
    LR = "logistic_regression"
    NB = "naive_bayes"


# prediction-related mandatory cols:
MADATORY_FEATURE_COLS = ["main_text"]
MADATORY_TARGET_COL = "productgroup"
USE_FEATURE_COLS = ['main_text', 'add_text', 'manufacturer']
FINAL_FEATURE_COLS = "text"


DATA_SOURCE_COLS = ['id', 'productgroup', 'main_text', 'add_text', 'manufacturer']
SEPERATOR = ";"
PREDITION_COL_NAME = "productgroup"
OUTPUT_FILE_NAME = "prediction.csv"

MODEL_FOLDER = "saved_models"
FILL_NAN_APPROACH = "empty_string" #drop