import pytest

try:
    from task_3 import author
except ModuleNotFoundError:
    assert False, 'Проверьте что у вас есть файл author в каталоге task_3'


class TestCacheArgs:

    @pytest.mark.parametrize('func_name', [
        'time_check',
        'cache_args',
        'long_heavy',
    ])
    def test_init_func(self, message_error, func_name):
        func = getattr(author, func_name, False)
        assert func, message_error('add_func', func_name)
        assert callable(func), message_error('add_call_func', func_name)

    @pytest.mark.parametrize('arguments', [

        (1, 1, 1, 1), (1, 2, 1, 2),
        (1, 2, 3, 4), (1,),
        (1, 2, 2, 1), (2, 2, 3),

    ])
    def test_cache_args_with_replace_call(self, mocker, arguments: tuple, message_error):
        from task_3.author import time_check, cache_args

        mock_long_heavy = mocker.patch('task_3.author.long_heavy')
        func = time_check(cache_args(mock_long_heavy))
        for args in arguments:
            func(args)
        assert mock_long_heavy.call_count == len(set(arguments)), message_error('wrong_cache_call', 'cash_args',
                                                                                arguments)
