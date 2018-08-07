import pandas as pd
from functools import reduce
import numpy as np
from sklearn.preprocessing import quantile_transform

# dataset = pd.read_csv('..\\test_data\pima-indians-diabetes.csv', header=None)
#
# # quantile_transform(X, n_quantiles=10, random_state=0)
# print(quantile_transform(dataset[1], n_quantiles=10, random_state=0).head())

from preprocessor_graph.common.PreprocessorGraph import PreprocessorGraph

from preprocessor_graph.checks import *

if __name__ == '__main__':
    preprocessor_graph = PreprocessorGraph()
    execution_graph = preprocessor_graph.graph

    # print(graph)

    path_to_data = """C:\\Users\\Arthur\\PycharmProjects\\Open_Robot\\test_data\\test_data.csv"""

    df = pd.read_csv(path_to_data)

    def get_class_obj_from_name(class_name):
        if class_name not in globals():
            raise ValueError(f'The class {class_name} has not been declared or imported. Make sure all the entries'
                             f' in the yaml file have corresponding checker classes '
                             f' and that they are properly imported.')

        return globals()[class_name]()

    def do_check(col_name, graph, accumulator):
        for type_entry in graph:

            if type(type_entry) == dict:
                checker = get_class_obj_from_name(list(type_entry.keys())[0])
            else:
                checker = get_class_obj_from_name(type_entry)

            if checker.check(df[col_name]):
                print(str(checker), ' for ', col_name)
                accumulator.append(checker.get_preprocessor(col_name))

                # If dict, keep traversing
                if type(type_entry) == dict:
                    return do_check(col_name, type_entry[list(type_entry.keys())[0]], accumulator)
                else:
                    return accumulator

    def flat_map(to_flatten):
        def recurse(to_flatten, accumulator):
            for item in to_flatten:
                if item is None:
                    continue
                elif type(item) == list:
                    accumulator.extend(recurse(item, []))
                else:
                    accumulator.append(item)
            return accumulator

        return recurse(to_flatten, [])

    col_steps = list()

    for col_name in df.columns:
        col_steps.append(do_check(col_name, execution_graph, []))

    print(col_steps)
    print(flat_map(col_steps))




