import requests

test_data = [
    ("customer_email=test@mail.com&customer_date=11.11.2011", "CustomerForm"),
    ("user_email=test@mail.com&user_register_date=2022-12-10", "UserRegister"),
    (
        "new_email=test@mail.com&new_order_date=2022-12-12",
        {"new_email": "email", "new_order_date": "date"},
    ),
]
test_url = "http://127.0.0.1:8000/get_form/"
for count, data in enumerate(test_data):
    print(f"Test request {count+1}\nInput data: {data[0]}")
    test_response = requests.post(test_url, data=data[0])
    if test_response.json() == data[1]:
        print("Ok(received the expected response)\n")
    else:
        print("Failure(received the unexpected response)\n")
