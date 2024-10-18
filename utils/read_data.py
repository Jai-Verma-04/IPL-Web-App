# -------------------------------------------------------------------------------------------------------
# File Name: read_data.py
# Author:   Jai Verma
# Description: Reads the parquet data files from the data folder using pandas.
# -------------------------------------------------------------------------------------------------------

# Importing the required libraries
import pandas as pd
import sys
import os
import functools

# Setting the current working directory as system path
current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))


def matches_data():
    '''
    Reads the Matches data from matches.parquet file.

    Returns:
    Dataframe: matches.parquet file as a dataframe.
    '''
    try:
        matches = pd.read_parquet("data\\processed\\matches.parquet")
    except Exception as e:
        return e
    
    return matches


def deliveries_data():
    '''
    Reads the Deliveries data from deliveries.parquet file.
    
    Returns:
    Dataframe: deliveries.parquet file as a dataframe.
    '''
    try:
        deliveries = pd.read_parquet("data\\processed\\deliveries.parquet")
    except Exception as e:
        return e
    
    return deliveries

print(deliveries_data())