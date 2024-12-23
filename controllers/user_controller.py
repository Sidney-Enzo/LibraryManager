from database.db_manager import db_manage

class UserManager:
    def __init__(self):
        self.db = db_manage

    def listar_usuarios(self):
        #Lista todos os usuários registrados.
        query = """
        SELECT id, nome, email
        FROM Users
        """
        usuarios = self.db.fetchall(query=query)
        print("Lista de Usuários:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}\nNome: {usuario['nome']}\nEmail: {usuario['email']}\n")

    def adicionar_usuario(self, nome, email):
        query = """
        SELECT email
        FROM Users
        """
        emails = self.db.fetchall(query=query)
        
        emails_utilizados = [email['email'] for email in emails]

        if str(email) in str(emails_utilizados):
            print("E-mail já cadastrado.")
        else:
                self.db.execute_query(
                    "INSERT INTO Users (nome, email) VALUES (%s, %s)", 
                    (nome, email)
                )
                print(f"Usuário '{nome}' adicionado com sucesso!")
            

    def editar_usuario(self):
        query = """
        SELECT id
        FROM Users
        """
        ids = self.db.fetchall(query=query)
        
        ids_disponiveis = [str(ids[0]['id']) for id in ids]
        
        user_id = input("Digite o ID do usuário a ser editado: ")

        if str(user_id) in str(ids_disponiveis):
            while True:
                campo = input("Digite o campo a ser editado (nome, email): ").lower
                match campo:
                    case 'email':
                        novo_valor = input("Digite o novo email: ")
                        break
                    case 'nome':
                        novo_valor = input("Digite o novo nome: ")
                        break
                    case _:
                        print('Inválido, tente novamente.')     
            try:
                self.db.execute_query(
                    f"UPDATE Users SET {campo} = %s WHERE id = %s", 
                    (novo_valor, user_id)
                )
                print(f"O campo '{campo}' do usuário ID {user_id} foi atualizado para '{novo_valor}'.")
            except Exception as e:
                print(f"Erro ao editar usuário: {e}")
        else:
            print("ID inválido.")
            
        
    def excluir_usuario(self, user_id):
        #Remove um usuário do banco de dados.  
        try:
            self.db.execute_query("DELETE FROM Users WHERE id = %s", (user_id,))
            print(f"Usuário ID {user_id} excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir usuário: {e}")

    def buscar_usuario_por_id(self, user_id):
        # Busca um usuário específico pelo ID.
        try:
            usuario = self.db.fetchone("SELECT * FROM Users WHERE id = %s", (user_id,))
            if usuario:
                print(f"ID: {usuario['id']} | Nome: {usuario['nome']} | Email: {usuario['email']}")
            else:
                print("Usuário não encontrado.")
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")

    def fechar_conexao(self):
        #Fecha a conexão com o banco de dados.
        
        self.db.close_connection()
