from preprocessing.common.preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np
import math


class CheckFloat(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        sample = df_column.dropna().sample(math.ceil(0.1 * df_column.size))
        diff = np.sum(sample - np.trunc(sample))
        float_like = diff != 0

        return (df_column.dtype in [np.dtype(float), np.float_, np.float16,
                                    np.float32, np.float64, np.cfloat, np.clongfloat,
                                    np.longfloat]) or float_like

    def get_preprocessor(self, col_name):
        return None
