class rectangle:
   _area=0
   _perimeter=0
 def_init_(self,length,width):
   self._length=length
   self._width=width
 def calc_area(self):
   self._area=self._length*self_width
   print("Areavis: ",self._area)
 def_It_(self,second):
   if self._area<second._area:
     return True
   else:
     return false
length1=int(input("Enter the lenth of Rectangle1 : "))
width1=int(input("Enter the width of Rectangle1 : "))
length2=int(input("Enter the lenth of Rectangle2 : "))
width2=int(input("Enter the width of Rectangle2 : "))
obj1=rectangle(length1,width1)
obj2=rectangle(length2,width2)
obj1.calc_area()
obj2.calc_area()
if obj1<obj2:
   print("Rectangle2 is largest")
else:
   print("Rectangle1 is largest or these are equal")
 