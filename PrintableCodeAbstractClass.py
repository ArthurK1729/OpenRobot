from abc import ABC, abstractmethod

class PrintableCodeAbstractClass(ABC):
    """
    Parent abstract class for other abstract classes that correspond to printable code
    """

    @abstractmethod
    def to_code(self):
        pass

    @abstractmethod
    def get_depedencies(self):
        pass