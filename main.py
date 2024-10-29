from message import Message
from decorators.header_decorator import HeaderDecorator
from decorators.footer_decorator import FooterDecorator
from decorators.date_decorator import DateDecorator
from decorators.base_64_decorator import Base64Decorator


# Пример использования
if __name__ == "__main__":
    message = Message("С днем рождения!")
    message.print()
    print()

    message = HeaderDecorator(Message("С днем рождения!"), "Дорогой мой друг!")
    message.print()
    print()

    message = FooterDecorator(HeaderDecorator(Message("С днем рождения!"), "Дорогой мой друг!"), "Твой брат")
    message.print()
    print()

    message = DateDecorator(FooterDecorator(HeaderDecorator(Message("С днем рождения!"), "Дорогой мой друг!"), "Твой брат"), "04.04.2001")
    message.print()
    print()

    message = DateDecorator(FooterDecorator(HeaderDecorator(Message("С днем рождения!"), "Дорогой мой друг!"), "Твой брат"))
    message.print()
    print()

    message = Base64Decorator(DateDecorator(FooterDecorator(HeaderDecorator(Message("С днем рождения!"), "Дорогой мой друг!"), "Твой брат")))
    message.print()