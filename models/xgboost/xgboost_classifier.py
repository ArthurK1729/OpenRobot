from models import PrintableModelAbstractClass

class XgboostClassifier(PrintableModelAbstractClass):

    def __init__(self, X_train, X_test, Y_train, Y_test):
        super().__init__(self, X_train, X_test, Y_train, Y_test)

    def to_code(self):
        return """
        xgboost code goes here1
        """

    def get_dependencies(self):
        return [
            'from xgboost import XGBClassifier'
        ]

    def fit(self):
        pass

    def predict(self):
        pass