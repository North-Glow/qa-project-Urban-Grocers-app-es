import requests
import data
import configuration

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response_u = post_new_user(data.user_body)
"""print(response_u.status_code)
print(response_u.json()['authToken'])"""


def post_new_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.auth_token)

"""response_k = post_new_kit(data.kit_body)
print(response_k.status_code)
print(response_k.json())"""

