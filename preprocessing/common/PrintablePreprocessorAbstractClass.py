from common.PrintableCodeAbstractClass import PrintableCodeAbstractClass
from abc import abstractmethod


class PrintablePreprocessorAbstractClass(PrintableCodeAbstractClass):

    def __init__(self, col_name):
        self.col_name = col_name

    @abstractmethod
    def transform(self, df):
        pass

    def __str__(self):
        return str(self.__class__) + f"({self.col_name})"

    def __repr__(self):
        return str(self.__class__) + f"({self.col_name})"