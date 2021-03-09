def fib(n):
 if(n<=1):
   return n
 else:
    return(fib(n-1)+fib(n-2))
n=int(input("Enter the limit : "))
if(n<=0):
    print("\nEnter a Positive Number")
else:
    print("\nFibonacci Series : ")
    for i in range(n):
      print(fib(i))