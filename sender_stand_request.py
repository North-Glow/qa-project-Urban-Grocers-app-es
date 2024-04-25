import requests
import data
import configuration

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response_user = post_new_user(data.user_body)


def post_new_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=response_user.json())

response_kit = post_new_kit(data.kit_body)

