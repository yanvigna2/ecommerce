import pandas as pd
from sqlalchemy import create_engine

# String de conexão com o MySQL
connection_string = "mysql+mysqlconnector://root:1234@localhost/olist_project"

# Tente conectar ao banco de dados
try:
    engine = create_engine(connection_string)
    connection = engine.connect()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao MySQL: {e}")
    exit()

# Carregue os dados das tabelas
try:
    df_orders = pd.read_sql('SELECT * FROM orders', engine)
    df_order_items = pd.read_sql('SELECT * FROM order_items', engine)
    print("Dados carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar dados: {e}")
    connection.close()
    exit()

# Limpeza de dados
df_orders['order_approved_at'] = df_orders['order_approved_at'].fillna(df_orders['order_purchase_timestamp'])

# Remova outliers em 'price'
Q1 = df_order_items['price'].quantile(0.25)
Q3 = df_order_items['price'].quantile(0.75)
IQR = Q3 - Q1
df_order_items = df_order_items[
    ~((df_order_items['price'] < (Q1 - 1.5 * IQR)) | (df_order_items['price'] > (Q3 + 1.5 * IQR)))
]

# Salve os dados processados
df_orders.to_csv('data/processed/orders_cleaned.csv', index=False)
df_order_items.to_csv('data/processed/order_items_cleaned.csv', index=False)

# Feche a conexão
connection.close()
print("Processo concluído! Dados salvos em 'data/processed/'.")