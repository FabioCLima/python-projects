#* Extreme Gradient Boosting exemplo:   
#******************************************************************************
"""[xgboost]
Boosting is a sequential technique which works on the principle of an 
ensemble. It combines a set of weak learners and delivers improved prediction
accuracy.
Weak learner is one which is slightly better than random guessing.        
"""
"""
UCI Machine Learning Repository ---> sklearn's dataset 
14 explanatory variables and target variable is median value of owner-occupied
homes per $1000s.
"""
#! Using XGBoost in Python
#%% 
from sklearn.datasets import load_boston  
boston = load_boston()
# %%
print(boston.keys())
# %%
print(boston.data.shape)
# %%
print(boston.feature_names)
# %%
print(boston.DESCR)
# %%
#! Conversão em pandas dataframe
import pandas as pd 

data = pd.DataFrame(boston.data)
data.columns = boston.feature_names   
data.head()
# %%
data['PRICE'] = boston.target
# %%
data.info()
# %%
linhas, features = data.shape
print(f"O dataset tem {linhas} linhas\n")
print(f"Boston dataset tem {features} variáveis\n")
# %%
pd.set_option("precision", 2)
print('Descrição estatística dos dados')
data.describe()
# %%

# %%
# Se for usar as variáveis categóricas no modelo, deve-se usar aplicar algum
# método de encoding adequado ao tipo de categoria da variável categórica
# XGboost trata internamente dados faltantes
# XGboost é não paramétrico - ou seja, não assume que as variáveis tenham
# alguma distribuição particular, não há necessidade de transformar o dado para
# distribuição normal.Não precisa padronizar os dados.

import xgboost as xgb 
from sklearn.metrics import mean_squared_error 
import numpy as np  
# %%
#! Separando a variável target e as variáveis independentes usando .iloc

X, y = data.iloc[:, :-1], data.iloc[:, -1]
print(X.shape)
print(len(y))
# %%
#! Convertendo o dataset em uma estrutura de dados otimizada chamada Dmatriz
#! que XGboost aceita e permite ganhos de performance e eficiência.
data_dmatrix = xgb.DMatrix(data = X, label = y)
# %%
#! XGboost hyperparameters
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
# %%
#! Instanciando o objeto xgb.Regressor()
xgb_reg = xgb.XGBRFRegressor(
    objective = 'reg:squarederror',
    colsample_bytree = 0.3,
    learning_rate=0.1,
    max_depth = 5,
    alpha = 10, 
    n_estimators = 10
)
# %%
xgb_reg.fit(X_train, y_train)
preds = xgb_reg.predict(X_test)
# %%
rmse = np.sqrt(mean_squared_error(y_test, preds))
print(f"RMSE: {rmse:.2f}")
# %%
#! k-fold Cross Validation using XGBoost
params = {
    "objective"              : "reg:squarederror",
    "colsample_bytree"       :  0.3,
    "learning_rate"          :  0.1,
    "max_depth"              :  5,
    "alpha"                  : 10
          }


cv_results = xgb.cv(
    dtrain = data_dmatrix,
    params=params,
    nfold=3,
    num_boost_round=50,     # usando no lugar do n_estimators(trees) 
    early_stopping_rounds=10,
    metrics="rmse",
    as_pandas=True,
    seed = 123
    )

cv_results.head()
# %%
#! Extraindo e printando o boosting com a métrica final
print((cv_results['test-rmse-mean']).tail(1))
# %%
# Bem melhor que o resultado anterior obtido que foi de RMSE = 22.22
# Pode-se tentar usar o grid-search, random-search e Bayesian Optimization para
# tentar alcançar valores de hiperparametrização ainda melhores

#! Visualizando tree boosting e a importância das features
#! plot_tree() function to visualization

xgb_reg = xgb.train(
    params=params, 
    dtrain=data_dmatrix, 
    num_boost_round=10
    )
# %%
import matplotlib.pyplot as plt  
import graphviz
xgb.plot_tree(xgb_reg, num_trees=0)
plt.rcParams['figure.figsize'] = [80, 10]
plt.show()
# %%
#! Examinando a importancia de cada feature dentro do modelo
"""[resumo]
Uma maneira simples de fazer isso é contando o número de vezes que cada feature
sofre split em todos os rounds de boosting(trees) no modelo, e então visualizar
o resultado como gráfico de barras, com as features ordenadas de acordo com o 
número de vezes que elas apareceram.    
"""
xgb.plot_importance(xgb_reg)
plt.rcParams['figure.figsize'] = [6, 8]
plt.show()
