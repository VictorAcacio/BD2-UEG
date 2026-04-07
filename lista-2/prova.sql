-- ============================================
-- CRIAÇÃO DAS TABELAS
-- ============================================

CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    sexo CHAR(1)
);

CREATE TABLE cursos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100)
);

CREATE TABLE matriculas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    aluno_id INT,
    curso_id INT,
    semestre VARCHAR(10),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- ============================================
-- INSERÇAO DE DADOS
-- ============================================

-- CURSOS
INSERT INTO cursos (nome) VALUES
('CC'),
('ADS'),
('SI');

-- ALUNOS
INSERT INTO alunos (nome, sexo) VALUES
('Ana', 'f'),
('Bruno', 'm'),
('Carlos', 'm'),
('Diana', 'f'),
('Eduardo', 'm'),
('Fernanda', 'f'),
('Gabriel', 'm'),
('Helena', 'f'),
('Igor', 'm'),
('Julia', 'f');

-- MATRICULAS
INSERT INTO matriculas (aluno_id, curso_id, semestre) VALUES
(1,1,'2026.1'), (2,1,'2026.1'), (3,1,'2026.2'),
(4,1,'2026.1'), (5,2,'2026.1'), (6,2,'2026.2'),
(7,3,'2026.1'), (8,3,'2026.1'), (9,1,'2026.1'),
(10,1,'2026.2'), (1,2,'2026.2'), (2,3,'2026.1'),
(3,2,'2026.1'), (4,3,'2026.2'), (5,1,'2026.1'),
(6,1,'2026.1'), (7,2,'2026.2'), (8,1,'2026.1'),
(9,3,'2026.2'), (10,2,'2026.1');

-- ============================================
-- CONSULTAS
-- ============================================

-- Alunos do curso CC
SELECT a.nome
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
JOIN cursos c ON m.curso_id = c.id
WHERE c.nome = 'CC';

-- Alunas do curso CC
SELECT a.nome
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
JOIN cursos c ON m.curso_id = c.id
WHERE c.nome = 'CC' AND a.sexo = 'f';

-- Nome do aluno e curso
SELECT a.nome, c.nome
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
JOIN cursos c ON m.curso_id = c.id;

-- Alunos de 2026.1
SELECT a.nome
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
WHERE m.semestre = '2026.1';

-- Aluno e curso em 2026.1
SELECT a.nome, c.nome
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
JOIN cursos c ON m.curso_id = c.id
WHERE m.semestre = '2026.1';

-- Questao Extra 1
SELECT a.nome
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
WHERE a.sexo = 'f';

-- Questao Extra 2
SELECT a.nome
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
JOIN cursos c ON m.curso_id = c.id
WHERE c.nome = 'ADS';
