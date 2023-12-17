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

    @abstractproperty
    @abstractmethod
    def first_name(self):
        pass

    @first_name.setter
    @abstractmethod
    def set_first_name(self):
        pass

    @abstractproperty
    @abstractmethod
    def last_name(self):
        pass

    @last_name.setter
    @abstractmethod
    def set_last_name(self):
        pass

    @abstractproperty
    @abstractmethod
    def death_date(self):
        pass

    @death_date.setter
    @abstractmethod
    def set_death_date(self):
        pass

    @abstractproperty
    @abstractmethod
    def birth_date(self):
        pass

    @birth_date.setter
    @abstractmethod
    def set_birth_date(self):
        pass
