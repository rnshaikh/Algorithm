"""
    pandas is library used for dealing with datasets.

    it is used for cleaning, exploring, analyzing and manipulating data.

    pandas reference to "panel data" or "python data analysis"
     
"""

#from statistics import mean, median
import pandas as pd


print("version", pd.__version__)



"""

The dataframes can be combines using the below approaches:

append() method: This is used to stack the dataframes horizontally. Syntax:
df1.append(df2)
concat() method: This is used to stack dataframes vertically. This is best used when the dataframes have the same columns and similar fields. Syntax:
pd.concat([df1, df2]) 
join() method: This is used for extracting data from various dataframes having one or more common columns.
df1.join(df2)
52. Can you 


"""

"""
"""
import pandas as pd
df1 = pd.Series([2, 4, 8, 10, 12])
df2 = pd.Series([8, 12, 10, 15, 16])



df1=df1[~df1.isin(df2)]
print(df1)




"""
    series : it is like column in table. hold 1 dimensional array of any type.

"""
print("\n\n\n")

print("Series....")
ser = pd.Series([1,2,3,4])
print("series variable", ser)

print("series iterating..")
for i in ser:
    print("el", i)

print("series with labels..... index")
ser = pd.Series([1,2,3,4], index=["x", "y", "z", "q"])
print("acces ele with label", ser["q"])


"""
data frame is 2 dimensional structure array or row and column like table.
"""
print("\n\n\n")
print("DataFrame")
daf = pd.DataFrame([["name", "age"], ["riz", "20"]])
print("example dataframe", daf)

"""
loc is used to returen specified row,s
"""
obj = [{
    "name": "rizw",
    "age": "25"
}, {"name": "abc", "age": "31"}]
df = pd.DataFrame(obj)
print("return 0 and 1st row using loc", df.loc[[0,1]], type(df))


"""
 give name to each rows
"""
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print("loc using row name", df.loc["day1"]) 


"""
 load csv file in dataframe'
 if data is more than max_row then df return first 5 and last 5 row

"""

df = pd.read_csv('username.csv')
print("csv dataframe", df)
print("csv dataframe to string to print entire dataframe", df.to_string())
pd.options.display.max_rows = 9999
print("max rows", pd.options.display.max_rows)

"""
  read json 
"""
df = pd.read_json('sample.json')
print("print entire dataframe with to_string", df.to_string())



"""
head() : return first 5 rows default or specified rows
tail(): retrun last 5 rows default or specified rows.
"""

df = pd.read_csv('username.csv')
print("df head: \n", df.head(2))
print("df tail: \n", df.tail(2))
print("info about dataframe : \n", df.info())


"""
empty cell: dropna - drop complete row with empty cell, return new df
fillna - fill value to empty celll return new df

"""

df = pd.read_csv('username.csv')
print("data frame with empty \n", df.to_string())
#df.dropna(inplace=True)
#df.dropna(subset=['Date'], inplace = True)

print("data frame without empty own \n", df.dropna())
print("data frame with fill empty value \n", df.fillna(0, inplace=True))
print("data frame with fill mean for empty value \n", df.fillna(df["Calories"].mean(), inplace=True))
print("data frame with fill meadian for empty value \n", df.fillna(df["Calories"].median(), inplace=True))
print("data frame with fill mode for empty value \n", df.fillna(df["Calories"].mode()[0], inplace=True))


"""
    fixed incorrect date format.
"""
#df['Date'] = pd.to_datetime(df['Date'])
#print(df.to_string())

"""
    fixed wrong data 

"""
df.loc[7, 'Duration'] = 45
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
print("Df after updating wrong data", df)



"""
    removing duplicated 
    df.duplicated()
    df.drop_duplicates()
"""
print("check duplicate \n", df.duplicated())

df.drop_duplicates(inplace=True)
print("drop duplicates \n", df)



"""
correlation : it is relationship between each column

"""

print("correlation \n", df.corr())


"""
    plotting: it used to draw different graph using given data set.

"""
import matplotlib.pyplot as plt

df.plot()
plt.show()

"""
plotting scatter plot
"""

df.plot(kind="scatter", x="Duration", y="Calories")
plt.show()


"""
plot histogram
"""
df["Calories"].plot(kind="hist")
plt.show()








