create database agencia_db;
use agencia_db;

-- Tablas Principales
CREATE TABLE Destino(
    id_destino int identity(1,1) primary key,
    nombre varchar(50) not null,
    descripcion varchar(500) not null,
    actividades varchar(200) not null,
	costo float
);

CREATE TABLE Cliente(
	id_cliente int identity(1,1) primary key,
	nombre varchar(500) not null,
	usuario varchar(100) not null unique,
	correo varchar(400) not null,
	contrasenia varchar(300) not null
);

CREATE TABLE PaqueteTuristico (
    id_paquete_turistico int identity(1,1) primary key,
    nombre_paquete varchar(100) not null unique,
    fecha_inicio date not null,
    fecha_termino datetime not null
);

-- Tablas Relacionales
create table Reserva (
	id_reserva int identity(1,1) primary key,
	id_cliente int REFERENCES Cliente(id_cliente) not null,
	id_paquete_turistico int REFERENCES PaqueteTuristico(id_paquete_turistico) not null,
	fecha_reserva datetime not null,
	estado BIT NOT NULL DEFAULT 1
);

create table DetallePaquete (
	id_detalle_paquete int identity(1,1)  primary key,
	id_paquete int REFERENCES PaqueteTuristico(id_paquete_turistico) not null,
	id_destino int REFERENCES Destino(id_destino) not null
);

-- Inserción Paquetes
INSERT INTO PaqueteTuristico(nombre_paquete, fecha_inicio, fecha_termino)
VALUES ('Paquete 1', '2025-02-03', '2025-02-15');

insert into PaqueteTuristico(nombre_paquete, fecha_inicio, fecha_termino)
values('Paquete 2', '2025-02-12', '2025-02-20');

insert into PaqueteTuristico(nombre_paquete, fecha_inicio, fecha_termino)
values('Paquete 3', '2025-03-20', '2025-04-01');

insert into PaqueteTuristico(nombre_paquete, fecha_inicio, fecha_termino)
values('Paquete 4', '2025-03-15', '2025-03-22');


-- inserción Destinos
insert into Destino(nombre, descripcion, actividades,costo)
values('San Pedro de Atacama', 'Con paisajes como el Valle de la Luna, los géiseres del Tatio y salares impresionantes.','Excursiones al Valle de la Luna y Valle de la Muerte, Visitar los géiseres del Tatio al amanecer.', 300000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Iquique', 'Famoso por sus playas, el casco histórico y el desierto de Pica y Humberstone (sitio declarado Patrimonio de la Humanidad).','Practicar parapente desde las dunas cercanas', 120000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Antofagasta', 'Hogar del Monumento Natural La Portada y acceso al desierto más árido del mundo', 'Excursiones al Salar de Atacama o al Observatorio ALMA', 250000)

insert into Destino(nombre, descripcion, actividades,costo)
Values('Santiago', 'La capital, con lugares como el Cerro San Cristóbal, el Palacio de La Moneda y los museos nacionales.','Visitar museos como el Museo de Arte Precolombino y el Museo Nacional de Historia.', 220000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Viña del Mar','Valparaíso es famosa por sus cerros, arte callejero y ascensores históricos, mientras que Viña del Mar tiene playas y festivales.','Relajarte en las playas de Viña del Mar,
visitar el jardín botánico y el famoso reloj de flores.', 310000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Isla de Pascua','Con sus icónicos moáis, volcanes y cultura única.','Practicar buceo o snorkel en las aguas cristalinas.', 580000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Valle del Elqui','Ideal para observar las estrellas, disfrutar del pisco chileno y relajarse.','Practicar trekking o relajarte en termas.', 450000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Pucón', 'Perfecto para deportes acuáticos, senderismo y disfrutar de termas.','Deportes acuáticos como kayak o paddle en el lago.', 130000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Valdivia','Con su fuerte historia colonial, cervecerías artesanales y ríos navegables.','Navegar por los ríos Calle-Calle y Valdivia.
Visitar los fuertes históricos en Corral y Niebla.', 200000);

insert into Destino(nombre, descripcion, actividades,costo)
values('Chiloé', 'Con su arquitectura tradicional, iglesias Patrimonio de la Humanidad y mitología rica. ','Visitar las iglesias Patrimonio de la Humanidad.
Explorar el Parque Nacional Chiloé y avistar fauna.', 600000)

insert into Destino(nombre, descripcion, actividades,costo)
values('Torres del Paine', 'Un paraíso para senderistas con montañas, glaciares y lagos de colores vibrantes.','Navegar por el lago Grey para ver el glaciar.
Avistamiento de guanacos, cóndores y otros animales.', 980000)

-- Inserción detalle paquetes -- -- -- -- -- -- -- -- -- -- -- -- -- --- -- -- -- -- -- -- -- -- -- -- -- -- --
insert into DetallePaquete(id_paquete, id_destino) values (2, 1);
insert into DetallePaquete(id_paquete, id_destino) values (2, 2);
insert into DetallePaquete(id_paquete, id_destino) values (2, 3);

insert into DetallePaquete(id_paquete, id_destino) values (3, 9);
insert into DetallePaquete(id_paquete, id_destino) values (3, 8);
insert into DetallePaquete(id_paquete, id_destino) values (3, 10);

insert into DetallePaquete(id_paquete, id_destino) values (4, 7);
insert into DetallePaquete(id_paquete, id_destino) values (4, 8);

insert into DetallePaquete(id_paquete, id_destino) values (5, 9);
insert into DetallePaquete(id_paquete, id_destino) values (5, 10);
insert into DetallePaquete(id_paquete, id_destino) values (5, 11);
insert into DetallePaquete(id_paquete, id_destino) values (5, 6);
insert into DetallePaquete(id_paquete, id_destino) values (5, 5);
insert into DetallePaquete(id_paquete, id_destino) values (5, 4);


-- Inserción de Reservas -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
insert into Reserva(id_cliente, id_paquete_turistico, fecha_reserva, estado) values (1, 2, GETDATE(), 1);
insert into Reserva(id_cliente, id_paquete_turistico, fecha_reserva, estado) values (1, 3, GETDATE(), 1);
insert into Reserva(id_cliente, id_paquete_turistico, fecha_reserva, estado) values (1, 4, GETDATE(), 1);

insert into Reserva(id_cliente, id_paquete_turistico, fecha_reserva, estado) values (3, 2, GETDATE(), 1);
insert into Reserva(id_cliente, id_paquete_turistico, fecha_reserva, estado) values (3, 5, GETDATE(), 1);

insert into Reserva(id_cliente, id_paquete_turistico, fecha_reserva, estado) values (5, 3, GETDATE(), 1);
-- VISTAS --------------------------------------------------------------------------------------------------------------------------------------------------------------------

CREATE VIEW vista_detalle_paquete AS
SELECT 
    PaqueteTuristico.nombre_paquete AS Nombre_Paquete,
    DetallePaquete.fecha_inicio AS Fecha_Inicio,
    DetallePaquete.fecha_termino AS Fecha_Termino,
    STRING_AGG(Destino.nombre, ', ') AS Destinos,
    SUM(Destino.costo) AS Costo_Total
FROM 
    PaqueteTuristico
JOIN 
    DetallePaquete ON PaqueteTuristico.id_paquete_turistico = DetallePaquete.id_paquete
JOIN 
    Destino ON DetallePaquete.id_destino = Destino.id_destino
GROUP BY 
    PaqueteTuristico.id_paquete_turistico, 
	PaqueteTuristico.nombre_paquete, 
	PaqueteTuristico.fecha_inicio, 
	PaqueteTuristico.fecha_termino;

-- Vista de reserva
CREATE VIEW vista_reserva AS
SELECT 
	Cliente.nombre AS 'nombre cliente',
	Cliente.usuario AS usuario,
	Cliente.correo AS cliente_correo,
	PaqueteTuristico.fecha_inicio,
	PaqueteTuristico.fecha_termino,
	Reserva.fecha_reserva,
	Reserva.estado,
	Destino.costo AS destino_costo
FROM 
	Reserva
JOIN 
	Cliente ON Reserva.id_cliente = Cliente.id_cliente
JOIN 
	PaqueteTuristico ON Reserva.id_paquete_turistico = PaqueteTuristico.id_paquete_turistico
JOIN 
	DetallePaquete ON PaqueteTuristico.id_paquete_turistico = DetallePaquete.id_paquete
JOIN 
	Destino ON DetallePaquete.id_destino = Destino.id_destino;


CREATE VIEW vista_reserva_agrupada AS
SELECT 
    Cliente.usuario AS "usuario",
    Cliente.nombre AS "nombre_cliente",
    Cliente.correo AS "correo_cliente",
    MIN(PaqueteTuristico.fecha_inicio) AS "primera_fecha_inicio",
    MAX(PaqueteTuristico.fecha_termino) AS "ultima_fecha_termino",
    COUNT(Reserva.id_reserva) AS "numero_reservas",
    SUM(Destino.costo) AS "costo_total_destinos"
FROM 
    Reserva
JOIN 
    Cliente ON Reserva.id_cliente = Cliente.id_cliente
JOIN 
    PaqueteTuristico ON Reserva.id_paquete_turistico = PaqueteTuristico.id_paquete_turistico
JOIN 
    DetallePaquete ON PaqueteTuristico.id_paquete_turistico = DetallePaquete.id_paquete
JOIN 
    Destino ON DetallePaquete.id_destino = Destino.id_destino
GROUP BY 
    Cliente.usuario, Cliente.nombre, Cliente.correo;

-- Vista de sesión reserva
CREATE VIEW VistaNuevasReservas AS
SELECT 
    os_user,
    ip_user,
    sesion_usuario,
    fecha,
    n_id_cliente AS id_cliente,
    n_id_paquete_turistico AS id_paquete_turistico,
    n_fecha_reserva AS fecha_reserva,
FROM 
    SesionReserva
WHERE 
    a_id_cliente IS NULL
    AND a_id_paquete_turistico IS NULL
    AND a_fecha_reserva IS NULL
;


select * from vista_detalle_paquete
select * from vista_reserva

-- TRIGGERS DE AUDITORIA ----------------------------------------------------------------------------------------------------------------------------------------------------
-- trigger de auditoría Destino
CREATE TABLE SesionDestino (
    os_user VARCHAR(100),
    ip_user VARCHAR(100),
    sesion_usuario VARCHAR(100),
    fecha DATETIME,
    a_nombre VARCHAR(50),
    a_descripcion VARCHAR(500),
    a_actividades VARCHAR(200),
    n_nombre VARCHAR(50),
    n_descripcion VARCHAR(500),
    n_actividades VARCHAR(200)
);

CREATE TRIGGER AuditoriaDestino
ON Destino
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO SesionDestino (
        os_user,
        ip_user,
        sesion_usuario,
        fecha,
        a_nombre,
        a_descripcion,
        a_actividades,
        n_nombre,
        n_descripcion,
        n_actividades
    )
    SELECT 
        SYSTEM_USER AS os_user,
        CAST(CONNECTIONPROPERTY('client_net_address') AS VARCHAR(100)) AS ip_user,
        SESSION_USER AS sesion_usuario,
        GETDATE() AS fecha,
        Deleted.nombre AS a_nombre,
        Deleted.descripcion AS a_descripcion,
        Deleted.actividades AS a_actividades,
        Inserted.nombre AS n_nombre,
        Inserted.descripcion AS n_descripcion,
        Inserted.actividades AS n_actividades
    FROM 
        Inserted
    INNER JOIN 
        Deleted
        ON Inserted.id_destino = Deleted.id_destino
    WHERE 
        Deleted.nombre != Inserted.nombre
        OR Deleted.descripcion != Inserted.descripcion
        OR Deleted.actividades != Inserted.actividades;
END;


-- trigger uditoria de reservas
CREATE TABLE SesionReserva (
    os_user VARCHAR(100),
    ip_user VARCHAR(100),
    sesion_usuario VARCHAR(100),
    fecha DATETIME,
    a_id_cliente INT,
    a_id_paquete_turistico INT,
    a_fecha_reserva DATETIME,
    n_id_cliente INT,
    n_id_paquete_turistico INT,
    n_fecha_reserva DATETIME
);

CREATE TRIGGER AuditoriaNuevaReserva
ON Reserva
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO SesionReserva (
        os_user,
        ip_user,
        sesion_usuario,
        fecha,
        a_id_cliente,
        a_id_paquete_turistico,
        a_fecha_reserva,
        n_id_cliente,
        n_id_paquete_turistico,
        n_fecha_reserva
    )
    SELECT 
        SYSTEM_USER AS os_user,
        CAST(CONNECTIONPROPERTY('client_net_address') AS VARCHAR(100)) AS ip_user,
        SESSION_USER AS sesion_usuario,
        GETDATE() AS fecha,
        NULL AS a_id_cliente,
        NULL AS a_id_paquete_turistico,
        NULL AS a_fecha_reserva,
        Inserted.id_cliente AS n_id_cliente,
        Inserted.id_paquete_turistico AS n_id_paquete_turistico,
        Inserted.fecha_reserva AS n_fecha_reserva
    FROM 
        Inserted;
END;


select * from Reserva
select * from Cliente where id_cliente = 8
select * from PaqueteTuristico where nombre_paquete = 'Paquete 1'