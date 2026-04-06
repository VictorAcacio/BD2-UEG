-- ============================================
-- Consulta 1: Total de vendas
-- Objetivo: Verificar quantidade total de registros de vendas
-- ============================================
SELECT COUNT(*) AS total_vendas
FROM sales;


-- ============================================
-- Consulta 2: Top 5 vendas com maior lucro
-- Objetivo: Identificar as vendas mais lucrativas
-- (ORDER BY + LIMIT)
-- ============================================
SELECT order_id, profit
FROM sales
ORDER BY profit DESC
LIMIT 5;


-- ============================================
-- Consulta 3: Total de vendas por loja
-- Objetivo: Ver quantas vendas cada loja realizou
-- (GROUP BY)
-- ============================================
SELECT store_id, COUNT(*) AS total_vendas
FROM sales
GROUP BY store_id;


-- ============================================
-- Consulta 4: Lojas com mais de 10100 vendas
-- Objetivo: Filtrar lojas com alto volume de vendas
-- (GROUP BY + HAVING)
-- ============================================
SELECT store_id, COUNT(*) AS total_vendas
FROM sales
GROUP BY store_id
HAVING COUNT(*) > 10100;


-- ============================================
-- Consulta 5: JOIN vendas e produtos
-- Objetivo: Relacionar vendas com os produtos vendidos
-- (JOIN 1)
-- ============================================
SELECT s.order_id, p.product_name, s.revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
LIMIT 10;

-- ============================================
-- Consulta 6: JOIN vendas e lojas
-- Objetivo: Relacionar vendas com lojas
-- (JOIN 2)
-- ============================================
SELECT s.order_id, st.store_name, s.revenue
FROM sales s
JOIN stores st ON s.store_id = st.store_id
LIMIT 10;

-- ============================================
-- Consulta 7: JOIN vendas, produtos e lojas
-- Objetivo: Mostrar venda completa (produto + loja)
-- (JOIN 3)
-- ============================================
SELECT s.order_id, p.product_name, st.store_name, s.revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN stores st ON s.store_id = st.store_id
LIMIT 10;

-- ============================================
-- Consulta 8: Receita total por produto
-- Objetivo: Somar receita por produto
-- (GROUP BY)
-- ============================================
SELECT p.product_name, SUM(s.revenue) AS total_receita
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
LIMIT 10;
