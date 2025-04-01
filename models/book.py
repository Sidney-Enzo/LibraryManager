class Book:
    def __init__(self, id: str, title: str, author: str, genre: str, is_available: bool=True):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = is_available