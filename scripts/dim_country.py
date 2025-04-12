import pandas as pd
import os
import country_converter as coco

# === Cargar tabla base ya despivotada ===
df_long = pd.read_csv(r"data\cleaned_mental_illnesses_prevalence_long.csv")

# === Crear carpeta snow_squema dentro de /data si no existe ===
os.makedirs("data/snow_squema", exist_ok=True)

# === Extraer países únicos ===
dim_country = df_long[["Code", "Entity"]].drop_duplicates().rename(columns={
    "Code": "CountryCode",
    "Entity": "CountryName"
}).reset_index(drop=True)

# === Enriquecer con continente y región ===
cc = coco.CountryConverter()
dim_country["Continent"] = cc.convert(names=dim_country["CountryName"], to="continent")
dim_country["UNRegion"] = cc.convert(names=dim_country["CountryName"], to="UNregion")


# === Idiomas manuales básicos (puedes expandir este diccionario luego) ===
idioma_dict = {
    "Afghanistan": "Dari, Pashto",
    "Albania": "Albanian",
    "Algeria": "Arabic, Berber",
    "Andorra": "Catalan",
    "Angola": "Portuguese",
    "Argentina": "Spanish",
    "Armenia": "Armenian",
    "Australia": "English",
    "Austria": "German",
    "Azerbaijan": "Azerbaijani",
    "Bahamas": "English",
    "Bahrain": "Arabic",
    "Bangladesh": "Bengali",
    "Barbados": "English",
    "Belarus": "Belarusian, Russian",
    "Belgium": "Dutch, French, German",
    "Belize": "English",
    "Benin": "French",
    "Bhutan": "Dzongkha",
    "Bolivia": "Spanish, Quechua, Aymara, Guarani",
    "Bosnia and Herzegovina": "Bosnian, Croatian, Serbian",
    "Botswana": "English, Tswana",
    "Brazil": "Portuguese",
    "Brunei": "Malay",
    "Bulgaria": "Bulgarian",
    "Burkina Faso": "French",
    "Burundi": "Kirundi, French, English",
    "Cambodia": "Khmer",
    "Cameroon": "English, French",
    "Canada": "English, French",
    "Cape Verde": "Portuguese",
    "Central African Republic": "French, Sango",
    "Chad": "French, Arabic",
    "Chile": "Spanish",
    "China": "Mandarin",
    "Colombia": "Spanish",
    "Comoros": "Comorian, Arabic, French",
    "Congo (Brazzaville)": "French",
    "Congo (Kinshasa)": "French",
    "Costa Rica": "Spanish",
    "Croatia": "Croatian",
    "Cuba": "Spanish",
    "Cyprus": "Greek, Turkish",
    "Czech Republic": "Czech",
    "Denmark": "Danish",
    "Djibouti": "French, Arabic",
    "Dominica": "English",
    "Dominican Republic": "Spanish",
    "East Timor": "Portuguese, Tetum",
    "Ecuador": "Spanish",
    "Egypt": "Arabic",
    "El Salvador": "Spanish",
    "Equatorial Guinea": "Spanish, French, Portuguese",
    "Eritrea": "Tigrinya, Arabic, English",
    "Estonia": "Estonian",
    "Eswatini": "Swazi, English",
    "Ethiopia": "Amharic",
    "Fiji": "English, Fijian, Hindi",
    "Finland": "Finnish, Swedish",
    "France": "French",
    "Gabon": "French",
    "Gambia": "English",
    "Georgia": "Georgian",
    "Germany": "German",
    "Ghana": "English",
    "Greece": "Greek",
    "Grenada": "English",
    "Guatemala": "Spanish",
    "Guinea": "French",
    "Guinea-Bissau": "Portuguese",
    "Guyana": "English",
    "Haiti": "French, Haitian Creole",
    "Honduras": "Spanish",
    "Hungary": "Hungarian",
    "Iceland": "Icelandic",
    "India": "Hindi, English",
    "Indonesia": "Indonesian",
    "Iran": "Persian",
    "Iraq": "Arabic, Kurdish",
    "Ireland": "Irish, English",
    "Israel": "Hebrew, Arabic",
    "Italy": "Italian",
    "Jamaica": "English",
    "Japan": "Japanese",
    "Jordan": "Arabic",
    "Kazakhstan": "Kazakh, Russian",
    "Kenya": "English, Swahili",
    "Kiribati": "English",
    "Korea, North": "Korean",
    "Korea, South": "Korean",
    "Kosovo": "Albanian, Serbian",
    "Kuwait": "Arabic",
    "Kyrgyzstan": "Kyrgyz, Russian",
    "Laos": "Lao",
    "Latvia": "Latvian",
    "Lebanon": "Arabic",
    "Lesotho": "English, Sesotho",
    "Liberia": "English",
    "Libya": "Arabic",
    "Liechtenstein": "German",
    "Lithuania": "Lithuanian",
    "Luxembourg": "Luxembourgish, French, German",
    "Madagascar": "Malagasy, French",
    "Malawi": "English, Chichewa",
    "Malaysia": "Malay",
    "Maldives": "Dhivehi",
    "Mali": "French",
    "Malta": "Maltese, English",
    "Marshall Islands": "Marshallese, English",
    "Mauritania": "Arabic",
    "Mauritius": "English",
    "Mexico": "Spanish",
    "Micronesia": "English",
    "Moldova": "Romanian",
    "Monaco": "French",
    "Mongolia": "Mongolian",
    "Montenegro": "Montenegrin",
    "Morocco": "Arabic, Berber",
    "Mozambique": "Portuguese",
    "Myanmar": "Burmese",
    "Namibia": "English",
    "Nauru": "Nauruan, English",
    "Nepal": "Nepali",
    "Netherlands": "Dutch",
    "New Zealand": "English, Maori, NZ Sign Language",
    "Nicaragua": "Spanish",
    "Niger": "French",
    "Nigeria": "English",
    "North Macedonia": "Macedonian",
    "Norway": "Norwegian",
    "Oman": "Arabic",
    "Pakistan": "Urdu"
    # Puedes seguir expandiendo esto según sea necesario
}
dim_country["Language"] = dim_country["CountryName"].map(idioma_dict).fillna("Unknown")

# === Guardar archivo final ===
output_path = "data/snow_squema/Dim_Country.csv"
dim_country.to_csv(output_path, index=False)
print(f"✅ Dim_Country guardada en: {output_path}")
