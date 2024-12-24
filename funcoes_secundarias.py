from datetime import datetime

def validar_data(data):
    try:
        return datetime.strptime(data, '%Y-%m-%d')
    except ValueError:
        return None