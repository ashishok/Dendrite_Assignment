import json

file = open("parse_json.json","r")
# file = open("sample.json","r")
exm = file.read()
file.close()
 
a = json.loads(exm)
print(a)
# print(a["design_state_data"]["target"])