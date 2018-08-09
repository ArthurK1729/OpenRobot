from preprocessing.common.preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass
from preprocessing.imputer.FloatImputerStep import FloatImputerStep


class CheckMissingFloats(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.hasnans

    def get_preprocessor(self, col_name):
        return FloatImputerStep(col_name)
