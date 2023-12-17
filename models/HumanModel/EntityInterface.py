from abc import ABC, abstractmethod, abstractproperty
from datetime import date
import Gender


class EntityInterface(ABC):

    @abstractproperty
    @abstractmethod
    def first_name(self):
        pass

    @first_name.setter
    @abstractmethod
    def set_first_name(self, first_name: str):
        pass

    @abstractproperty
    @abstractmethod
    def last_name(self):
        pass

    @last_name.setter
    @abstractmethod
    def set_last_name(self, last_name: str):
        pass

    @abstractproperty
    @abstractmethod
    def death_date(self) -> date:
        pass

    @death_date.setter
    @abstractmethod
    def set_death_date(self, death_date: date):
        pass

    @abstractproperty
    @abstractmethod
    def birth_date(self) -> date:
        pass

    @birth_date.setter
    @abstractmethod
    def set_birth_date(self, birth_date: date):
        pass

    @abstractproperty
    @abstractmethod
    def gender(self) -> Gender:
        pass

    @abstractmethod
    def set_gender(self, gender: Gender):
        pass
