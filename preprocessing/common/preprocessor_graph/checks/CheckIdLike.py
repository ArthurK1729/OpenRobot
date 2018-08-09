from preprocessing.common.preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np
import math


class CheckIdLike(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        sample = df_column.dropna().sample(math.ceil(0.1 * df_column.size))
        # If the number of distincts comprises more than 90% of the overall sample, then it's safe to assume
        # that we're dealing with a column of integer IDs
        too_many_distincts = sample.count()*0.9 < sample.nunique()

        return too_many_distincts

    def get_preprocessor(self, col_name):
        return None
