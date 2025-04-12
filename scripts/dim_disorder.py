import pandas as pd
import os

# === Crear carpeta si no existe ===
os.makedirs("data/snow_squema", exist_ok=True)

# === Cargar archivo base de prevalencia ===
print("Cargando archivo de prevalencia...")
df = pd.read_csv(r"data\cleaned_mental_illnesses_prevalence_long.csv")
print("Archivo cargado correctamente.")

# === Extraer trastornos únicos ===
disorders = df["Disorder"].drop_duplicates().sort_values().reset_index(drop=True)

# === Crear tabla Dim_Disorder con ID numérico ===
dim_disorder = pd.DataFrame({
    "DisorderID": range(1, len(disorders)+1),
    "DisorderName": disorders
})

# === Agregar grupo de trastorno manualmente ===
grupo_dict = {
    "Depression": "Mood Disorder",
    "Bipolar": "Mood Disorder",
    "Anxiety": "Anxiety Disorder",
    "Schizophrenia": "Psychotic Disorder",
    "EatingDisorders": "Behavioral Disorder"
}
dim_disorder["DisorderGroup"] = dim_disorder["DisorderName"].map(grupo_dict).fillna("Other")

# === Guardar archivo ===
output_path = r"data/snow_squema/Dim_Disorder.csv"
dim_disorder.to_csv(output_path, index=False)
print(f"✅ Dim_Disorder guardada en: {output_path}")
