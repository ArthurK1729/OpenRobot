from PrintableCodeAbstractClass import PrintableCodeAbstractClass
from abc import abstractmethod
import inspect
import re

class PrintableModelAbstractClass(PrintableCodeAbstractClass):
    """
    Must be inherited and implemented by every model class
    """

    def __init__(self, model, X_train, X_test, Y_train, Y_test, imports_loc):
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test
        self.model = model
        self.imports_loc = imports_loc

        super().__init__()

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    def get_dependencies(self):
        return inspect.getsourcelines(self.imports_loc)[0]

    def get_code(self):
        return "\n".join(map(lambda x: str.strip(re.sub(r"""def.*""", '', inspect.getsource(x).replace('self.', ''))),
                             [self.fit, self.predict]))

