"""" 
1-how big is your data set
2-what the names of columns
3-shape and columns
shape -it is a attribute it is returened in tuple in form of no rows and no of columns
"""
import pandas as pd   
data={
    "Name":["Ram","Ayush","Sheetal","Pritam","Naman","Divyansd","Dj"],
    "Age":[21,23,23,40,50,100,27],
    "Salary":[50,100,100,70,69,90,95],
    "Performance rating":[85,100,100,70,75,80,95]
}
df=pd.DataFrame(data)
print(df)
print(f"shape: ",df.shape)
print(f"column names: ",df.columns)
print("it shows the rows ",df.index)
