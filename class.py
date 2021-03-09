class rectangle:
  __area = 0
  __perimeter = 0
def _init__(self,length,width):
 self.__length=length
 self.__width=width
def calc__area(self):
 self.__area=self.__length*self.__width
 print("Area is :",self.__area)
def __lt__(self,second):
 if self.__area<second.__area:
    return True
 else:
    return False
length1=int(input("Enter length of the rectangle 1 : "))
width1=int(input("Enter width of the rectangle 1 : "))
length2=int(input("Enter length of the rectangle 2 : "))
width2=int(input("Enter width of the rectangle 2 : "))
obj1=rectangle(length1,width1)
obj2=rectangle(length2,width2)
obj1.calc__area()
obj2.calc__area()
if obj1<obj2:
  print("Rectangle2 is large")
else:
  print("Rectangle1 is largest")