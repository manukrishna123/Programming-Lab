z=[]
v=['a','e','i','o','u']
a=input("\nEnter a string: ")
for i in a:
  if i in v and i not in z:
    z.append(i)
print(z)
 