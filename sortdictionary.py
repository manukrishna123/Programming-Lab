dict={}
x=int(input("Enter the number of elements in dictionary : "))
for i in range(x):
   dict[i]=input("Enter the elements : ")
asc=sorted(dict.values())
print(asc)
asc.reverse()
print(asc)
