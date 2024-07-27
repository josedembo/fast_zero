from http import HTTPStatus


def test_root_dev_retornar_ok_and_hello_world(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello world'}  # Assert


def test_html_dev_retornar_ok_and_hmtl_text(client):
    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """<html>
        <head>
            <title>
                Olá Mundo
            </title>
        </head>
        <body>
            <h1>
                Olá Mundo
            <h1>
        </body>
    </html>"""
    )


def test_create_user(client):
    response = client.post(
        '/users/',  # Act
        json={
            'username': 'usertest',
            'password': 'passtest',
            'email': 'test@mail.com',
        },
    )
    # assert: Is status codes 201?
    assert response.status_code == HTTPStatus.CREATED

    # asser: Is retorded the rigth user data filds?
    assert response.json() == {
        'id': 1,
        'username': 'usertest',
        'email': 'test@mail.com',
    }
