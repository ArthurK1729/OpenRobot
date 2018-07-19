from models.xgboost.xgboost_classifier import XgboostClassifier
import pandas as pd
import os

if __name__ == '__main__':
    print('Execution started!')
    dataset = pd.read_csv(os.path.join('test_data', 'pima-indians-diabetes.csv'), header=None)
    model = XgboostClassifier(dataset)

    model.fit()
    model.predict()

    print('Generated code is: ' + model.to_code())
