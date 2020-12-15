import pandas as pd
from scipy.stats import skew
from sklearn.model_selection import train_test_split
from loguru import logger

from config import *


class FeatEngineering(object):

    def __init__(self, run_mode: str = ""):
        self.run_mode = run_mode if len(run_mode) > 0 else config["run_mode"]
        self.skewness_threshold = config["skewness_threshold"]
        self.fill_nan_approach = config["fill_nan_approach"]
        self.feature_cols = config["feature_col"]
        self.target_col = config["native_target_col"]
        self.final_feature_col = config['final_feature_col']
        self.pickle_folder = config["model_folder"]
        if self.run_mode == RUN_MODE.TRAIN.value:
            self.test_train_split = config["test_train_split_ratio"]
        logger.info(f"** doing feature engineering")

    def do_feature_engineering(self, pdf: pd.DataFrame):
        """
        """
        logger.info("! start feature engineering !")
        if self.run_mode == RUN_MODE.TRAIN.value:
            self.checkSkewness(pdf=pdf)
            pdf = self.dealWithNan(pdf=pdf)
            pdf = self.uniteFeatureColumns(pdf=pdf)
            x_train, y_train, x_test, y_test = self.split_test_train(pdf=pdf)
            res = [x_train, y_train, x_test, y_test]
        elif self.run_mode == RUN_MODE.PREDICT.value:
            res = self.uniteFeatureColumns(pdf=pdf)
        else:
            raise Exception(" Selected RUN_MODE is not correct!...")

        logger.info(f"** FINISHED feature engineering!")

        return res

    def checkSkewness(self, pdf: pd.DataFrame):
        """
        To balance the target categories.
        """
        pdf_count = pdf.groupby([self.target_col]).size().to_frame(name="counts").reset_index()
        skewness = skew(pdf_count.values[:, 1])
        if_skewed = True if abs(skewness) > self.skewness_threshold or skewness==np.nan else False
        if if_skewed:
            logger.warning("! Data is skewed. down-sampling or up-sampling is recommended !")

    def dealWithNan(self, pdf: pd.DataFrame):
        """
        """
        if self.fill_nan_approach == "empty_string":
            pdf = pdf.fillna(value='')
        elif self.fill_nan_approach == "drop":
            pdf = pdf.dropna()
        else: 
            logger.ERROR("! selected Nan handdling approach is not valid !")
        return pdf

    def uniteFeatureColumns(self, pdf: pd.DataFrame):
        pdf[self.final_feature_col] = pdf[self.feature_cols].agg(' '.join, axis=1)
        return pdf

    def split_test_train(self, pdf: pd.DataFrame):
        """
        Returns: x_train, y_train, x_test, y_test
        """
        x_train, x_test, y_train, y_test = train_test_split(pdf[[self.final_feature_col]], pdf[self.target_col], test_size=self.test_train_split, random_state=0)
        return x_train, y_train, x_test, y_test
