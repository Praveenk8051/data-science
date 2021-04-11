import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score,classification_report
import time
import matplotlib.pyplot as plt


df_main=pd.read_csv('task/task_data.csv')
df_main['class_label']=df_main['class_label'].astype(str)
array = df_main.values


X = array[:,2:12]
y = array[:,1]

feat_labels = df_main.columns[2:12]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

start_time_before = time.time()
forest = ExtraTreesClassifier(n_estimators=1000, random_state=0)
forest.fit(X_train, y_train)
end_time_before=time.time() - start_time_before

lis=[]
lis=sorted(zip(feat_labels, forest.feature_importances_), key=lambda x: x[1], reverse=True)
print("---Execution time for Classification task of %d Sensors is %s seconds ---" % (len(forest.feature_importances_), (end_time_before)))

# Print the feature ranking
print("Feature ranking: Before")

for i in range(len(lis)):
    print(lis[i])
    
    
sfm = SelectFromModel(forest, threshold=0.03)
sfm.fit(X_train, y_train)


for feature_list_index in sfm.get_support(indices=True):
    print(feat_labels[feature_list_index])

X_important_train = sfm.transform(X_train)
X_important_test = sfm.transform(X_test)

start_time_after = time.time()
forest_important = ExtraTreesClassifier(n_estimators=1000, random_state=0)
forest_important.fit(X_important_train, y_train)
end_time_after=time.time() - start_time_after

lis=[]
lis=sorted(zip(feat_labels, forest_important.feature_importances_), key=lambda x: x[1], reverse=True)
print("---Execution time for Classification task of %d Sensors is %s seconds ---" %( len(forest_important.feature_importances_), (end_time_after)))
# Print the feature ranking
print("Feature ranking: After")

for i in range(len(lis)):
    print(lis[i])

y_pred = forest.predict(X_test)

accuracy_before=accuracy_score(y_test, y_pred)
print(accuracy_before)


y_important_pred = forest_important.predict(X_important_test)

accuracy_after=accuracy_score(y_test, y_important_pred)
print(accuracy_after)


print(classification_report(y_test, y_pred,target_names=['1.0','-1.0']))


















