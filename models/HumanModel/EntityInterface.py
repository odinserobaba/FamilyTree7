from abc import ABC, abstractmethod, abstractproperty


class EntityInterface(ABC):
    @abstractproperty
    @abstractmethod
    def ID(self):
        pass

    @ID.setter
    @abstractmethod
    def setID(self):
        pass

    @ID.getter
    @abstractmethod
    def setID(self):
        pass
