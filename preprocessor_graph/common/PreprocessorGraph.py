import yaml


class PreprocessorGraph:
    def __init__(self):
        with open('C:\\Users\\Arthur\\PycharmProjects\\Open_Robot\\preprocessor_graph\\common\\checker_steps.yaml') \
                as file:
            self._graph = yaml.load(file.read())

    @property
    def graph(self):
        return self._graph
