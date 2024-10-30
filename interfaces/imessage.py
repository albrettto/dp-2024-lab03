from abc import ABC, abstractmethod


class IMessage(ABC):
    """Абстрактный интерфейс сообщения с методами для вывода и получения содержимого."""

    @abstractmethod
    def print(self):
        """Выводит сообщение."""
        pass

    @abstractmethod
    def get_content(self):
        """Возвращает содержимое сообщения."""
        pass
