import fitting
import data
import numpy as np


"""
"""

def visualize(feature_1, feature_2, classifier):
    """
    6.3: Creates a scatter plot of diabetes data, displaying areas of predicted negative/positive result.

    Args:
        feature_1 (string): The first feature to plot by
        feature_2 (string): The second feature to plot by

    Returns:
        plt: the scatter plot
        float: the accuracy score on the training set
        float: the accuracy score on the validation set
    """
    
    trained_classifier, training_score, validation_score = fitting.fit(classifier, include_features=[feature_1, feature_2])
    plt = data.create_scatter_plot(feature_1, feature_2);

    X = data.data_frame[[feature_1, feature_2]].values
    y = data.data_frame['diabetes'].values
    step = 0.5

    # Mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step),
                         np.arange(y_min, y_max, step))
    x_r = xx.ravel()
    y_r = yy.ravel()
    r = np.c_[x_r, y_r]
    Z = trained_classifier.predict(r)

    Z = Z.reshape(xx.shape)
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.coolwarm)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.scatter(X,X)

    #plt.show(block=True)

    return plt, training_score, validation_score


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
    d = visualize(a,b,c)
    d[0].show()
