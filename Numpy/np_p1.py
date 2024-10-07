
# converting an lilst to array using numpy
import numpy

mylist = [10,20,30,40,50]
print(mylist , type(mylist))

arr= numpy.array(mylist)
print(arr,  type(arr))

 

#  using array objects to acheive some fucntionalities

import numpy as np
mylist = [10,20,30,40,50]

arr = numpy.array(mylist)
print("Array is ", arr)
# this will print the Array 
print("Size of array ",arr.size)
#  this will print the length of the array
print("DataType  of Array ", arr.dtype)
#  this willl print the data rype that is being used fir array
print("Dimension of Array ", arr.ndim)
# this will print the number of dimensions of the array that is wether it is 1d, 2d 3d etc
print("Shape  of Array ", arr.shape)
# this will print the shape ie m X n value of the matrix how many rows , how many coloumns


# creating a 1 dimensional array using list and numpy
import numpy as np
mylist = [10,20,30,40,50]

arr = np.array(mylist)
print("printing elements ")
for i in arr:
    print(i)



# creating a 2 dimensional array using list and numpy
import numpy as np
mylist = [[10,20,30,40,50],[60,70,80,90,100],[60,70,80,90,100]]

arr = np.array(mylist)
print(arr)
#  we are displaying row by row 
print("printing elements ")
for i in arr :
        print(i)


#how to display element by element
for row in arr:
      for ele in row:
            print(ele, end=" ")
      print()

import numpy
mylist = [[10,20,30],[60,70,80],[60,70,80]]
matrix = numpy.array(mylist)

# this will display the first two rows and fiirst two coloumns
sqbox1 = matrix[0:2 , 0:2]
print(sqbox1)


# this will display the first 3 rows and first two coloumns
sqbox1 = matrix[0:3 , 0:2]
print(sqbox1)
