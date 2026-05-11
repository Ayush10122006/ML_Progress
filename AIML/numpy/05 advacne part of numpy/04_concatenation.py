"""" 
np.concatinate(array_1,array_2),axis=0
if axis =0 it will stack row wise is is known as vertical stacking
if axis =1 if will insert the value column wise horizontal stacking
"""
import numpy as np
arr_1=np.array([1,2])
arr_2=np.array([3,4])
new_arr=np.concatenate((arr_1,arr_2))
print(new_arr)