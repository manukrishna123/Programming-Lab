AreaS=lambda s:s*s
AreaR=lambda length,breadth:length*breadth
AreaT=lambda B,H:(B*H)/2
s=int(input("\nArea of Square\nEnter length of side ofsquare : "))
length=float(input("\n Area of rectangle\nEnter length of rectangle:"))
breadth=float(input("enter breadth of rectangle:"))
B=float(input("\nArea of triangle\nEnter base of triangle:"))
H=float(input("Enter height of triangle:"))
print("Area of Square : ",AreaS(s))
print ("Area of rectangle:",AreaR(length,breadth))
print ("Area of triangle:",AreaT(B,H))
                           
