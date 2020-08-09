"""
Simple Airflow Demo using Plotly/Dash Stock viewer 

This toy dashboard was used as a quick way to get used to implementing 
airflow DAGs to automate the process of refreshing datasets. 
There are two things which whould happen every night for this dashboard 
to function normally: pull_data.main() needs to get called, and 
clean_data.main() needs to get called. 
pull_data.main() >> clean_data.main()

"""
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from pathlib import Path
import pathlib
import json
import routines

# import the dataset 
df = routines.import_data()

def main():
    cols = df.columns
    print(cols)
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])
    fig.show()


if __name__ == "__main__":
    main()