
from models.HumanModel.EntityInterface import EntityInterface
from datetime import datetime, date, time
import Gender


class Human(EntityInterface):

    def __init__(self, first_name: str, last_name: str, gender: Gender, birth_date: date, death_date: date):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._birth_date = birth_date
        self._death_date = death_date

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

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def set_gender(self, gender: Gender):
        self._gender = gender
