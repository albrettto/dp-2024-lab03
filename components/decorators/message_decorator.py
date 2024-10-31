from interfaces.imessage import IMessage


class MessageDecorator(IMessage):
    """Базовый декоратор для класса IMessage, позволяющий расширять функциональность сообщений."""

    def __init__(self, message: IMessage):
        """
        Инициализирует декоратор с сообщением, которое требуется обернуть.

        Params:
            message (IMessage): Сообщение для обертывания и расширения функциональности.
        """
        self._message = message

    def print(self):
        """Выводит сообщение, делегируя вывод оборачиваемому сообщению."""
        print(self.get_content())

    def get_content(self) -> str:
        """
        Возвращает содержимое оборачиваемого сообщения.

        Returns:
            str: Содержимое оборачиваемого сообщения.
        """
        return self._message.get_content()
