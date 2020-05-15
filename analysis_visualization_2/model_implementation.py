import models_config as md
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
import matplotlib.pyplot as plt

#function to read data
def getData():
    dataframe=pd.read_csv(r'task/task_data.csv')
    dataframe['class_label']=dataframe['class_label'].astype(str)
    array = dataframe.values
    X = array[:,2:len(dataframe.columns)]
    Y = array[:,1]
    
    return X,Y


#Get the data
X,y=md.getData()

#Split the train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


#Train the model
model = AdaBoostClassifier(n_estimators=1000,random_state=0)
model.fit(X_train, y_train)
importance = model.feature_importances_
indices = np.argsort(importance)[::-1]

# Print the feature ranking
print("Sensor ranking using Ada Boost Classifier and probabilities of their impact:")

for f in range(X.shape[1]):
    print("Sensors: %d: %f" % (indices[f], importance[indices[f]]))
    

# Plot the sensor importance/ranking
a4_dims = (8.27, 8.27)
plt.figure(figsize=a4_dims)
plt.title("Sensor Rankings using Ada Boost Classifier")
plt.bar(range(X.shape[1]), importance[indices], color="g")
plt.xticks(range(X.shape[1]), indices)
plt.ylabel('Probabilities')
plt.xlabel('Sensors')
plt.xlim([-1, X.shape[1]])
plt.show()