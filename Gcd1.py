def compute_hcf(a,b):
 if a>b:
  smallest=b
 else:
  smallest=a
 for i in range(1,smallest+1):
  if((a%i==0) and (b%i==0)):
   hcf=i
 return hcf

n1=int(input("Enter the first no: "))
n2=int(input("Enter the second no: "))
print("GCD is ",compute_hcf(n1,n2))


  