from datetime import datetime

def validar_data(data: str) -> datetime:
    try:
        return datetime.strptime(data, '%Y-%m-%d')
    except ValueError:
        return None
    
def input_int(message: str, error: str = "Value is not a number.") -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error)