import statistics

"""Funcion encargada de crear el JSON - Metricas"""
def metrics_to_json(metrics):
    return {metric[0]: {
        "id": metric[0], 
        "name": metric[1]
    } for metric in metrics}

def recent_values_to_json(rov):
    return [
        {
            "value": value[0]
        } 
        for value in rov
    ]
