from .user import User
from .currency import Currency


class UserCurrency:
    """
    id - Уникальный идентификатор записи.
    user - Объект User.
    currency - Объект Currency.
    """

    def __init__(self, user: User, currency: Currency, uc_id: int):
        self.user = user
        self.currency = currency
        self.id = uc_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_val: int):
        if not isinstance(id_val, int):
            raise TypeError("ID должен быть целым числом.")
        if id_val <= 0:
            raise ValueError("ID должен быть положительным числом.")
        self.__id = id_val

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user_obj: User):
        if not isinstance(user_obj, User):
            raise TypeError("Пользователь должен быть объектом класса User.")
        self.__user = user_obj

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency_obj: Currency):
        if not isinstance(currency_obj, Currency):
            raise TypeError("Валюта должна быть объектом класса Currency.")
        self.__currency = currency_obj
