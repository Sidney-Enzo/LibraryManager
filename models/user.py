class User:
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.name} | Email: {self.email}"

