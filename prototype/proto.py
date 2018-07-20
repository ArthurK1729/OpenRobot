import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import config
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

seed = 7
test_size = config.test_size

dataset = pd.read_csv('test_data\pima-indians-diabetes.csv', header=None)

X = dataset.iloc[:, 0:8]
Y = dataset.iloc[:, 8]

X_train, X_test, Y_train, Y_test \
= train_test_split(X, Y, test_size=test_size, random_state=seed)
model = GridSearchCV(XGBClassifier(),
                   config.model_parameters['XGBoostClassifier'],
                   scoring = 'roc_auc',
                   verbose= 2, refit=True)

model.fit(X_train, Y_train)

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(Y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
