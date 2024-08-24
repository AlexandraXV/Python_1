import requests


class API:
    def __init__(self, url):
        self.url = url

    # получить токен
    def api_get_token(self, user='raphael', password='cool-but-crude'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    # получить последнее айди компании
    def get_id_company(self):
        resp = requests.get(self.url + '/company')
        company_id = resp.json()
        return company_id[-1]['id']

    # получить список сотрудников
    def api_get_employees_list(self, company_id):
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp

    # добавить нового сотрудника
    def api_get_employee(self, id):
        headers = {'x-client-token': self.api_get_token()}
        resp = requests.get(self.url + '/employee/' + str(id),
                            headers=headers)
        return resp.json()

    # получить айди сотрудника
    def api_get_id_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    # изменить данные сотрудника
    def api_edit_employee(self, id, new_lastName, new_email, new_url, new_phone,
                          new_isActive):
        employee = {
            "lastName": new_lastName,
            "email": new_email,
            "url": new_url,
            "phone": new_phone,
            "isActive": new_isActive
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(id),
                              json=employee, headers=my_headers)
        return resp.json()
