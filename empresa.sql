create database empresa;

use empresa;

create table equipamento(
codigo int primary key auto_increment,
descricao varchar(100),
marca varchar(100),
valor float);