from .author import Author

class App:
    """
    name - Название приложения.
    version - Версия приложения.
    author - Объект Author.
    """
    def __init__(self, name: str, version: str, author: Author):
        self.__name:  str = name
        self.__version: str = version
        self.__author: Author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Название приложения должно быть строкой.")
        if len(name) >= 1:
            self.__name = name
        else:
            raise ValueError('У приложения должно быть название')


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        if not isinstance(version, str):
            raise TypeError("Версия приложения должна быть строкой.")
        self.__version = version

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: Author):
        if not isinstance(author, Author):
            raise TypeError("Автор должен быть объектом класса Author.")
        self.__author = author