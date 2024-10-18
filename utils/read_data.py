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

@functools.cache
def matches_data():
    '''
    Reads the Matches data from matches.parquet file.

    Returns:
    Dataframe: matches.parquet file as a dataframe.
    '''
    path = os.path.join('data', 'processed', 'matches.parquet')
    try:
        matches = pd.read_parquet(path=path)
    except Exception as e:
        return e
    
    return matches


@functools.cache
def deliveries_data():
    '''
    Reads the Deliveries data from deliveries.parquet file.
    
    Returns:
    Dataframe: deliveries.parquet file as a dataframe.
    '''
    path = os.path.join('data', 'processed', 'deliveries.parquet')
    try:
        deliveries = pd.read_parquet(path=path)
    except Exception as e:
        print(e)

    return deliveries