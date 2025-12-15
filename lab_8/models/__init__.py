# models/__init__.py

from .author import Author
from .app import App
from .user import User
from .currency import Currency
from .user_currency import UserCurrency

# Список для удобного создания тестовых данных и имитации базы данных
MODELS = [Author, App, User, Currency, UserCurrency]