import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import numpy as np

df=pd.read_csv(r'C:\Users\MY PC\Desktop\Industrial_DS\Files\task\task_data.csv')
df.columns
dfy=df['class_label'].values
sensor_cols=['sensor'+str(i) for i in range(0,10)]
dfx=df[sensor_cols]

vis_data = TSNE(n_components=2, random_state=0).fit_transform(dfx.values)
target_ids = range(len(df['class_label'].unique()))
a4_dims = (8.7, 8.27)
plt.figure(figsize=a4_dims)
colors = 'r', 'g'
labels=['class_label=1.0','class_label=-1.0']
for i, c, label in zip(target_ids, colors, df['class_label'].unique()):
    plt.scatter(vis_data[dfy == i, 0], vis_data[dfy == i, 1], c=c, label=labels[i])
plt.legend()
plt.xlabel('TSE-1')
plt.ylabel('TSE-2')
plt.show()