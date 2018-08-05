from preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np


class CheckString(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.dtype == np.dtype(str)

    def get_preprocessor(self):
        return None
