from preprocessing.common.PrintablePreprocessorAbstractClass import PrintablePreprocessorAbstractClass
from preprocessing.label_encoder.imports.imports import *
import preprocessing.label_encoder.imports.imports
import inspect
import re


class LabelEncoderStep(PrintablePreprocessorAbstractClass):

    def __init__(self, col_name):
        self.imports_loc = preprocessing.label_encoder.imports.imports
        self.col_name = col_name

    def get_code(self):
        def extract_code(text):
            if type(text) == list:
                new_list = map(lambda line: re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', line
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              .replace('df_encoded_labels', """df_encoded_labels_{}""".format(self.col_name.lower()))
                              )).strip(), text)
                return "\n".join(new_list)

            elif type(text) == str:
                return re.sub(r"""return.*""", '', re.sub(r"""def.*""", '', text
                              .replace('self.', '')
                              .replace('col_name', """'{}'""".format(self.col_name))
                              .replace('df_encoded_labels', """df_encoded_labels_{}""".format(self.col_name.lower()))
                              )).strip()

        return "\n".join(map(extract_code, [inspect.getsourcelines(self.transform)[0]]))

    def get_dependencies(self):
        return inspect.getsourcelines(self.imports_loc)[0]

    def transform(self, df):
        le = LabelEncoder()
        df_encoded_labels = pd.Series(le.fit_transform(df[self.col_name]), name="""{}_labels""".format(self.col_name))
        df = df.drop([self.col_name], axis=1)
        df = df.join(df_encoded_labels)
        return df
