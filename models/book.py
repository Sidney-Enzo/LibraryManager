class Book:
    def __init__(self, id, title, author, genre, is_available=True):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = is_available