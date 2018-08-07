from preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np
import math
from .CheckFloat import CheckFloat

class CheckInteger(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        if CheckFloat().check(df_column):
            sample = df_column.dropna().sample(math.ceil(0.1 * df_column.size))
            diff = np.sum(sample - np.trunc(sample))
            if diff == 0:
                return True

        return df_column.dtype in [np.dtype(int), np.int8, np.int16, np.int32, np.int64,
                                   np.int_, np.intc, np.intp,
                                   np.uint8, np.uint16, np.uint32, np.uint64,
                                   np.uintc, np.uintp, int]

    def get_preprocessor(self, col_name):
        return None
