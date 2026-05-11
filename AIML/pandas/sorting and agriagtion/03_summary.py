# df["column"].mean()
# df["column_name"].sum()
# df["column name"].min()
# df["column name"].max()
import pandas as pd   
data={
    "Name":["shyam","ram","ghamshyam"],
    "age":[10,20,30],
    "city":["mumbai","Nagur","Bihar"],
    "salary":[10000,80000,50000],
    "rating":[100,80,20]
    
}
df=pd.DataFrame(data)
max_age=df["age"].max()
avg_salary=df["salary"].mean()
sumof_rating=df["rating"].sum()
print(max_age)
print(avg_salary)
print(sumof_rating)
print(df)