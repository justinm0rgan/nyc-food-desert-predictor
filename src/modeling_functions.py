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
def confusion_matrix(estimator, X, y, title, display_labels=['Not Food Desert', 'Food Desert']):
    '''Function that plots confusion matrix for model
    Enter estimator, X, y, cmap
    Display labels and font have defaults but can be altered'''
    fig, ax = fig, ax = plt.subplots(figsize=(12, 10))
    metrics.plot_confusion_matrix(estimator, X, y, 
                              cmap=plt.cm.Blues, 
                              display_labels=display_labels, 
                              ax=ax)
    ax.set_ylabel('True', fontdict={'fontsize':18})
    ax.set_xlabel('Predicted', fontdict={'fontsize':18})
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.title(title, fontdict={'fontsize':20})