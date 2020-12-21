#!/usr/bin/env python
'''This file contains general functions utilized in more then one notebook in the NYC Food Desert Predictor 
capstone project for Flatiron School'''

# import built in modules
import pandas as pd
import numpy as np
import geopandas as gpd
import contextily as ctx
from shapely.geometry import Polygon, LineString, Point
import os
import pickle
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
# set directory
PROJECT_DIR = ".."
IMAGES_PATH = os.path.join(PROJECT_DIR, 'images')
os.makedirs(IMAGES_PATH, exist_ok=True)

# functions start here

# function for saving figures
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=250):
    '''Function that saves visual as png at a specified resolution
    Enter fig_id to specify what you would like your figure to be called.
    Other paremeters have default values and can be altered if needed'''
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

if __name__ == '__main__':
    _test()
