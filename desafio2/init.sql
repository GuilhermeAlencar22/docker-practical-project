-- Script executado na primeira inicialização do container
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(50)
);

INSERT INTO funcionarios (nome, cargo) VALUES
('Guilherme Alencar', 'Analista de Dados'),
('Mariana Costa', 'Dev Back-End'),
('Lucas Mendes', 'DevOps Engineer');
