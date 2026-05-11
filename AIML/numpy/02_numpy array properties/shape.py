#it will tell the shape of array
import numpy as np
array=np.array([[1,2,3],
              [4,5,6]])
print(array.shape)
#it will tell the size of the array
import numpy as np
arr_2d=np.array([[1,2,3],
                [4,5,6]])
print(arr_2d.size)
#it will tell the no of dimensions in the array ndim
import numpy as np
arr_1d=np.array([1,2,3])
arr_two_d=np.array([[1,2,3],[4,5,6]])
arr_3d=np.array([[1,2],[3,4],[5,6]])
print(arr_1d.ndim)
print(arr_two_d.ndim)
print(arr_3d.ndim)
# to check the data type in the array
import numpy as np
arr = np.array([10,20,30,30.5,40])
print(arr.dtype)
