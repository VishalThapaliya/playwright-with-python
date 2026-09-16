def test_user_api_get(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status == 200
    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "Bret"
    print(data["id"])
    print(data["username"])

    print("Test completed successfully!!!")
    response.dispose()

def test_users_api_get_with_headers(playwright):
    request = playwright.request.new_context(
        extra_http_headers = {
            "Accept": "application/json",
        }
    )
    response = request.get("https://reqres.in/api/users")

    assert response.status == 200
    res_data = response.json()
    print(res_data)

    assert res_data["data"][2]["first_name"] == "Emma"
    print(res_data["data"][2]["first_name"])

    response.dispose()
    print("Test completed successfully")