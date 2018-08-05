from preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np


class CheckInteger(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.dtype in [np.dtype(int), np.int8, np.int16, np.int32, np.int64,
                                   np.int_, np.intc, np.intp,
                                   np.uint8, np.uint16, np.uint32, np.uint64,
                                   np.uintc, np.uintp, int]

    def get_preprocessor(self):
        return None
