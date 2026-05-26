-- CA total --
SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;

-- CA Par régions --
SELECT region, SUM(prix * qte) AS chiffre_affaires_region
FROM ventes
GROUP BY region
ORDER BY chiffre_affaires_region DESC;

-- CA par produit --
SELECT produit, SUM(qte) AS quantite_totale, SUM(prix * qte) AS chiffre_affaires_produit
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaires_produit DESC;
