-- Importação dos dados de Clientes
LOAD DATA LOCAL INFILE 'D:/olist_ecommerce/data/raw/olist_customers_dataset.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

USE olist_project;
-- Importação dos dados de Pedidos
LOAD DATA INFILE 'D:/olist_ecommerce/data/raw/olist_orders_dataset.csv'
INTO TABLE orders
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
SET order_delivered_carrier_date = NULLIF(order_delivered_carrier_date, '');


-- Importação dos dados de Itens de Pedidos
LOAD DATA INFILE 'D:/olist_ecommerce/data/raw//olist_order_items_dataset.csv'
INTO TABLE order_items
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Importação dos dados de Produtos
LOAD DATA INFILE 'D:/olist_ecommerce/data/raw/olist_products_dataset.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Importação dos dados de Pagamentos
LOAD DATA INFILE 'D:/olist_ecommerce/data/raw/olist_order_payments_dataset.csv'
INTO TABLE order_payments
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
