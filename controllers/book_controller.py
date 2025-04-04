from database.db_manager import db_manager

class BookController:
    def __init__(self):
        self.db = db_manager

    def add_book(self, title: str, author_id: str|int, genre: str) -> None:
        query = "INSERT INTO Books (title, author_id, genre) VALUES (%s, %s, %s);"
        self.db.execute_query(query, (title, author_id, genre))

    def list_books(self) -> None:
        query = """
        SELECT id, title, author_id, genre, is_available
        FROM Books;
        """
        books = self.db.fetchall(query)
        for book in books:
            disponibilidade = "Disponível" if book['is_available'] else "Indisponível"   

            print(f"""
            ID: {book['id']}
            Título: {book['title']}
            Autor: {book['author_id']}
            Gênero: {book['genre']}
            Disponibilidade: {disponibilidade}""")

    def list_books_disponiveis(self):
        query = """
        SELECT id, title, author_id, genre
        FROM Books WHERE is_available = %s;
        """

        books = self.db.fetchall(query, (True))
    
        for book in books:
            print(f"""
            ID: {book['id']}
            Título: {book['title']}
            Autor: {book['author_id']}
            Gênero: {book['genre']}""")

    def delete_book(self, book_id: str|int) -> None:
        query = "DELETE FROM Books WHERE id = %s;"
        query_title = """
        SELECT title
        FROM Books WHERE id = %s;
        """
        title = self.db.fetchall(query_title, (book_id))

        if title:  
            print(f"O livro {title[0]['title']} foi excluído.")
            self.db.execute_query(query, (book_id,))
        else:
            print("Livro não encontrado.")
        

    def editar_livro(self):
        livros = self.list_books()
        if not livros:
            print("Nenhum livro encontrado.")
            return

        # Exibe a lista de livros
        print("Livros disponíveis:")
        for livro in livros:
            print(f"{livro['id']} - {livro['title']} (Autor: {livro['author_id']})")

        ids_disponiveis = [str(livro['id']) for livro in livros]

        # Seleção de ID
        while True:
            id_livro = input("Digite o ID do Livro que você deseja editar: ").strip()
            if id_livro in ids_disponiveis:
                break

            print("O ID inserido é inválido. Por favor, digite um ID existente na lista.")

        # Seleciona o título atual
        while True:
            titulo_atual = next(livro['title'] for livro in livros if str(livro['id']) == id_livro)
            menu = input(f"""
                O que você deseja editar no Livro '{titulo_atual}'?
                1- Título
                2- Gênero
                3- Disponibilidade (Sim/Não)
                4- Autor
                0- Sair
            """).strip()
            
            match menu:
                case '1':  # Editar Título
                    novo_titulo = input("Digite o novo título: ").strip()
                    query = "UPDATE Books SET title = %s WHERE id = %s;"
                    titulo_atual = novo_titulo
                    self.db.execute_query(query, (novo_titulo, id_livro))
                    print("Título atualizado com sucesso!")

                case '2':  # Editar Gênero
                    novo_genero = input("Digite o novo gênero: ").strip()
                    query = "UPDATE Books SET genre = %s WHERE id = %s;"
                    self.db.execute_query(query, (novo_genero, id_livro))
                    print("Gênero atualizado com sucesso!")

                case '3':  # Editar Disponibilidade
                    disponibilidade = input("O livro está disponível? (Sim/Não): ").strip().lower()
                    is_available = disponibilidade == 'sim'
                    query = "UPDATE Books SET is_available = %s WHERE id = %s;"
                    self.db.execute_query(query, (is_available, id_livro))
                    print("Disponibilidade atualizada com sucesso!")

                case '4':  # Editar Autor
                    novo_author_id = input("Digite o ID do novo autor: ").strip()
                    query = "UPDATE Books SET author_id = %s WHERE id = %s;"
                    self.db.execute_query(query, (novo_author_id, id_livro))
                    print("Autor atualizado com sucesso!")

                case '0':  # Sair
                    print("Edição finalizada.")
                    break

                case _:  # Opção inválida
                    print("Opção inválida; Tente novamente.")
