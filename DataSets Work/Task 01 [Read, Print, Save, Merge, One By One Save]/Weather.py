import pandas as pd

#For reading Data
df= pd.read_csv('seattle-weather.csv',nrows=50)

#For Print All Lines
print(df)

# Optional: Printing first and last 5 rows of the dataset
#print(df.head())
#print(df.tail())

#For Filling Missing/Empty Value/Cells Like Numbers or Characters
#df.fillna(1)

#For Ignore Missing/Empty Value/Cells
#df.dropna()

#For Selecting Selective Columns then print and store Data in 1st New File
m = df[['date','precipitation','temp_max','temp_min','wind']]
print(m)

#Creating 1st New File
m.to_csv("newdata1.csv")

#For Selecting one Column Data then print and store Data in 2nd New File
m1 = df[['weather']]
print(m1)

#Creating 2nd New File
m1.to_csv("data2.csv")

#Reading New Files
a = pd.read_csv("data1.csv")
a1 = pd.read_csv("data2.csv")

#For Concatinating New Files Data
a2 = pd.concat([a,a1],axis=1)

#Concatinating Files Data Store in One New File
a2.to_csv("final.csv")

#Add a New Column (Combine All Row Values)
a2["combined"] = a2.astype(str).agg(' '.join, axis=1)

a2.to_csv("Combined-Data.csv")

print(a2)


# Read the first row to get headers
first_row = pd.read_csv("final.csv", nrows=1)
first_row.to_csv("final_appended.csv", mode='w',header=True)  # Write headers

# Write a Python program that reads a CSV file named finalfile.csv and stores all its rows into a new CSV file named all_rows.csv. The first line of the new file should contain the column names, and each row should be written in a comma-separated format.
df = pd.read_csv("seattle-weather.csv")
with open("all_rows.csv", "w") as file:
    file.write(",".join(df.columns) + "\n")

    for i in range(len(df)):
        row = df.iloc[i]
        file.write(",".join(map(str, row.values)) + "\n")
df2 = pd.read_csv("all_rows.csv")
print(df2)