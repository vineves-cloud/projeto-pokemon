SELECT
    tipo as 'Tipo',
    CAST(AVG(ataque) as INTEGER) as 'Média de ataque'
    
FROM
    pokemon
GROUP BY
    tipo