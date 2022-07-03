#length of string

import enum


sample_string = "the clever fox jumps on the sheeps"
short_string = "google.com"

print(len(sample_string))

#number of characters

for ind, char in enumerate(short_string):
    print("Character %s, Index: %d"%(char,ind))


str_prt1 = short_string[0:2]
str_prt2 = short_string[-2:]

print(str_prt1+str_prt2)

print(sample_string[:5:1])