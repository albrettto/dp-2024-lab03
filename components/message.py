from interfaces.imessage import IMessage


class Message(IMessage):
    """Реализация интерфейса IMessage для работы с сообщениями."""

    def __init__(self, content: str):
        """
        Инициализирует объект Message с заданным содержимым.

        Params:
            content (str): Текст сообщения, который будет сохранен в объекте.
        """
        self._content = content

    def print(self):
        """Выводит содержимое сообщения в консоль."""
        print(self.get_content())

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения.

        Returns:
            str: Содержимое сообщения.
        """
        return self._content
