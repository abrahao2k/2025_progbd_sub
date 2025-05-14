create database banco;

use banco;

create table cliente(
codigo int primary key auto_increment,
nome varchar(100) not null,
saldo float);

