from DataHandler.DataReader import DataReader
from FeatEng.FeatureEngineering import FeatEngineering
from Modelling.Model import Model

if __name__ == "__main__":
    data_handler = DataReader()
    data = data_handler.retrieve_data_source()

    feature_handler = FeatEngineering()
    pdf = feature_handler.do_feature_engineering(data)

    model = Model()
    model.run(pdf)
