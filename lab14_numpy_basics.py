"""
Question 1.


Write a function that receives two numpy arrays and do the followings:

Find the intersection among two arrays
Remove the intersections from the first array.
"""

 

import numpy as np

import random as rnd

 

a = np.array([1,2,3,4,5])

b = np.array([5,6,7,8,9])

 

d = np.intersect1d(a,b)

c = np.setdiff1d(a,d)

 

print(c)

 
"""
Question 2.

Write a function that receives two numpy arrays. First it should find all the 
positions where elements of two arrays match. Then change the values of those 
element in the second array to -1. No loop is allowed.
"""
 

a = np.array([1,2,3, 2,3,4,3,4,5,6])

b = np.array([7,2,10,2,7,4,9,4,9,6])

 

c = np.where(a == b)

b[c] = -1

print(b)

 

 
"""
Question 3.

Write a function that takes a numpy array and extract all the elements in a 
range of [a, b]. a and b are read from end user.
"""
 

arr = np.array([1,2,3, 2,3,4,3,4,5,6])

index = np.where((arr >= 5) & (arr <= 10))

print(arr [index])

 
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

Write a program that can print all the even days of August 2019.
"""
 

import numpy as np

import random as rnd

 

aug = np.arange('2019-08', '2019-09', dtype='datetime64[D]')

 

evenDays = aug[1::2]

 

for i in evenDays:

    print(i)

 
"""
Question 7.

Write a program that asks your date of birth and calculate and print your age 
as hours. E.g., I am 330083 hours old.
"""
 

import numpy as np

import random as rnd

 

TNow = np.datetime64('now', 'h')

 

bd = np.datetime64(input('When is your birthday!?'))

 

print(TNow- bd)