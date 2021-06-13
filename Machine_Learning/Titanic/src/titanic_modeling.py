# %%
import os
import pandas as pd
import numpy as np


# %%
SRC_DIR = os.path.abspath(".")         # endereço do script
BASE_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
# %%
data_file = os.path.join(DATA_DIR, 'train.csv')
print(data_file)
# %%
df = pd.read_csv(data_file)
df.head()
# %%
df.info()
# %%
df.dtypes
# %%
df = df.drop(['PassengerId', 'Name', 'Cabin'], axis=1)
df.isna().sum()
# %%
df.describe()
# %%
df.describe(include=['O'])
# %%
df[df['Age'].isna()].head()
# %%
print(df[['Sex', 'Age']].groupby('Sex')['Age'].median())
df['Embarked'].mode()
# %%
df['Age'] = df.groupby("Sex", as_index=False)['Age'].apply(lambda g: g.fillna(g.median())).reset_index(drop=True)
# %%
df = df.fillna({'Embarked':'S'})
# %%
df.isna().sum()
# %%
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', "Fare", 'Embarked']
label = 'Survived'
# %%
from sklearn.preprocessing import (OneHotEncoder, OrdinalEncoder)
onehot = OneHotEncoder()
# %%
onehot_arr = onehot.fit_transform(df[['Sex', 'Embarked']]).toarray()
onehot_arr
# %%
onehot.categories_
# %%
df_onehot = pd.DataFrame(onehot_arr, columns=[
    'Sex=female', 'Sex=male', 'Embarked=C', 'Embarked=Q', 'Embarked=S'
]).astype("int")

# %%
df_onehot.head()

# %%
features = ['Pclass', 'Age', 'SibSp', 'Parch', "Fare"]
df_features = df[features]
df_features = pd.concat([df_features, df_onehot], axis=1)
df_label = df[label]
df_features.head()
# %%
X, y = df_features, df_label
# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=123)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
# %%
from sklearn.tree import DecisionTreeClassifier
model =  DecisionTreeClassifier(random_state=123)
model.fit(X_train, y_train)
# %%
y_pred=model.predict(X_test)
pred_results = pd.DataFrame({'y_test':y_test, 'y_pred':y_pred})
pred_results.head()
# %%
titanic_crosstab = pd.crosstab(pred_results.y_pred, pred_results.y_test)
titanic_crosstab
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
from sklearn.model_selection import cross_val_score

acc_list = cross_val_score(model, X_train, y_train, cv=5)
result = round(np.mean(acc_list*100), 3)
print(f"The average accuracy is {result:.2f}%")
# %%
import matplotlib.pyplot as plt 
from sklearn import tree
# %%
titanic_tree = model
titanic_tree.feature_importances_
# %%
previsores= df_features.columns.tolist()
previsores
# %%
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(25, 75))
tree.plot_tree(
    titanic_tree,
    feature_names=previsores,
    filled=True)
# %%
