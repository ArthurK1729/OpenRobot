from preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np
import math
import re


class CheckString(PreprocessorCheckAbstractClass):
    def __init__(self):
        self.alphabet = re.compile('[A-Z]|[a-z]|\s')

    def check(self, df_column):
        if df_column.dtype == np.dtype(object):
            return self._string_like(df_column)

    def _string_like(self, df_column):
        # Get 10% of the data
        sample = df_column.dropna().sample(math.ceil(0.1*df_column.size))

        # Check that every entry of the sample is string like
        return all(self.alphabet.search(entry) for entry in sample)

    def get_preprocessor(self, col_name):
        return None
