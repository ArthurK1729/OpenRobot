import yaml
import pandas as pd

from preprocessing.common.preprocessor_graph.checks import *

class PreprocessorGraph:
    def __init__(self, path_to_data):
        with open('C:\\Users\\Arthur\\PycharmProjects\\Open_Robot\\preprocessing\\common\\preprocessor_graph\\common\\checker_steps.yaml') \
                as file:
            self._graph = yaml.load(file.read())

        self.df = pd.read_csv(path_to_data)

    def _get_class_obj_from_name(self, class_name):
        if class_name not in globals():
            raise ValueError(f'The class {class_name} has not been declared or imported. Make sure all the entries'
                             f' in the yaml file have corresponding checker classes '
                             f' and that they are properly imported.')
        return globals()[class_name]()

    def _do_check(self, col_name, graph, accumulator):
        for type_entry in graph:

            if type(type_entry) == dict:
                checker = self._get_class_obj_from_name(list(type_entry.keys())[0])
            else:
                checker = self._get_class_obj_from_name(type_entry)

            if checker.check(self.df[col_name]):
                print(str(checker), ' for ', col_name)
                accumulator.append(checker.get_preprocessor(col_name))

                # If dict, keep traversing
                if type(type_entry) == dict:
                    return self._do_check(col_name, type_entry[list(type_entry.keys())[0]], accumulator)
                else:
                    return accumulator

    def _flat_map(self, to_flatten):
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

    def get_preprocessing_steps(self):
        col_steps = list()

        for col_name in self.df.columns:
            col_steps.append(self._do_check(col_name, self._graph, []))

        print(col_steps)
        preprocessing_steps = self._flat_map(col_steps)
        print(preprocessing_steps)

        return preprocessing_steps
