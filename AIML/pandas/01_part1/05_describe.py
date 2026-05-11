#step1- sample data frame using dictionary
import pandas as pd
data={
    "Name":["Ram","Ayush","Sheetal","Pritam","Naman","Divyansd","Dj"],
    "Age":[21,23,23,40,50,100,27],
    "Salary":[50,100,100,70,69,90,95],
    "Performance rating":[85,100,100,70,75,80,95]
}
df=pd.DataFrame(data)
print("sample Dataframe")
print(df)
print("descriptive statisticks")
print(df.describe())
