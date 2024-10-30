from datetime import datetime
from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class DateDecorator(MessageDecorator):
    """Декоратор для добавления даты к сообщению."""

    def __init__(self, message: IMessage, date: str = None):
        """
        Инициализирует декоратор с сообщением и датой.

        Params:
            message (IMessage): Объект сообщения, к которому будет добавлена дата.
            date (str, optional): Дата в формате строки. Если не указана, используется текущая дата.
        """
        super().__init__(message)
        self._date = date if date else datetime.now().strftime("%d.%m.%Y")

    def print(self):
        """Выводит сообщение, а затем дату."""
        self._message.print()
        print(self._date)

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения с добавленной датой.

        Returns:
            str: Содержимое сообщения с добавленной датой.
        """
        return f"{self._message.get_content()}\n{self._date}"
