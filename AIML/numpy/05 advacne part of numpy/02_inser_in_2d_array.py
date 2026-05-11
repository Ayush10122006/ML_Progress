import numpy as np
arr_2d=np.array([[1,2],[3,4]])
#insert a new array
new_arr_2d=np.insert(arr_2d,1,[5,6],axis=0)
new_arr_2d1=np.insert(arr_2d,1,[8,9],axis=1)
print(new_arr_2d)
print(new_arr_2d1)