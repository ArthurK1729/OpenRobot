from preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np


class CheckFloat(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.dtype == np.dtype(float)

    def get_preprocessor(self):
        return None
