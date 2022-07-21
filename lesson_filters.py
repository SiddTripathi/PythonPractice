#filters are used to filter the list based on boolean value returned by function and then implementing filter on the list based on boolean results

dromes = ["demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk"]

#check whether this list is palindrome or not. See how the function word returns true or false for any word which is passed. Filter will take each word from dromes and pass it to words
# and it will then only return list of words which return true from words

def words(word):
    return word == word[::-1]
    

palindrome = list(filter(words,dromes))
print(palindrome)


