import config
from sklearn.model_selection import train_test_split

# Make this extend PrintableCode


class Preprocessor():
    """
    Inspects the data and applies known heuristics to clean the data, apply binning, normalisation etc
    """
    def __init__(self, data):
        seed = 7
        test_size = config.test_size

        X = data.iloc[:, 0:8]
        Y = data.iloc[:, 8]

        self.X_train, self.X_test, self.Y_train, self.Y_test \
            = train_test_split(X, Y, test_size=test_size, random_state=seed)

    def get_data(self):
        return [self.X_train, self.X_test, self.Y_train, self.Y_test]
