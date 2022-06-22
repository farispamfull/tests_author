import pytest

try:
    from task_4 import author
except ModuleNotFoundError:
    assert False, 'Проверьте что у вас есть файл author в каталоге task_4'


class TestMakeDividerOf:

    def test_make_divider_init(self, message_error):
        func = getattr(author, 'make_divider_of', False)
        assert func, message_error('add_func', 'make_divider_of')
        assert callable(func), message_error('add_call_func', 'make_divider_of')

    def test_make_divider_of_call(self):
        from task_4.author import make_divider_of

        try:
            make_divider_of(2)
        except TypeError:
            assert False, 'Проверьте, что make_divider_of принимает аргумент'

    def test_make_divider_of_return_call_func(self):
        from task_4.author import make_divider_of

        div = make_divider_of(2)
        assert callable(div), 'Проверьте, что make_divider_of возвращает функцию'
        try:
            div(2)
        except TypeError:
            assert False, 'Проверьте, что функция, которую возвращает make_divider_of, принимает аргумент'

    @pytest.mark.parametrize('args', [
        (2, 2), (2, 4), (4, 2), (10, 1)
    ])
    def test_make_divider_of_correct_work(self, args):
        from task_4.author import make_divider_of
        divider, dividend = args
        div = make_divider_of(divider)
        result = div(dividend)
        assert isinstance(result, float), f'проверьте, что осуществляется нецелочисленное деление'
        assert result == dividend / divider, (f'Проверьте, что функция division_operation правильно работает, '
                                              f'когда делитель {divider}, а делимое {dividend}')
