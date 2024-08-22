import requests

body = {
    "id": 0,
    "firstName": "string",
    "lastName": "string",
    "middleName": "string",
    "companyId": 0,
    "email": "string",
    "url": "string",
    "phone": "string",
    "birthdate": "2024-08-22T14:05:53.814Z",
    "isActive": True
}


class API:
    def __init__(self, url):
        self.url = url

    def api_get_token(self, user='raphael', password='cool-but-crude'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    def get_id_company(self):
        resp = requests.get(self.url + '/company')
        company_id = resp.json()
        return company_id[-1]['id']

    def api_get_employees_list(self, company_id):
        resp = requests.get(self.url + '/employee' + str(company_id))
        return resp

    def api_post_employee(self):
        headers = {'x-client-token': self.api_get_token()}
        resp = requests.post(self.url + '/employee',
                             headers=headers, json=body)
        return resp

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
