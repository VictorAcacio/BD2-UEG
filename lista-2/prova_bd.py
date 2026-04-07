import pandas as pd
from sqlalchemy import create_engine, text

# ---------------------------------------------
# Configuração do banco
# ---------------------------------------------
DB_USER = "root"
DB_PASS = "root123"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "prova_bd"

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---------------------------------------------
# Teste de conexão
# ---------------------------------------------
with engine.begin() as conn:
    conn.execute(text("SELECT 1"))

print("Conexão com o banco OK.")



