import pandas as pd
import os
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

parameters = {'objective':['binary:logistic'],
              'learning_rate': [0.05], #so called `eta` value
              'max_depth': [6],
              'min_child_weight': [11],
              'silent': [1],
              'subsample': [0.8],
              'colsample_bytree': [0.7],
              'n_estimators': [5], #number of trees, change it to 1000 for better results
              'missing':[-999],
              'seed': [1337]}


X = dataset.iloc[:, 0:8]
Y = dataset.iloc[:,8]



seed = 7
test_size = 0.33


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)


model = XGBClassifier()

clf = GridSearchCV(model, parameters,
                   scoring='roc_auc',
                   verbose=2, refit=True)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
predictions = [round(value) for value in y_pred]



accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))