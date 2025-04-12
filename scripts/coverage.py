import pandas as pd

# === Cargar dataset ===
file_path = r"data\4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv"
df = pd.read_csv(file_path)

# === Renombrar columnas ===
df.columns = [
    "Entity", "Code", "Year",
    "MajorDepression", "Bipolar", "EatingDisorders",
    "Dysthymia", "Schizophrenia", "Anxiety"
]

# === Validación básica ===
print(df.isnull().sum())
print(df.dtypes)

# === Despivotar enfermedades ===
df_long = df.melt(
    id_vars=["Entity", "Code", "Year"],
    value_vars=[
        "MajorDepression", "Bipolar", "EatingDisorders",
        "Dysthymia", "Schizophrenia", "Anxiety"
    ],
    var_name="Disorder",
    value_name="Coverage"
)

# === Guardar archivo limpio ===
output_path = r"data\cleaned_adult_population_coverage_long.csv"
df_long.to_csv(output_path, index=False)
print("📊 Archivo despivotado guardado en:", output_path)
