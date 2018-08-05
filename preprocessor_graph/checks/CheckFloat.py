from preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np


class CheckFloat(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.dtype in [np.dtype(float), np.float_, np.float16,
                                   np.float32, np.float64, np.cfloat, np.clongfloat,
                                   np.longfloat]

    def get_preprocessor(self):
        return None
