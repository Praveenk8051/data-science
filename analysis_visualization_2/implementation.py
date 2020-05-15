import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier

df_main=pd.read_csv('task/task_data.csv')
df_main['class_label']=df_main['class_label'].astype(str)
df=df_main.copy()


array = df.values
X = array[:,2:len(df.columns)]
y = array[:,1]
# Build a forest and compute the feature importance
forest = ExtraTreesClassifier(n_estimators=1000,random_state=0)

forest.fit(X, y)
importance = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importance)[::-1]

# Print the feature ranking
print("Feature ranking and probabilities of their impact:")

for f in range(X.shape[1]):
    print("%d. Sensors: %d -- %f" % (f + 1, indices[f], importance[indices[f]]))

# Plot the feature importance of the forest
a4_dims = (11.7, 8.27)
plt.figure(figsize=a4_dims)
plt.title("Feature importance")
plt.bar(range(X.shape[1]), importance[indices],
        color="g", xerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.ylabel('Probabilities')
plt.xlabel('Sensors')
plt.xlim([-1, X.shape[1]])
plt.show()

