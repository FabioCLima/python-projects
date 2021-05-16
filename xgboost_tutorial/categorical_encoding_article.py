# %%
import pandas as pd   
import numpy as np          
import seaborn as sns  
import matplotlib.pyplot as plt
from sklearn.utils import shuffle          



#! Dataset 

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers, na_values="?")
df.head()

#%%
df.info()
# %%
df.dtypes
# %%
feature_missing_data = []
for feature in df.columns.to_list():     
    aux = df[feature].isna().sum()
    if aux != 0:    
        feature_missing_data.append(feature)
        
print(feature_missing_data)

# %%
dados_ausentes = {'num-of-doors' : 'four',
                  'bore'         : df['bore'].mean(axis=0),
                  'horsepower'   : df['horsepower'].mean(axis=0),
                  'stroke'       : df['stroke'].mean(axis=0),
                  'peak-rpm'     : df['peak-rpm'].mean(axis=0)
                  }
df.fillna(dados_ausentes, inplace= True)
df.drop(['normalized-losses'], axis=1, inplace=True)
df.dropna(how = "any", axis = 0, inplace=True)

df.head()
# %%
df.isna().sum()

# %%
df.dtypes
# %%
df.shape
# %%
df['num-of-cylinders'].value_counts()
df['symboling'].value_counts()
# %%
df.drop('make', axis = 1, inplace=True)
features_categoricas = df.select_dtypes(exclude=[np.number]).columns.to_list()
features_categoricas
# %%
df.drop('symboling', axis = 1, inplace = True)
features_numericas = (df.drop('price', axis = 1)
                      .select_dtypes(include=[np.number]).columns.to_list())
features_numericas
# %%
features_nominais = ['fuel-type', 'aspiration', 'num-of-doors', 'body-style',
 'drive-wheels', 'engine-location', 'engine-type', 'fuel-system']
features_ordinais = [ 'num-of-cylinders']
import sklearn
#! Importando transformadores
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
#! Importando avaliadores de modelo de regressão
from sklearn.metrics import r2_score, mean_squared_error,  explained_variance_score, max_error, median_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV

#! Pipelines
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer


X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#! Pipeline de preprocessamento
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(missing_values=np.nan, strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('one-hot', OneHotEncoder(handle_unknown='ignore', sparse=False))
]) 

categorical_ord_transformer = Pipeline(steps = [
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('ordinal', OrdinalEncoder(handle_unknown='ignore'))
]) 

preprocessor = ColumnTransformer(
    transformers = [
        ('numerical', numeric_transformer, features_numericas),
        ('nominais', categorical_transformer, features_nominais),
        ('ordinal', categorical_ord_transformer, features_ordinais)
    ]
)
# %%
from sklearn.ensemble import RandomForestRegressor
model = Pipeline(steps = [
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(random_state=123))
        ])

model.fit(X_train, y_train)
# %%

#! Criando um dataframe com y_test, y_pred e residuals
y_pred = model.predict(X_test)
residuals = y_test - y_pred
df_pred_actual = pd.DataFrame({
    'predicted' : np.round(y_pred, 3),
    'actual' : np.round(y_test, 3),
    'residuals': np.round(residuals, 3)
})
df_pred_actual.reset_index(drop=True).head()

#%%
def RMSE(y_test, y_pred):
    """
    Calculates Root Mean Squared Error between the actual and the predicted labels.
    
    """
    RMSE = np.sqrt(mean_squared_error(y_test,y_pred))
    return RMSE


# Função para calcular as métricas do modelo
#
def show_scores(model):

    k = X.shape[1]
    n = len(y)
    y_pred = model.predict(X_test)
    

    # explained variance score
    evars = explained_variance_score(y_test, y_pred)
    # maximum residual error
    max_erro = max_error(y_test, y_pred)
    
    mse = mean_squared_error(y_test, y_pred)
   
    r2_training = model.score(X_train, y_train)
    r2_true = r2_score(y_test, y_pred)
    # r2 score ajustado para o número de features
    #  é a única métrica aqui que considera o problema de overfitting 
    r2_adjusted = 1 - ( (1 - r2_true) * (n - 1)/ (n - k - 1) )
    rmse = RMSE(y_test, y_pred)
    # mean absolute percentual error
    mape = np.mean( np.abs( (y_test - y_pred) / y_test ) ) * 100
     
    scores = {
        "model name" : model.named_steps['regressor'].__class__.__name__, 
        "R2_score(training data)" : np.round(r2_training, 3),
        "R2_score(test data)" : np.round(r2_true, 3),
        "R2_adjusted" : np.round(r2_adjusted, 3),
        "Explained Variance Score" : np.round(evars, 3),
        "Maximum Residual Error" : np.round(max_erro, 3),
        "Mean Square Error" : np.round(mse, 3),
        "Root Mean Square Error" : np.round(rmse, 3),
        "Mean Absolute Percentual Error(%)" : np.round(mape, 3)
    }
    results = pd.Series(scores)
    metricas = results.to_frame()
    return metricas
#%%
metricas = show_scores(model)
# %%
metricas
# %%
scores = cross_val_score(
    model, X_test, y_test, scoring="neg_mean_squared_error", cv = 10)
rmse_scores = np.sqrt(-scores)
rfr_rmse_scores = np.round(rmse_scores, 3)

def display_scores(scores):     
    print(f"Scores: {scores}")
    print(f"Mean: {scores.mean():.2f}")
    print(f"Standard deviation: {scores.std():.2f}")
# %%
display_scores(rfr_rmse_scores)
# %%
rfr_parms = {"regressor__max_features" : [2, 4, 6, 8, 10, 20],
             "regressor__max_depth"    : [3, 4, 5, 6, 7, 8]}
# %%
from sklearn.model_selection import KFold
def grid_search(regressor, param_grid, kfold):     
    
    search = GridSearchCV(Pipeline(steps = [
             ('preprocessor', preprocessor), 
             ('regressor', regressor)
    ]), 
    param_grid, 
    cv = kfold,
    scoring="neg_mean_squared_error",
    n_jobs=-1)
    search.fit(X, y)
    print(f"Melhores parâmetros: {search.best_params_}")
    print(f"Melhor score: {np.sqrt(-search.best_score_):.2f}")

# %%
kfold = KFold(n_splits = 5, shuffle = True, random_state = 123)
grid_search(RandomForestRegressor(random_state=123), rfr_parms, kfold)
# %%
grid_CV = GridSearchCV(Pipeline(steps = [
             ('preprocessor', preprocessor), 
             ('regressor', RandomForestRegressor(random_state=123))
    ]), 
    rfr_parms, 
    cv = kfold,
    scoring="neg_mean_squared_error",
    n_jobs=-1)

grid_CV.fit(X_train, y_train)
final_model = grid_CV.best_estimator_
metricas = show_scores(final_model)
metricas
# %%
