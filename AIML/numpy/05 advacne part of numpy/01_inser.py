""" 
np.insert(array,index,values,axis=None)
array-origgnal array
index-
axis=0 means row wise
axis=1 means inserting data column wise
if axis is none it is inserted into a flatten value
"""
import numpy as np
arr=np.array([10,20,30,40,50,60])

print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)
  
