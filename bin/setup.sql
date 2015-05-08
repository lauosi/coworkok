CREATE ROLE vagrant LOGIN NOINHERIT CREATEDB PASSWORD 'vagrant';
CREATE DATABASE template_postgis;
\c template_postgis
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
\c postgres
UPDATE pg_database SET datistemplate = true where datname = 'template_postgis';
CREATE DATABASE coworkok TEMPLATE template_postgis OWNER vagrant;
