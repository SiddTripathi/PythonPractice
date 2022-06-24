#Numbpy arrays - great alternatives to python lists

#they are fast, easy to work with, and give users the opportunity to perform calculations across entire arrays.

age = [23,24,25,27,13,15]
weight = [62.13,66.24,66.14,71.00,36.45,33.20]

import numpy as np

np_age = np.array(age)
np_weight = np.array(weight)

print(type(np_age))
print(type(age))

#now for example if you want to perform an operation on each element of list, you can do it easily in case of numpy array. But if its a simple list, u need to loop it.

bmi = np_weight/np_age

print(bmi)

double_age = age*2

double_numpy_age = np_age *2

print(double_age)
print(double_numpy_age)       #now notice the difference, in simple list - *2 will create another list with similar elements. Multilpy list as whole by two. But in numpy
                              # array, *2 will mean multiply every element of array by 2


#create a subset of elements based on condition. Example create a subset from np_age where each element is more than 20. Pass the condition inside [] of numpy array

print(np_age[np_age>20])

#exercise

weight_new = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weight_new = np.array(weight_new)

weight_lbs = np_weight_new*2.2

print(weight_lbs)