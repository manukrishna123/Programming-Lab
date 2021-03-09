d1={}
d2={}
d3={}
a=int(input("Enter the limit of dictionary 1 :"))
for i in range(a):
  d1[i]=int(input("\nEnter the elements : "))
b=int(input("\nEnter the limit of dictionary 2 : "))
for i in range(3,3+b):
   d2[i]=int(input("\n Enter the elements : "))
print(d1)
print(d2)
for i in d1:
  if i not in d2:
    n={i:d1[i]}
    d3.update(n)
  else:
    n={i:d1[i]+d2[i]}
    d3.update(n)
for i in d2:
  if i not in d1:
    n={i:d2[i]}
    d3.update(n)
print(d3)

     
