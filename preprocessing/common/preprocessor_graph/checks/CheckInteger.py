from preprocessing.common.preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np
import math


class CheckInteger(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        sample = df_column.dropna().sample(math.ceil(0.1 * df_column.size))
        diff = np.sum(sample - np.trunc(sample))
        integer_like = diff == 0

        return (df_column.dtype in [np.dtype(int), np.int8, np.int16, np.int32, np.int64,
                                   np.int_, np.intc, np.intp,
                                   np.uint8, np.uint16, np.uint32, np.uint64,
                                   np.uintc, np.uintp, int]) or integer_like

    def get_preprocessor(self, col_name):
        return None
