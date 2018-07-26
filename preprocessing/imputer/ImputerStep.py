from preprocessing.common.PrintablePreprocessorAbstractClass import PrintablePreprocessorAbstractClass
from preprocessing.imputer.imports.imports import *
import preprocessing.imputer.imports.imports
import inspect
import re


class ImputerStep(PrintablePreprocessorAbstractClass):

    def __init__(self, col_name):
        self.imports_loc = preprocessing.imputer.imports.imports
        self.col_name = col_name

    def get_code(self):
        def extract_code(text):
            if type(text) == list:
                new_list = map(lambda line: re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', line
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              .replace('df_imputed', """df_imputed_{}""".format(self.col_name.lower()))
                              )).strip(), text)
                return "\n".join(new_list)

            elif type(text) == str:
                return re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', text
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              .replace('df_imputed', """df_imputed_{}""".format(self.col_name.lower()))
                              )).strip()

        return "\n".join(map(extract_code, [inspect.getsourcelines(self.transform)[0]]))

    def get_dependencies(self):
        return inspect.getsourcelines(self.imports_loc)[0]

    def transform(self, df):
        imputer = Imputer(missing_values=np.nan, strategy='median', axis=0)
        df_imputed = imputer.fit_transform(df[[self.col_name]]).ravel()
        df = df.drop([self.col_name], axis=1)
        df['{}_imputed'.format(self.col_name)] = df_imputed
        return df
