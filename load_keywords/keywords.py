
from abc import ABC,abstractmethod

class Keywords(ABC):
    """Abstract Class in order to create an interface to differents methods to save keywords like a database or file
    """

    @abstractmethod
    def load_keywords(self):
        pass
    
    @abstractmethod
    def save_keyword(self):
        pass
    
    @abstractmethod
    def delete_keyword(self):
        pass