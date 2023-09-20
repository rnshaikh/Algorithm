import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 4, 6, 8, 10])

print("item not present in series", s1[~s1.isin(s2)])


sd1 = pd.Series([1,2,3,4,5])
sd2 = pd.Series([2,4,6,8,10])

un = pd.Series(np.union1d(sd1, sd2))
in1 = pd.Series(np.intersect1d(sd1,sd2))
print("not common in both", un[~un.isin(in1)])


d1 = pd.Series([1,2,3,4,56,7])
print("min, max, median, 25th 75percential",d1.min(), d1.max(), d1.median(), d1.mean(), np.percentile(d1, q=[25, 75]))

d1 = d1.append(pd.Series([1,2,2,2,3,4, 80]))
print("count frequency", d1.value_counts())



d1[~d1.isin(d1.value_counts().index[:1])] = 'Other'
print("dispaly max vaule other as other", d1)


d1 = pd.Series([1,3,5,25,30,4,7])
print("find index where value is multiple of 5 ", np.where(d1 % 5 == 0)) 


print("Extract position of given ele", pd.Index(d1).get_loc(5))



wo = pd.Series(["python", "loc", "pHP", "js"])
print("capitalized", wo.map(lambda x : x[0].upper() + x[1:-1] + x[-1].upper()))

print("Calculate no of ch", wo.map(lambda x: len(x)))



print("Calculate diff of diff", d1.diff().diff().to_list())



date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("Original Series:")
print(date_series)
date_series = date_series.map(lambda x: parse(x))
print("Day of month:")
print(date_series.dt.day.tolist())
print("Day of year:")
print(date_series.dt.dayofyear.tolist())
print("Week number:")
print(date_series.dt.weekofyear.tolist())
print("Day of week:")
print(date_series.dt.weekday_name.tolist())




nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("\nPositions of the values surrounded by smaller values on both sides:")
temp = np.diff(np.sign(np.diff(nums)))
print("Temp", np.diff(nums), np.sign(np.diff(nums)),  np.diff(np.sign(np.diff(nums))), np.where(temp == -2)[0]+1)

result = np.where(temp == -2)[0] + 1
print(result)
