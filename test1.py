import random
import numpy as np
import pandas as pd
import qeds
import matplotlib.pyplot as plt

#%matplotlib inline
# activate plot theme
import qeds

# Dataframe 
bagel = pd.DataFrame({
    "City" : ["Montreal","Montreal","Montreal", "Montreal", "Montreal","Montreal","New York", "New York", "New York", "New York", "New York", "New York"],
    "BagelProduced" : [5, 10, 20, 25, 30, 35, 3, 13, 23, 23, 33, 33],
    "Year": [2020, 2021, 2022, 2023, 2024, 2025, 2020, 2021, 2022, 2023, 2024, 2025]
})

# Look at dataframe
bagel