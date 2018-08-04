from abc import ABC, abstractmethod
from typing import Type, List
import pandas as pd
from preprocessing.common.PrintablePreprocessorAbstractClass import PrintablePreprocessorAbstractClass


class PreprocessorCheckAbstractClass(ABC):
    """
    Every preprocessing checker must implement this abstract class
    """

    def __init__(self, parent_node, child_nodes):
        self.parent_node: Type[PreprocessorCheckAbstractClass] = parent_node
        self.child_nodes: List[Type[PreprocessorCheckAbstractClass]] = child_nodes

    @abstractmethod
    def check(self, df_column: Type[pd.Series]) -> bool:
        pass

    @abstractmethod
    def get_preprocessor(self) -> Type[PrintablePreprocessorAbstractClass]:
        pass
