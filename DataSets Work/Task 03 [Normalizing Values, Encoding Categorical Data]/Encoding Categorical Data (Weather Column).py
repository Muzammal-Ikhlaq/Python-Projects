import pandas as pd

df = pd.read_csv('seattle-weather.csv', nrows=50)

# Unique weather categories mapping
weather_mapping = {
    'drizzle': 0,
    'rain': 1,
    'sun': 2,
    'snow': 3
}

# Apply mapping to the 'weather' column
df['weather_encoded'] = df['weather'].map(weather_mapping)

# Print encoded weather column
print(df[['weather', 'weather_encoded']])
