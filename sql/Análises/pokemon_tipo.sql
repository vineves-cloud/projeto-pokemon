SELECT
    tipo as Tipo,
    count(tipo) as 'Qtd de Pokemon'
FROM 
    pokemon
GROUP BY
    tipo