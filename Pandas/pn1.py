import pandas as pd
import numpy as np

# storing a directory of csv file in variable path  make sure to use 'r' before the path 
path=r"E:\PYthon Programming Apna College\Pandas\CSV\NY_weather.csv"
# now using that directory to read the csv file 
df = pd.read_csv(path)
# printing the csv file which now can be accesed with the help if variable df
print(df)


"""# HOW TO ACCES A CSV FILE FROM A CSV FILE"""
# method 1
c1=df.EST 
# print(c1)
print("EST column has been printed and now we will print Temperature")
c2=df.Temperature
print(c2)

# method 2
c1=df['EST']
print(c1)
c2=df["Temperature"]
print(c2)
print(df[['EST',"Temperature"]])

c1_c2 = df[['EST', 'Temperature']]

print("EST and Temperature columns together:")
print(c1_c2)


#  combining two coloumns and resulting into a 3rd column 
EST_TEmp = df['EST'].astype(str) + df ['Temperature'].astype(str)
print(EST_TEmp)

# how to rename a coloumns in pandas using  rename() function

df.rename(columns={'EST':"DATE" , "Temperature":"temp"},inplace=True)
print(df)


# applying a function on a coloumn  in pandas
# method1
df['temp + 3 degrees']=df['temp'].apply(lambda x:x+3)
# print(df["temp + 3 degrees"])
print(df)
# method2
df['temp+20']=df['temp']**2
print(df)