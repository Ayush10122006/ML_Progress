
import pandas as pd   
data={
    "Name":["Ram","Ayush","Sheetal","Pritam","Naman","Divyansd","Dj"],
    "Age":[21,23,23,40,50,100,27],
    "Salary":[50000,10000,10000,70000,69000,90000,90000],
    "Performance rating":[85,100,100,70,75,80,95]
}
df=pd.DataFrame(data)
print("sample data frame",df)
print("Names(single column return series)")
print(df["Name"])
#selecting multiple columns
subset=df[["Name","Salary"]]
print('\nsubset with the name and salary')
print(subset)
