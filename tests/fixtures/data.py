import pytest


@pytest.fixture
def valid_show_contact_string():
    def wrapper(name, address, phone, birthday, *args, **kwargs):
        return f"{name} — адрес: {address}, телефон: {phone}, день рождения: {birthday}"
    return wrapper
