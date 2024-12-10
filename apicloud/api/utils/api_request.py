import requests
from requests.auth import HTTPBasicAuth

def get_api_data(endpoint, username, password, params=None):
    """
    Realiza una petición GET a un API REST y devuelve los datos en formato JSON.

    :param endpoint: URL del endpoint de la API (string).
    :param username: Usuario para autenticación básica.
    :param password: Contraseña para autenticación básica.
    :param params: Parámetros adicionales para la consulta (dict, opcional).
    :return: Respuesta en formato JSON o mensaje de error.
    """
    try:
        # Configura la autenticación básica
        auth = HTTPBasicAuth(username, password)

        # Realiza la petición
        response = requests.get(endpoint, auth=auth, params=params)

        # Verifica si la respuesta es exitosa (status_code 200)
        response.raise_for_status()

        # Devuelve los datos en formato JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Maneja errores y devuelve un mensaje útil
        return {"error": str(e)}
