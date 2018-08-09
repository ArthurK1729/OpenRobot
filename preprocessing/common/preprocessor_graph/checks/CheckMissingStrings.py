from preprocessing.common.preprocessor_graph.common.PreprocessorCheckAbstractClass import PreprocessorCheckAbstractClass

class CheckMissingStrings(PreprocessorCheckAbstractClass):

    def check(self, df_column):
        return df_column.hasnans

    def get_preprocessor(self, col_name):
        return None
