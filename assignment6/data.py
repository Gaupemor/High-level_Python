import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

"""
Module for data analysis of diabetes.svc using pandas.
"""

# generalize for more than one format? (csv, excel etc.)
def _setup():
    """
    6.1: Private setup method, prepares the data frame from the cvs-file 'diabetes'.

    Returns:
        DataFrame: the entire data frame
        DataFrame: the training set
        DataFrame: the validation set
    """
    data = pd.read_csv("diabetes.csv", index_col=[0])

    # create data_frame w/o samples containing NaN
    data_frame = pd.DataFrame(data).dropna()

    # create training- and validation sets - stratify by 'diabetes' (pos/neg)
    # training_set/validation_set ratio: approx. 80% / 20%
    # pos/neg ratio in 'diabetes' for all sets: approx. 33% / 67%
    training_set, validation_set = train_test_split(
        data_frame, test_size=0.2, stratify=data_frame['diabetes'])

    return data_frame, training_set, validation_set


# create data frame, training set and validation set
data_frame, training_set, validation_set = _setup()


# create scatter plot based on two dimentions of panda data frame
def create_scatter_plot(feature_1, feature_2):
    """
    Creates a scatter plot of the diabetes data based on 2 features.

    Args:
        feature_1 (string): The first feature to plot by
        feature_2 (string): The second feature to plot by

    Returns:
        plt: scatter plot
    """
    if feature_1 not in data_frame.columns and feature_2 not in data_frame.columns:
        raise Exception(f"'{d1}' and/or '{d2}' not present in data frame.");

    #label for axis label box
    ax_neg = data_frame[data_frame['diabetes'].str.contains("neg")].plot.scatter(x=feature_1, y=feature_2, c="Blue", label="negative")
    ax_pos = data_frame[data_frame['diabetes'].str.contains("pos")].plot.scatter(x=feature_1, y=feature_2, c="Red", label="positive", ax=ax_neg)
    plt.legend(title="Diabetes")
    return plt
