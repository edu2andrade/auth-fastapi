def test_signup(client):
    # Test invalid password
    invalid_password = {
        "username": "Johnny23",
        "email": "johndoe@email.com",
        "password": "Password123"
    }
    response = client.post("/auth/signup", json=invalid_password)
    assert response.status_code == 400
    assert "Password must contain" in response.json()["detail"]

    # Test invalid email
    invalid_email = {
        "username": "Johnny23",
        "email": "johndoe@email",
        "password": "Password123!"
    }
    response = client.post("/auth/signup", json=invalid_email)
    assert response.status_code == 422  # Pydantic validation error
    error_detail = response.json()["detail"][0]
    assert "value_error" in error_detail["type"]
    assert "value is not a valid email address" in error_detail["msg"]

    # Test valid signup
    user_data = {
        "username": "Johnny23",
        "email": "johndoe@email.com",
        "password": "Password123!"
    }

    response = client.post("/auth/signup", json=user_data)
    response_data = response.json()

    assert response.status_code == 201
    assert "id" in response_data
    assert "username" in response_data
    assert "email" in response_data
    assert "access_token" in response_data
    assert "refresh_token" in response_data
    assert "password_hash" not in response_data
    