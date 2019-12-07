import data
import sklearn
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

"""
Module to create a trained classifier for diabetes.cvs using sklearn.
"""

def fit(classifier='mlp', include_features=None, exclude_features=None):
    """
    6.2: Creates a trained classifier from the data module using sklearn.

    Args:
        include_features (string[]): mutually exclusive from 'exclude_features'
        exclude_features (string[]): mutually exclusive from 'include_features'
        classifier (string): which classifier to use ('mlp' by default)
            options:
                'mlp'
                'svc'
                'neighbors'

    Returns:
        Classifier: the trained classifier
        float: the accuracy score on the training set
        float: the accuracy score on the validation set
    """
    #data.create_scatter_plot("insulin", "glucose")

    classifiers = {"mlp": MLPClassifier(alpha=1, max_iter=1000),
        "neighbors": KNeighborsClassifier(n_neighbors=1),
        "svc": SVC(gamma=2, C=1)}

    if classifier not in classifiers.keys():
        raise Exception(f"There is no implementation for the given classifier '{classifier}'.\n" +
            f"Available classifiers: {list(classifiers.keys())}");

    c = classifiers[classifier]

    if include_features is not None and exclude_features is not None:
        raise Exception("'include_features' and 'exclude_features' are mutually exclusive parametres. Only pass one per call.")

    fitting_set = data.training_set
    fitted_validation_set = data.validation_set

    if exclude_features is not None:
        if 'diabetes' in exclude_features:
            exclude_features.remove('diabetes')
        fitting_set = fitting_set.drop(exclude_features, axis=1)
        fitted_validation_set = fitted_validation_set.drop(exclude_features, axis=1)
    if include_features is not None:
        if 'diabetes' not in include_features:
            include_features.append('diabetes')
        fitting_set = fitting_set[include_features]
        fitted_validation_set = fitted_validation_set[include_features]

    trained_classifier = c.fit(fitting_set.drop('diabetes', axis=1), fitting_set['diabetes'])


    prediction = trained_classifier.predict(fitting_set.drop('diabetes', axis=1))
    training_score = accuracy_score(
         y_true=fitting_set['diabetes'].values,
         y_pred=prediction)
    prediction = trained_classifier.predict(fitted_validation_set.drop('diabetes', axis=1))
    validation_score = accuracy_score(
         y_true=fitted_validation_set['diabetes'].values,
         y_pred=prediction)

    return trained_classifier, training_score, validation_score

if __name__ == "__main__":
    print('Choose two unique features to visualize')
    print('------------')
    for a in data.data_frame.columns:
        print(a)
    print('------------')
    a = input('\nfirst feature: \n>')
    b = input('\nsecond feature: \n>')
    print('\nChoose classifier\n--------')
    print('mlp\nneighbors\nsvc\n--------')
    c = input('\n>')
    d = fit(c, include_features=[a, b])
    print('Training score: ', d[1], '\nValidation score: ', d[2])