from common.PrintableCodeAbstractClass import PrintableCodeAbstractClass
from abc import abstractmethod


class PrintablePreprocessorAbstractClass(PrintableCodeAbstractClass):

    @abstractmethod
    def transform(self, df):
        pass
