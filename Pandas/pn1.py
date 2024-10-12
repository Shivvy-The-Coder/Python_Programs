import pandas as pd
import numpy as np

# storing a directory of csv file in variable path  make sure to use 'r' before the path 
path=r"E:\PYthon Programming Apna College\Pandas\CSV\NY_weather.csv"
# now using that directory to read the csv file 
df = pd.read_csv(path)
df2=pd.read_csv(path)
print(df2)
# printing the csv file which now can be accesed with the help if variable df
print(df)

df['temp']=df2['Temperature']
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

#finding sum , max , min, median , mean , count etc
maxTemp = df['temp'].max()
minTemp = df['temp'].min()
meanTemp = df['temp'].mean()
medianTemp=df['temp'].median()
sumTemp=df['temp'].sum()

print("Performing aggregate function on these are ")
print("maxtemp",maxTemp)
print("mintemp",minTemp)
print("meantemp",meanTemp)
print("mediantemp",medianTemp)
print("sumtemp",sumTemp)

# i am adding this comment just fir the purpose of  testing the commit functionality of github

# filterng rows based on coloumn values

Temp_Greater_30 = df[df['temp']>30]
print(df)


# sorting the data based on  a coloumn value

df_sorted = df.sort_values(by='temp' , ascending=False)
print(df_sorted)

total = df['temp'].count()
print(total)

df_sorted_asc=df.sort_values(by='temp',ascending=True)
print(df_sorted_asc)

# df=df.drop('temp', axis=0)
# print(df)

# i dropped coloumn temp , but i regained it by creating another data fram from th main csv file
#  and then adding the temperatur col as name temp in df  from df2
#  like this 
# df['temp']=df2['Temperature']


# how to check for null values i python df

check_null_values_in_temp = df['temp'].isnull()
print(check_null_values_in_temp)

print("learning python was great")
