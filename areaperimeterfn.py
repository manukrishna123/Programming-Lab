def cal(r):
  import math
  area=math.pi*r**2
  perimeter=2*math.pi*r
  return area,perimeter
r=float(input("Enter the radius : "))
a,b=cal(r)
print("The area ofb circle = ",a)
print("Perimeter of circle = ",b)
