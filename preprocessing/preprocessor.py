import config
from .default_imports import *
import preprocessing.default_imports
from PrintableCodeAbstractClass import PrintableCodeAbstractClass
import re
import inspect
from functools import reduce


class Preprocessor(PrintableCodeAbstractClass):
    """
    Inspects the data and applies known heuristics to clean the data, apply binning, normalisation etc
    """
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.do_splits(path_to_data)
        self.applied_heuristics = []
        super().__init__()


    def do_splits(self, path_to_data):
        seed = 7
        test_size = config.test_size

        dataset = pd.read_csv(path_to_data, header=None)

        X = dataset.iloc[:, 0:8]
        Y = dataset.iloc[:, 8]

        self.X_train, self.X_test, self.Y_train, self.Y_test \
            = train_test_split(X, Y, test_size=test_size, random_state=seed)

    def get_splits(self):
        return self.X_train, self.X_test, self.Y_train, self.Y_test

    def get_code(self):
        def extract_code(text):
            if type(text) == list:
                new_list = map(lambda line: re.sub(r"""def.*""", '', line
                                                   .replace('self.', '')
                                                   .replace('return ', 'model = ')
                                                   .replace('path_to_data', "'{}'".format(self.path_to_data)))
                                                   .strip(), text)
                return "\n".join(new_list)

            elif type(text) == str:
                return re.sub(r"""def.*""", '', text
                              .replace('self.', '')
                              .replace('return ', 'model = ')).strip()

        return "\n".join(list(map(extract_code, [inspect.getsourcelines(self.do_splits)[0]])) +
                         list(map(lambda heuristic: heuristic.get_code(), self.applied_heuristics)))

    def get_dependencies(self):
        return inspect.getsourcelines(preprocessing.default_imports)[0] \
               + reduce(lambda h1, h2: h1 + h2, map(lambda heuristic: heuristic.get_dependencies(),
                                                    self.applied_heuristics), [])

