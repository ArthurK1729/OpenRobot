from models.xgboost.xgboost_classifier import XgboostClassifier
from preprocessing.preprocessor import Preprocessor
import pandas as pd
import os

if __name__ == '__main__':
    print('Execution started!')
    dataset = pd.read_csv(os.path.join('test_data', 'pima-indians-diabetes.csv'), header=None)
    preprocessor = Preprocessor(dataset)
    model = XgboostClassifier(*preprocessor.get_data())
    model.fit()
    model.predict()

    print("Final code: \n" + str("".join(model.get_dependencies())))
    print(model.get_code())
