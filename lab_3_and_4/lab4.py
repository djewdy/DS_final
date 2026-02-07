import requests

def call_local_service(operation, a, b):
    url = f"http://127.0.0.1:5000/api/{operation}"
    params = {"a": a, "b": b}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"{operation.capitalize()}({a}, {b}) = {data['result']}")
    else:
        print(f"Error calling service: {response.text}")

if __name__ == "__main__":
    call_local_service("add", 10, 5)
    call_local_service("subtract", 10, 5)
    call_local_service("multiply", 10, 5)
    call_local_service("divide", 10, 5)