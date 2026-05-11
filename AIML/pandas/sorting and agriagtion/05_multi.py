import pandas as pd   
data={
    "Name":["shyam","ram","ghamshyam","shyam","gyan"],
    "age":[10,20,30,50,10],
    "city":["Mumbai","Nagur","Bihar","Delhi","Punjab"],
    "salary":[100000,80000,50000,60000,100000],
    "rating":[100,80,20,70,40]
    
}
df=pd.DataFrame(data)
grouped=df.groupby(["age","Name"])["salary"].sum()
print(grouped)
#sum()
#mean()-find average
#min()
#max()
#std()