for x in range(1, 101):
  if x % 3 == 0 and x % 5 ==0:
    print(f"{x} FIZZ BUZZ!")
  elif x % 3 == 0:
    print(f"{x} FIZZ")
  elif x % 5 == 0:
    print(f"{x} BUZZ")
  else:
    print(x)

for x in ['FIZZ BUZZ' if x % 15 == 0 else 'FIZZ' if x % 3 == 0 else 'BUZZ' if x % 5 == 0 else x for x in range(1, 101)]:
  print(x)

names = [
  ["John", "123 Main St", "555-1234"], 
  ["Tim", "456 Elm St", "555-5678"], 
  ["Mary", "789 Oak St", "555-9012"], 
  ["Beatrice", "101 Pine St", "555-3456"]
]

for name in names:
  print(name[2])

for x in range(len(names)):
  if x % 2 == 1:
    print(names[x])
