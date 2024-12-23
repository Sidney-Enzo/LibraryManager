-- Criação do banco de dados
CREATE DATABASE library_manager;

-- Uso do banco de dados
USE library_manager;
-- Tabela de Autores


CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    nacionalidade VARCHAR(50)
);

-- Tabela de Livros
CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre VARCHAR(50),
    is_available BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Tabela de Usuários
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

-- Tabela de Empréstimos
CREATE TABLE Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    user_id INT NOT NULL,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

Select * from books;

-- Inserção de dados na tabela de autores
INSERT INTO authors (name, nacionalidade) 
VALUES 
    ('J.K. Rowling', 'Britânica'),
    ('George R.R. Martin', 'Americano'),
    ('Haruki Murakami', 'Japonês'),
    ('Gabriel García Márquez', 'Colombiano'),
    ('Jane Austen', 'Britânica'),
    ('F. Scott Fitzgerald', 'Americano'),
    ('J.R.R. Tolkien', 'Britânico');
