import pandas as pd

# Convert numerical values into a normalized range between 0 and 1.
df = pd.read_csv('seattle-weather.csv', nrows=50)

a = df[['wind','temp_min','temp_max','precipitation']]

c=(a-a.min()) / (a.max() - a.min())
print(c)


