#Python provides built-in json libraries to encode and decode the json
#we use json module


#json object decoded to python dictionary,   json array decoded to python list see below example

import json

json_string = '{ "name":"John", "age":30, "city":"New York"}'
json_list = '["Ford","Range","BMW"]'

decoded_dict=json.loads(json_string)
decoded_list=json.loads(json_list)

print(decoded_dict["name"])
print(type(decoded_dict))
print(type(decoded_list))


#difference between loads and load in json function is that load is used to read files and loads is used to read strings

#to read json file use below syntax
with open('D:\Python_Pactice\PythonPractice\json_sample.json','r') as content:
    data = json.load(content)

print(data)
print(type(data))

#converting python data structures to JSON.The data type will be JSON String.
back_tojson = json.dumps(decoded_dict)
back_tojson1 = json.dumps(data)
print(type(back_tojson))
print(type(back_tojson1))


#exercise 
import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name]=name
    salaries[salary]=salary
    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])