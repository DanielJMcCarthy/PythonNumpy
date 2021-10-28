
import numpy as np
"""
Generate a random 1-d numpy array in the range [1-100] and then perform the following: (Note: You are not allowed to use any loop to the following tasks).

Extract all the odd numbers
Change the odd numbers to -1
Extract all the even numbers
Increment the even numbers by 1
 
"""
 

 

 

arr = np.array([])

for i in range(100):

    arr = np.append(arr, rnd.randint(1, 100))

   

arr[arr % 2 == 1] = -1
#same thing for even.
 

arr[arr % 2 == 0] = arr[arr % 2 == 0] + 1

 

print(arr)

 


 
"""
Generate a random 1-d numpy array in the range [1-100] and then perform the following: (Note: You are not allowed to use any loop to the following tasks).

Extract all the odd numbers
Change the odd numbers to -1
Extract all the even numbers
Increment the even numbers by 1
 
"""
 

 

 

arr = np.array([])

for i in range(100):

    arr = np.append(arr, rnd.randint(1, 100))

   

arr[arr % 2 == 1] = -1
#same thing for even.
 

arr[arr % 2 == 0] = arr[arr % 2 == 0] + 1

 

print(arr)

 

 

 

 
"""
Question 2.

Write a function that receives two numpy arrays and do the followings:

Find the intersection among two arrays
Remove the intersections from the first array.
 
"""
 

a = np.array([1,2,3,4,5])

b = np.array([5,6,7,8,9])

 

 

d = np.intersect1d(a,b)

c = np.setdiff1d(a,d)

 

print(d)

 

"""

Question 3.

Write a function that receives two numpy arrays. 
First it should find all the positions where elements of two arrays match. 
Then change the values of those element in the second array to -1. No loop is allowed.

"""

a = np.array([1,2,3, 2,3,4,3,4,5,6])

b = np.array([7,2,10,2,7,4,9,4,9,6])

 

c = np.where(a == b)

b[c] = -1

print(b)

 



"""
Question 3.

Write a function that takes a numpy array and extract all the elements in a range of [a, b]. 
a and b are read from end user.
"""
 

a = np.array([1,2,3, 2,3,4,3,4,5,6])

index = np.where((a >= 5) & (a <= 10))

print(a[index])

 

"""
Question 4.

Write a NumPy program to print the NumPy version in your system.
"""
 

print(np.__version__)

 
"""
Question 5.

Write a NumPy program to add a border (filled with 0's) around an existing array.

"""

 

x = np.ones((3,3))

print("Original array:")

print(x)

print("0 on the border and 1 inside in the array")

x = np.pad(x, pad_width=2, mode='constant', constant_values=0)

print(x)

 

x = np.array([[1, 2],[3, 4],[5, 3],[2, 5]])

print("Original array:")

print(x)

print("0 on the border and 1 inside in the array")

x = np.pad(x, pad_width=1, mode='mean')

print(x)

 
"""
Question 6.

Write a program that can find all the unique values in a 2D numpy array.
"""
 

    
arr = np.array([[1, 3],[4, 5],[3, 4]])

 

print(np.unique(arr))

