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
            
            # Menu de Livros
            case '1': 
                while True:
                    menu_livros()
                    opcao_livros = input("Escolha uma opção: ")

                    match opcao_livros:
                        #Listar Livros
                        case '1':
                            book_manager.list_books()

                        #Adicionar Livros    
                        case '2':
                            title = input("Título: ")
                            author_id = input("ID Do Autor: ")
                            genre = input("Gênero: ")
                            book_manager.add_book(title, author_id, genre)
                            print("Livro adicionado com sucesso!")
                        
                        # Editar Livros
                        case '3':
                            book_manager.editar_livro()
                        
                        # Excluir Livros
                        case '4':
                            livro_id = input("Digite o ID do livro a ser excluído: ")
                            book_manager.delete_book(livro_id)
                            
                        # Voltar ao Menu Principal
                        case '5':
                            break
                        
                        case _:
                            print("Opção inválida.")
            

            # Menu de Usuários
            case '2':
                while True:
                    menu_usuarios()
                    opcao_usuarios = input("Escolha uma opção: ")

                    match opcao_usuarios:
                        
                        # Listar Usuários
                        case '1':
                            user_manager.listar_usuarios()
                        
                        # Adicionar um novo usuário
                        case '2':
                            nome = input("Digite o nome do usuário: ")
                            email = input("Digite o email do usuário: ")
                            user_manager.adicionar_usuario(nome, email)
                        
                        # Editar um usuário
                        case '3':
                            user_manager.editar_usuario()
                        
                        # Excluir um usuário
                        case '4':
                            user_id = input("Digite o ID do usuário a ser excluído: ")
                            user_manager.excluir_usuario(user_id)
                        
                        # Voltar ao menu principal
                        case '5':
                            break

                        case _:
                            print("Opção inválida.")

            #Menu de Emprestimos
            case '3':
                while True:
                    menu_emprestimos()
                    opcao_emprestimos = input("Escolha uma opção: ")

                    match opcao_emprestimos:

                        # Listar Empréstimos
                        case '1':
                            loan_manager.listar_loans()

                        #Adicionar Empréstimo à Usuário
                        case '2':
                            loan_manager.adicionar_loan()

                        # Devolver Livro
                        case '3':
                            loan_manager.devolver_livro()
                        
                        #Voltar ao Menu Principal
                        case '4':
                            break
                        
                        case _:
                            print("Opção inválida.")

if __name__ == "__main__":
    main()