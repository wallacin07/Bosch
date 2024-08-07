SELECT
	S.Nome,
	E.Descricao,
	S.Capacidade,
	Count(EP.Presenca)
	

FROM EventoPessoa EP
RIGHT JOIN Pessoa P
	On EP.IDPessoa = P.IDPessoa
RIGHT JOIN Evento E
	On EP.IDEvento = E.IDEvento
RIGHT JOIN Sala S
	On E.IDSala =  S.IDSala
Order by Count(EP.Presenca) DESC

