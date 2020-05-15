import models_config as md

'''
Rank the Features based on different Algorithms.. 
    Decision Trees, AdaBoost and GradientBoosting Classifiers 
'''


def process_models(string):
    # get the data
    X, y, df_cols = md.getdata()
    # Split the train and test data
    X_train, X_test, y_train, y_test = md.split_data(X, y)

    '''Classify the model based on all Features'''
    model_before = md.classify(string, X_train, y_train)

    print('Analysis for', string)

    # eliminate the features based on the ranking
    sfm = md.selectimportant_features(model_before, X_train, y_train)

    # print the selected columns
    md.printranking(sfm, df_cols)
    # create subset with only selected important features
    x_important_train, x_important_test = md.split_subset(sfm, X_train, X_test)

    # train the model with new features columns along with cross-validation, log the details
    model_final = md.classify_cross_validation(string, x_important_train, y_train)

    return model_final


# Process the models
model1_final = process_models('Decision Trees')
model2_final = process_models('Gradient Boosting Classifier')
model3_final = process_models('AdaBoost Classifier')
