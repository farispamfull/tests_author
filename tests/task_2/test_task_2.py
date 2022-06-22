try:
    from task_2 import author
except ModuleNotFoundError:
    assert False, 'Проверьте что у вас есть файл author в каталоге task_2'


class TestContact:
    test_contact = {
        'name': "Михаил Булгаков",
        'phone': "2-03-27",
        'birthday': '15.05.1891',
        'address': "Россия, Москва, Большая Пироговская, дом 35б, кв. 6",
    }

    def test_init(self, message_error):
        assert getattr(author, 'Contact', False), message_error('add_class', 'Contact')
        assert callable(author.Contact), message_error('add_call_class', 'Contact')
        try:
            contact = author.Contact(**self.test_contact)
        except TypeError:
            assert False, message_error('add_correct_params', 'Contact', 4)
        for attr, value in self.test_contact.items():
            assert hasattr(contact, attr), message_error('add_attr', 'Contact', attr)
            assert getattr(contact, attr) == value, message_error('wrong_attr_value', 'Contact', attr)

    def test_show_contact(self, capsys, message_error, valid_show_contact_string):
        contact = author.Contact(**self.test_contact)
        assert hasattr(contact, 'show_contact'), message_error('has_method', 'Contact', 'show_contact')
        assert callable(contact.show_contact), message_error('attr_to_method', 'Contact', 'show_contact')
        capsys.readouterr()
        contact.show_contact()
        out, err = capsys.readouterr()
        assert out.strip() == valid_show_contact_string(**self.test_contact), message_error('wrong_method_value',
                                                                                            'Contact', 'show_contact')
