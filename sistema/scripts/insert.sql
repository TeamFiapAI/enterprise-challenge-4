INSERT 
    INTO operadores (nome, funcao)
VALUES
    ('João Silva', 'Técnico de manutenção'),
    ('Maria Souza', 'Operadora de máquina'),
    ('Carlos Pereira', 'Supervisor de produção');

INSERT 
    INTO maquinas (nome, descricao, localizacao)
VALUES 
    ('Máquina A', 'Prensa hidráulica de alta pressão', 'Setor 1'),
    ('Máquina B', 'Injetora de plástico', 'Setor 2'),
    ('Máquina C', 'Esteira transportadora', 'Setor 3');


-- Inserts de registros gerados automaticamente

INSERT 
    INTO registros (id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES
 (3, NULL, '2024-05-09 03:52:47', 25.18, 73.36, 1577, 1729, 0, TRUE);

INSERT 
    INTO registros (id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES
    (2, 2, '2023-04-06 21:35:36', 22.22, 60.99, 731, 3542, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-11-06 10:04:59', 42.45, 63.42, 899, 3072, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-12-06 22:56:59', 20.81, 27.42, 1586, 1587, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-09-13 12:38:17', 30.11, 68.31, 977, 1565, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-12-14 06:50:22', 43.67, 64.25, 1120, 2112, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-09-29 09:13:21', 49.73, 19.55, 960, 3244, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-10-21 11:26:53', 30.59, 75.11, 1399, 3369, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-02-19 12:36:33', 41.45, 45.72, 797, 2757, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-03-27 16:43:34', 27.35, 60.31, 1958, 3406, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-05-07 15:06:59', 46.71, 50.32, 1026, 3507, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-11-01 16:57:12', 46.35, 11.1, 1406, 2917, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-12-24 21:19:45', 20.9, 30.46, 1659, 2153, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-11-02 16:15:14', 41.41, 28.92, 817, 1943, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-12-03 12:02:22', 21.56, 67.96, 1565, 3386, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-10-15 00:55:10', 23.12, 74.91, 726, 3335, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-01-24 22:59:29', 36.15, 29.6, 1497, 2378, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-06-19 13:03:03', 48.96, 24.55, 1249, 3749, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-07-02 18:51:04', 35.64, 43.18, 1866, 1972, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-06-05 12:51:04', 35.15, 76.82, 1513, 2613, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-05-22 09:24:21', 20.37, 50.97, 514, 2461, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-04-23 14:46:26', 28.5, 13.48, 1107, 2019, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-03-01 18:25:12', 33.72, 20.28, 1558, 3716, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-01-08 05:12:03', 34.67, 74.42, 563, 1941, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-03-15 14:42:41', 23.83, 12.86, 835, 2621, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-05-24 12:24:07', 47.16, 11.23, 1416, 3377, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-12-27 19:47:07', 44.45, 78.85, 679, 3476, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-06-22 14:01:49', 40.18, 28.43, 1779, 2508, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-03-15 08:53:52', 48.25, 31.4, 1930, 2731, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-11-25 00:18:04', 46.37, 54.06, 1412, 2100, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-10-03 22:36:20', 36.09, 64.93, 1641, 3197, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-11-21 17:59:24', 48.97, 35.43, 791, 3806, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-11-12 11:25:57', 36.75, 73.92, 1592, 2872, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-10-15 20:32:44', 44.26, 26.46, 1893, 1673, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-07-07 04:55:03', 45.68, 37.03, 1307, 3629, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-11-23 05:10:58', 43.7, 72.03, 739, 2869, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-02-03 06:25:16', 48.9, 14.15, 797, 2800, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-05-23 04:36:39', 40.76, 59.68, 1817, 2433, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-10-26 05:13:09', 39.38, 64.07, 1435, 3225, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-06-11 00:10:12', 36.21, 60.98, 1332, 3439, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-06-07 03:44:02', 37.57, 38.45, 952, 3612, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-10-22 16:28:45', 42.96, 55.94, 1978, 3599, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-08-27 03:50:45', 43.07, 30.3, 1789, 1950, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-12-10 21:20:03', 30.54, 76.25, 1872, 3465, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-02-24 16:16:56', 37.0, 23.79, 1326, 3630, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-06-25 12:19:03', 46.21, 63.8, 553, 2746, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-09-28 02:33:39', 27.69, 21.06, 1939, 2855, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-11-01 02:22:04', 23.19, 34.61, 985, 3611, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-09-28 16:55:27', 47.66, 10.42, 1327, 3446, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-05-02 03:35:37', 41.03, 72.7, 1325, 3725, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-10-02 16:38:18', 37.44, 79.62, 1491, 1979, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-08-27 20:12:22', 48.11, 17.38, 546, 2166, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-06-22 22:39:51', 36.5, 57.54, 1409, 1941, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-05-16 22:50:47', 22.75, 70.26, 1534, 3549, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-04-10 22:23:11', 46.09, 75.19, 607, 2252, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-04-21 11:42:23', 28.23, 21.98, 1482, 2025, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-03-31 19:14:55', 22.96, 77.88, 693, 2329, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-12-10 06:11:45', 28.16, 37.69, 1519, 2677, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-04-12 23:15:08', 38.48, 76.76, 1314, 3389, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-03-12 04:30:51', 43.48, 16.06, 1322, 2866, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-12-03 22:58:03', 25.79, 55.17, 1013, 1809, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-03-18 21:49:51', 28.49, 52.62, 815, 2267, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-03-03 20:36:16', 31.58, 21.59, 1061, 2032, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-03-30 08:20:45', 37.17, 19.17, 905, 1600, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-08-02 01:56:04', 39.69, 34.76, 538, 3635, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-10-12 05:54:08', 24.09, 76.93, 1637, 2994, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-09-24 14:29:49', 34.18, 20.44, 960, 1877, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-10-29 04:27:04', 45.75, 76.64, 1709, 3571, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-10-12 16:03:19', 46.69, 27.98, 631, 3140, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-03-28 17:30:44', 33.61, 36.84, 1322, 1538, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-11-01 05:22:54', 25.83, 19.33, 1054, 2759, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-05-15 21:02:45', 42.76, 17.12, 1059, 3614, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-09-24 16:13:50', 22.53, 17.19, 955, 3826, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-03-25 06:00:19', 43.28, 25.27, 519, 2209, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-10-21 04:20:04', 44.95, 46.84, 1497, 1773, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-01-22 00:13:15', 29.62, 70.03, 1709, 2058, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-08-24 05:21:32', 24.5, 70.92, 1102, 1900, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-03-19 03:56:48', 31.67, 78.14, 1288, 3399, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-11-07 06:13:20', 47.43, 25.08, 1696, 1965, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-09-26 15:01:53', 44.92, 47.01, 1435, 1655, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-10-08 15:20:07', 28.49, 31.82, 1671, 3124, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-02-27 08:23:27', 46.63, 44.29, 1043, 2028, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-07-17 23:02:32', 31.26, 42.78, 1584, 3716, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-01-28 14:05:03', 46.38, 45.49, 1134, 2947, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-01-14 23:17:49', 23.43, 42.22, 1219, 3280, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-11-05 07:19:08', 34.76, 19.9, 1799, 2856, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-06-01 02:00:40', 42.28, 67.23, 1396, 2960, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-10-19 14:04:47', 33.08, 34.25, 1159, 2724, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-11-27 18:51:19', 38.17, 63.79, 1174, 2134, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2023-06-05 19:43:18', 22.14, 39.59, 1249, 2971, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-04-01 10:30:05', 34.12, 70.43, 989, 3369, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-09-25 07:40:13', 23.7, 54.86, 1639, 2052, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-05-28 04:03:38', 33.19, 68.68, 814, 2211, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-08-12 07:24:51', 38.77, 64.26, 707, 2504, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (3, NULL, 
'2024-01-20 16:39:47', 32.0, 41.63, 935, 3973, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2023-05-15 02:01:41', 39.91, 12.84, 1951, 2234, 0, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-07-02 08:01:11', 42.75, 29.88, 1883, 3804, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2024-09-23 13:00:54', 24.74, 18.76, 1575, 3515, 1, FALSE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (2, 2, 
'2024-10-17 02:19:41', 24.46, 76.16, 1443, 1716, 1, TRUE);
INSERT INTO registros 
(id_maquina, id_operador, data_coleta, temperatura, umidade, potenciometro, gasAO, gasDO, alarme)
VALUES (1, 1, 
'2023-11-07 20:22:56', 47.72, 18.87, 1969, 3396, 0, TRUE);
