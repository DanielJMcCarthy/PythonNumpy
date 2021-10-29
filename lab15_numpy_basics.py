
#Q1.i:

 
import numpy as np

data = np.genfromtxt(‘bikeSharing.csv', delimiter=',')

compareHolidays(data, 0)

compareHolidays(data, 1)

def compareHolidays(data, holiday):

    subset = data[data[:, 5] == holiday]

    print ("Number of entries ", len(subset))

    print ("Mean", np.mean(subset[:, 15]))

 

#Q1ii:

# The following sample shows how to normalize the temp column.

data = np.genfromtxt(‘bikeSharing.csv', delimiter=',')

newdata = np.copy(data)

print (newdata[:, 9])

newdata[:, 9] *= 41

print (newdata[:, 9])

 

 

#Q1iii:

data = np.genfromtxt(‘bikeSharing.csv', delimiter=',')

result = data[:, 13]>data[:, 14]

print ("Percentage of time where causal users > registered", (len(data[result])*100.0)/len(data) )

 

 

#Q1iv:

def averageNumRentalBikesPerCondition(data):

     conditions = {1:"Clear", 2:"Misty", 3:"Light Rain", 4:"Heavy Rain"}

     for key in conditions:

         subsetData = data[data[:,8]==key]

         print (np.mean(subsetData[:, 15]))

def main():

      data = np.genfromtxt(‘bikeSharing.csv', delimiter=',')

      averageNumRentalBikesPerCondition(data)

 

 

#Q1v:

def main():

      data = np.genfromtxt(‘bikeSharing.csv', delimiter=',')

      for temp in range(1, 40, 5):

            analyseTemp(data, temp, temp+4)

 

 

def analyseTemp(data, minValue, maxValue):

     # the temperature values stored in the array are multiplied by 41

      higherTempCondition = (data[:,9]*41)>=minValue

      lowerTempCondition = (data[:,9]*41)<=maxValue

      subset = data[higherTempCondition & lowerTempCondition]

      meanValue = np.mean(subset[:, 13])

      print ("For temp in range ", minValue, "to", maxValue, "the mean number of casual users was ", meanValue)