#!/usr/bin/env python
'''This file contains functions utilized within the EDA Jupyter Notebook of the NYC Food Desert Predictor capstone 
project for Flatiron School'''

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
from .functions import save_fig

# functions start here

def cat_data(df):
    '''Generate number of unique values and catplot of columns in df classified as category'''
    print(df.select_dtypes(include=['category']).nunique())
    for col in df.select_dtypes(include='category').columns:
        fig = sns.catplot(x=col, kind='count', data=df)
        fig.set_ylabels('Count')
        fig.set_xlabels('')
        fig.set(title=col)
        fig.set_xticklabels()
        plt.show()

# function that selects numerical dtypes and creates boxplots
def num_data(df):
    '''Generate boxplot in df from numerical column data'''
    for col in df.select_dtypes(include=['int64','float']).columns:
        fig = sns.boxplot(x=col, orient='v', data=df)
        plt.show()

# function that can easily recreate map given parameters
def create_choropleth_map(df, col, color_map, title, vmax=1):
    '''Take in dataframe, column, cmap, title and vmax (default set to 1). Create choropleth 
    map with colorbar and save file to image directory with imputing title as lowercase 
    with underscores between words'''
    
    # set color min
    vmin = 0
    
    # create map figure and axes
    fig, ax = plt.subplots(figsize=(50,40))

    # call .plot() method on df
    ax = df.plot(column = col, 
                            cmap=color_map, 
                            ax=ax,
                            vmin=vmin,
                            vmax=vmax,
                            edgecolor='face',
                            legend=True,
                            legend_kwds={'shrink': 0.7})


    # figure has two axes, cb is 2nd
    cb = fig.axes[1]

    # # set params for cb
    cb.tick_params(labelsize=40,
                      direction='out', 
                      length=6, 
                      width=2,
                      grid_alpha=1)

    # set map title
    ax.set_title(title, fontdict={'fontsize': 70}, loc='center')


    # remove axis surrounding map
    ax.set_axis_off()

    # save map
    save_fig(title.lower().replace(' ', '_'))
    plt.show()


# ENGINEERED FEATURE
# function that will create rate columns
# create rate columns per feature
def rate_column(df, col_1, col_2):
    '''Enter dataframe and column names, adds new rate column onto dataframe'''
    df['rate' + col_1] = df[col_1] / df[col_2]

def create_choropleth_map_points(df1, df2, col1, col2, cmap, title, ptcolor, vmax=1):
    '''Creates a choropleth map with points
    Select df1 and col1 for polygon geometries
    Select df2 and col2 for point
    Enter cmap for desired color palette
    Enter title for map title and image saved name
    Optional vmax parameter with default as 1'''
    # set color min
    vmin = 0 

    # create map figure and axes
    fig, ax = plt.subplots(figsize=(50,40))

    # call .plot() method on df
    ax = df1.plot(column = col1, 
                            cmap=cmap, 
                            ax=ax,
                            vmin=vmin,
                            vmax=vmax,
                            edgecolor='face',
                            legend=True,
                            legend_kwds={'shrink': 0.7},
                            missing_kwds={
                                "color": "lightgrey",
                            })

    df2.plot(column = col2,
                            marker='o',
                            color=ptcolor,
                            markersize=500,
                            ax=ax,
                            zorder=1)

    # figure has two axes, cb is 2nd
    cb = fig.axes[1]

    # # set params for cb
    cb.tick_params(labelsize=60,
                      direction='out', 
                      length=6, 
                      width=2,
                      grid_alpha=1)

    # add annotation
    ax.annotate("•", xy=(0.80, .895), size=100, xycoords='figure fraction', color=ptcolor)
    ax.annotate("Food Desert", xy=(0.82, .90), size=70, xycoords='figure fraction')
    ax.annotate("•", xy=(0.80, .855), size=100, xycoords='figure fraction', color='lightgrey')
    ax.annotate("Missing Values", xy=(0.82, .86), size=70, xycoords='figure fraction')
    # set map title
    ax.set_title(label=title,fontdict={'fontsize': 100}, loc='center')


    # remove axis surrounding map
    ax.set_axis_off()

    # save map
    save_fig(title.lower().replace(' ', '_'))
    plt.show()

# function for creating lmplot
def lmplot(data, x, y, xlabel, ylabel, title, height=12, aspect=1, theme='poster', target='LILATracts_halfAnd10',\
          style='darkgrid'):
    '''Creates lmplot to comepare two variables vs the target 
    Enter dataframe, x, y, xlabel, ylabel, title.
    Height and aspect have default values
    Seaborn theme default poster, theme to darkgrid
    Target default to LILATracts_halfAnd10'''
    sns.set_style(style)
    sns.set_theme(theme)
    sns.lmplot(x=x, 
               y=y,  
               data=data,
              height=12,
              aspect=1,
               legend_out=False,
              hue=target)\
        .set(ylabel=ylabel, 
             xlabel=xlabel, 
             title=title)\
        ._legend.set_title('Target')
    save_fig(title.lower().replace(' ', '_'))
    plt.show();

if __name__ == '__main__':
    _test()