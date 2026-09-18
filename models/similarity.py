import pandas as pd
import numpy as np
import os

def load_data():
    try:
        matrix = pd.DataFrame(np.zeros((100, 100)))
        items = pd.DataFrame(np.zeros((100, 3)))
        interactions = pd.DataFrame(np.zeros((1000, 3)))
        return matrix, items, interactions
    except:
        return None, None, None
