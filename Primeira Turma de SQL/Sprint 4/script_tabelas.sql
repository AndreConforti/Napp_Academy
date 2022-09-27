CRIAÇÃO DAS TABELAS:

create table PRODUTOS(
	IDPRODUTO serial primary key,
	EAN VARCHAR(18) not null,
	NOME VARCHAR(30),
	DESCRICAO VARCHAR(30),
	ESTOQUE INT not null,
	BRUTO NUMERIC(5,2) not null,
	LIQUIDO NUMERIC(5,2) not null,
	status varchar(15) not null
)

create table VENDA(
	IDVENDA serial primary key,
	DATA_VENDA DATE not null,
	BRUTO NUMERIC(5,2) not null,
	LIQUIDO NUMERIC(5,2) not null,
	DESCONTO NUMERIC(5,2) not null,
	status varchar(15) not null
)

CREATE TABLE vendas_itens (
	id_venda int not null,
	order_number int not null,
	data_venda date not null,
	id_produto int not null,
	ean varchar(18) NOT NULL,
	nome_prod varchar(30) not null,
	quantidade int not null,
	bruto numeric(5, 2) NOT NULL,
	liquido numeric(5, 2) NOT NULL,
	desconto numeric(5, 2) NOT NULL,
	status varchar(15) not null,
	CONSTRAINT vendas_itens_id_produto_fkey FOREIGN KEY (id_produto) REFERENCES public.produtos(idproduto),
	CONSTRAINT vendas_itens_id_vendas_fkey FOREIGN KEY (id_venda) REFERENCES public.venda(idvenda)
);


INSERINDO DADOS:

VENDAS:
insert into venda(data_venda,bruto,liquido,desconto,status) values('2022-01-01', 56.89, 51.89, 5,'Faturado'),
('2022-01-01', 50.37, 50.37, 0,'Faturado'),
('2022-01-01', 52.40, 51, 1.40,'Faturado'),
('2022-01-01', 29.86, 27.86, 2,'Faturado'),
('2022-01-01', 76.89, 73.89, 3,'Faturado');

PRODUTOS:
INSERT INTO produtos (ean,nome,descricao,estoque,bruto,liquido,status) VALUES
('7896094919693','Neosaldina','20 Comprimidos',10,19.86,19.86,'Ativo'),
('7896641803871','Engov citrus','250ml',18,10.65,10.65,'Ativo'),
('7891058019099','Novalgina','1g 10 Comprimidos',6,21.89,21.89,'Ativo'),
('7896094908529','Doril ','CAIXA 18 COMPRIMIDOS',10,25.00,25.00,'Ativo'),
('7894916143202','Dipirona','500mg 10 Comprimidos ',10,5.00,5.00,'Ativo');

VENDAS - ITENS:
insert into vendas_itens(id_venda,order_number,data_venda,id_produto,ean,nome_prod,quantidade,bruto,liquido,desconto,status)
values(1,1,'2022-01-01',3,'7891058019099','Novalgina',1,21.89,16.89,5,'Faturado'),
(1,2,'2022-01-01',4,'7896094908529','Doril ',1,25,25,0,'Faturado'),
(1,3,'2022-01-01',5,'7894916143202','Dipirona',2,5,5,0,'Faturado'),
(2,1,'2022-01-01',1,'7896094919693','Neosaldina',2,39.72,39.72,0,'Faturado'),
(2,2,'2022-01-01',2,'7896641803871','Engov citrus ',1,10.65,10.65,0,'Faturado'),
(3,1,'2022-01-01',3,'7891058019099','Novalgina',2,21.89,20.49,1.4,'Faturado'),
(3,2,'2022-01-01',2,'7896641803871','Engov citrus',1,10.65,10.65,0,'Faturado'),
(3,3,'2022-01-01',1,'7896094919693','Neosaldina',1,19.86,19.86,0,'Faturado'),
(4,1,'2022-01-01',3,'7896094919693','Neosaldina',1,19.86,17.86,2,'Faturado'),
(4,2,'2022-01-01',5,'7894916143202','Dipirona',2,5,5,0,'Faturado'),
(5,1,'2022-01-01',4,'7896094908529','Doril',2,25,22,3,'Faturado'),
(5,2,'2022-01-01',3,'7891058019099','Novalgina',1,21.89,21.89,0,'Faturado'),
(5,3,'2022-01-01',5,'7896094908529','Doril',1,5,5,0,'Faturado');

