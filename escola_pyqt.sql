create database escola;

use escola;

create table aluno(
codigo int primary key auto_increment,
nome varchar(100) not null,
curso varchar(100),
turno varchar(100),
atleta varchar(100),
bolsista varchar(100),
obs varchar(200));