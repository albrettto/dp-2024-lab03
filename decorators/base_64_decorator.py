import base64
from decorators.message_decorator import MessageDecorator


class Base64Decorator(MessageDecorator):
    """Декоратор для кодирования содержимого сообщения в Base64 формат."""

    def print(self):
        """Выводит закодированное в Base64 содержимое сообщения."""
        encoded_content = base64.b64encode(self.get_content().encode("utf-8")).decode(
            "utf-8"
        )
        print(encoded_content)

    def get_content(self):
        """Возвращает содержимое сообщения, закодированное в Base64."""
        return base64.b64encode(self._message.get_content().encode("utf-8")).decode(
            "utf-8"
        )
