import time
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn import svm
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


#define read data function
def getData():
    # Get the data
    df = pd.read_csv(r'task/task_data.csv')
    df['class_label'] = df['class_label'].astype(str)
    array = df.values
    X = array[:, 2:len(df.columns)]
    y = array[:, 1]

    return X,y

#define models
def classify(string,X_train,y_train):


    if string=='Random Forest Classifier':
        start_time = time.time()
        classifier = ExtraTreesClassifier(n_estimators=1000, random_state=0)
        classifier.fit(X_train, y_train)

    elif string=='Gradient Boosting Classifier':
        start_time = time.time()
        classifier = GradientBoostingClassifier(n_estimators=100, random_state=0, learning_rate=1.0)
        classifier.fit(X_train, y_train)


    elif string=='AdaBoost Classifier':
        start_time = time.time()
        classifier = AdaBoostClassifier(n_estimators=100, random_state=0)
        classifier.fit(X_train, y_train)
#SVM with radial basis function as kernel
    else:
        classifier = svm.SVC(kernel='rbf')
        classifier.fit(X_train, y_train)
        return classifier

    end_time=time.time() - start_time

    return classifier,end_time


#select important features with threshold
def selectImportant_features(model,X_train,y_train):
    sfm = SelectFromModel(model, threshold=0.03)
    sfm.fit(X_train, y_train)
    return sfm

#split the test and train data
def split_data(X,y):
    return train_test_split(X, y, test_size=0.2, random_state=0)

#split data based on ranking
def split_subset(sfm, X_train, X_test):
    return sfm.transform(X_train),sfm.transform(X_test)

#calculate the accuracy of the model
def accuracy_model(model_, X_test, y_test):
    y_pred = model_.predict(X_test)
    return accuracy_score(y_test, y_pred)

def printRanking(model):
    importance = model.feature_importances_
    indices = np.argsort(importance)[::-1]
    # Print the Sensor ranking
    for f in range(len(indices)):
        print("%d. Sensors: %d -- %f" % (f + 1, indices[f], importance[indices[f]]))
    print('')


