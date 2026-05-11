"""""
reshape(rows,columns)specify the new shape
if and only if data mthches
it doesnot create a copy it returns a view

"""""
import numpy as np
arr=np.array([10,20,30,40,50,60])
reshaped_Arr=arr.reshape(2,3)
print(reshaped_Arr)