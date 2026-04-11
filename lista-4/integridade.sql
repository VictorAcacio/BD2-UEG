-- PK
ALTER TABLE alunos ADD PRIMARY KEY (id);
ALTER TABLE cursos ADD PRIMARY KEY (id);
ALTER TABLE matriculas ADD PRIMARY KEY (id);
--apesar de que eu ja tinha criado as pk no inicio, deixei o codigo.


-- FK
ALTER TABLE matriculas
ADD CONSTRAINT fk_aluno
FOREIGN KEY (aluno_id) REFERENCES alunos(id);

ALTER TABLE matriculas
ADD CONSTRAINT fk_curso
FOREIGN KEY (curso_id) REFERENCES cursos(id);

-- UNIQUE (evita duplicação)
ALTER TABLE matriculas
ADD CONSTRAINT unique_matricula
UNIQUE (aluno_id, curso_id, semestre);

-- CHECK
ALTER TABLE alunos
ADD CONSTRAINT chk_sexo CHECK (sexo IN ('m', 'f'));
--ate coloquei mais nos testes que fiz, ainda ficou passando quando colocava outra letra, pelo que vi quando fui procurar parece que check nao funciona tao bem nessa versao do mysql.
