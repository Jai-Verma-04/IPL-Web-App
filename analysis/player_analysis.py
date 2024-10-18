# -------------------------------------------------------------------------------------------------------
# File Name: player_analysis.py
# Author: Jai Verma
# Description: Analyse and extract some key stats from the data for a selected player.
#              These functions will be used by the Player Analysis page to display these stats for the
#              player selected by the user.
# -------------------------------------------------------------------------------------------------------


# Importing the required libraries
import os
import sys
import pandas as pd


# Setting the current working directory as system path
current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))


# importing read_data from utils to read the data from the parquet files.
from utils.read_data import matches, deliveries    



#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#
