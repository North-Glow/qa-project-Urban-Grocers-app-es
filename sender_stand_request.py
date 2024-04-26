import requests
import data
import configuration

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_kit(kit_body, token):
    data.auth_token["Content-Type"] = data.headers["Content-Type"]
    data.auth_token["Authorization"] = token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=data.auth_token)