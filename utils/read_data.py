import pandas as pd

import sys
import os

current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

def matches_data():
    matches = pd.read_parquet("data\\processed\\matches.parquet")
    return matches


def deliveries_data():
    deliveries = pd.read_parquet("data\\processed\\deliveries.parquet")
    return deliveries