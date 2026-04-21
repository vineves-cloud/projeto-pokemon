SELECT
    tipo as tipo,
    count(tipo) as 'qtd_pokemon'
FROM 
    pokemon
GROUP BY
    tipo
ORDER BY
    tipo