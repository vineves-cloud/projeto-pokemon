SELECT
    nome,
    ataque
FROM pokemon
ORDER BY ataque DESC
LIMIT 1;

SELECT
    AVG(ataque)
AS  media_ataque
FROM pokemon;

SELECT 
    AVG(defesa) INTEGER
FROM pokemon
GROUP BY tipo;