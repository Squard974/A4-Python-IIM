import requests
from requests import HTTPError

from requests import Session

#methode avec Session

class TEST():
    
    def __init__ (self):
        
        self.session = Session()
        self.session.headers = {
            'x-api-key': "eff3180c-2cae-4bef-9a40-013ca522c279"
        }
        self.base_url = "https://9bnqhyqrq0.execute-api.eu-west-1.amazonaws.com/dev"

    def get_user (self):
        res = self.session.get(
            url=f"{self.base_url}/manageUser"
        )
        print(res.text)
        res.raise_for_status()

    def create_user (self, email):
        res = self.session.post(
            url=f"{self.base_url}/getToken",
            json={"email": email}
        )
        print(res.text)
        res.raise_for_status()
        

test = TEST()
email = "bbbb@example.com"  # Exemple d'email à envoyer
test.create_user(email)
test.get_user()

#methode avec requests

# try:
#     res = requests.post(
#         url="https://9bnqhyqrq0.execute-api.eu-west-1.amazonaws.com/dev/manageUser",
#         headers={
#             'x-api-key': "eff3180c-2cae-4bef-9a40-013ca522c279"
#         }
#     )
#     res.raise_for_status()
#     print('1', res.text, res.status_code)

# except HTTPError as error:
#     print(error.response.status_code, error.response.text)
# except Exception as error:
#     print('2', error)