import pandas as pd   
data={
    "Name":["Ram","Ayush","Sheetal","Pritam","Naman","Divyansd","Dj"],
    "Age":[21,23,23,40,50,100,27],
    "Salary":[50000,100000,100000000,70000,69000,90000,95000],
    "Performance rating":[85,100,100,70,75,80,95]
}
df=pd.DataFrame(data)
#.loc[]
# df.loc[row_index,"column_name"]=new name
df.loc[0,"Salary"]=55555
print(df)