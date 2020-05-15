import models_config as md

import pandas as pd
import matplotlib.pyplot as plt

'''
Rank the Sensors based on different Algorithms.. 
    Random Forest Classifier, SVM, AdaBoost and GradientBoosting Classifiers 
'''
def processModels(string):
    #get the data
    X,y = md.getData()
    #Split the train and test data
    X_train, X_test, y_train, y_test = md.split_data(X,y)

    if string =='SVM Classifier':
        model_before= md.classify(string, X_train, y_train)
        accuracy_before = md.accuracy_model(model_before, X_test, y_test)
        print(string, 'Accuracy:', accuracy_before)
        pass
    else:
        # train the model
        model_before, execution_time_before = md.classify(string, X_train, y_train)
        # accuracy of the model before dropping the features
        accuracy_before = md.accuracy_model(model_before, X_test, y_test)
        print('Analysis for', string)
        #Print features selected before
        print('Sensor Ranking')
        md.printRanking(model_before)

        #eliminate the features based on the ranking
        sfm=md.selectImportant_features(model_before,X_train,y_train)
        #create subset with important features
        X_important_train,X_important_test=md.split_subset(sfm, X_train, X_test)

        #train the model with new sensor columns
        model_after,execution_time_after=md.classify(string, X_important_train,y_train)

        #accuracy of the model
        accuracy_after=md.accuracy_model(model_after, X_important_test, y_test)

        #Print Accuracy and Execution Time
        print('Classifier Training time')
        print('Before Feature Selection:',execution_time_before, '\nAfter Feature Selection', execution_time_after,'\n')

        print('Accuracy Calculation of Classifier')
        print('Before Feature Selection:',accuracy_before, '\nAfter Feature Selection', accuracy_after,'\n')


#Process the models
processModels('Random Forest Classifier')
processModels('Gradient Boosting Classifier')
processModels('AdaBoost Classifier')
processModels('SVM Classifier')
