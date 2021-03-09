str=input("\nEnter a string: ")
a=str.split()
b=set(a)
for i in b:
   print(i,a.count(i))