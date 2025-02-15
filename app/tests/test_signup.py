def test_signup(client):
    user_data = {
        "username": "Johnny23",
        "email": "johndoe@email.com",
        "password": "Password_123"
    }

    response = client.post("/auth/signup", json=user_data)
    response_data = response.json()

    assert response.status_code == 201
    assert "id" in response_data
    assert "username" in response_data
    assert "email" in response_data
    assert "access_token" in response_data
    assert "password_hash" not in response_data
    