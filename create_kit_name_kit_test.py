import data
import sender_stand_request

def get_kit_name(new):
    this_body = data.kit_body.copy()
    this_body["name"] = new
    return this_body


def assert_positivo(kit_body):
    kit_name = get_kit_name(kit_body)
    response = sender_stand_request.post_new_kit(kit_name)
#    print(response)
#    print(response.json()["name"])
    assert response.status_code == 201
    assert response.json()["name"] == kit_body


def assert_negativo(kit_body):
    response = sender_stand_request.post_new_kit(kit_body)
#    print(response)
#    print(name)
    assert response.status_code == 400


def test_kit_body_name_1():
    assert_positivo("a")
#print(test_kit_body_name_1())


def test_kit_body_name_511():
    assert_positivo("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
#print(test_kit_body_name_511())


def test_kit_body_name_0():
    assert_negativo("")
#print(test_kit_body_name_0())


def test_kit_body_name_512():
    assert_negativo("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
#print(test_kit_body_name_512())

def test_kit_body_name_ce():
    assert_positivo('"№%@",')
#print(test_kit_body_name_ce())

def test_kit_body_name_sp():
    assert_positivo(" A Aaa ")
#print(test_kit_body_name_sp())

def test_kit_body_name_num():
    assert_positivo("123")
#print(test_kit_body_name_num())

def test_kit_body_name_nume():
    assert_negativo(1234)
#print(test_kit_body_name_nume())

def test_kit_body_name_wo():
    assert_negativo()
#print(test_kit_body_name_wo())


def test_get_new_user_token():
    assert sender_stand_request.response_u.json()['authToken'] != ""