import requests
import psycopg2

from sqlalchemy import create_engine, text

db_connect = ("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


class SQL:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    # получить последнее айди компании
    def sql_last_company_id(self):
        self.db = create_engine(db_connect)
        with self.db.connect() as connection:
            result = connection.execute(
                text("select id from company order by id desc limit 1")
            )
            return result.fetchall()

    # получить список сортрудников
    def sql_get_list_employee(self, company_id):
        with self.db.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM employee WHERE id = :company_id"),
                {"company_id": company_id}
            )
            return result.fetchall()

    # добавить нового сотруднка
    def sql_add_new_employee(self, first_name, last_name, phone, email, company_id, is_active):
        with self.db.connect() as connection:
            employee_data = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email,
                'company_id': company_id,
                'is_active': is_active
            }
            rows = connection.execute(
                text("insert into employee (first_name, last_name, phone, company_id, is_active) values (:first_name, :last_name, :phone, :company_id, :is_active)"),
                employee_data)
        connection.commit()
        return rows

    # получить айди нового сотрудника
    def sql_get_id_employee(self):
        with self.db.connect() as connection:
            result = connection.execute(
                text("SELECT id FROM employee ORDER BY id DESC LIMIT 1"))
            return result.fetchone()[0]

    # изменить данные сотрудника
    def sql_edit_employee(self, first_name, last_name, phone, email, company_id, is_active):
        with self.db.connect() as connection:
            employee_data = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email,
                'company_id': company_id,
                'is_active': is_active
            }
            result = connection.execute(
                text("update employee set first_name =:first_name, last_name =:last_name, phone =:phone, is_active =:is_active where id =:id"),
                employee_data
            )
            connection.commit()
            return result.fetchall()

    # delete employee
    def sql_delete_employee(self, id):
        with self.db.connect() as connection:
            delete = {'new_id': id}
            result = connection.execute(
                text("delete from employee where id =:new_id", delete)
            )
