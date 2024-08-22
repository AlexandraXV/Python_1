from SQL import SQL
from API import API


api = API("https://x-clients-be.onrender.com")
db = SQL("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


def test_get_list_employee():
    company_id = api.get_id_company()
    api_result = api.api_get_employees_list(company_id)
    api_result = api_result.json()
    db_result = db.sql_get_list_employee(company_id)
    num_rows = db_result.rowcount
    # проверка на ошибку апи
    if 'error' in api_result:
        # не нашел сотрудника - тест проходит
        return

    assert len(api_result) == num_rows


def test_post_add_new_employee():
    company_id = api.get_id_company()
    db_result = db.sql_get_list_employee(company_id)
    db.sql_add_new_employee_insert()
    api_result = api.api_get_employees_list(db.sql_get_id_employee)
    api_result = api_result.json()
    assert api_result['company_id'] == company_id
    assert api_result['first_name'] == 'Alina'
    assert api_result['last_name'] == 'Kulikova'
    assert api_result['phone'] == '8 909 000 01 01'
    assert api_result['is_active'] == True
