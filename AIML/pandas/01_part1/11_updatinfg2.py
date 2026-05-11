import pandas as pd   
data={
    "Name":["Ram","Ayush","Sheetal","Pritam","Naman","Divyansh","Dj"],
    "Age":[21,23,23,40,50,100,27],
    "Salary":[50000,100000,100000000,70000,69000,90000,95000],
    "Performance rating":[85,100,100,70,75,80,95]
}
df=pd.DataFrame(data)
df["Salary"]=df["Salary"]*2
print(df)