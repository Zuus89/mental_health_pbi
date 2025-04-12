import pandas as pd

# === Cargar el archivo ===
df_major = pd.read_csv(r"data\3- adult-population-covered-in-primary-data-on-the-prevalence-of-major-depression.csv")

# === Renombrar columnas ===
df_major.columns = ["Entity", "Code", "Year", "MajorDepressionCoverage"]

# === Validación de datos ===
print("📏 Shape:", df_major.shape)
print("🧪 Nulos por columna:\n", df_major.isnull().sum())
print("🔠 Tipos de datos:\n", df_major.dtypes)
print("📅 Años únicos:", df_major["Year"].unique())

# === Guardar versión limpia ===
output_path = r"data\cleaned_major_depression_coverage.csv"
df_major.to_csv(output_path, index=False)

print("✅ Archivo limpio guardado en:", output_path)
