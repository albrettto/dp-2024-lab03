from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class FooterDecorator(MessageDecorator):
    """Декоратор для добавления подписи к сообщению."""

    def __init__(self, message: IMessage, footer: str):
        """Инициализирует декоратор с сообщением и подписью."""
        super().__init__(message)
        self._footer = footer

    def print(self):
        """Выводит сообщение, а затем подпись."""
        self._message.print()
        print(self._footer)

    def get_content(self):
        """Возвращает содержимое сообщения с добавленной подписью."""
        return f"{self._message.get_content()}\n{self._footer}"
