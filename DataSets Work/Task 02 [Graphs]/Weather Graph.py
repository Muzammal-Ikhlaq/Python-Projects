import pandas as pd
import matplotlib.pyplot as plt

# Read Data
df = pd.read_csv('seattle-weather.csv')

# Select multiple columns
data = df[['temp_max', 'temp_min', 'wind']]

# Line Graph
plt.figure(figsize=(8, 5))
#for column in data.columns:
 #   plt.plot(data[column], label=column)
plt.plot(df['temp_max'], 'b*-',label='temp_max')
plt.plot(df['temp_min'], 'g*-',label='temp_max')
plt.title('Line Graph')
plt.legend(loc=2)
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

# Box Plot
data.plot(kind='box')
plt.title('Box Plot')
plt.ylabel('Value')
plt.show()

# Pie Chart
plt.figure(figsize=(8, 5))
data.mean().plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'green', 'red'])
plt.title('Pie Chart')
plt.show()
