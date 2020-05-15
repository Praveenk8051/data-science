from sklearn.model_selection import KFold
import time
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


# define read data function
def getdata():
    # Get the data
    df = pd.read_csv('sample.csv')
    df_cols = ['column' + str(i + 1) for i in range(0, len(df.columns))]
    df.columns = df_cols
    array = df.values
    X = array[:, 0:len(df.columns) - 1]
    y = array[:, -1]
    return X, y, df_cols


# define models
def classify(string, X_train, y_train):
    if string == 'Decision Trees':
        start_time = time.time()
        classifier = DecisionTreeClassifier()
        classifier.fit(X_train, y_train)

    elif string == 'Gradient Boosting Classifier':
        start_time = time.time()
        classifier = GradientBoostingClassifier(n_estimators = 100, random_state = 0, learning_rate = 1.0)
        classifier.fit(X_train, y_train)

    else:
        start_time = time.time()
        classifier = AdaBoostClassifier(n_estimators = 100, random_state = 0)
        classifier.fit(X_train, y_train)

    end_time = time.time() - start_time

    return classifier


# select important features with threshold
def selectimportant_features(model, X_train, y_train):
    sfm = SelectFromModel(model, threshold = 0.05)
    sfm.fit(X_train, y_train)
    return sfm


def classify_cross_validation(string, X, y):
    scores = []
    cv = KFold(n_splits = 5, random_state = 42, shuffle = False)

    for train_index, test_index in cv.split(X):
        X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
        model = classify(string, X_train, y_train)
        scores.append(model.score(X_test, y_test))
    print('Mean Cross Validation Accuracy of ', string, ':', np.mean(scores))
    print('')


# split the test and train data
def split_data(X, y):
    return train_test_split(X, y, test_size = 0.2, random_state = 0)


# split data based on ranking
def split_subset(sfm, X_train, X_test):
    return sfm.transform(X_train), sfm.transform(X_test)


# calculate the accuracy of the model
def accuracy_model(model_, X_test, y_test):
    y_pred = model_.predict(X_test)
    return accuracy_score(y_test, y_pred)


def printranking(model, column_names):
    # Print the names of the most important features
    print('Selected columns out of 295 features!!')
    for feature_list_index in model.get_support(indices = True):
        print(column_names[feature_list_index], end = ", ", flush = True)
    print('')
