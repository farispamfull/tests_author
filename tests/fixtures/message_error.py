import pytest


class MessageErrorStrategy:

    @staticmethod
    def resolve(attr, *args, **kwargs):
        msg_error = MessageErrorStrategy._attr_map(attr)
        return msg_error(*args, **kwargs)

    @classmethod
    def _attr_map(cls, attr):
        value = getattr(cls, attr, None)
        if not value:
            raise AttributeError(attr)
        return value

    @staticmethod
    def add_class(class_name):
        return f'Проверьте, что у вас добавлен класс {class_name}'

    @staticmethod
    def add_attr(class_name, attr):
        return f'Проверьте, что у класса {class_name} есть свойство {attr}'

    @staticmethod
    def add_method(class_name, method):
        return f'Проверьте, что у класса {class_name}  есть метод {method}'

    @staticmethod
    def attr_to_method(class_name, method):
        return f'Проверьте, что у класса {class_name}  {method} является методом, а не свойством'

    @staticmethod
    def add_call_class(class_name):
        return f'проверьте, что {class_name} имеет метод __init__'

    @staticmethod
    def add_call_func(func_name):
        return f'проверьте, что {func_name} является функцией'

    @staticmethod
    def add_correct_params(class_name, count):
        current_str = 'обязательными' if count > 1 else 'обязательным'
        return f'Проверьте, что класс {class_name} инициализируется с {count} {current_str} параметрами'

    @staticmethod
    def wrong_attr_value(class_name, attr):
        return f'Проверьте что класс у {class_name} правильно присваивается свойство {attr}'

    @staticmethod
    def wrong_method_value(class_name, method):
        return f'Проверьте что класс у {class_name} правильно работает метод {method}'

    @staticmethod
    def wrong_cache_call(func, arguments):
        arguments = ', '.join(map(str, arguments))
        return (f'Проверьте, что декоратор {func} правильно кеширует, '
                f'когда происходят последовательные вызовы с этими аргументами {arguments}')

    @staticmethod
    def add_func(func):
        return f'Проверьте, что у вас есть функция {func}'



@pytest.fixture
def message_error():
    def wrapper(attr, *args, **kwargs):
        message: str = MessageErrorStrategy.resolve(attr, *args, **kwargs)
        return message

    return wrapper
