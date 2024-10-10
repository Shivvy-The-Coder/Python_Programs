import pandas as pd
import numpy as np

path=r"E:\PYthon Programming Apna College\Pandas\CSV\NY_weather.csv"

df = pd.read_csv(path)

print(df)

# how to extrat a single coloumn of  data from the dataframe
c1=df.EST
print(c1)

c2=df.Temperature
print(c2)

print(df.head(10))