from controllers.book_controller import BookController
from controllers.user_controller import UserManager
from controllers.loan_controller import LoanManager

class App:
    def __init__(self, menu: tuple):
        self._display, self._update = menu

        self.book_manager = BookController()
        self.user_manager = UserManager()
        self.loan_manager = LoanManager()

        self._running = True

    def switch(self, menu: tuple) -> None:
        self._display, self._update = menu
    
    def stop(self) -> None:
        self._running = False

    def run(self) -> None:
        while self._running:
            self._display()
            self._update(self)

def exibir_menu() -> None:
    print("""\n===== Bem-vindo ao Library Manager =====
1. Gerenciar Livros
2. Gerenciar Usuários
3. Gerenciar Empréstimos
4. Sair""")

def exibir_update(app) -> None:
    choice = input("Escolha uma opção: ").strip()
    menus = {
        '1': (menu_livros, menu_livros_update),
        '2': (menu_usuarios, menu_usuarios_update),
        '3': (menu_emprestimos, menu_emprestimos_update)
    }

    try:
        app.switch(menus[choice])
    except KeyError:
        if choice == '4':
            app.stop()
        else:
            print("Opção invalida.")

def menu_livros() -> None:
    print("""\n===== Gerenciamento de Livros =====
1. Listar Livros
2. Adicionar Livro
3. Editar Livro
4. Excluir Livro
5. Voltar""")
    
def menu_livros_update(app: App) -> None:
    opcao_livros = input("Escolha uma opção: ").strip()

    match opcao_livros:
        #Listar Livros
        case '1':
            app.book_manager.list_books()

        #Adicionar Livros    
        case '2':
            title = input("Título: ").strip()
            author_id = input("ID Do Autor: ").strip()
            genre = input("Gênero: ").strip()
            app.book_manager.add_book(title, author_id, genre)
            print("Livro adicionado com sucesso!")
        
        # Editar Livros
        case '3':
            app.book_manager.book_manager.editar_livro()
        
        # Excluir Livros
        case '4':
            livro_id = input("Digite o ID do livro a ser excluído: ").strip()
            app.book_manager.book_manager.delete_book(livro_id)
            
        # Voltar ao Menu Principal
        case '5':
            app.switch((exibir_menu, exibir_update))
        
        case _:
            print("Opção inválida.")

def menu_usuarios() -> None:
    print("""\n===== Gerenciamento de Usuários =====
1. Listar Usuários
2. Adicionar Usuário
3. Editar Usuário
4. Excluir Usuário
5. Voltar""")
    
def menu_usuarios_update(app: App) -> None:
    opcao_usuarios = input("Escolha uma opção: ").strip()

    match opcao_usuarios:
        # Listar Usuários
        case '1':
            app.user_manager.listar_usuarios()
        
        # Adicionar um novo usuário
        case '2':
            nome = input("Digite o nome do usuário: ").strip()
            email = input("Digite o email do usuário: ").strip()
            app.user_manager.adicionar_usuario(nome, email)
        
        # Editar um usuário
        case '3':
            app.user_manager.editar_usuario()
        
        # Excluir um usuário
        case '4':
            user_id = input("Digite o ID do usuário a ser excluído: ").strip()
            app.user_manager.excluir_usuario(user_id)
        
        # Voltar ao menu principal
        case '5':
            app.switch((exibir_menu, exibir_update))

        case _:
            print("Opção inválida.")

def menu_emprestimos() -> None:
    print("""\n===== Gerenciamento de Empréstimos =====
1. Listar Empréstimos
2. Adicionar Empréstimo
3. Devolver Livro
4. Voltar""")
    
def menu_emprestimos_update(app: App) -> None:
    opcao_emprestimos = input("Escolha uma opção: ").strip()

    match opcao_emprestimos:

        # Listar Empréstimos
        case '1':
            app.loan_manager.listar_loans()

        #Adicionar Empréstimo à Usuário
        case '2':
            app.loan_manager.adicionar_loan()

        # Devolver Livro
        case '3':
            app.loan_manager.devolver_livro()
        
        #Voltar ao Menu Principal
        case '4':
            app.switch((exibir_menu, exibir_update))
        
        case _:
            print("Opção inválida.")
    
def main() -> None:
    app = App((exibir_menu, exibir_update))
    app.run()

if __name__ == "__main__":
    main()