--criar os usuarios

CREATE USER 'aluno'@'localhost' IDENTIFIED BY '123';
CREATE USER 'professor'@'localhost' IDENTIFIED BY '123';

-- inserir as permissoes

GRANT SELECT ON prova_bd.* TO 'aluno'@'localhost';
GRANT SELECT, UPDATE ON prova_bd.* TO 'professor'@'localhost';

-- exemplo caso queira revogar o acesso

REVOKE UPDATE ON prova_bd.* FROM 'aluno'@'localhost';
