import pandas as pd
from datetime import datetime

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

#adding column different for each row
air['dt'] = air.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
print(air.head())