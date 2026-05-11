import pandas as pd
data={
    "time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}
df=pd.DataFrame(data)
print('befoe interpolation')
print(df)
df['value']=df['value'].interpolate(meathod="linear")
print("after interpolation")
print(df)
"""   
interpolation uised for
1-wime series data
2-numeri data with trends
3-avoid droping values


"""