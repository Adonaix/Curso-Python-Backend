import requests

URL_BASE = "http://127.0.0.1:8000"

def get_usuario():
    response = requests.get(URL_BASE + "/usuario/2")
    print("Resultado:", response.json())

def put_favorito():
    respuesta = requests.put(URL_BASE + "/usuario/favorito",
                              params={"nombre": "Bistec",
                                  "ultima_fecha": "21 de agosto de 2024",
                                  "id": 1})
    print("Respuesta de favorito: ", respuesta.json())

def get_item():
    response = requests.get(URL_BASE + "/item", params={"id":"ajsdh"})
    print("Resultado:", response.json())                               

if __name__ == "__main__":
    #get_usuario()
    #put_favorito()
    get_item()
