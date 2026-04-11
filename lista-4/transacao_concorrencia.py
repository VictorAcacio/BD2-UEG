import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="prova_bd"
)

cursor = conexao.cursor()

print("Simulação de concorrência...")

try:
    conexao.start_transaction()

    aluno_id = int(input("Aluno ID: "))
    curso_id = int(input("Curso ID: "))
    semestre = input("Semestre: ")

    # 🔒 LOCK
    cursor.execute("SELECT * FROM alunos WHERE id = %s FOR UPDATE", (aluno_id,))
    cursor.fetchone()

    cursor.execute("SELECT * FROM cursos WHERE id = %s FOR UPDATE", (curso_id,))
    cursor.fetchone()

    # Verifica duplicidade
    cursor.execute("""
        SELECT COUNT(*) FROM matriculas
        WHERE aluno_id = %s AND curso_id = %s AND semestre = %s
    """, (aluno_id, curso_id, semestre))

    if cursor.fetchone()[0] > 0:
        raise Exception("Matrícula já existe!")

    cursor.execute("""
        INSERT INTO matriculas (aluno_id, curso_id, semestre)
        VALUES (%s, %s, %s)
    """, (aluno_id, curso_id, semestre))

    import time
    input("Pressione ENTER para confirmar (simula atraso)...")
    time.sleep(10)

    conexao.commit()
    print("Matrícula realizada com sucesso!")

except Exception as e:
    conexao.rollback()
    print("Erro:", e)

cursor.close()
conexao.close()
