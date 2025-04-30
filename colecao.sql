create database colecao;

use colecao;

create table item(
codigo int primary key auto_increment,
descricao varchar(100),
valor float,
observacao varchar(200));

insert into item values(
null,"cubo 3x3 arredondado",18,"sem borda");

insert into item values(
null,"cubo 2x2",15,"borda preta");

insert into item values(
null,"cubo 3x3",25,"cor solida");

insert into item values(
null,"piramide",20,"espelhada");

update item
set observacao = "borda fina"
where codigo = 3;

update item
set descricao = "cubo 3x3 arredondado",
    valor = 22.50
where codigo = 5;

# PERIGO!!!!! UPDATE COM WHERE PRA VÁRIAS LINHAS
update item
set valor = 0
where codigo >= 1;

# ATUALIZADO VÁRIAS LINHAS SEM SER PELO CÓDIGO
update produtos
set desconto = 10
where categoria = "frutas";


# excluir um registro

DELETE FROM ITEM
WHERE codigo = 5;


# FUNÇÕES DE AGREGAÇÃO

# SOMA DOS VALORES DE UMA COLUNA
select sum(valor) from item;

# MÉDIA DOS VALORES DE UMA COLUNA
# não considera valores nulos
select avg(valor) from item;

# MAIOR E MENOR VALORES
select max(valor) from item;
select min(valor) from item;

# CONTAGEM DE RESULTADOS DE UMA CONSULTA
select count(*) from item
where valor > 20;



insert into item values (null,"Prisma",null,"Colorido");
insert into item values (null,"Cubo 5x5",0,"Verde");






