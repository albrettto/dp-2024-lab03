from imessage import IMessage


class MessageDecorator(IMessage):
    def __init__(self, message: IMessage):
        self._message = message

    def print(self):
        self._message.print()

    def get_content(self):
        return self._message.get_content()
