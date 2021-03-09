f=open("name.txt","r")
a=f.read()
lst=a.split()
rev_str=[]
for i in lst:
  rev_str.append(i[::-1])
s=" ".join(rev_str)
print(s)