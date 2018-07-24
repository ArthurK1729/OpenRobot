from common import config
from preprocessing.common.default_imports import *
import preprocessing.common.default_imports
from common.PrintableCodeAbstractClass import PrintableCodeAbstractClass
import re
import inspect
from functools import reduce

from preprocessing.one_hot_encoder.OneHotEncoderStep import OneHotEncoderStep
from preprocessing.label_encoder.LabelEncoderStep import LabelEncoderStep
from preprocessing.log_trasform.LogTransformStep import LogTransformStep


class Preprocessor(PrintableCodeAbstractClass):
    """
    Inspects the data and applies known heuristics to clean the data, apply binning, normalisation etc
    """
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.applied_heuristics = []
        self.X_train = pd.DataFrame()
        self.X_test = pd.DataFrame()
        self.Y_train = pd.DataFrame()
        self.Y_test = pd.DataFrame()

        self.load_data()
        self.df = self.df

        self.preprocess_columns()
        # Careful not to introduce data pollution during preprocessing. Only apply normalisation etc
        # individually to X_* and Y_*

        # self.do_splits()

        # Apply and check for heuristics applicability in this section
        super().__init__()

    def preprocess_columns(self):
        encoder1 = OneHotEncoderStep('new_col')
        encoder2 = LabelEncoderStep('Animals')
        encoder3 = LogTransformStep('continuous')
        self.applied_heuristics.extend([encoder1, encoder2, encoder3])
        self.apply_heuristics()
        print(self.df.head())



    def load_data(self):
        self.df = pd.read_csv(self.path_to_data)

    def apply_heuristics(self):
        for heuristic in self.applied_heuristics:
            self.df = heuristic.transform(self.df)

    def do_splits(self):
        X = self.df.iloc[:, 0:8]
        Y = self.df.iloc[:, 8]

        self.X_train, self.X_test, self.Y_train, self.Y_test \
            = train_test_split(X, Y, test_size=config.test_size, random_state=config.seed)

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

        return "\n".join(list(map(extract_code, [inspect.getsourcelines(self.load_data)[0],
                                                 inspect.getsourcelines(self.do_splits)[0]])) +
                         list(map(lambda heuristic: heuristic.get_code(), self.applied_heuristics)))

    def get_dependencies(self):
        return inspect.getsourcelines(preprocessing.common.default_imports)[0] \
               + reduce(lambda h1, h2: h1 + h2, map(lambda heuristic: heuristic.get_dependencies(),
                                                    self.applied_heuristics), [])

