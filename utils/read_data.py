from functools import cache, lru_cache
import pandas as pd

import sys
import os

current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

from config import MATCHES_PROCESSED_DATA, DELIVERIES_PROCESSED_DATA

@lru_cache
def matches_data():
    matches = pd.read_csv(MATCHES_PROCESSED_DATA)
    return matches

@lru_cache
def deliveries_data():
    deliveries = pd.read_csv(DELIVERIES_PROCESSED_DATA)
    return deliveries