class User:
    """
    id - Уникальный идентификатор
    name - Имя пользователя
    """

    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id_val: int):
        if not isinstance(id_val, int):
            raise TypeError("ID пользователя должен быть целым числом.")
        if id_val <= 0:
            raise ValueError("ID пользователя должен быть положительным числом.")
        self._id = id_val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_val: str):
        if not isinstance(name_val, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if len(name_val.strip()) < 1:
            raise ValueError('Имя пользователя не может быть пустым.')
        self._name = name_val.strip()