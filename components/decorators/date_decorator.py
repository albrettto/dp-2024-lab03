from datetime import datetime
from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class DateDecorator(MessageDecorator):
    """Декоратор для добавления даты к сообщению."""

    def __init__(self, message: IMessage, date: str = None):
        """Инициализирует декоратор с сообщением и датой."""
        super().__init__(message)
        self._date = date if date else datetime.now().strftime("%d.%m.%Y")

    def print(self):
        """Выводит сообщение, а затем дату."""
        self._message.print()
        print(self._date)

    def get_content(self):
        """Возвращает содержимое сообщения с добавленной датой."""
        return f"{self._message.get_content()}\n{self._date}"
