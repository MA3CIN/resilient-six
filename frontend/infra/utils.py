"""Funcion encargada de crear el JSON - Dispositivo"""

def devices_to_json(devices):
    return {device[0]: {
        "id": device[0], 
        "model": device[1], 
        "owner": device[2], 
        "name": device[3], 
        "comment": device[4]
    } for device in devices}

"""Funcion encargada de crear el JSON - Dispositivo"""

def devices_to_json_full(devices):
    return {device[0]: {
        "model_id": device[0], 
        "model_name": device[1], 
        "category_name": device[2], 
        "manufacturer_name": device[3], 
        "energy_consumption": device[4]
    } for device in devices}

"""Funcion encargada de crear el JSON - Model"""
def models_to_json(models):
    return {model[0]: {
        "id": model[0], 
        "manufacturer": model[1], 
        "category": model[2], 
        "energy_consumption": model[3], 
        "name": model[4]
    } for model in models}

"""Funcion encargada de crear el JSON - Categoria"""
def categories_to_json(categories):
    return {categorie[0]: {
        "id": categorie[0], 
        "name": categorie[1]
    } for categorie in categories}