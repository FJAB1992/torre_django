-- Insertando datos en la tabla de deportes
insert into deportes (nombre) values
('Fútbol'),
('Baloncesto'),
('Tenis'),
('Voleibol'),
('Atletismo');

-- Insertando datos en la tabla de instalaciones
insert into instalaciones (nombre, direccion, iluminacion, cubierta) values
('Estadio Municipal', 'Calle Principal, 123', true, true),
('Polideportivo Municipal', 'Avenida de los Deportes, 456', true, false),
('Club de Tenis', 'Calle del Set, 789', false, true),
('Pista de Voleibol Playa', 'Calle de la Arena, S/N', false, false),
('Pista de Atletismo', 'Avenida de los Corredores, 101', true, true);

-- Insertando datos en la tabla de equipos
insert into equipos (nombre, id_deporte, equipacion_principal, equipacion_suplente, contacto, telefono, email) values
('Real Madrid', 1, 'Blanca', 'Negra', 'Juan Pérez', '123456789', 'info@realmadrid.com'),
('FC Barcelona', 1, 'Azul y Grana', 'Negra', 'Maria López', '987654321', 'info@fcbarcelona.com'),
('Los Angeles Lakers', 2, 'Amarilla y Púrpura', 'Blanca', 'John Smith', '555123456', 'info@lakers.com'),
('Chicago Bulls', 2, 'Roja', 'Negra', 'Emily Johnson', '555789012', 'info@bulls.com'),
('Equipo de Tenis Nadal', 3, 'Blanca', 'Naranja', 'Rafael Nadal', '999888777', 'info@rnadal.com');

-- Insertando datos en la tabla de jugadores
insert into jugadores (nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono) values
('Cristiano', 'Ronaldo', 'dos Santos', 1, 7, '1985-02-05', 1.87, 83, '111222333'),
('Lionel', 'Messi', '', 2, 10, '1987-06-24', 1.70, 72, '444555666'),
('LeBron', 'James', '', 3, 23, '1984-12-30', 2.03, 113, '777888999'),
('Michael', 'Jordan', '', 4, 23, '1963-02-17', 1.98, 98, '999000111'),
('Rafael', 'Nadal', 'Parera', 5, 1, '1986-06-03', 1.85, 85, '333444555');

-- Insertando datos en la tabla de partidos
insert into partidos (id_deporte, fecha_hora, id_instalacion, id_local, id_visitante, puntos_local, puntos_visitante, observaciones) values
(1, '2024-02-22 15:00:00', 1, 1, 2, 2, 1, 'Partido de Liga'),
(2, '2024-02-23 18:30:00', 2, 3, 4, 110, 108, 'Partido de Temporada Regular'),
(3, '2024-02-24 10:00:00', 3, 5, 0, 0, 0, 'Partido de Exhibición'),
(4, '2024-02-25 14:15:00', 4, 3, 5, 21, 18, 'Partido Amistoso'),
(5, '2024-02-26 17:45:00', 5, 5, 0, 0, 0, 'Entrenamiento');

-- Insertando 5 partidos más que se jueguen en diciembre de 2024
insert into partidos (id_deporte, fecha_hora, id_instalacion, id_local, id_visitante, puntos_local, puntos_visitante, observaciones) values
(6, '2024-12-01 16:00:00', 1, 2, 1, 0, 0, 'Partido de Liga'),
(7, '2024-12-05 20:15:00', 2, 4, 3, 95, 98, 'Partido de Temporada Regular'),
(8, '2024-12-10 11:30:00', 3, 0, 5, 0, 0, 'Partido de Exhibición'),
(9, '2024-12-15 13:45:00', 4, 5, 3, 25, 22, 'Partido Amistoso'),
(10, '2024-12-20 18:00:00', 5, 0, 4, 0, 0, 'Entrenamiento');

-- Insertando dos jugadores que pertenezcan al mismo equipo de dos equipos distintos
INSERT INTO jugadores (nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono) VALUES
('Sergio', 'Ramos', 'García', 1, 4, '1986-03-30', 1.84, 75, '111222333'),
('Gerard', 'Piqué', 'Bernabeu', 2, 3, '1987-02-02', 1.94, 85, '444555666');

-- Insertando 3 partidos más
INSERT INTO partidos (id_deporte, fecha_hora, id_instalacion, id_local, id_visitante, puntos_local, puntos_visitante, observaciones) VALUES
(1, '2024-12-25 14:00:00', 1, 1, 2, 3, 2, 'Partido de Navidad'),
(2, '2024-12-28 19:30:00', 2, 3, 4, 100, 102, 'Partido de Temporada Regular'),
(3, '2024-12-30 12:00:00', 3, 5, 1, 1, 3, 'Partido de Exhibición');

-- Insertando 3 jugadores más para cada equipo
-- Suponiendo que los IDs de los equipos son 1 y 2

-- Jugadores para el equipo con id_equipo = 1
INSERT INTO jugadores (nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono) VALUES
('Gareth', 'Bale', '', 1, 11, '1989-07-16', 1.83, 74, '777888999'),
('Karim', 'Benzema', '', 1, 9, '1987-12-19', 1.87, 81, '111222333'),
('Luka', 'Modric', '', 1, 10, '1985-09-09', 1.74, 66, '444555666');

-- Jugadores para el equipo con id_equipo = 2
INSERT INTO jugadores (nombre, apellido1, apellido2, id_equipo, dorsal, fecha_nacimiento, altura, peso, telefono) VALUES
('Antoine', 'Griezmann', '', 2, 7, '1991-03-21', 1.76, 73, '999000111'),
('Jordi', 'Alba', '', 2, 18, '1989-03-21', 1.70, 68, '222333444'),
('Frenkie', 'de Jong', '', 2, 21, '1997-05-12', 1.81, 74, '555666777');
