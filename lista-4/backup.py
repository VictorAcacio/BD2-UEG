import os

CONTAINER_NAME = "bd2-victor-mysql"
DB_USER = "root"
DB_PASSWORD = "root123"
DB_NAME = "prova_bd"

# ==============================
# 1. BACKUP DO BANCO
# ==============================
print("=== BACKUP DO BANCO ===")

backup_cmd = f"docker exec {CONTAINER_NAME} mysqldump -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > backup.sql"

if os.system(backup_cmd) == 0:
    print("Backup realizado com sucesso!\n")
else:
    print("Erro ao fazer backup.\n")

# ==============================
# 2. REMOVER BANCO 
# ==============================
remover = input("Deseja remover o banco para simular falha? (s/n): ")

if remover.lower() == 's':
    print("\n=== REMOVENDO BANCO ===")

    drop_cmd = f'docker exec -i {CONTAINER_NAME} mysql -u {DB_USER} -p{DB_PASSWORD} -e "DROP DATABASE {DB_NAME};"'

    if os.system(drop_cmd) == 0:
        print("Banco removido com sucesso!\n")
    else:
        print("Erro ao remover banco.\n")

# ==============================
# 3. RESTAURAÇÃO DO BANCO
# ==============================
restaurar = input("Deseja restaurar o banco? (s/n): ")

if restaurar.lower() == 's':
    print("\n===RESTAURANDO BANCO ===")

    # recria banco antes
    create_cmd = f'docker exec -i {CONTAINER_NAME} mysql -u {DB_USER} -p{DB_PASSWORD} -e "CREATE DATABASE {DB_NAME};"'
    os.system(create_cmd)

    restore_cmd = f"docker exec -i {CONTAINER_NAME} mysql -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} < backup.sql"

    if os.system(restore_cmd) == 0:
        print("Banco restaurado com sucesso!\n")
    else:
        print("Erro ao restaurar.\n")

# ==============================
# FINAL
# ==============================
print("Processo finalizado!")
