#the algorithms

d1 = {1: 'a1', 
      2: {3: 'a3'}, 
      5: 'a5'}


d2 = {2: {4: 'a4'}, 
      3: 'a3', 
      5: 'five'}

d0 = {}

d0.update(d1)
print(d0)

print("d1 before: ", d1)
d1.update(d2)
d1.update(d0)
d1.update(d2[2])
print("d1 after: ", d1)

