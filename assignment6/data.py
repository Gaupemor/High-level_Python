import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

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

    #reset index? not if index_col already set
    #data_frame.reset_index(drop=True)

    # create training- and validation sets - stratify by 'diabetes' (pos/neg)
    # training_set/validation_set ratio: approx. 80% / 20%
    # pos/neg ratio in 'diabetes' for all sets: approx. 33% / 67%
    training_set, validation_set = train_test_split(
        data_frame, test_size=0.2, stratify=data_frame['diabetes'])

    return data_frame, training_set, validation_set


# create data frame, training set and validation set
data_frame, training_set, validation_set = _setup()


# create scatter plot based on two dimentions of panda data frame
def create_scatter_plot(d1, d2):

    if d1 not in data_frame.columns and d2 not in data_frame.columns:
        raise Exception(f"'{d1}' and/or '{d2}' not present in data frame.");

    # check that dtype is a numerical

    #label for axis label box
    ax_neg = data_frame[data_frame['diabetes'].str.contains("neg")].plot.scatter(x=d1, y=d2, c="Blue", label="negative")
    ax_pos = data_frame[data_frame['diabetes'].str.contains("pos")].plot.scatter(x=d1, y=d2, c="Red", label="positive", ax=ax_neg)
    plt.legend(title="Diabetes")
    #plt.title('Diabetes plot')
    #plt.show(block=True)
    return plt

#create_scatter_plot('insulin', 'glucose')
