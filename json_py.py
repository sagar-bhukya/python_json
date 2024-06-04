import json

a={
    "name":"sagar",
    "age":22,
    "state":"TS"
}
b=json.dumps(a) #converting dicyt to json
print(b)

# list conversion to Array
print(json.dumps(['Welcome',"to","gudur"]))

# tuple conversion to Array
print(json.dumps(('Welcome',"to","gudur")))

#string conversion to string
print(json.dumps("Hi"))

#int conversion to number
print(json.dumps(123))

#float conversion to number
print(json.dumps(123.456))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))


#serializastion
var={
    "subjects":
    {
        "maths":100,
     "physics":200

    }
}

with open("sample.json",'w') as p:
    json.dump(var,p,indent=4)

#desialization
with open("sample.json",'r') as read_it:
    data= json.load(read_it)
    print(data)

# Initialize JSON data
json_data = '[ {"studentid": 1, "name": "Nikhil", "subjects": ["Python", "Data Structures"]},{"studentid": 2, "name": "Nisha", "subjects": ["Java", "C++", "R Lang"]} ]'

json_to_py=json.loads(json_data)
print(json_to_py)
#for pretty print
json_formated=json.dumps(json_to_py,indent=4)
print(json_formated)

#Sorting JSON



 
