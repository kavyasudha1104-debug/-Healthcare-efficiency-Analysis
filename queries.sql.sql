
-- ##Query 1 — CREATE TABLE
CREATE TABLE health_spend (
    country_name VARCHAR(100),
    country_code VARCHAR(10),
    year INT,
    health_expenditure DECIMAL(10,2)
);

-- Query 2 — CREATE VIEW (master_health)
CREATE VIEW master_health AS
SELECT h.country_name, h.country_code, h.year,
       h.health_expenditure, l.life_exp, i.mortality_rate
FROM health_spend h
INNER JOIN life_expectancy l 
    ON h.country_code = l.country_code AND h.year = l.year
INNER JOIN infant_mortality i 
    ON h.country_code = i.country_code AND h.year = i.year;

-- Query 3 — CASE WHEN
CASE
    WHEN health_expenditure > 10 THEN 'High Spender'
    WHEN health_expenditure > 5  THEN 'Medium Spender'
    ELSE 'Low Spender'
END AS spending_category

-- Query 4 — CTE + RANK()
WITH efficiency AS (
    SELECT country_name,
           AVG(life_exp) / AVG(health_expenditure) AS efficiency_score
    FROM master_health
    GROUP BY country_name
)
SELECT country_name, efficiency_score,
       RANK() OVER (ORDER BY efficiency_score DESC) AS rank
FROM efficiency;

-- Query 5 — Outlier Detection
WITH country_avg AS (
    SELECT country_name,
           AVG(health_expenditure) AS avg_spend,
           AVG(life_exp) AS avg_life_exp
    FROM master_health
    GROUP BY country_name
)
SELECT country_name, avg_spend, avg_life_exp
FROM country_avg
WHERE avg_spend < 5 AND avg_life_exp > 72;

-- Query 6 — Window Function
SELECT country_name, year, life_exp,
       AVG(life_exp) OVER (PARTITION BY year) AS global_avg,
       life_exp - AVG(life_exp) OVER (PARTITION BY year) AS diff_from_global
FROM master_health
WHERE year = 2019;

-- Query 7 — Trend Analysis with DENSE_RANK
WITH year_2000 AS (SELECT country_name, life_exp AS life_2000 FROM master_health WHERE year = 2000),
year_2020 AS (SELECT country_name, life_exp AS life_2020 FROM master_health WHERE year = 2020)
SELECT y0.country_name, y0.life_2000, y2.life_2020,
       y2.life_2020 - y0.life_2000 AS improvement,
       DENSE_RANK() OVER (ORDER BY (y2.life_2020 - y0.life_2000) DESC) AS rank
FROM year_2000 y0
JOIN year_2020 y2 ON y0.country_name = y2.country_name;