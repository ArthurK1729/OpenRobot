from models.PrintableModelAbstractClass import PrintableModelAbstractClass

from models.xgboost.imports.imports import *
import models.xgboost.imports.imports
from sklearn.metrics import accuracy_score
import config
import inspect


class XgboostClassifier(PrintableModelAbstractClass):
    parameters = config.model_parameters['XGBoostClassifier']

    def __init__(self, X_train, X_test, Y_train, Y_test):
        model = GridSearchCV(XGBClassifier(), self.parameters,
                   scoring = 'roc_auc',
                   verbose= 2, refit=True)

        super().__init__(model,
                         X_train, X_test, Y_train, Y_test,
                         models.xgboost.imports.imports)

    def fit(self):
        self.model.fit(self.X_train, self.Y_train)

    def predict(self):
        y_pred = self.model.predict(self.X_test)
        predictions = [round(value) for value in y_pred]

        accuracy = accuracy_score(self.Y_test, predictions)
        print("Accuracy: %.2f%%" % (accuracy * 100.0))