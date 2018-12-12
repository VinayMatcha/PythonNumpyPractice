import pandas as pd

air = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
print(air.columns)

air.columns = ["month", "Airline"]
print(air.columns)

print(air["month"])
#works only for strings
print(air.month)
#adding new column. For bias
air['one'] = 1
print(air.head())