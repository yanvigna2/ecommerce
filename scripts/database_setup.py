from sqlalchemy import create_engine, text

# Parâmetros para conexão do banco de dados

DB_USER = 'root'
DB_PASSWORD = '1234' 
DB_HOST = 'localhost'
DB_NAME = 'olist_project'

engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# Execução do script SQL para criação das tabelas

with engine.connect() as conn:
    with open('sql/create_tables.sql', 'r') as file:
        sql_commands = file.read()
    conn.execute(text(sql_commands))
    conn.commit()

print('Banco de dados e tabelas criadas com sucesso!')