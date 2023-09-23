# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from iris_scatter import iris_scatter
import sklearn
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    iris = load_iris()
    iris_scatter(iris)

    print(iris)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
