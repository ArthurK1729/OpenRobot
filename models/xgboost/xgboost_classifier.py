from models.PrintableModelAbstractClass import PrintableModelAbstractClass
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

class XgboostClassifier(PrintableModelAbstractClass):
    parameters = {'objective': ['binary:logistic'],
                  'learning_rate': [0.05],  # so called `eta` value
                  'max_depth': [6],
                  'min_child_weight': [11],
                  'silent': [1],
                  'subsample': [0.8],
                  'colsample_bytree': [0.7],
                  'n_estimators': [5],  # number of trees, change it to 1000 for better results
                  'missing': [-999],
                  'seed': [1337]}

    def __init__(self, data):
        seed = 7
        test_size = 0.33
        model = GridSearchCV(XGBClassifier(), self.parameters,
                   scoring='roc_auc',
                   verbose=2, refit=True)


        X = data.iloc[:, 0:8]
        Y = data.iloc[:, 8]

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

        super().__init__(model, X_train, X_test, Y_train, Y_test)

    def to_code(self):
        return "\n".join([])

    def get_dependencies(self):
        return [
            'from sklearn.model_selection import train_test_split',
            'from sklearn.model_selection import GridSearchCV',
            'from xgboost import XGBClassifier',
            'from sklearn.metrics import accuracy_score'
        ]

    def fit(self):
        self.model.fit(self.X_train, self.Y_train)

    def predict(self):
        y_pred = self.model.predict(self.X_test)
        predictions = [round(value) for value in y_pred]

        accuracy = accuracy_score(self.Y_test, predictions)
        print("Accuracy: %.2f%%" % (accuracy * 100.0))