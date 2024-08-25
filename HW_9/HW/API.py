import requests
import allure


@allure.epic("API запросы")
class API:
    def __init__(self, url):
        self.url = url

    @allure.step("API. Получить токен {user} : {password}")
    def api_get_token(self, user='raphael', password='cool-but-crude'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    @allure.step("API. Получить последнее id компании")
    def get_id_company(self):
        resp = requests.get(self.url + '/company')
        company_id = resp.json()
        return company_id[-1]['id']

    @allure.step("API. Получить список сотрудников по {company_id}")
    def api_get_employees_list(self, company_id):
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp

    @allure.step("API. Получить нового сотрудника по {id}")
    def api_get_employee(self, id):
        headers = {'x-client-token': self.api_get_token()}
        resp = requests.get(self.url + '/employee/' + str(id),
                            headers=headers)
        return resp.json()

    @allure.step("API. Получить {id} сотрудника")
    def api_get_id_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
