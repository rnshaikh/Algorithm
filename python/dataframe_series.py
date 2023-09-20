import pandas as pd

obj = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(obj)
print("Dataframe", df)



df = pd.DataFrame(obj, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print("Dataframe with index", df)
print("data frame information", df.info())
print("first 3 rows", df[:3])
print("Name and Score", df[["name", "score"]])
print("No of row and cols", len(df.axes[0]), len(df.axes[1]))
print("Score between 15 and 20", df[df["score"].between(15,20)])
print("No of attemts > 2 and score < 15", df[(df["attempts"] > 2) & (df["score"]<15)])
print("Sum of attempts", df["attempts"].sum())
print("Sorting by name", df.sort_values(by=["name", "score"], ascending=[False, True]))

df["qualify"] = df["qualify"].map({"yes": True, "no":False})
print("Replace quality with True, False", df)

print("change name jame - suresh", df["name"].replace("James", "Suresh"))

color =["Blue", "Red", "Green", "Voilet", "Yellow", "Red", "Blue", "Green","RED", "Pink"]
df["color"] = color
print("append color col", df)

print("iter rows")
for index, row in df.iterrows():
    print("row,", row)

print("rename col", df.rename(columns={"name": "name1"}))