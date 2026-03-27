# Global Healthcare Efficiency Analysis

## Project Overview
Analyzed WHO and World Bank health expenditure data across 
150+ countries from 2000-2021 to answer: 
"Does spending more on healthcare guarantee better outcomes?"

## Key Findings
- USA spends 17% of GDP — highest globally — yet ranks 
  below 27 countries in life expectancy efficiency
- Monaco has highest life expectancy at 86 years with 
  only 3.8% GDP spending
- Eritrea, Cambodia and Bhutan improved life expectancy 
  by 10+ years between 2000 and 2020
- Low spender countries like Monaco, Singapore and UAE 
  outperform many high spenders

## Tools Used
- PostgreSQL — database and SQL analysis
- Python (pandas, sqlalchemy) — data cleaning and import
- Tableau Public — interactive dashboard

## Live Dashboard
 dashboard : (https://public.tableau.com/views/GlobalHealthcareEfficiencyAnalysis/Dashboard1)

## SQL Concepts Used
- INNER JOIN across 3 tables
- CREATE VIEW for reusable queries
- CASE WHEN for categorization
- CTE (Common Table Expression)
- RANK() and DENSE_RANK() window functions
- AVG() OVER PARTITION BY
- LAG() for trend analysis
- Data cleaning with DELETE WHERE

## Data Sources
- World Bank: Current health expenditure % of GDP
- World Bank: Life expectancy at birth
- World Bank: Infant mortality rate