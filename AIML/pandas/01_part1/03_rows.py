#head() and tail()
#head(n) it will show the fist n rows  if n value is not passes
#tail(n) it will show the first n rows if n value is not given 
#here n is the variable
import pandas as pd    

df=pd.read_json("json.json")
print("Display 10 rows of first")
print(df.head(10))
print("Display 10 rows of last")
print(df.tail(10))