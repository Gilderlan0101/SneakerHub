from aplication.comfigure_db.users import UserModel

import sqlite3

def add_user(user: UserModel):
    ''' nome do banco '''
    banco = sqlite3.connect('sqlite.db')

    ''' Criando o banco sqlite '''
    cursor = banco.cursor()

    ''' O Que vai te na tabela do banco de dados '''
    # Se a tabela não existir, descomente a linha abaixo
    cursor.execute(('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER NOT NULL,
        password TEXT NOT NULL
    )
    '''))


    cursor.execute('''
                    INSERT INTO users (name, email, age, password)
                    VALUES (?, ?, ?, ?)''',(user.name, user.email, user.age, user.password))

    banco.commit()
    banco.close()  # Fechar a conexão após a operação

# Criando um novo usuário
new_user = UserModel(name="Gilderlan", email="contato@example.com", age=20, password="securepassword")

# Adicionando o usuário ao banco de dados
add_user(new_user)

