#A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key. It can be
#any data type.It is initialized by {}


phonebook = {}

#phonebook[key] = value

phonebook["Sidd"] = 12345
phonebook["Prashant"] = 6789

#phonebook{
# "Sidd":12345
# "Prashant":6789
# }
print(phonebook)

#some operations in dictionary

details = {
    "Sid":30,
    "Ron":40,
    "Pat":28,
    "Kish":25,
    "Ish":22,
    "Neha":29

}

#iterate a dictionary
#use enumerate if you want index of each key. If you want element of each key then use .items

def iterate_dict(dict):
    for name,age in dict.items():
        print(name,age)  
    
iterate_dict(details)

print("**********")
#delete or remove an element from dictionary

del details["Ish"]
iterate_dict(details)

print("**********") #key is case sensetive. Should be given as given
details.pop("Neha")
iterate_dict(details)

#update key is used to add/append multiple key:value to existing dictionary
new_values ={"Harsh":24,"Vaidya":29}
details.update(new_values)
iterate_dict(details)


#exercise
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here

phonebook["Jake"] = 938273443

del phonebook["Jill"]

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")
    