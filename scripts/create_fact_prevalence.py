import pandas as pd
import os

# === Crear carpeta si no existe ===
os.makedirs("data/snow_squema", exist_ok=True)

# === Cargar datos base ===
df = pd.read_csv("data/cleaned_mental_illnesses_prevalence_long.csv")
dim_disorder = pd.read_csv("data/snow_squema/Dim_Disorder.csv")

# === Renombrar para merge y consistencia ===
df = df.rename(columns={"Code": "CountryCode", "Disorder": "DisorderName"})

# === Agregar ID del trastorno desde Dim_Disorder ===
df = df.merge(dim_disorder[["DisorderID", "DisorderName"]], on="DisorderName", how="left")

# === Seleccionar columnas finales ===
fact_prevalence = df[["CountryCode", "Year", "DisorderID", "Prevalence"]]

# === Guardar CSV limpio ===
fact_prevalence.to_csv("data/snow_squema/Fact_Prevalence.csv", index=False)
print("✅ Fact_Prevalence creada sin normalización y guardada en 'data/snow_squema'")
