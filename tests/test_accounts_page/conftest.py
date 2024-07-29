import random

import pytest


@pytest.fixture
def new_random_data():
    return {
        'name': f'test{random.randint(10000, 99999)}',
        'number': random.randint(1, 10)
    }


@pytest.fixture
def other_random_data():
    return {
        'name': f'test{random.randint(100000, 999999)}',
        'number': random.randint(11, 20)
    }


@pytest.fixture
def delete_record_after_test(other_random_data, accounts_page):
    yield
    row_number = accounts_page.get_number_by_name(other_random_data['name'])
    accounts_page.delete_record(row_number)


@pytest.fixture
def add_new_record(new_random_data, accounts_page):
    accounts_page.add_area(new_random_data['name'], new_random_data['number'])
    row_number = accounts_page.get_number_by_name(new_random_data['name'])
    return row_number
