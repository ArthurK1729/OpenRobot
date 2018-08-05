from preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np


class CheckInteger(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.dtype == np.dtype(int)

    def get_preprocessor(self):
        return None
