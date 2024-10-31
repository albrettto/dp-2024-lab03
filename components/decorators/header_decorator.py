from interfaces.imessage import IMessage
from components.decorators.message_decorator import MessageDecorator


class HeaderDecorator(MessageDecorator):
    """Декоратор для добавления заголовка к сообщению."""

    def __init__(self, message: IMessage, header: str):
        """
        Инициализирует декоратор с сообщением и заголовком.

        Params:
            message (IMessage): Объект сообщения, к которому будет добавлен заголовок.
            header (str): Заголовок, который нужно добавить.
        """
        super().__init__(message)
        self._header = header

    def print(self):
        """Выводит заголовок и затем сообщение."""
        print(self.get_content())

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения с добавленным заголовком.

        Returns:
            str: Содержимое сообщения с добавленным заголовком.
        """
        return f"{self._header}\n{self._message.get_content()}"
