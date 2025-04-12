import pandas as pd

# === Cargar archivo ===
df_treatment = pd.read_csv(r"data\5- anxiety-disorders-treatment-gap.csv")

# === Renombrar columnas ===
df_treatment.columns = [
    "Entity", "Code", "Year",
    "Adequate", "Other", "Untreated"
]

# === Calcular suma original por fila ===
df_treatment["Total"] = df_treatment["Adequate"] + df_treatment["Other"] + df_treatment["Untreated"]

# === Normalizar para que sumen 100% ===
df_treatment["Adequate"] = df_treatment["Adequate"] / df_treatment["Total"] * 100
df_treatment["Other"] = df_treatment["Other"] / df_treatment["Total"] * 100
df_treatment["Untreated"] = df_treatment["Untreated"] / df_treatment["Total"] * 100

# === Eliminar columna auxiliar ===
df_treatment.drop(columns="Total", inplace=True)

# === Guardar versión limpia ===
output_path = r"data\cleaned_treatment_gap_normalized.csv"
df_treatment.to_csv(output_path, index=False)

print("✅ Archivo limpio y normalizado guardado en:", output_path)
