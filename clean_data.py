"""
This is a small cleaning script which is basically just a placeholder so we can 
use it to create an Airflow DAG. 

The cleaning scritp in a real ETL pipeline would be much more sophistocated
and would probably use tools such as PySpark for performance. 
"""
import pandas as pd
import pathlib
import json
import routines 


def main():
    """
    This script loads the stock dataframe from the pickle file, 
    processes the pandas dataframe, then writes the data back 
    out to a .pkl file in the /data/ directory 
    :return: NA
    """
    
    # STEP 1: import the dataset 
    df = routines.import_data()

    # STEP 2: Clean the dataset 
    df['Date'] = df.index
    # convert the new date column to pd.datetime 
    df['Date']= pd.to_datetime(df['Date']) 

    # STEP 3: Export the dataset 
    routines.pickle_data(df=df)


if __name__ == "__main__":
    main()


