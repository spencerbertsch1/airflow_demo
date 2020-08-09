import pandas as pd
import pathlib
import json

# get current file path 
FPATH = pathlib.Path(__file__).parent.absolute()

# import data - TODO use pathlib -> Path instead of strings
def import_data() -> pd.DataFrame:
    """
    Function to import the .pkl file from the /data/ directory and return a 
    pandas dataframe representing the time series data 
    :return: pd.DataFrame - stock data 
    """
    return pd.read_pickle(str(FPATH) + '/data/series_data1.pkl')


def pickle_data(df: pd.DataFrame):
    """
    simple function to write the pandas dataframe object to a .pkl file in the PATH/data/ directory 
    :return: NA
    """
    # first we want to make sure the dataframe is not empty
    assert df.shape[0] > 0, f"Dataframe pulled from AlphaVantage is empty. Check the ticker being requested and try again."
    
    # now we can pickle the data and send it to the correct directory
    df.to_pickle(str(FPATH) + '/data/series_data1.pkl') 