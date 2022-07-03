#list comprehension is like one line statement to manipulate and play around list. It creates a new list bbased on another list
# Example - say for example we need to create a list of integers which specify the length of each word except the word 'the'

#splitsentence() - splits 

sentence = "This city is Auckland and its the most beautiful city in the New Zealand"

words = sentence.split()
words_len = []

for word in words:
    if word != 'the':
        words_len.append(len(word))

print(words)
print(words_len)

#but this above program can be done in lesser number of lines using list comprehension

sent = "The quick brown fox jumps over the lazy dog"

words = sent.split()

word_len = [len(word) for word in words if word.lower() !="the"] #u see instead of writing multi-line for loop, we write a list comprehension in one line

print(words)
print(word_len)

#Exercise - create list out of another list numbers which only contains positive numbers
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

new_list = []
new_list = [num for num in numbers if num>0]
inxex_postive = [i for i,num in enumerate(numbers) if num>0]

print(new_list)
print(inxex_postive)