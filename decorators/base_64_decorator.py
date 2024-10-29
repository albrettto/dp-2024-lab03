import base64
from decorators.message_decorator import MessageDecorator


class Base64Decorator(MessageDecorator):
    def print(self):
        encoded_content = base64.b64encode(self.get_content().encode("utf-8")).decode(
            "utf-8"
        )
        print(encoded_content)

    def get_content(self):
        return base64.b64encode(self._message.get_content().encode("utf-8")).decode(
            "utf-8"
        )
