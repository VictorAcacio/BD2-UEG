-- ==============================
-- USAR BANCO
-- ==============================
USE prova_bd;

-- ==============================
-- LIMPAR (caso já exista)
-- ==============================
DROP VIEW IF EXISTS alunos_global;
DROP TABLE IF EXISTS alunos_goianesia;
DROP TABLE IF EXISTS alunos_anapolis;

-- ==============================
-- 1 e 2 - FRAGMENTAÇÃO HORIZONTAL
-- ==============================

CREATE TABLE alunos_goianesia AS
SELECT * FROM alunos
WHERE campus = 'Goianesia';

CREATE TABLE alunos_anapolis AS
SELECT * FROM alunos
WHERE campus = 'Anapolis';

-- ==============================
-- 3 - VISÃO GLOBAL
-- ==============================

CREATE VIEW alunos_global AS
SELECT * FROM alunos_goianesia
UNION ALL
SELECT * FROM alunos_anapolis;

-- ==============================
-- 4 - Replicação da tabela disciplinas
-- ==============================

-- A tabela disciplinas pode ser replicada integralmente em todos os campi.

-- Isso significa que cada unidade teria uma cópia completa da tabela, evitando a necessidade de acessar outro servidor para consultas.

-- ==============================
-- 5 - Vantagens e problemas da replicação
-- ==============================

-- Vantagens:
--  *Maior disponibilidade dos dados
--  *Melhor desempenho em consultas locais
--  *Tolerância a falhas
-- Problemas:
--  *Necessidade de sincronização entre cópias
--  *Possibilidade de inconsistência temporária
--  *Maior custo de manutenção

-- ==============================
-- 6 - Transação distribuída (matrícula)
-- ==============================

-- Uma transação distribuída ocorre quando uma operação envolve mais de um nó.

-- Exemplo:

-- Inserir matrícula no banco do campus do aluno
-- Registrar disciplinas associadas
-- Confirmar a operação em todos os nós

-- Se alguma etapa falhar, toda a transação deve ser desfeita (rollback).

-- ==============================
-- 7 - Possíveis falhas
-- ==============================

-- Falha de nó
--  *Um servidor pode parar, interrompendo a transação.

-- Falha de comunicação
--  *Problemas de rede podem impedir sincronização entre os bancos.

-- Falha de concorrência
--  *Duas transações simultâneas podem gerar conflitos.

-- ***Impacto:***
-- Essas falhas podem causar inconsistência de dados, perda de informações ou interrupção do sistema.
