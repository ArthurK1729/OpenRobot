from preprocessing.common.preprocessor import Preprocessor
import os

if __name__ == '__main__':
    print('Execution started!')

    preprocessor = Preprocessor(os.path.join('test_data', 'one_hot_test.csv'))

    # model = XgboostClassifier(*preprocessor.get_splits())
    # model.fit()
    # model.predict()
    #
    # # Make sure not to duplicate imports
    dependencies_pool = set(preprocessor.get_dependencies())
                            # + model.get_dependencies())
    print("".join(dependencies_pool))
    print(preprocessor.get_code())
    # print(model.get_code())
