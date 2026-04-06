import pandas as pd
from sqlalchemy import create_engine, text

# ---------------------------------------------
# Configuração do banco
# ---------------------------------------------
DB_USER = "root"
DB_PASS = "root123"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "aula1"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---------------------------------------------
# Teste de conexão
# ---------------------------------------------
with engine.begin() as conn:
    conn.execute(text("SELECT 1"))

print("Conexão com o banco OK.")

# ---------------------------------------------
# Leitura do CSV
# ---------------------------------------------
customers = pd.read_csv("archive/customers.csv")
sales = pd.read_csv("archive/sales.csv")
stores = pd.read_csv("archive/stores.csv")
calendar = pd.read_csv("archive/calendar.csv")
products = pd.read_csv("archive/products.csv")

# ---------------------------------------------
# Conferência
# ---------------------------------------------
print(customers.head())
print(stores.head())
print(sales.head())
print(calendar.head())
print(products.head())

# ---------------------------------------------
# Carga no MySQL
# ---------------------------------------------
customers.to_sql(
    "customers", engine,
    if_exists="replace", index=False
)

stores.to_sql(
    "stores", engine,
    if_exists="replace", index=False
)

sales.to_sql(
    "sales", engine,
    if_exists="replace", index=False
)

calendar.to_sql(
    "calendar", engine,
    if_exists="replace", index=False
)

products.to_sql(
    "products", engine,
    if_exists="replace", index=False
)

print("Dados carregados com sucesso.")

# ---------------------------------------------
# Conferência final
# ---------------------------------------------
check = """
SELECT
 (SELECT COUNT(*) FROM customers) AS customers,
 (SELECT COUNT(*) FROM stores) AS stores,
 (SELECT COUNT(*) FROM sales) AS sales,
 (SELECT COUNT(*) FROM calendar) AS calendar,
 (SELECT COUNT(*) FROM products) AS products;
"""

print(pd.read_sql(check, engine))
