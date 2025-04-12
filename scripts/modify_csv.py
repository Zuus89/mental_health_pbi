import pandas as pd

# Asegúrate de tener tu DataFrame `fact_prevalence` cargado
fact_prevalence = pd.read_csv("data/snow_squema/Fact_Prevalence.csv")

# Guardar CSV con coma como separador decimal y punto y coma como separador de columnas
fact_prevalence.to_csv(
    "data/snow_squema/Fact_Prevalence_comma_decimal.csv",
    index=False,
    sep=";",
    decimal=","
)

print("✅ Archivo guardado con separador decimal ',' y columnas con ';'")
