from typing import Union

class Currency:
    """
    id - Уникальный идентификатор
    num_code - Цифровой код
    char_code - Символьный код
    name - Название валюты
    value - Курс (число)
    nominal - Номинал (число)
    """

    def __init__(self, currency_id: str, num_code: str, char_code: str, name: str, value: Union[float, str],
                 nominal: int):
        self.__id: str = currency_id
        self.__num_code: str = num_code
        self.__char_code: str = char_code
        self.__name: str = name
        self.__value: float = self.__parse_value(value)
        self.__nominal: int = nominal

    def __parse_value(self, val: Union[float, str]) -> float:
        if isinstance(val, float):
            return val
        if isinstance(val, str):
            try:
                return float(val.replace(',', '.'))
            except ValueError:
                raise ValueError(f"Некорректное значение курса: '{val}'")
        raise TypeError("Значение курса должно быть числом или строкой.")

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id_val: str):
        if not isinstance(id_val, str):
            raise TypeError("ID валюты должен быть строкой.")
        if len(id_val) >= 1:
            self.__id = id_val
        else:
            raise ValueError('ID валюты не может быть пустым.')

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, num_code: str):
        if not isinstance(num_code, str):
            raise TypeError("Цифровой код должен быть строкой.")
        self.__num_code = num_code

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, char_code: str):
        if not isinstance(char_code, str):
            raise TypeError("Символьный код должен быть строкой.")
        if len(char_code.strip()) != 3:
            raise ValueError("Символьный код должен состоять из 3 символов.")
        self.__char_code = char_code.upper()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Название валюты должно быть строкой.")
        if len(name) < 1:
            raise ValueError("Название валюты не может быть пустым.")
        self.__name = name

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, val: Union[float, str]):
        self.__value = self.__parse_value(val)

    @property
    def nominal(self) -> int:
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal: Union[int, str]):
        if isinstance(nominal, str):
            try:
                nominal = int(nominal)
            except ValueError:
                raise TypeError("Номинал должен быть целым числом.")

        if not isinstance(nominal, int):
            raise TypeError("Номинал должен быть целым числом.")

        if nominal <= 0:
            raise ValueError("Номинал должен быть положительным числом.")
        self.__nominal = nominal

