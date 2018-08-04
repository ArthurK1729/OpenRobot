from abc import ABC, abstractmethod

class PreprocessorCheckAbstractClass(ABC):
    """
    Every preprocessing checker must implement this abstract class
    """

    @abstractmethod
    def check(self, df_column) -> bool:
        pass