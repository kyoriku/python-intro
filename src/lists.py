names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
print(names[2])

variable_1 = "Tim"
names = ["John", variable_1, "Mary", 41, "Bluto"]
print(names[1])

names = []

names = ["John", "April"]
print(len(names))

names = ["John", "April"]
names.append("Bob")
print(names)

names = ["John", "April"]
names.insert(0, "Bob")
print(names)

names = ["John", "April"]
names.extend(["Tim", "Bob"])
print(names)

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.remove("Bluto")
print(names)

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.pop(0)
print(names)

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.pop(1)
print(names)

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.remove("Mary")
print(names)

names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]]
print(names)

names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]]
print(names[4][2])

numbers = [1,2,3,4]
names = ["John", "Mary", "Beatrice", "Bluto", numbers]
print(names[4][2])

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
print(names[1])

math_problem = ["1 + 1", "John", "Tim", "Mary", "Beatrice", "Bluto"]
print(math_problem[0])

info = [
  ["John", "123 Main St", "555-1234"],
  ["Tim", "456 Elm St", "555-5678"],
  ["Mary", "789 Oak St", "555-9012"],
  ["Beatrice", "101 Pine St", "555-3456"]
]
print(info[1])
print(info[2][2])
