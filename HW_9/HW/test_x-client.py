from SQL import SQL
from API import API

api = API("https://x-clients-be.onrender.com")
db = SQL("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


def test_get_list_employee():
    company_id = api.get_id_company()
    api_result = api.api_get_employees_list(company_id)
    api_result = api_result.json()
    db_result = db.sql_get_list_employee(company_id)

    assert len(api_result) == len(db_result)


def test_add_new_employee():
    company_id = api.get_id_company()
    db.sql_add_new_employee('Alina', 'Kulikova',
                            '8 909 999 00 00', 'kitig69989@hapied.com', company_id, True)
    employee = api.api_get_employee(db.sql_get_id_employee())
    assert employee['firstName'] == 'Alina'
    assert employee['lastName'] == 'Kulikova'
    assert employee['phone'] == '8 909 999 00 00'
    assert employee['email'] == 'kitig69989@hapied.com'
    assert employee['companyId'] == company_id
    assert employee['isActive'] == True
    id = db.sql_get_id_employee()
    db.sql_delete_employee(id)


def test_edit_employee():
    company_id = api.get_id_company()
    db.sql_add_new_employee('Vrode', 'Pomenyalsa',
                            '89999999999', 'kitig69989@hapied.com', company_id, True)
    id = db.sql_get_id_employee()
    db.sql_edit_employee('Alina', 'Kulikova',
                         '8 000 000 00 00', company_id, False, id)
    employee = api.api_get_id_employee(id=id)
    assert employee['firstName'] == 'Alina'
    assert employee['lastName'] == 'Kulikova'
    assert employee['phone'] == '8 000 000 00 00'
    assert employee['companyId'] == company_id
    assert employee['isActive'] == False
    id = db.sql_get_id_employee()
    db.sql_delete_employee(id)
