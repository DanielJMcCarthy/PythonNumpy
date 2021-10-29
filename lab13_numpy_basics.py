"""
Question 1. 

A nXn numpy array is given where n is divisible by 3. You are required to write 
a python program that can dived the array into 9 sub-arrays and only return 
the middle section.

"""
  

arr = np.array([[1, 3, 4, 2, 3, 5],[4,6, 4, 5, 1, 5],[3,3, 41, 25, 1, 4]              

                 ,[3,3, 4, -5, 1, 4],[3,3, 4, 5, 1, 4],[3,3, 4, 5, 1, 4]])

 

a = int(len(arr)/3)

 

res = arr[a:a*2 , a:a*2]

 

print(res)

 
"""
Question 2.

Write a function that receives a 2D numpy arrays and extract the rows with 
even index and from those rows extract the second half of the columns.

"""

arr = np.array([[1, 3, 4, 2, 3, 5],[4,6, 4, 5, 1, 5],[3,3, 41, 25, 1, 4]              

                 ,[3,3, 4, -5, 1, 4],[3,3, 4, 5, 1, 4],[3,3, 4, 5, 1, 4]])




a =int(len(arr[0])/2)

print(arr[1:: 2, a:]) # rows with indexes: 1,3,5,7,9,…

print(arr[:: 2, a:]) # rows with indexes: 0,2,4,6,8,…

 

 
"""
Question 3.

Write a function that reads the bikeSharing file and identify the number of different seasons.

"""

myfile = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')

 

print(set(myfile[:,1]))

---

myfile = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')

 

print(np.unique(myfile[:,1]))

 
"""
Question 4.

Write a function that reads the bikeSharing file and identify the maximum, 
minimum and mean temperature of all entries. Look at the lecture note to 
find out the index associated with temperature.
"""
 

 

myfile = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')

 

print(np.min(myfile[:,9]))