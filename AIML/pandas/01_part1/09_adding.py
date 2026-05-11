import pandas as pd   
data={
    "Name":["Ram","Ayush","Sheetal","Pritam","Naman","Divyansd","Dj"],
    "Age":[21,23,23,40,50,100,27],
    "Salary":[50000,100000,100000000,70000,69000,90000,95000],
    "Performance rating":[85,100,100,70,75,80,95]
    }
df=pd.DataFrame(data)
print(df)
#square brackets df["column_name"]=some data
df["bonus"]=df["Salary"]*0.1
print(df)
#using insert method
#df.insert()
#df.insert(loc,"column_name",some_data)
df.insert(3,"employe_id",[10,20,30,40,50,60,80])
print(df)