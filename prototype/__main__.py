import pandas as pd
import numpy as np
from sklearn.preprocessing import quantile_transform

# dataset = pd.read_csv('..\\test_data\pima-indians-diabetes.csv', header=None)
#
# # quantile_transform(X, n_quantiles=10, random_state=0)
# print(quantile_transform(dataset[1], n_quantiles=10, random_state=0).head())

from preprocessor_graph.common.PreprocessorGraph import PreprocessorGraph
from preprocessor_graph.checks import *

# Temp imports
from preprocessor_graph.checks.CheckInteger import CheckInteger
from preprocessor_graph.checks.CheckFloat import CheckFloat
from preprocessor_graph.checks.CheckString import CheckString


if __name__ == '__main__':
    preprocessor_graph = PreprocessorGraph()
    graph = preprocessor_graph.graph

    # print(graph)

    path_to_data = """C:\\Users\\Arthur\\PycharmProjects\\Open_Robot\\test_data\\test_data.csv"""

    df = pd.read_csv(path_to_data)

    def get_class_obj_from_name(class_name):
        return globals()[class_name]()

    # Build the recursive checker here
    for col in df.columns:
        for type_entry in graph:
            checker = get_class_obj_from_name(list(type_entry.keys())[0])
            if checker.check(df[col]):
                print(str(checker), ' for ', col)
                break

    #
    # def do_check():
    #     pass

