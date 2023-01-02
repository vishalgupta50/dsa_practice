import requests as re



base_url = "https://reqres.in/"





class API_REQUESTS():

    def __init__(self, username="abcd", password="abcd"):
        self.username = username
        self.password = password
        self.base_url = "https://reqres.in/"


    def authenticate(self, username, pwd, base_url):
        result = re.get(base_url, auth=(username, pwd))
        return result.headers


    def get(self, request_url, prams=None, header=None):
        url = self.base_url + request_url
        result = re.get(url=url, params=prams, headers=header)
        return result

    def post(self, request_url, data, headers, param):
        result = re.post(url=base_url+request_url, data=data, headers=headers, params=param)
        return result

    # def delete(self, request_url, data, headers)


api_request = API_REQUESTS()
response = api_request.get("api/users", {'page': 3})
print(response.status_code)
print(response.json())






