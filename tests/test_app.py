from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_dev_retornar_ok_and_hello_world():
    client = TestClient(app)  # Arrenge

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello world'}  # Assert
