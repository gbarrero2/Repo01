# client.py
# lab2 giovanni barrero 
import requests

def rpc_client(method, params):
    data = {"method": method, "params": params}
    response = requests.post('http://localhost:5000/rpc', json=data)
    if response.status_code == 200:
        result = response.json()
        return result['result']
    else:
        print(f"Error: {response.status_code}")
        return None

# Ejemplos de llamadas al servidor RPC
resultado_suma = rpc_client("sumar", [5, 3])
resultado_resta = rpc_client("restar", [8, 2])

print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la resta: {resultado_resta}")
