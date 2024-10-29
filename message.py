from imessage import IMessage


class Message(IMessage):
    def __init__(self, content):
        self._content = content

    def print(self):
        print(self._content)

    def get_content(self):
        return self._content
