import pandas as pd
import os

# === Crear carpeta si no existe ===
os.makedirs("data/snow_squema", exist_ok=True)

# === Cargar archivos base ===
burden_df = pd.read_csv("data/2- burden-disease-from-each-mental-illness(1).csv")
dim_disorder = pd.read_csv("data/snow_squema/Dim_Disorder.csv")
fact_prevalence = pd.read_csv("data/snow_squema/Fact_Prevalence.csv")

# === Renombrar columnas de burden para facilitar melt ===
burden_df.columns = [
    "CountryName", "CountryCode", "Year",
    "Depression", "Schizophrenia", "Bipolar", "EatingDisorders", "Anxiety"
]

# === Despivotar ===
burden_long = burden_df.melt(
    id_vars=["CountryCode", "CountryName", "Year"],
    value_vars=["Depression", "Schizophrenia", "Bipolar", "EatingDisorders", "Anxiety"],
    var_name="DisorderName",
    value_name="Burden"
)

# === Agregar DisorderID desde Dim_Disorder ===
burden_long = burden_long.merge(dim_disorder[["DisorderID", "DisorderName"]], on="DisorderName", how="left")

# === Unir con Fact_Prevalence usando CountryCode, Year, DisorderID ===
fact_extended = fact_prevalence.merge(
    burden_long[["CountryCode", "Year", "DisorderID", "Burden"]],
    on=["CountryCode", "Year", "DisorderID"],
    how="left"
)

# === Verificar nulos en Burden ===
missing_burden = fact_extended["Burden"].isnull().sum()
print(f"❗Valores nulos en columna 'Burden': {missing_burden}")

# === Guardar resultado ===
fact_extended.to_csv("data/snow_squema/Fact_Prevalence.csv", index=False)
print("✅ Fact_Prevalence actualizado con columna 'Burden' y guardado.")
