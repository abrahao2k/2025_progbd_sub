# criar um banco de dados
create database aula3;

# escolher o banco ativo
use aula3;

# criar uma tabela
create table pessoas(
codigo int primary key auto_increment,
nome varchar(60) not null,
idade int
);

# inserir dados na tabela
insert into pessoas values (1,"Ana",26);

# inserir sem informar o código
insert into pessoas values(null,"Bia",29); 

# inserir apenas algumas colunas
insert into pessoas(nome) values ("Caio");

insert into pessoas(nome, idade)
values("Diana", 36);

# inserir vários cadastros em um comando
insert into pessoas values 
(null,"Elias",42),
(null,"Felicia",17),
(null,"Gabriel",34);

# selecionar todos os dados da tabela
select * from pessoas;

# exibir algumas colunas (qualquer ordem)
select idade, nome from pessoas;

# ordenar os valores de uma coluna
select * from pessoas order by idade;

# ordem decrescente (do maior pro menor)
select * from pessoas order by codigo desc;

# exibir algumas LINHAS
select * from pessoas where idade < 30;

select * from pessoas where nome = "ANA";

# exibir apenas valores nulos
select * from pessoas where idade IS NULL;

# operador AND (todas verdadeiras)
select * from pessoas
where codigo >= 4 and idade <= 35;

# operador OR (mínimo uma verdadeira)
select * from pessoas
where nome = "Bia" or idade = 42
or nome = "Fernando" or idade = 17;

# intervalos numéricos
select * from pessoas
where idade between 26 and 34; # inclusive

select * from pessoas
where idade >= 26 and idade =< 34; # inclusive

select * from pessoas
where idade > 26 and idade < 34; # exclui

select * from pessoas
where nome >= "carlos" and nome <= "fabio";

# seleção de conjuntos
select * from pessoas
where idade in (20, 26, 32, 42, 56);

select * from pessoas
where nome in ("caio", "felicia", "guilherme");


# expressão usando AND e OR
# select * from alunos where
# (curso = 'info' and ano = 1) or
# (curso = 'edif' and ano = 2);