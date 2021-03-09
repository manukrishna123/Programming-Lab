f=open("name.txt","r")
a=f.read()
lst=a.split()
print(max(lst,key=len))