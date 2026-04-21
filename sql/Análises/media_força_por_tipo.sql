SELECT
    tipo as 'Tipo',
    ROUND(AVG(ataque),2) as 'media_ataque'
    
FROM
    pokemon
GROUP BY
    tipo