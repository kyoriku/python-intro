num = 0
while num < 10:
  print(num)
  num += 1

num = 0
while num < 10:
  num += 1
  if num == 5:
    break
  print(num)

num = 0
while num < 10:
  num += 1
  if num == 5:
    continue
  print(num)

for num in range(6):
  print(num)

for num in range(6):
  print("I LOVE CHEESE!")

names = ["John", "Mary", "Tim"]
for name in names:
  print(name)

name = "John Doe"
for x in name:
  print(x)

for x in range(3):
  print(x)
else:
  print("All Done!")

for x in range(3):
  print(x)
print("All Done!")

for x in range(3):
  pass
