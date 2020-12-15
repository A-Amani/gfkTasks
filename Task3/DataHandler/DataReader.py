from config import *
import pandas as pd


class DataReader():
    def __init__(self):
        self.mandatory_cols = config["mandatory_cols"]
        self.native_cols = config["data_source_native_cols"]
        self.data_source_path = config["source_data"]
        self.seperator = config["seperator"]

    def retrieve_data_source(self) -> pd.DataFrame:
        """
        """
        pdf = self.read_dataFile()
        self.validate_datasource(pdf)
        return pdf


    def read_dataFile(self):
        """
        """
        try:
            pdf = pd.read_csv(self.data_source_path, delimiter=self.seperator, usecols=self.native_cols)
        except Exception:
            raise Exception("cannot read the data_handling source!")
        return pdf

    def validate_datasource(self, pdf:  pd.DataFrame):
        """
        """
        if set(self.mandatory_cols).issubset(set(pdf.columns)):
            pass
        else:
            logger.ERROR("! Mandatory cols are not present in the data_handling source provided !")
            raise Exception("Mandatory cols are not present in the data_handling source provided ")
