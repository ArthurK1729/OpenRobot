from preprocessing.common.preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
import numpy as np
import math
import re
from preprocessing.drop.DropColumn import DropColumn


class CheckDropColumn(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return True

    def get_preprocessor(self, col_name):
        return DropColumn(col_name)
