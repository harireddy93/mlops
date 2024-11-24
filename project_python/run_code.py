import logging 
import pandas as pd 
import ingest_data 

if __name__== "__main__":
    ingest_data.Ingest_Data(data_path="Datasets/data_set_purchase.csv")
