import PrintableCodeAbstractClass
from PrintableCodeAbstractClass import PrintableCodeAbstractClass
from abc import abstractmethod

class PrintableModelAbstractClass(PrintableCodeAbstractClass):
    """
    Must be inherited and implemented by every model class
    """

    def __init__(self, model, X_train, X_test, Y_train, Y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test
        self.model = model

        super().__init__()

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass