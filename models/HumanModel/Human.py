
from models.HumanModel.EntityInterface import EntityInterface
from datetime import datetime, date, time


class Human(EntityInterface):
    @property
    def ID(self):
        self._id = 0

    @ID.setter
    def setID(self, id: int):
        self._id = id

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def set_first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def set_last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def death_date(self):
        return self._death_date

    @death_date.setter
    def set_death_date(self, death_date: date):
        self._death_date = date

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def set_birth_date(self, birth_datee: date):
        self._birth_date = date
