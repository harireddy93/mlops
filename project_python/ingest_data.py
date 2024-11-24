import logging
import pandas as pd

"""
Creating the  class to Inget data 
"""
class IngestData:
    def __init__(self,data_path:str):
        self.data_path = data_path

    def get_data(self,data_path):
        logging.info(f"loading file from datapath : {self.data_path}")
        return pd.read_csv(self.data_path)
        
def Ingest_Data(data_path:str) -> pd.DataFrame:
    """
    Ingest data from the data_path

    """
    try:
        Ingest_Data_func = IngestData(data_path)
        df= Ingest_Data_func.get_data(data_path)
        return df
    except Exception as e:
        logging.error(f"Error while ingesting the data {e}")



