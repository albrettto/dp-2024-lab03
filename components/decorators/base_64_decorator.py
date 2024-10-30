import base64
from components.decorators.message_decorator import MessageDecorator


class Base64Decorator(MessageDecorator):
    """Декоратор для кодирования содержимого сообщения в Base64 формат."""

    def print(self):
        """Выводит закодированное в Base64 содержимое сообщения."""
        print(self.get_content())

    def get_content(self) -> str:
        """
        Возвращает содержимое сообщения, закодированное в Base64.

        Returns:
            str: Содержимое сообщения, закодированное в Base64 формате.
        """
        return base64.b64encode(self._message.get_content().encode("utf-8")).decode(
            "utf-8"
        )
