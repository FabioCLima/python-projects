#train_model.py
import time

import numpy as np
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

from logger import log_config

#train_model.py

# loads the logger module
logger = log_config()

# reading the titanic dataset
df = sns.load_dataset('titanic')

# remove rows with missing values
df.dropna(inplace=True)

# Selects the quantitative variables
num_features = df.select_dtypes(include=np.number).drop('survived', axis=1).columns.tolist()
logger.info(f'Variáveis selecionadas para treino do modelo >>> {num_features}')

# Split the dataset in train set and test set
X_train, X_teste, y_train, y_test = train_test_split(df[num_features], df['survived'], random_state=24)

# Fit the model
start = time.time()
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
end = time.time()

# calculates the training execution time
t = np.round((end - start) / 60)
logger.info('Tempo de execução do treino >>> {p0} {p1}'.format(p0=t, p1='min' if t >= 1 else 'seg'))

# model evaluation
y_pred = clf.predict(X_teste)
score = f1_score(y_test, y_pred)
logger.info('Métrica usada >>> f1_score')
logger.info(f'Score do treino >>> {score:.2f}')
