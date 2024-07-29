import time


def test_add_new_area(accounts_page, delete_record_after_test, other_random_data):
    start_count = accounts_page.table_rows.count()
    accounts_page.add_area(other_random_data['name'], other_random_data['number'])
    finish_count = accounts_page.table_rows.count()
    assert start_count + 1 == finish_count


def test_cancel_dialog_box(accounts_page):
    accounts_page.cancel_dialog_b0x()
    time.sleep(2)
    assert accounts_page.add_record.is_located()


def test_exit_dialog_box(accounts_page):
    accounts_page.exit_dialog_box()
    time.sleep(2)
    assert accounts_page.add_record.is_located()



def test_editing_area(accounts_page, add_new_record, other_random_data, delete_record_after_test):
    accounts_page.edit_table_element(add_new_record)
    accounts_page.editing_name_area.send_keys(other_random_data['name'])
    accounts_page.editing_number_area.send_keys(other_random_data['number'])
    accounts_page.editing_btn_save.click()
    time.sleep(2)
    assert accounts_page.get_number_by_name(other_random_data['name'])


def test_delete_area(accounts_page, add_new_record, new_random_data):
    accounts_page.delete_record(add_new_record)
    assert not accounts_page.get_number_by_name(new_random_data['name'])
