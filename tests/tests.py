import base64
import unittest
from datetime import datetime

from components.decorators.base_64_decorator import Base64Decorator
from components.decorators.date_decorator import DateDecorator
from components.decorators.footer_decorator import FooterDecorator
from components.decorators.header_decorator import HeaderDecorator
from components.message import Message


class TestMessageDecorators(unittest.TestCase):
    """Тесты для проверки функциональности различных декораторов для сообщений."""

    def test_message(self):
        """Тестирует базовый класс Message: проверяет, что сообщение возвращает правильное содержимое."""
        message = Message("Привет")
        self.assertEqual(message.get_content(), "Привет")

    def test_header_decorator(self):
        """Тестирует HeaderDecorator: проверяет добавление заголовка к сообщению."""
        message = HeaderDecorator(Message("Привет"), "Друг")
        expected_content = "Друг\nПривет"
        self.assertEqual(message.get_content(), expected_content)

    def test_footer_decorator(self):
        """Тестирует FooterDecorator: проверяет добавление подписи к сообщению."""
        message = FooterDecorator(Message("Привет"), "С наилучшими пожеланиями")
        expected_content = "Привет\nС наилучшими пожеланиями"
        self.assertEqual(message.get_content(), expected_content)

    def test_header_and_footer(self):
        """Тестирует сочетание HeaderDecorator и FooterDecorator: проверяет добавление заголовка и подписи."""
        message = FooterDecorator(
            HeaderDecorator(Message("Привет"), "Друг"), "С наилучшими пожеланиями"
        )
        expected_content = "Друг\nПривет\nС наилучшими пожеланиями"
        self.assertEqual(message.get_content(), expected_content)

    def test_date_decorator_with_specific_date(self):
        """Тестирует DateDecorator с конкретной датой: проверяет добавление указанной даты к сообщению."""
        message = DateDecorator(Message("Привет"), "01.01.2023")
        expected_content = "Привет\n01.01.2023"
        self.assertEqual(message.get_content(), expected_content)

    def test_date_decorator_with_current_date(self):
        """Тестирует DateDecorator с текущей датой: проверяет добавление текущей даты к сообщению."""
        message = DateDecorator(Message("Привет"))
        expected_date = datetime.now().strftime("%d.%m.%Y")
        expected_content = f"Привет\n{expected_date}"
        self.assertEqual(message.get_content(), expected_content)

    def test_base64_decorator(self):
        """Тестирует Base64Decorator: проверяет кодирование содержимого сообщения в Base64."""
        message = Base64Decorator(Message("Привет"))
        expected_content = base64.b64encode("Привет".encode("utf-8")).decode("utf-8")
        self.assertEqual(message.get_content(), expected_content)

    def test_combined_decorators(self):
        """Тестирует комбинированное использование декораторов: проверяет вложенное декорирование сообщения."""
        message = Base64Decorator(
            DateDecorator(
                FooterDecorator(
                    HeaderDecorator(Message("Привет"), "Друг"),
                    "С наилучшими пожеланиями",
                )
            )
        )
        combined_content = (
            "Друг\nПривет\nС наилучшими пожеланиями\n"
            + datetime.now().strftime("%d.%m.%Y")
        )
        expected_content = base64.b64encode(combined_content.encode("utf-8")).decode(
            "utf-8"
        )
        self.assertEqual(message.get_content(), expected_content)


if __name__ == "__main__":
    unittest.main()
