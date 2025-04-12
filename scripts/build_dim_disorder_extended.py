import pandas as pd
import os

# === Cargar archivos base ===
dim_disorder = pd.read_csv("data/snow_squema/Dim_Disorder.csv")
disorder_metadata = pd.read_csv(
    "data/7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv"
)

# === Renombrar columna de metadata para claridad ===
disorder_metadata = disorder_metadata.rename(columns={
    "Entity": "DisorderName",
    "Number of countries with primary data on prevalence of mental disorders": "CountriesWithData"
})

# === Definir mapeo entre Dim_Disorder y metadata ===
disorder_country_data = {
    "Anxiety": disorder_metadata.loc[disorder_metadata["DisorderName"] == "Anxiety disorders", "CountriesWithData"].values[0],
    "Bipolar": disorder_metadata.loc[disorder_metadata["DisorderName"] == "Bipolar disorder", "CountriesWithData"].values[0],
    "Depression": disorder_metadata.loc[disorder_metadata["DisorderName"] == "Major depressive disorder", "CountriesWithData"].values[0],
    "EatingDisorders": disorder_metadata.loc[
        disorder_metadata["DisorderName"].isin(["Bulimia nervosa", "Anorexia nervosa"]),
        "CountriesWithData"
    ].mean(),
    "Schizophrenia": disorder_metadata.loc[disorder_metadata["DisorderName"] == "Personality disorders", "CountriesWithData"].values[0]
}

# === Agregar columna a Dim_Disorder ===
dim_disorder["CountriesWithData"] = dim_disorder["DisorderName"].map(disorder_country_data)

# === Crear carpeta si no existe ===
os.makedirs("data/snow_squema", exist_ok=True)

# === Guardar resultado ===
dim_disorder.to_csv("data/snow_squema/Dim_Disorder.csv", index=False)

print("✅ Dim_Disorder guardada exitosamente con columna 'CountriesWithData'")
