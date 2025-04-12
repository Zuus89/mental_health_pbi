# clean_data.py

import pandas as pd

# === Cargar el archivo ===
df = pd.read_csv(r"data\1- mental-illnesses-prevalence.csv")

# === Renombrar columnas ===
df.columns = [
    "Entity", "Code", "Year",
    "Schizophrenia", "Depression", "Anxiety", "Bipolar", "EatingDisorders"
]

# === Filtrar solo países reales (con código ISO) ===
df = df[df["Code"].notna()]

# === Despivotar ===
df_long = df.melt(
    id_vars=["Entity", "Code", "Year"],
    value_vars=["Schizophrenia", "Depression", "Anxiety", "Bipolar", "EatingDisorders"],
    var_name="Disorder",
    value_name="Prevalence"
)

# === Guardar dataset limpio ===
output_path = r"data\cleaned_mental_illnesses_prevalence_long.csv"
df_long.to_csv(output_path, index=False)

print("✅ Archivo limpio, despivotado y solo con países guardado en:", output_path)

