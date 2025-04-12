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

---

## 📊 Power BI Dashboard

Built using a snowflake schema model and multiple DAX measures. It focuses on both analysis and storytelling.

### 📌 Key Metrics (DAX)

- `Average Prevalence` = `AVG([Prevalence])`
- `Average Burden` = `AVG([Burden])`
- `Total Countries` = `DISTINCTCOUNT([CountryCode])`
- `Total Years` = `DISTINCTCOUNT([Year])`

### 📈 Visuals Used

- Cards with tooltips (prevalence, burden, country/year counts)
- Line chart (Prevalence over time by disorder)
- Map visual (bubble map by country burden or prevalence)
- Bar chart (Average burden by disorder)
- Matrix table (Country × Disorder breakdown)
- Slicers: Year, Disorder, Country, Continent
- Bookmarks: Toggle between Prevalence / Burden
- Custom Tooltips: Country/disorder metadata shown on hover

---

## 🎯 Goal

Designed to showcase:
- ETL automation with Python
- Data modeling with star schema
- Advanced Power BI techniques (tooltips, bookmarks, slicers)
- Visual storytelling and professional layout

---

## 👤 Author

**Cristóbal Elton**  
[LinkedIn](https://linkedin.com/in/cristobalelton)

