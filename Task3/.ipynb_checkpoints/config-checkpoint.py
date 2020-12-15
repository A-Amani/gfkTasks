from const import *

config = {
    "run_mode" : RUN_MODE.TRAIN.value,
    "model_selection":  MODEL.SVM.value,
    "model_folder": MODEL_FOLDER,
    "source_data": 'data/testset_C.csv',
    "mandatory_cols": MADATORY_FEATURE_COLS + [MADATORY_TARGET_COL],
    "test_train_split_ratio": 0.3,
    "skewness_threshold": 0.4,
    "mandatory_cols": MADATORY_FEATURE_COLS, #only change this if new model proves otherwise,
    "prediction_col": PREDITION_COL_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data_source_native_cols": DATA_SOURCE_COLS,
    "seperator": SEPERATOR,
    "native_target_col": MADATORY_TARGET_COL,
    "feature_col": USE_FEATURE_COLS,
    "mandatory_feature_col": MADATORY_FEATURE_COLS,
    "final_feature_col": FINAL_FEATURE_COLS,
    "fill_nan_approach": FILL_NAN_APPROACH
}