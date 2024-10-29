from datetime import datetime
from decorators.message_decorator import MessageDecorator
from imessage import IMessage


class DateDecorator(MessageDecorator):
    def __init__(self, message: IMessage, date: str = None):
        super().__init__(message)
        self._date = date if date else datetime.now().strftime("%d.%m.%Y")

    def print(self):
        self._message.print()
        print(self._date)

    def get_content(self):
        return f"{self._message.get_content()}\n{self._date}"
