#%%
import os
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn. metrics import classification_report
from sklearn.metrics import (accuracy_score, precision_score, recall_score )

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import category_encoders as ce
from feature_engine.encoding import OneHotEncoder
import warnings
warnings.filterwarnings("ignore")
from sklearn import set_config
set_config(display='diagram')
pd.options.display.max_columns = 200
pd.options.display.max_rows = 999
pd.set_option("precision", 3)

SRC_DIR = os.path.abspath(".")         # endereço do script
BASE_DIR = os.path.dirname(SRC_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMGS_DIR = os.path.join(BASE_DIR, "images")

df = pd.read_csv(os.path.join(DATA_DIR, "train.csv"))
df.head()

# %%
dropar = ['PassengerId','Cabin', 'Ticket', 'Name']
df.drop(dropar, axis = 1, inplace=True)
df.dtypes
# %%
df['Pclass']=df['Pclass'].astype('O')
df.describe(include=['O'])
# %%
df['family_size'] = df.SibSp + df.Parch + 1
df.info()
# %%
print('As features Age(numérica) e Embarked(categórica) tem dados faltantes')
print('Dados categóricos, vamos preencher pela moda')
print('Dados numéricos, vamos preencher os faltantes com um ML calculado só \
com as outras features numéricas')
# %%
# variavel categórica
_= df.fillna({'Embarked': 'S'}, inplace=True)

# Imputando a variável numérica através de um modelo de machine learning
df_age = df[~df['Age'].isna()].copy() # pegando as linhas completas sem missing
from sklearn.tree import DecisionTreeRegressor
features_age = df_age.select_dtypes(include=['int', 'float']).drop(['Age', 'Survived'], axis=1).columns
features_age
# %%
tree_reg_age=DecisionTreeRegressor(max_depth=3, random_state=123)  # instanciando um decision tree regressor para calcular as idades faltantes
tree_reg_age.fit(df_age[features_age], df_age['Age'])
df['AgePredicted'] = tree_reg_age.predict(df[features_age])


def input_age(row):
    if np.isnan(row['Age']):
        return row['AgePredicted']
    else:
        return row['Age']


df["Age"] = df[["Age", "AgePredicted"]].apply(input_age, axis=1)
df.drop('AgePredicted', axis=1, inplace = True)
df.info()
#%%
print('Problema de classificação binária')
target_column = 'Survived' 
df[target_column].value_counts() # 0-morreu, 1-sobreviveu
# %%
features_numericas = df.select_dtypes(include=['int', 'float']).drop(['Survived'], axis=1).columns
features_numericas
# %%
features_categoricas = df.select_dtypes(include=['object']).columns
features_categoricas
# %%
print('Número de mortos/sobreviventes por classe de viagem')
pd.crosstab(index=df['Pclass'], columns=df['Survived'])
# %%
print('Número de mortos/sobreviventes por genero')
pd.crosstab(index=df['Sex'], columns=df['Survived'])
# %%
_= df.hist(figsize=(15, 8))
# %%
columns = ['Age', 'Fare', "family_size"]
_ = sns.pairplot(data=df, vars=columns, hue=target_column,
    plot_kws={'alpha':0.2}, height = 3, diag_kind='kde')
# %%
ax=sns.scatterplot(x='Age',
                   y='Fare',
                   data=df, 
                   hue='Survived', 
                   alpha=0.5)
# %%
X = df[features_numericas].copy()
X.columns.to_list()
# %%
y = df['Survived']
# %%
# Separate into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                 test_size=0.2, random_state=0)

logistic_model = LogisticRegression(penalty='l2', C=1.0, solver='liblinear').fit(X_train, y_train)
print(logistic_model)
# %%
logistic_model.fit(X_train, y_train)
predictions = logistic_model.predict(X_test)
# %%

print('Qual a proporção dos labels foram corretamente previstas pelo modelo')
print('Accuracy: ', accuracy_score(y_test, predictions))
accuracy = accuracy_score(y_test, predictions)
print(f'Quantos amostras foram previstas corretamente--> {accuracy*100:.2f}%')

precision = precision_score(y_test, predictions)
recall = recall_score(y_test,predictions)
print("Qtos passageiros que o modelo previu que sobreviveram, realmente sobreviveram?")
print(f"precision={precision*100:.2f}%\n")
print("Qtos dos sobreviventes(reais) o modelo previu corretamente?")
print(f"recall={recall*100:.2f}%")

# %%
print(classification_report(y_test, predictions))
# %%
pred_results = pd.DataFrame({'y_test': y_test,
                            'y_pred': predictions})
pred_results.sample(10)
# %%
titanic_train_crosstab= pd.crosstab(pred_results.y_pred, 
                                    pred_results.y_test)
titanic_train_crosstab
# %%
# Criando um modelo com todas as features e usando pipeline
num_features = df.select_dtypes(include=['int64', 'float64']).drop('Survived', axis=1).columns
num_features
# %%
cat_features = df.select_dtypes(include=['category', 'object']).columns
cat_features
#%%
features = df.drop('Survived', axis=1).columns.to_list()
features
# %%
onehot = OneHotEncoder(variables=['Pclass', 'Sex', 'Embarked'],drop_last=False)


# %%
onehot.fit(df[features])
onehot.transform(df[features]).head()
# %%
X=onehot.transform(df[features])
y=df['Survived']
print(X.shape)
# %%
# Separate into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                 test_size=0.2, random_state=0)

logistic_model = LogisticRegression(penalty='l2', C=1.0, solver='liblinear').fit(X_train, y_train)
print(logistic_model)
# %%
logistic_model.fit(X_train, y_train)
predictions = logistic_model.predict(X_test)
# %%

print('Qual a proporção dos labels foram corretamente previstas pelo modelo')
print('Accuracy: ', accuracy_score(y_test, predictions))
accuracy = accuracy_score(y_test, predictions)
print(f'Quantos amostras foram previstas corretamente--> {accuracy*100:.2f}%')

precision = precision_score(y_test, predictions)
recall = recall_score(y_test,predictions)
print("Qtos passageiros que o modelo previu que sobreviveram, realmente sobreviveram?")
print(f"precision={precision*100:.2f}%\n")
print("Qtos dos sobreviventes(reais) o modelo previu corretamente?")
print(f"recall={recall*100:.2f}%")

# %%
print(classification_report(y_test, predictions))
#%%
from sklearn.metrics import confusion_matrix

# Print the confusion matrix
cm = confusion_matrix(y_test, predictions)
print (cm)
y_scores = logistic_model.predict_proba(X_test)
# %%
from sklearn.metrics import roc_curve


# calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_scores[:,1])

# plot ROC curve
fig = plt.figure(figsize=(6, 6))
# Plot the diagonal 50% line
plt.plot([0, 1], [0, 1], 'k--')
# Plot the FPR and TPR achieved by our model
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
# %%
from sklearn.metrics import roc_auc_score

auc = roc_auc_score(y_test,y_scores[:,1])
print('AUC: ' + str(auc))
# %%
