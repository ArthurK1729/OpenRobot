model_parameters = {
    'XGBoostClassifier': {'objective': ['binary:logistic'],
                              'learning_rate': [0.05],  # so called `eta` value
                              'max_depth': [6],
                              'min_child_weight': [11],
                              'silent': [1],
                              'subsample': [0.8],
                              'colsample_bytree': [0.7],
                              'n_estimators': [5],  # number of trees, change it to 1000 for better results
                              'missing': [-999],
                              'seed': [1337]}
}