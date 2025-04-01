
# LibraryManager 📚

**LibraryManager** é um sistema de gerenciamento de bibliotecas desenvolvido com Python, MySQL e conceitos de Programação Orientada a Objetos (POO). Este projeto demonstra integração de Python com MySQL, usando variáveis de ambiente para proteção de informações sensíveis como credenciais de banco de dados.

---

## Funcionalidades ⚙️

- **Gerenciamento de Livros** 📖:
  - Adicionar, listar, editar e excluir livros.
- **Gerenciamento de Usuários** 👤:
  - Cadastrar, listar e excluir usuários.
- **Controle de Empréstimos** 📅:
  - Registrar empréstimos, verificar status de devoluções e consultar histórico.
- **Relatórios** 📊:
  - Gerar relatórios simples como:
    - Livros disponíveis.
    - Livros emprestados.
    - Histórico de empréstimos por usuário.

---

## Tecnologias Utilizadas 💻

- **Python**: Linguagem principal do projeto.
- **MySQL**: Banco de dados relacional para armazenar informações.
- **MySQL Workbench**: Ferramenta para gerenciar o banco de dados.
- **Python-dotenv**: Para gerenciar variáveis de ambiente com segurança.
- **Datetime**: Biblioteca Python para manipulação de datas e horas, utilizada para registrar e formatar informações temporais.
- **Pytest**: Para testar funções
---

## Como Configurar o Projeto ⚙️

### Pré-requisitos 🛠️

1. Python 3.10+ instalado.
2. MySQL instalado e configurado.
3. MySQL Workbench (opcional, para gerenciar o banco visualmente).

### Passos para Configuração 📑

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/meuNobre/LibraryManager.git
   cd LibraryManager
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente** 🔐: 
   - Crie um arquivo `.env` no diretório raiz com o seguinte conteúdo:
     ```plaintext
     DB_HOST=localhost
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_NAME=library_manager
     ```

4. **Configure o banco de dados** 📋:
   - No MySQL Workbench, crie um banco de dados chamado `library_manager`.
   - Execute o script `database/library_schema.sql` para criar as tabelas.

5. **Execute o projeto**:
   ```bash
   python main.py
   ```

---

## Estrutura do Banco de Dados 🗃️

O banco de dados contém as seguintes tabelas:

- **Books** 📚:
  - Armazena informações sobre os livros disponíveis na biblioteca.
- **Users** 👥:
  - Armazena informações sobre os usuários da biblioteca.
- **Loans** 📑:
  - Registra os empréstimos realizados.

---

## Estrutura do Projeto 🛠️

```plaintext
LibraryManager/
├── README.md
├── requirements.txt
├── main.py
├── .env.example
├── funcoes_secundarias.py
├── test.py
├── database/
│   ├── library_schema.sql
│   └── db_manager.py
├── models/
│   ├── book.py
│   ├── user.py
│   └── loan.py
└── controllers/
    ├── book_controller.py
    ├── user_controller.py
    └── loan_controller.py
```

---

## Licença📜

Este projeto é licenciado sob a [MIT License](LICENSE).

---

## 📞 Contact / Contato

[pt-br]
- GitHub: [meuNobre](https://github.com/meuNobre)
- Email: miguelnobre0411@gmail.com
- Discord: icloudsz

---
Feito com ❤️ por [Nobre](https://github.com/meuNobre).
