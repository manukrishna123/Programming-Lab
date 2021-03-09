x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))
while y!=0:
   r=x%y
   x=y
   y=r
print("GCD is ",x)