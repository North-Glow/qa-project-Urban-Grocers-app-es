import data
import sender_stand_request


def get_kit_name(new):
    this_body = data.kit_body.copy()
    this_body["name"] = new
    return this_body


def assert_positivo(kit_body):
    kit_name = get_kit_name(kit_body)
    response = sender_stand_request.post_new_kit(kit_name,sender_stand_request.post_new_user(data.user_body).json())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body


def assert_negativo(kit_body):
    response = sender_stand_request.post_new_kit(kit_body,sender_stand_request.post_new_user(data.user_body).json())
    assert response.status_code == 400


def test_kit_body_name_1():
    assert_positivo("a")


def test_kit_body_name_511():
    assert_positivo("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_kit_body_name_0():
    assert_negativo("")


def test_kit_body_name_512():
    assert_negativo("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_kit_body_name_caracteres_especiales():
    assert_positivo('"№%@",')


def test_kit_body_name_espacios_en_nombre():
    assert_positivo(" A Aaa ")


def test_kit_body_name_numero_string():
    assert_positivo("123")


def test_kit_body_name_numero():
    assert_negativo(1234)


def test_kit_body_name_sin_cuerpo_en_solicitud():
    assert_negativo()


def test_get_new_user_token():
    assert sender_stand_request.post_new_user(data.user_body).json() != ""