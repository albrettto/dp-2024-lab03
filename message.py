from imessage import IMessage


class Message(IMessage):
    """Реализация интерфейса IMessage для работы с сообщениями."""

    def __init__(self, content: str):
        """Инициализирует объект Message с заданным содержимым."""
        self._content = content

    def print(self):
        """Выводит содержимое сообщения в консоль."""
        print(self._content)

    def get_content(self):
        """Возвращает содержимое сообщения."""
        return self._content
