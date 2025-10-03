-- TABELA DE MÁQUINAS
CREATE TABLE maquinas (
    id_maquina NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    descricao CLOB,
    localizacao VARCHAR2(100)
);

-- TABELA DE OPERADORES
CREATE TABLE operadores (
    id_operador NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    funcao VARCHAR2(100)
);

-- TABELA DE REGISTROS ESP32
CREATE TABLE registros (
    id_registro NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_maquina NUMBER NOT NULL,
    id_operador NUMBER NULL,
    data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperatura NUMBER(5,2),   -- Ex: 40.50
    umidade NUMBER(5,2),       -- Ex: 2.30
    potenciometro NUMBER,      -- Ex: 1333
    gasAO NUMBER,              -- Ex: 3628
    gasDO NUMBER(1),           -- 0 ou 1
    alarme NUMBER(1),          -- 0 ou 1
    CONSTRAINT fk_maquina FOREIGN KEY (id_maquina) REFERENCES maquinas (id_maquina),
    CONSTRAINT fk_operador FOREIGN KEY (id_operador) REFERENCES operadores (id_operador)
);
