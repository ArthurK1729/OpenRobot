from abc import ABC, abstractmethod
import inspect


class PrintableCodeAbstractClass(ABC):
    """
    Parent abstract class for other abstract classes that correspond to printable code
    """

    @abstractmethod
    def get_code(self):
        pass

    @abstractmethod
    def get_dependencies(self):
        pass
