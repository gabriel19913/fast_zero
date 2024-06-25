from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (garantir)
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'testusername',
        'id': 1,
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'id': 1,
                'email': 'test@test.com',
            }
        ]
    }


def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername',
        'id': 1,
        'email': 'test@test.com',
    }


def test_get_user_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    response = client.put(  # UserSchema
        '/users/1',
        json={
            'username': 'testusername2',
            'id': 1,
            'password': '123',
            'email': 'test@test.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername2',
        'id': 1,
        'email': 'test@test.com',
    }


def test_update_user_not_found(client):
    response = client.put(  # UserSchema
        '/users/2',
        json={
            'username': 'testusername2',
            'id': 1,
            'password': '123',
            'email': 'test@test.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_delete_user_not_found(client):
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
