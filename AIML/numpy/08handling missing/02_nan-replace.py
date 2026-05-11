import numpy as np
arr=np.array([1,2,3,np.nan,4,np.nan,6])
clean_arr=np.nan_to_num(arr,nan=100)
print(clean_arr)