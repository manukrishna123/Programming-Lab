def add(a,b):
  return "{}+{}={}".format(a,b,a+b)
def sub(a,b):
  return "{}-{}={}".format(a,b,a-b)
def mul(a,b):
  return "{}*{}={}".format(a,b,a*b)
def div(a,b):
  return "{}*{}={}".format(a,b,a/b)
ch=input("Enter the choice : ")
if ch=='1':
  a=int(input("Enter value of a : "))
  b=int(input("Enter value of b : "))
  print(add(a,b))
elif ch=='2':
  a=int(input("Enter value of a : "))
  b=int(input("Enter value of b : "))
  print(sub(a,b))
elif ch=='3':
  a=int(input("Enter value of a : "))
  b=int(input("Enter value of b : "))
  print(mul(a,b))
elif ch=='4':
  a=int(input("Enter value of a : "))
  b=int(input("Enter value of b : "))
  print(div(a,b))
else:
   print("Enter valid choice : ")