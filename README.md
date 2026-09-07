# Global Healthcare Efficiency Analysis

An international healthcare analytics project investigating a simple but important question:

> **Does spending more on healthcare necessarily lead to better health outcomes?**

Using healthcare expenditure, life expectancy, and infant mortality data across **150+ countries from 2000–2021**, the project combines PostgreSQL and Python analysis with an interactive Tableau dashboard to identify spending patterns, outcome differences, and countries that achieve stronger health outcomes relative to their level of spending.

🔗 **[View Interactive Tableau Dashboard](https://public.tableau.com/views/GlobalHealthcareEfficiencyAnalysis/Dashboard1)**

## Key Findings

* The **United States spends approximately 17% of GDP on healthcare**, the highest share among the countries analyzed, yet does not achieve the strongest life-expectancy outcomes relative to its spending.
* **Monaco** records life expectancy of approximately **86 years** while spending around **3.8% of GDP** on healthcare.
* Countries including **Eritrea, Cambodia, and Bhutan** improved life expectancy by more than **10 years** between 2000 and 2020.
* Several lower-spending countries, including **Monaco, Singapore, and the UAE**, achieve stronger outcomes than many higher-spending countries.
* The analysis highlights that **higher healthcare expenditure alone does not guarantee proportionally better health outcomes**.

## Business Questions

The analysis focuses on five questions:

1. **Does higher healthcare spending correspond to higher life expectancy?**
2. **Which countries achieve strong health outcomes with relatively lower spending?**
3. **Which countries have the largest improvements in life expectancy over time?**
4. **How does healthcare spending relate to infant mortality?**
5. **Which countries appear most efficient in converting healthcare spending into outcomes?**

## Analytical Approach

### 1. Data Preparation

Healthcare expenditure, life expectancy, and infant mortality data were cleaned and imported into PostgreSQL for analysis.

### 2. Cross-Country Comparison

Countries were compared based on healthcare expenditure and key health outcomes to identify differences in performance across spending levels.

### 3. Efficiency Analysis

The analysis compares health outcomes against healthcare spending to identify countries that achieve relatively strong outcomes without being among the highest spenders.

### 4. Trend Analysis

Year-over-year changes were analyzed to identify countries with significant improvements in life expectancy.

### 5. Ranking & Segmentation

Countries were ranked and categorized using SQL window functions to identify high-performing and lower-performing groups.

## SQL Analysis

The project uses PostgreSQL to perform the core analysis, including:

* Joining multiple healthcare datasets
* Creating reusable analytical views
* Conditional categorization with `CASE WHEN`
* Common Table Expressions (CTEs)
* Country rankings using `RANK()` and `DENSE_RANK()`
* Window-based averages using `AVG() OVER`
* Year-over-year analysis using `LAG()`
* Data cleaning and filtering

Example analytical pattern:

```sql
WITH country_analysis AS (
    SELECT
        country,
        year,
        healthcare_spending,
        life_expectancy,
        LAG(life_expectancy) OVER (
            PARTITION BY country
            ORDER BY year
        ) AS previous_life_expectancy
    FROM healthcare_data
)
SELECT
    country,
    year,
    life_expectancy - previous_life_expectancy AS annual_change
FROM country_analysis
WHERE previous_life_expectancy IS NOT NULL;
```

## Project Structure

| File              | Purpose                                            |
| ----------------- | -------------------------------------------------- |
| `import_data.py`  | Cleans and imports source datasets into PostgreSQL |
| `queries.sql.sql` | Contains the core SQL analysis                     |
| `README.md`       | Project documentation                              |

## Data Sources

The analysis uses publicly available World Bank indicators:

* **Current health expenditure (% of GDP)**
* **Life expectancy at birth**
* **Infant mortality rate**

The dataset covers **150+ countries across 2000–2021**.

## Tech Stack

**PostgreSQL · SQL · Python · pandas · SQLAlchemy · Tableau Public**

## Dashboard

The Tableau dashboard provides an interactive view of:

* Healthcare expenditure by country
* Life expectancy comparisons
* Infant mortality patterns
* Country rankings
* Long-term trends
* Spending vs outcome relationships

🔗 **[Open Tableau Dashboard](https://public.tableau.com/views/GlobalHealthcareEfficiencyAnalysis/Dashboard1)**

## What This Project Demonstrates

* Business question framing
* Healthcare and economic data analysis
* SQL data transformation and analysis
* Multi-table joins
* Window functions and CTEs
* Ranking and segmentation
* Time-series trend analysis
* Cross-country benchmarking
* Translating analytical results into business insights
* Tableau dashboard development
