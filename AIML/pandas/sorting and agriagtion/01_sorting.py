#sorting data
#saort data 1 column soert_values
import pandas as pd
#df.sort_values(by="column Name",True/False,inplace=true)
data= {
    "Name":["ayush","arun","aura"],
    "Age":[20,30,4],
    "salary":[10000,20000,30000]

}
df=pd.DataFrame(data)
df.sort_values(by='Age',ascending=False,inplace=True)
print('sorted document')
print(df)