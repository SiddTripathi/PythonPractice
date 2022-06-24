#String operation include, 
#length - length of string
#count('letter') - occurence of that letter in string
#index('letter') - index of that letter in string
#index slicing - string[begining index:end index] - will return only string with those indexes begining index - end index-1 eg 2:6 means index 2 to index 5
#index skipping - str[begin index: end index: skips] eg: str[2:8:1] begin with 2 end at 7 and skip 1 letter.
#str.upper() - converts string to upper case
#str.lower() - converts string to lower case
#str.startswith("letter or word") - returns true if string starts with same letter or word
#str.split(" ") - splits item at occurence of whatever passed in parenthesis. (",") split at comma, (" ") split at space


#exercise
s = "Strings are Awesome"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))