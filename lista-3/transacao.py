import mysql.connector

# conexão com banco
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root123",
    database="prova_bd"
)

cursor = conexao.cursor()

# dados para teste
aluno_id = 1
curso_id = 999
semestre = "2026.1"

try:
    print("Iniciando transação...")
    conexao.start_transaction()

    # 1 - verifica aluno
    cursor.execute("SELECT COUNT(*) FROM alunos WHERE id = %s", (aluno_id,))
    if cursor.fetchone()[0] == 0:
        raise Exception("Aluno não existe.")

    # 2 - verifica curso
    cursor.execute("SELECT COUNT(*) FROM cursos WHERE id = %s", (curso_id,))
    if cursor.fetchone()[0] == 0:
        raise Exception("Curso não existe.")

    # 3 - insere matrícula
    cursor.execute("""
        INSERT INTO matriculas (aluno_id, curso_id, semestre)
        VALUES (%s, %s, %s)
    """, (aluno_id, curso_id, semestre))

    # 4 - commit
    conexao.commit()
    print("Matrícula realizada com sucesso!")

except Exception as e:
    # rollback
    conexao.rollback()
    print("Erro na transação:", e)

finally:
    cursor.close()
    conexao.close()
