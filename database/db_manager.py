import mysql.connector as db
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "library_manager",
}

class DatabaseManager:
    def __init__(self, db_config):
        self.connection = db.connect(**db_config)
        self.cursor = self.connection.cursor(dictionary=True)
        self.db_config = db_config

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetchall(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()

    def conectar_db(self):
        return db.connect(**self.db_config)

    def obter_livros(self):
        with self.conectar_db() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Books")
            return cursor.fetchall()

    def listar_livros(self, livros):
        print("Lista de Livros:")
        for livro in livros:
            print(f"ID: {livro['id']} | Título: {livro['title']} | Autor: {livro['author']}")

    def obter_valor_por_id(self, lista, campo, id_desejado):
        return next((item[campo] for item in lista if str(item['id']) == id_desejado), None)

    def editar_campo(self, id_livro, campo, novo_valor):
        with self.conectar_db() as conn:
            cursor = conn.cursor()
            cursor.execute(f"UPDATE Books SET {campo} = %s WHERE id = %s", (novo_valor, id_livro))
            conn.commit()
        nome_amigavel = self.nomenclatura_amigavel(campo)
        print(f"{nome_amigavel} atualizado com sucesso!")

    def listar_autores(self):
        with self.conectar_db() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, name FROM authors")
            return cursor.fetchall()

    def solicitar_novo_valor(self, opcao, livros, id_livro):
        campos = {
            '1': ('title', "Digite o novo título"),
            '2': ('genre', "Digite o novo gênero"),
            '4': ('author', "Digite o ID do novo autor")
        }
        campo, mensagem = campos[opcao]
        valor_atual = self.obter_valor_por_id(livros, campo, id_livro)

        if campo == 'author':
            autores = self.listar_autores()
            self.listar_livros(autores)
            ids_autores = [str(autor['id']) for autor in autores]
            while True:
                novo_valor = input(f"{mensagem} (atual: {valor_atual}): ")
                if novo_valor in ids_autores:
                    break
                print("ID inválido. Tente novamente.")
        else:
            novo_valor = input(f"{mensagem} (atual: {valor_atual}): ")

        if str(novo_valor) == str(valor_atual):
            print(f"O {campo} inserido é idêntico ao atual. Nenhuma alteração foi realizada.")
            return None, None

        return campo, novo_valor

    def nomenclatura_amigavel(self, campo):
        nomes_amigaveis = {
            'title': 'Título',
            'genre': 'Gênero',
            'price': 'Preço',
            'author': 'Autor'
        }
        return nomes_amigaveis.get(campo, campo)

    def fetchone(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()
    

db_manager = DatabaseManager(db_config)
