import json

dict1={
    "name":"sagar",
    "age":22,
    "phone":8501079132
}
#method 1-----------using write
#serialization
object_data=json.dumps(dict1,indent=4)
#create a file
with open("json_with_files\sample.json",'w') as file:
    file.write(object_data)


#method 2--------
#using dump
with open("json_with_files\sample1.json",'w') as p:
    json.dump(dict1,p,indent=4) 


#reading file using load
with open("json_with_files\sample1.json",'r') as OpenFile:
    load_data=json.load(OpenFile)
print(load_data)