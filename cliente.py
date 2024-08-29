import requests

URL_BASE = "http://127.0.0.1:8000"

def get_usuario():
    response = requests.get(URL_BASE + "/usuario/2")
    print("Resultado:", response.json())

if __name__ == "__main__":
    get_usuario()
