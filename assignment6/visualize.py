import fitting
import data
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import neighbors, datasets
from resources import resources
#pip install python-resources


def make_probability_scatterplot(feature_1, feature_2):
    trained_classifier = fitting.fit(include_features=[feature_1, feature_2])
    plt = data.create_scatter_plot(feature_1, feature_2);

    X = data.data_frame[[feature_1, feature_2]].values
    y = data.data_frame['diabetes'].values
    h = .02  # step size in the mesh

    print(resources.getrlimit())
    print("got here")
    exit()

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    print("past mesh");
    x_r = xx.ravel()
    print("x ravel")
    y_r = yy.ravel()
    print("y ravel")
    r = np.c_[x_r, y_r]
    print("past ravel")
    Z = trained_classifier.predict(r)
    print("past predict")

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    print("past plt")


    #add subplots to scatter plot
    plt.show()

make_probability_scatterplot('insulin', 'glucose');
