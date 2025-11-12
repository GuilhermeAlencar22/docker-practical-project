CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(50)
);

INSERT INTO funcionarios (nome, cargo) VALUES
('Guilherme Alencar', 'Analista de Dados'),
('Mariana Costa', 'Dev Back-End'),
('Ricardo', 'RH'),
('Rodrigo', 'Design'),
('Lucas Mendes', 'Devops');
