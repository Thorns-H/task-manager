import json

# Esta función se encarga de permitirnos configurar la cantidad de 
# elementos en nuestra 'simulación' modificidando el archivo config.json

def load_config(file_path) -> dict:

    with open(file_path, 'r') as file:
        config = json.load(file)

    return config

