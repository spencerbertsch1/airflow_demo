"""
Read data from an API into local flat files 

"""
import pandas as pd
import requests
import pathlib
import routines
import json

# parse the configs from config.json 
with open('config.json') as config_file:
    config_data = json.load(config_file)


def query_alphaVantage_timeSeries_endpoint(ticker: str = "MSFT"):
    """

    :return: pd.DataFrame representing the full daily time series data for the chosen security
    """
    pub_key = "demo" # TODO add api key to git ignore and use here 
    endpoint = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=full&apikey=" + pub_key
    # retrieve data from endpoint
    r = requests.get(endpoint)

    # convert to python dictionary
    x = r.json()

    # define df in pandas 
    df = pd.DataFrame.from_dict(x['Time Series (Daily)']).T

    # rename columns
    df = df.rename(columns={"1. open": "Open", 
                "2. high": "High",
                "3. low": "Low", 
                "4. close": "Close",
                "5. volume": "Volume"})

    # change types from string to float
    return df.astype(float)


def main():
    security_to_pull = config_data['security']
    df = query_alphaVantage_timeSeries_endpoint(ticker = security_to_pull)
    routines.pickle_data(df=df)
    print(f'...data pulled successfully | {df.shape[0]} rows written to /data/...')  # TODO <-- replace with logger 


if __name__ == "__main__":
    main()