
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



# creating an array without using any other data structure like we previously done

import numpy as np
n=int(input("Enter the size of the array"))
arr=np.ndarray(shape=(n) , dtype=int)

print("Enter the array elements")
for i in range (n):
      arr[i]=int(input())

print("Array elements ", arr)

print(arr.size)

# constructing 2d array 

import numpy as np

r=int(input("Enter number of rows"))
c=int(input("Enter number of cols"))

arr =np.ndarray(shape=(r,c) , dtype=int)

for i in  range(r):
      for j in range(c):
            arr[i][j]=int(input())
            
print(arr)

print(arr.ndim)
print(arr.size)
print(arr.shape)
print(arr.dtype) 


# import numpy as np

#how to take input in n dimensional array in python

import numpy as np
arr=np.ndarray(shape=(3,3,3), dtype = int)

x=arr.shape[0]
y=arr.shape[1]
z=arr.shape[1]
print(x,y,z)

val=1
for i in range(x):
      for j in range (y):
            for k in range (z):
                  arr[i][j][k]=val
                  val+=1

print(arr)



# how to reshape an array 
import numpy as np
mylist=[10,20,30,40,50,60,70,80]
arr = np.array(mylist)
print(arr)
print(arr.size)
print(arr.ndim)

res=arr.reshape(2,2,2)
# this means we are reshaping  the array to 2 rows 4 coloiumns
print(res)