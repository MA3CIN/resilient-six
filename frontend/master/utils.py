import statistics 

def validar_campos(formulario):
    campos_vacios = False
    for campo in formulario.keys():
        valor = formulario.get(campo, '').strip()
        if not valor:
            campos_vacios = True
            break
    return not campos_vacios

"""Funcion encargada de crear el JSON - Metricas"""
def metrics_to_json(metrics):
    return {metric[0]: { "id": metric[0], "name": metric[1]} for metric in metrics}

def getMean(data):
    values = [dato['value'] for dato in data]
    media = statistics.mean(values)
    return media

def getSDev(data):
    values = [dato['value'] for dato in data]
    desviacion_estandar = statistics.stdev(values)
    return desviacion_estandar

def getAVG(data):
    values = [dato['value'] for dato in data]
    suma_total = statistics.fsum(values)
    promedio = suma_total / len(data)
    return promedio