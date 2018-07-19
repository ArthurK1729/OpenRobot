import PrintableCodeAbstractClass
from abc import abstractmethod

class PrintableModelAbstractClass(PrintableCodeAbstractClass):
    """
    Must be inherited and implemented by every model class
    """

    def __init__(self, X_train, X_test, Y_train, Y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test

    @abstractmethod
    def fit(self, X_train, Y_train):
        pass

    @abstractmethod
    def predict(self, X_test, Y_test):
        pass