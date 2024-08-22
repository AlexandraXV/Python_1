import requests
import psycopg2

from sqlalchemy import create_engine, text

db_connect = ("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


class SQL:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def sql_get_list_employee(self, company_id):
        self.db = create_engine(db_connect)
        with self.db.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM employee WHERE id = :company_id"),
                {"company_id": company_id}
            )
            return result

    def sql_add_new_employee_insert(self):
        self.db = create_engine(db_connect).connect()
        sql = text(
            "insert into employee (first_name, last_name, phone, company_id, is_active) values (:first_name, :last_name, :phone, :company_id, :isActive)")
        rows = self.db.execute(sql, {'first_name': 'Alina',
                                     'last_name': 'Kulikova',
                                     'phone': '8 909 000 01 01',
                                     'company_id': 3880,
                                     'isActive': True})
        self.db.commit()
        return rows

    def sql_get_id_employee(self):
        self.db = create_engine(db_connect)
        with self.db.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM employee ORDER BY id DESC LIMIT 1"))
            return result
