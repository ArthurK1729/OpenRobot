from preprocessing.common.PrintablePreprocessorAbstractClass import PrintablePreprocessorAbstractClass
from preprocessing.log_trasform.imports.imports import *
import preprocessing.log_trasform.imports.imports
import inspect
import re


class LogTransformStep(PrintablePreprocessorAbstractClass):

    def __init__(self, col_name):
        super().__init__(col_name)
        self.imports_loc = preprocessing.log_trasform.imports.imports

    def get_code(self):
        def extract_code(text):
            if type(text) == list:
                new_list = map(lambda line: re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', line
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              .replace('df_log_transformed', """df_log_transformed_{}""".format(self.col_name.lower()))
                              )).strip(), text)
                return "\n".join(new_list)

            elif type(text) == str:
                return re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', text
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              .replace('df_log_transformed', """df_log_transformed_{}""".format(self.col_name.lower()))
                              )).strip()

        return "\n".join(map(extract_code, [inspect.getsourcelines(self.transform)[0]]))

    def get_dependencies(self):
        return inspect.getsourcelines(self.imports_loc)[0]

    def transform(self, df):
        df_log_transformed = df[self.col_name].apply(lambda x: np.log(x + 1))\
            .rename('log_transformed_{}'.format(self.col_name))
        df = df.drop([self.col_name], axis=1)
        df = df.join(df_log_transformed)
        return df
