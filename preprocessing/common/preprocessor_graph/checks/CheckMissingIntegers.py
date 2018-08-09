from preprocessing.common.preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
from preprocessing.imputer.IntegerImputerStep import IntegerImputerStep


class CheckMissingIntegers(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.hasnans

    def get_preprocessor(self, col_name):
        return IntegerImputerStep(col_name)
