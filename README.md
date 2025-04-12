# 🧠 Mental Health Data Model – ETL with Python

This project implements a full ETL process in Python to build a snowflake-style data model, designed for analytical use in Power BI. The model focuses on the global prevalence and burden of mental health disorders, based on datasets from Our World in Data (Kaggle).

---

## 📁 Project Structure

```

/data
    └── raw_data/  ← Original Kaggle CSVs
    └── cleaned/  ← Intermediate cleaned/reshaped data
    └── snow_squema/ ← Final model ready for Power BI

```

---

## ⚙️ ETL Process Overview

### 1. Data Cleaning & Transformation

Multiple sources were cleaned and standardized using `pandas`:
- Wide-to-long reshaping using `melt()`
- Column and type normalization
- ISO code completion using `Dim_Country`
- Integration of prevalence and burden data (DALYs)

### 2. Data Model (Snowflake Schema)

#### 🔹 `Fact_Prevalence`
Main fact table containing country-level yearly prevalence for each disorder, and DALY burden.

| CountryCode | Year | DisorderID | Prevalence | Burden |
|-------------|------|------------|------------|--------|

#### 🔹 `Dim_Country`
Includes country metadata enriched via `country_converter` and manual mapping.

| CountryCode | CountryName | Continent | UNRegion | Language |

#### 🔹 `Dim_Disorder`
Mental disorder reference table, including disorder group and number of countries with primary data available.

| DisorderID | DisorderName | DisorderGroup | CountriesWithData |

#### 🔹 `Dim_Time` *(optional, under development)*
Designed to support temporal hierarchy in Power BI (e.g., Year, Decade, Era).

---

## 🧰 Tools Used

- **Python 3.x**
- Libraries: `pandas`, `os`, `country_converter`
- IDE: Visual Studio Code

---

## 📈 Next Step: Power BI

This dataset is now ready to be imported into Power BI to build:
- Trend analysis of disorder prevalence
- Regional comparisons by DALY burden
- Data completeness heatmaps

---

## 👤 Author

Project by **Cristóbal Elton**  
[LinkedIn](https://linkedin.com/in/cristobalelton)

