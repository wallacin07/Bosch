use AULA_SQL

--CREATE  TRIGGER  GerarLog -- � o nome definido pelo usu�rio para o novo trigger
--ON  TABELA_DE_CLIENTES -- � a tabela � qual o trigger se aplica.
--AFTER INSERT
--AS
--BEGIN
--    Insert Into Log (Data,Operacao,Observacao) VALUES (SYSDATETIME(),'Inser��o', (SELECT NOME FROM inserted))
--END

--DROP TRIGGER Burlar

--Insert Into TABELA_DE_CLIENTES (CPF,NOME,ENDERECO_1) VALUES(55969633115,'Alberto', 'Rua do meu cora��o')

CREATE  TRIGGER  Burlar -- � o nome definido pelo usu�rio para o novo trigger
ON  TABELA_DE_CLIENTES -- � a tabela � qual o trigger se aplica.
Instead of DELETE
AS
BEGIN
    Delete From ITENS_NOTAS_FISCAIS WHERE NUMERO IN (SELECT NUMERO FROM NOTAS_FISCAIS WHERE CPF = (SELECT CPF FROM deleted))
	delete From NOTAS_FISCAIS WHERE CPF IN (SELECT CPF FROM deleted)
	Delete FROM TABELA_DE_CLIENTES where CPF in (SELECT CPF FROM deleted)

END

delete from TABELA_DE_CLIENTES where CPF = '19290992743'

select * from TABELA_DE_CLIENTES
select * from NOTAS_FISCAIS
select * from ITENS_NOTAS_FISCAIS