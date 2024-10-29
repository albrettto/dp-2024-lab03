from decorators.message_decorator import MessageDecorator
from imessage import IMessage


class FooterDecorator(MessageDecorator):
    def __init__(self, message: IMessage, footer: str):
        super().__init__(message)
        self._footer = footer

    def print(self):
        self._message.print()
        print(self._footer)

    def get_content(self):
        return f"{self._message.get_content()}\n{self._footer}"
