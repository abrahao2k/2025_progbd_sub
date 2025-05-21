create database videogames;
use videogames;
create table jogos(
codigo int primary key auto_increment,
titulo varchar(100) not null,
plataforma varchar(100));

insert into jogos values(1,'Tetris','Game boy');
insert into jogos values(2,'Sonic','Mega Drive');
insert into jogos values(3,'Mario Kart','Switch');
insert into jogos values(4,'Elden Ring','PC');
insert into jogos values(5,'Candy Crush','Android');