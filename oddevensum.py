lim=int(input("Enter the limit : "))
even=0
odd=0
for i in range(1,lim+1):
   if i%2==0:
     even=even+i
   else:
     odd=odd+i
print("Sum of even numbers upto",lim,"is",even)
print("Sum of odd numbers upto",lim,"is",odd)
