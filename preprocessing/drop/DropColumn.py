from preprocessing.common.PrintablePreprocessorAbstractClass import PrintablePreprocessorAbstractClass
from preprocessing.drop.imports.imports import *
import preprocessing.drop.imports.imports
import inspect
import re


class DropColumn(PrintablePreprocessorAbstractClass):

    def __init__(self, col_name):
        super().__init__(col_name)
        self.imports_loc = preprocessing.drop.imports.imports

    def get_code(self):
        def extract_code(text):
            if type(text) == list:
                new_list = map(lambda line: re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', line
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              )).strip(), text)
                return "\n".join(new_list)

            elif type(text) == str:
                return re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', text
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              )).strip()

        return "\n".join(map(extract_code, [inspect.getsourcelines(self.transform)[0]]))

    def get_dependencies(self):
        return inspect.getsourcelines(self.imports_loc)[0]

    def transform(self, df):
        print(df)
        df = df.drop([self.col_name], axis=1)
        return df
