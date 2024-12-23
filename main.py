from database.db_manager import db_manage
from controllers.book_controller import BookController
from controllers.user_controller import UserManager
from controllers.loan_controller import LoanManager



def exibir_menu():
    print("""\n===== Bem-vindo ao Library Manager =====
1. Gerenciar Livros
2. Gerenciar Usuários
3. Gerenciar Empréstimos
4. Sair""")

def menu_livros():
    print("""\n===== Gerenciamento de Livros =====
1. Listar Livros
2. Adicionar Livro
3. Editar Livro
4. Excluir Livro
5. Voltar""")

def menu_usuarios():
    print("""\n===== Gerenciamento de Usuários =====
1. Listar Usuários
2. Adicionar Usuário
3. Editar Usuário
4. Excluir Usuário
5. Voltar""")


def menu_emprestimos():
    print("""\n===== Gerenciamento de Empréstimos =====
1. Listar Empréstimos
2. Adicionar Empréstimo
3. Devolver Livro
4. Voltar""")
    
def main():
   
    book_manager = BookController()
    user_manager = UserManager()
    loan_manager = LoanManager()

    while True:
        exibir_menu()
        choice = input("Escolha uma opção: ")

        match choice:
            case '1':
                # Menu de Livros
                while True:
                    menu_livros()
                    opcao_livros = input("Escolha uma opção: ")

                    match opcao_livros:
                        case '1':
                            books = book_manager.list_books()
                            for book in books:
                                print(f"""
            ID: {book['id']}
            Título: {book['title']}
            Autor: {book['author_id']}
            Gênero: {book['genre']}""")
                        case '2':
                            title = input("Título: ")
                            author_id = input("ID Do Autor: ")
                            genre = input("Gênero: ")
                            book_manager.add_book(title, author_id, genre)
                            print("Livro adicionado com sucesso!")
                        
                        case '3':
                            book_manager.editar_livro()
                        
                        case '4':
                            livro_id = input("Digite o ID do livro a ser excluído: ")
                            book_manager.delete_book(livro_id)
                            
                        
                        case '5':
                            break
                        
                        case _:
                            print("Opção inválida.")

            case '2':
                # Menu de Usuários
                while True:
                    menu_usuarios()
                    opcao_usuarios = input("Escolha uma opção: ")

                    match opcao_usuarios:
                        case '1':
                            user_manager.listar_usuarios()
                        case '2':
                            nome = input("Digite o nome do usuário: ")
                            email = input("Digite o email do usuário: ")
                            user_manager.adicionar_usuario(nome, email)
                        case '3':
                            user_manager.editar_usuario()
                        case '4':
                            user_id = input("Digite o ID do usuário a ser excluído: ")
                            user_manager.excluir_usuario(user_id)
                        case '5':
                            break
                        case _:
                            print("Opção inválida.")

            case '3':
                pass

if __name__ == "__main__":
    main()