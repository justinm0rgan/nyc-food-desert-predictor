#!/usr/bin/env python
'''This file contains functions utilized within the Modeling Jupyter Notebook of the NYC Food Desert Predictor capstone 
project for Flatiron School'''

# import necessary packages
import pandas as pd
import numpy as np
import os
import pickle
from collections import Counter

# visualization packages
import matplotlib.pyplot as plt
import seaborn as sns

# modeling
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFECV
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBRegressor
import xgboost as xgb
from xgboost import XGBClassifier
from xgboost import plot_importance

# import function from other module to save figures
from .functions import save_fig

# function that prints neat formatted scoring metrics for model scoring
def get_model_scores(model, y_train, y_train_pred, y_test, y_test_pred, ):
    '''Enter model type, y_train, y_train_pred, y_test, y_test_pred.
    Returns modeling scores printed out in a consistent format'''
    print('\033[1m' + 'Below are the scoring metrics for {} model'.format(model) + '\033[0m')
    print('\n')
    print('Train {} Accuracy: {}'.format(model, metrics.accuracy_score(y_train, y_train_pred)))
    print('Test {} Accuracy: {}'.format(model, metrics.accuracy_score(y_test, y_test_pred)))
    print('\n')
    print('Train {} F1: {}'.format(model, metrics.f1_score(y_train,y_train_pred)))
    print('Test {} F1: {}'.format(model, metrics.f1_score(y_test,y_test_pred)))
    print('\n')
    print('Train {} Recall: {}'.format(model, metrics.recall_score(y_train, y_train_pred)))
    print('Test {} Recall: {}'.format(model, metrics.recall_score(y_test, y_test_pred)))
    print('\n')
    print('Train {} Precision: {}'.format(model, metrics.precision_score(y_train, y_train_pred)))
    print('Test {} Precision: {}'.format(model, metrics.precision_score(y_test, y_test_pred)))

# function for plotting confusion matrix
def confusion_matrix(estimator, X, y, title, display_labels=['Not Food Desert', 'Food Desert'],\
    normalize='all'):
    '''Function that plots confusion matrix for model
    Enter estimator, X, y
    Display labels and normalize have defaults but can be altered'''
    fig, ax = fig, ax = plt.subplots(figsize=(12, 10))
    plt.rcParams.update({'font.size': 16})
    metrics.plot_confusion_matrix(estimator, X, y, 
                              cmap=plt.cm.Blues, 
                              display_labels=display_labels, 
                              ax=ax,
                              normalize=normalize)
    ax.set_ylabel('True', fontdict={'fontsize':18})
    ax.set_xlabel('Predicted', fontdict={'fontsize':18})
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.title(title, fontdict={'fontsize':20})

# function that geospatially visualizes predictions
def create_choropleth_map_pred(df1, df2, df3, col1, col2, col3, cmap, title, ptcolor):
    '''Creates a choropleth map with three dataframes for plotting predictions
    Select df1 and col1 for negative class
    Select df2 and col2 for positive calss
    Select df3 and col3 for predicted positive class
    Enter cmap for desired color palette
    Enter title for map title and image saved name'''

    # create map figure and axes
    fig, ax = plt.subplots(figsize=(50,40))

    # call .plot() method on df
    ax = df1.plot(column = col1, 
                            cmap=cmap, 
                            ax=ax,
                            edgecolor='face',
                            zorder=1,
                            alpha=0.5,
                            missing_kwds={
                                "color": "lightgrey",
                            })

    df2.plot(column = col2,
                            color=ptcolor,
                            ax=ax,
                            zorder=3,
                            alpha=0.65)
    df3.plot(column = col3,
                    color='yellow',
                    ax=ax,
                    zorder=2)
    
    # add annotation
    ax.annotate("•", xy=(0.78, .895), size=90, xycoords='figure fraction', color='olive')
    ax.annotate("True Positive", xy=(0.80, .90), size=70, xycoords='figure fraction')
    
    ax.annotate("•", xy=(0.78, .855), size=90, xycoords='figure fraction', color='yellow')
    ax.annotate("False Positive", xy=(0.80, .86), size=70, xycoords='figure fraction')
    
    ax.annotate("•", xy=(0.78, .815), size=90, xycoords='figure fraction', color=ptcolor, alpha=0.65)
    ax.annotate("Food Desert", xy=(0.80, .82), size=70, xycoords='figure fraction')
    
    ax.annotate("•", xy=(0.78, .765), size=90, xycoords='figure fraction', color='purple', alpha=0.5)
    ax.annotate("Not Food Desert", xy=(0.80, .77), size=70, xycoords='figure fraction')
    
    ax.annotate("•", xy=(0.78, .725), size=90, xycoords='figure fraction', color='lightgrey')
    ax.annotate("Missing Values", xy=(0.80, .72), size=70, xycoords='figure fraction')
    
    # set map title
    ax.set_title(label=title,fontdict={'fontsize': 100}, loc='center')


    # remove axis surrounding map
    ax.set_axis_off()

    # save map
    save_fig(title.lower().replace(' ', '_'), transparent=True)
    plt.show()
