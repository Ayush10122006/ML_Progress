import pandas as pd   
data={
    "Name":["Ram","Ayush","Sheetal","Pritam","Naman","Divyansd","Dj"],
    "Age":[21,23,23,40,50,100,27],
    "Salary":[50000,100000,100000000,70000,69000,90000,95000],
    "Performance rating":[85,100,100,70,75,80,95]
}
df=pd.DataFrame(data)
high_salary=df[df['Salary']>50000]
print("employs have high salray than 50 k")
print(high_salary)
#filter roews salary >50k and age>30
filtered=df[(df['Age']>30) & (df['Salary']>50000)]
print("employe list age >30 + salary >50000",filtered)
#using or confition

conditions = df[(df['Performance rating'] > 90) | (df['Performance rating'] > 770)]
