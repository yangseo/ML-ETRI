# Homework01 iris scatter python code

import sklearn
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np


def iris_scatter(iris_data):
    # Use a breakpoint in the code line below to debug your script.
    species = iris_data.target

    data = iris_data.data
    X = np.transpose(data)
    d, N =np.shape(X)

    K=3

    color = ['r', 'g', 'b']

    plt.figure(figsize=(16, 16))
    plot_inx = 0
    for i in range(d):
        x_i = X[i, :]
        for j in range(d):
            x_j = X[j, :]
            plot_inx = plot_inx + 1
            plt.subplot(d, d, plot_inx)

            for k in range(K):
                inx = species == k
                plt.scatter(x_j[inx], x_i[inx], c=color[k])

    plt.show()
