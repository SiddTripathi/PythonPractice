#Pandas - high level data manipulation tool. Data structure for this is data frames. These allow you to store and manipualte tabular data in rows 
# of observation and columns of variables.





#Here were encountering error before because one my files was named string.py Now note that string.py is one of the modules in python. When you used pandas and imported it
# pandas module imports string module as well. But python interpreter confused string module with our local string module and hence threw error when trying to do 
# data frame. SO NEVER NAME YOUR FILE IN THE NAME OF MODULE. NOW CHANGING MY FILE NAMES TO DIFFERENT




dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd

brics = pd.DataFrame(dict)

#print(brics)

#provide index of your choice in data frame. Like instead of default numbers, you can provide two letter COuntry code

brics.index = ["BR","RU","IN","CH","SA"]

#print(brics)

#importing a csv file

cars = pd.read_csv('D:\Python_Pactice\PythonPractice\Lesson_pandas\Book.csv')

print(cars)

print(cars['Model'])

print(cars[['Brand']])

print(cars[['Model','Year']])

#Data frames have indexes so you can travers them just like lists. You can provide specific index or range of index to retreieve elements.
#there are numerous ways of traversing a dataframe. You can also use iloc (integer index based travers) and loc (label based meaning specify ros and columns)