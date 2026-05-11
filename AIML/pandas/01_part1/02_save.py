import pandas as pd   
data={
    "Name":["shyam","ram","ghamshyam"],
    "age":[10,20,30],
    "city":["mumbai","Nagur","Bihar"]
}
df=pd.DataFrame(data)
print(df)
#we created a file into a csv format
df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)