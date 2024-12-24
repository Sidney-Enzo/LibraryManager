from database.db_manager import db_manager
from funcoes_secundarias import validar_data
from controllers.book_controller import BookController
from controllers.user_controller import UserManager

class LoanManager(BookController, UserManager):
    def __init__(self):
        self.db = db_manager

    def listar_loans(self):
        query = """SELECT 
        Loans.id,Books.title,Loans.user_id,Loans.loan_date, Loans.return_date
        FROM Loans
        INNER JOIN 
        Books ON Loans.book_id = Books.id;"""  
        lista_emprestimos = self.db.fetchall(query,)
        print("Lista de empréstimos ativos:")
        for emprestimo in lista_emprestimos:
            print(f"""ID: {emprestimo['id']}""")
            
    def adicionar_loan(self):
        #Verificacao Books
        print("Livros disponíveis para empréstimo:")
        self.list_books_disponiveis()

        book_id = int(input("Digite o ID do livro que será emprestado: "))

        query_book = "SELECT * FROM Books WHERE id = %s"
        livro = self.db.fetchone(query_book,(book_id))
        livro = livro['title'] if livro else None

        if not livro:
            print(f"Erro: Livro com ID {book_id} não encontrado.")
            return
        
        #Verificacao_Users
        user_id = int(input("Digite o ID do usuário que pegará o livro: "))

        query_user = "SELECT * FROM Users WHERE id = %s"
        user = self.db.fetchone(query_user, user_id)
        
        if not user:
            print(f"Erro: Usuário com ID {user_id} não encontrado.")
            return

        #Solicitação e Validação Datas
        loan_date = validar_data(input("Digite a data de ínicio do empréstimo(formato YYYY-MM-DD): "))
        return_date = validar_data(input("Digite a data de fim do empréstimo(formato YYYY-MM-DD): "))

        if not loan_date or not return_date:
            print("Data informada no formato errado.")
                
        else:
            query_insert_loan = "INSERT INTO Loans (book_id, user_id, loan_date, return_date) VALUES (%s, %s, %s, %s)"
            
            query_update_book = """
            UPDATE Books
            SET is_available = %s 
            WHERE id = %s"""

            query_select_id = """
            SELECT id FROM Loans WHERE book_id = %s 
            """

            try:
                self.db.execute_query(query_insert_loan, (book_id, user_id, loan_date, return_date))
                self.db.execute_query(query_update_book, (False, book_id))

                last_id = self.db.fetchone(query_select_id, (book_id))[0]
                last_id = last_id['id'] if last_id else None

                print(f"Empréstimo de ID {last_id} registrado.\nO livro '{livro}' foi emprestado para '{user}'.\n")
            except Exception as e:
                print(f"Erro ao registrar o empréstimo: {e}")
        
    def devolver_livro(self):

        ID_Emprestimo = int(input("Digite o ID do Empréstimo: "))

        query_loan_check = """
            SELECT id FROM Loans WHERE id = %s
            """
        
        query_delete_loan = """"DELETE FROM Loans WHERE id = %s"""

        query_update_book= """
        UPDATE Books
        SET is_available = %s
        WHERE id = (SELECT book_id FROM Loans WHERE id = %s)
        """ 
        
        emprestimo = self.db.fetchone(query_loan_check, (ID_Emprestimo))
        
        if emprestimo:
            self.db.execute_query(query=query_update_book, params=(True, ID_Emprestimo))
            self.db.execute_query(query=query_delete_loan, params=(ID_Emprestimo))
            
        else:
             print(f"Empréstimo com ID {ID_Emprestimo} não encontrado.")
        
