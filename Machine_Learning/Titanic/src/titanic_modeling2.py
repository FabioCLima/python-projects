#%%
import os
import pandas as pd
import numpy as np

SRC_DIR = os.path.abspath(".")         # endereço do script
BASE_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMGS_DIR = os.path.join(BASE_DIR, "images")

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)


def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution= 300):
    path=os.path.join(IMGS_DIR, fig_id + "." + fig_extension)
    print("Salving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.save_fig(path, format=fig_extension, dpi=resolution)


# %%
train_data = pd.read_csv(os.path.join(DATA_DIR, 'train.csv'))
train_data.head()
#%%
train_data.describe()
# %%
train_data['Survived'].value_counts()
# %%
train_data['Pclass'].value_counts().plot(kind='bar')
# %%
train_data['Sex'].value_counts()
# %%
train_data.shape
# %%
train_data.columns.tolist()
# %%
#! vamos dropar algumas features que não serão usadas para gerar o modelo
train_data = train_data.drop(['PassengerId', 'Name', 'Cabin', 'Ticket'], axis=1)
train_data.shape
# %%
#! Filling the missing age values by the median value
train_data['Age'] = train_data.groupby('Sex', as_index=False)['Age'].apply(lambda g: g.fillna(g.median())).reset_index(drop=True)
train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])
# %%
train_data['Pclass']=train_data['Pclass'].astype('category')
# %%
train_data_new=pd.get_dummies(train_data)
train_data_new.head()
# %%
X = train_data_new.drop('Survived', axis = 1)
y = train_data_new['Survived']

# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=123)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
# %%
from sklearn.tree import DecisionTreeClassifier
tree_model =  DecisionTreeClassifier(random_state=123)
tree_model.fit(X_train, y_train)
# %%
y_pred=tree_model.predict(X_test)
pred_results = pd.DataFrame({'y_test':y_test, 'y_pred':y_pred})
pred_results.head()
# %%
titanic_crosstab = pd.crosstab(pred_results.y_pred, pred_results.y_test)
titanic_crosstab
# %%
tree_model.score(X_test, y_test)
# %%
from sklearn.metrics import(accuracy_score,
                            precision_score,
                            recall_score,
                            confusion_matrix)

acc = accuracy_score(y_test, y_pred)
print(acc)
prec = precision_score(y_test, y_pred)
print(prec)
recall = recall_score(y_test, y_pred)
print(recall)
# %%
tree_model
# %%
# Lets use de AUC(Area Under Curve) as new evaluation metric.
# Our target value is a binary

from sklearn.metrics import roc_curve, auc
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)
# %%
roc_auc
# %%
max_depths = np.linspace(1, 32, 32, endpoint=True)
train_results = []
test_results = []
for max_depth in max_depths:
   dt = DecisionTreeClassifier(max_depth=max_depth, random_state=123)
   dt.fit(X_train, y_train)
   train_pred = dt.predict(X_train)
   false_positive_rate, true_positive_rate, thresholds = roc_curve(y_train, train_pred)
   roc_auc = auc(false_positive_rate, true_positive_rate)
   # Add auc score to previous train results
   train_results.append(roc_auc)
   y_pred = dt.predict(X_test)
   false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
   roc_auc = auc(false_positive_rate, true_positive_rate)
   # Add auc score to previous test results
   test_results.append(roc_auc)
from matplotlib.legend_handler import HandlerLine2D
line1, = plt.plot(max_depths, train_results,"b", label="Train AUC")
line2, = plt.plot(max_depths, test_results, "r", label="Test AUC")
plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.ylabel("AUC score")
plt.xlabel("Tree depth")
plt.show()
# %%
