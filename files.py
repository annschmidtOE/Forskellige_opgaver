import json

with open("person.txt") as f:
    text = f.read()
print(text)

name = "Anna"

with open("me.txt", "w") as f:
    f.write(name)
    print(type(text))

with open("me.txt") as f:
    data = f.read()

print(data)


#person = {
#     'first_name' : 'Anna',
#     "last_name" : "Schmidt",
#     "year" : 
#     }

f = open("person.json", "w")
f.write(json.dumps(person)) #convert dict to json
f.close()

f = open("person.json", "r")
data = f.read()
f.close()
print(data)
print(type(data)) #<class 'str'>

data_json = json.loads(data)
print(type(data_json))

print(data_json["first_name"])

data_json["nick_name"] = "Idiot"

print(data_json)

string_data = json.dumps(data_json)

f = open("person.txt", "w")
f.write(string_data)
f.close()



name = "Anna"
last_name = "Schmidt"

f = open("kea.txt", "w")
f.write(name + "\n" + last_name)
f.clost()


year = 2024
f = open("kea.txt", "a")
f.write("\n" + str(year))
f.close()




