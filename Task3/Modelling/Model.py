import os
from pathlib import Path
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pandas.core.series as pdSeries
from loguru import logger

from config import *


class Model(object):

    def __init__(self, run_mode: str = ""):
        self.run_mode = run_mode if len(run_mode) > 0 else config["run_mode"]

        self.model_folder = config["model_folder"]
        self.model_selection = config["model_selection"]
        self.model_file_name = f"{self.model_folder}/model.pkl"
        self.final_feature_col = config['final_feature_col']

        self.model = None
        
        if self.run_mode == RUN_MODE.PREDICT.value:
            self.prediction_col = config["prediction_col"]
            self.output_file_name = config["output_file_name"]
        logger.info(f"! do model {self.run_mode}, active model is {self.model_selection} !")

    def construct_preProcessing_pipline(self):
        descriptive_features_pipeline = Pipeline(steps=
            [
                ('CountVectorizer', CountVectorizer()),
                ('Tfidf', TfidfTransformer())
            ]
        )

        preprocessing_pipeline = ColumnTransformer(transformers=
            [
                ('preprocessing_pipeline',descriptive_features_pipeline, self.final_feature_col)
            ]
        )
        return preprocessing_pipeline

    def construct_classifier_pipline(self):
        if self.model_selection == 'svm': 
            classifier_pipline = SGDClassifier()
        elif self.model_selection == 'naive_bayes': 
            classifier_pipline = MultinomialNB()
        elif self.model_selection == 'knn': 
            classifier_pipline = KNeighborsClassifier()
        elif self.model_selection == 'logistic_regression': 
            classifier_pipline = LogisticRegression()

        return classifier_pipline

    def construct_model_pipline(self, preprocessing_pipeline, classifier_pipline):
        pipe = Pipeline(steps=
            [
                ('preprocessor', preprocessing_pipeline),
                ('classifier', classifier_pipline)
            ]
        )
        return pipe

    
    def run(self, data):
        if self.run_mode == RUN_MODE.TRAIN.value:
            x_train, y_train, x_test, y_test = data
            pp = self.construct_preProcessing_pipline()
            clf = self.construct_classifier_pipline()
            pipe = self.construct_model_pipline(pp,clf)
            self.model = pipe.fit(x_train, y_train)
            Model.save_model(model=self.model, file_name=self.model_file_name)
            logger.info(f"! saved model: {self.model_selection} to {self.model_file_name} !")

            self.evaluate_model(x_test, y_test, self.model)
                    
        if self.run_mode == RUN_MODE.PREDICT.value:
            self.model = Model.load_model(file_name=self.model_file_name)
            x = data
            y = self.model.predict(x)
            logger.info(f"predicted categories are: {y}")
            return y

    def evaluate_model(self, x_test: pdSeries.Series, y_test: pdSeries.Series, pipe:Pipeline):
        predicted = pipe.predict(x_test)
        logger.info("model accuracy is: %.3f \n" % pipe.score(x_test, y_test) )
        logger.info(metrics.classification_report(y_test, predicted, target_names=y_test.unique()))

    @staticmethod
    def save_model(model, file_name:str):
        """
        """
        if file_name != "":
            with open(file_name, 'wb') as fp:
                pickle.dump(model, fp)


    @staticmethod
    def load_model(file_name: str):
        try:
            fn = os.path.join(Path(__file__).parents[1], file_name)

            with open(fn, 'rb') as fp:
                return pickle.load(fp)
        except FileNotFoundError:
            raise FileNotFoundError("! model doesn't exist! need to train first !")


