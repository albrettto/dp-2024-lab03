from imessage import IMessage
from decorators.message_decorator import MessageDecorator


class HeaderDecorator(MessageDecorator):
    def __init__(self, message: IMessage, header: str):
        super().__init__(message)
        self._header = header

    def print(self):
        print(self._header)
        self._message.print()

    def get_content(self):
        return f"{self._header}\n{self._message.get_content()}"
