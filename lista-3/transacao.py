import mysql.connector

# =======================================
# CONEXÃO
# =======================================
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="prova_bd"
    )
    cursor = conexao.cursor()
    print("Conectado ao banco com sucesso!")

except Exception as e:
    print("Erro ao conectar:", e)
    exit()

# =======================================
# 1. INSERÇÃO COM COMMIT
# =======================================
print("\n--- Teste de COMMIT ---")

try:
    conexao.start_transaction()

    aluno_id = 2
    curso_id = 1
    semestre = "2026.1"

    cursor.execute("""
        INSERT INTO matriculas (aluno_id, curso_id, semestre)
        VALUES (%s, %s, %s)
    """, (aluno_id, curso_id, semestre))

    conexao.commit()
    print("Inserção confirmada (COMMIT).")

except Exception as e:
    conexao.rollback()
    print("Erro:", e)

# =======================================
# 2. TESTE DE ROLLBACK
# =======================================
print("\n--- Teste de ROLLBACK ---")

try:
    conexao.start_transaction()

    # erro proposital (curso inexistente)
    cursor.execute("""
        INSERT INTO matriculas (aluno_id, curso_id, semestre)
        VALUES (%s, %s, %s)
    """, (1, 999, "2026.1"))

    conexao.commit()
    print("Não deveria aparecer")

except Exception as e:
    conexao.rollback()
    print("Rollback executado:", e)

# =======================================
# 3. LISTAR ALUNOS
# =======================================
print("\n--- Alunos ---")

cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)

# =======================================
# 4. LISTAR CURSOS
# =======================================
print("\n--- Cursos ---")

cursor.execute("SELECT * FROM cursos")
for linha in cursor.fetchall():
    print(linha)

# =======================================
# 5. MATRÍCULAS POR SEMESTRE
# =======================================
print("\n--- Matrículas por semestre ---")

semestre = input("Digite o semestre: ")

cursor.execute("""
    SELECT a.nome, c.nome, m.semestre
    FROM matriculas m
    JOIN alunos a ON m.aluno_id = a.id
    JOIN cursos c ON m.curso_id = c.id
    WHERE m.semestre = %s
""", (semestre,))

dados = cursor.fetchall()

if dados:
    for linha in dados:
        print(linha)
else:
    print("Nenhum resultado.")

# =======================================
# 6. CONSULTA POR ALUNO
# =======================================
print("\n--- Consultar matrículas de um aluno ---")

aluno_id = input("Digite o ID do aluno: ")

cursor.execute("""
    SELECT a.nome, c.nome, m.semestre
    FROM matriculas m
    JOIN alunos a ON m.aluno_id = a.id
    JOIN cursos c ON m.curso_id = c.id
    WHERE a.id = %s
""", (aluno_id,))

dados = cursor.fetchall()

for linha in dados:
    print(linha)

# =======================================
# 7. CANCELAMENTO DE MATRÍCULA
# =======================================
print("\n--- Cancelar matrícula ---")

matricula_id = input("Digite o ID da matrícula: ")

try:
    conexao.start_transaction()

    cursor.execute(
        "SELECT COUNT(*) FROM matriculas WHERE id = %s",
        (matricula_id,)
    )

    if cursor.fetchone()[0] == 0:
        raise Exception("Matrícula não encontrada.")

    cursor.execute(
        "DELETE FROM matriculas WHERE id = %s",
        (matricula_id,)
    )

    conexao.commit()
    print("Matrícula removida com sucesso!")

except Exception as e:
    conexao.rollback()
    print("Erro:", e)

# =======================================
# FINALIZAR
# =======================================
cursor.close()
conexao.close()
