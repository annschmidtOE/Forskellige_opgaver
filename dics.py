
cat = {
       "name" : "Hannibal", 
       "age": 2
       }

#print(cat)

dog = {
    "name" : "Dino",
    "age" : 10
}

#print(dog)

animals = []
animals.append(cat)
animals.append(dog)


print(animals[1]["name"])

dog["gender"] = "male"

print(animals)

letters = ["a","b","c"]
for letter in letters:
    print(letter)

for animal in animals:
    print(animal)

for age in animals:
    print(age["age"])

"""
first_name = "Anna"
last_name1 = "Schmidt"

year = 2024

letters = ["a","b","c"]

person = {
    "name" : "XXX", "last_name" : "Schmidt", "salary" : 20000
}


people = []
people.append(person)
print(people)
print(people[0]["last_name"])
"""

