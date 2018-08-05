import pandas as pd
import numpy as np
from sklearn.preprocessing import quantile_transform

# dataset = pd.read_csv('..\\test_data\pima-indians-diabetes.csv', header=None)
#
# # quantile_transform(X, n_quantiles=10, random_state=0)
# print(quantile_transform(dataset[1], n_quantiles=10, random_state=0).head())

from preprocessor_graph.common.PreprocessorGraph import PreprocessorGraph

preprocessor_graph = PreprocessorGraph()
graph = preprocessor_graph.graph

print(graph)