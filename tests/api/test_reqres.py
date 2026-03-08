import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {"x-api-key": "reqres_3105a0c993024739a143fcb6f0e1fb4f"}

def test_get_list_users():
    response = requests.get(f"{BASE_URL}/users?page=1", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999", headers=HEADERS)
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "John Doe", "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data

def test_register_successful():
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "token" in response.json()

def test_register_missing_password():
    payload = {"email": "sydney@fife"}
    response = requests.post(f"{BASE_URL}/register", json=payload, headers=HEADERS)
    assert response.status_code == 400
    assert "error" in response.json()

def test_update_user():
    payload = {"name": "Jane Doe", "job": "Senior QA"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 204