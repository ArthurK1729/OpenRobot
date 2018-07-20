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

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def get_model(self):
        pass

    def get_dependencies(self):
        return inspect.getsourcelines(self.imports_loc)[0]

    def get_code(self):
        def extract_code(text):
            if type(text) == list:
                new_list = map(lambda line: re.sub(r"""def.*""", '', line
                                                   .replace('self.', '')
                                                   .replace('return ', 'model = ')).strip(), text)
                return "\n".join(new_list)

            elif type(text) == str:
                return re.sub(r"""def.*""", '', text
                              .replace('self.', '')
                              .replace('return ', 'model = ')).strip()

        return "\n".join(map(extract_code, [inspect.getsource(self.get_model),
                                            inspect.getsourcelines(self.fit)[0],
                                            inspect.getsourcelines(self.predict)[0]]))

