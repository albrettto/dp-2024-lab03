from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class FooterDecorator(MessageDecorator):
    """Декоратор для добавления подписи к сообщению."""

    def __init__(self, message: IMessage, footer: str):
        """
        Инициализирует декоратор с сообщением и подписью.

        Params:
            message (IMessage): Объект сообщения, к которому будет добавлена подпись.
            footer (str): Подпись, которую нужно добавить.
        """
        super().__init__(message)
        self._footer = footer

    def print(self):
        """Выводит сообщение, а затем подпись."""
        print(self.get_content())

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения с добавленной подписью.

        Returns:
            str: Содержимое сообщения с добавленной подписью.
        """
        return f"{self._message.get_content()}\n{self._footer}"
