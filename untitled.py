1. GRAPHICS
2. GRAPHICS_MAIN.PY
   1.1 circle.py
       from math import pi
       def area_circle(radius):
         return pi*radius*radius
       def perimeter_circle(radius):
         return 2*pi*radius
1.2 rectangle.py
   def area_rec(length,width):
     return length*width
   def perimeter_rec(length,width):
     return 2*(length+width)
1.3 _init_.py
1.4 tdgraphics
  1.4.1 inint.py
  1.4.2 cuboid.py
        def area_cuboid(l,b,h):
          return 2*(l*h + b*h + l*b)
        def perimeter_cuboid(l,b,h):
          return 4*(l+b+h)
  1.4.3 sphere.py
        from math import pi
        def area_sphere(radius):
          return 4*(pi*radius*radius)
        def perimeter_sphere(radius):
          return 2*pi*radius
2. graphics main.py
import graphics
from graphics import circle,rectangle
from graphics.tdgraphics import cuboid,sphere
from graphics.circle import *
print("Area of a circle with radius 10 is : ",circle.area_circle(10))
print("Permeter of a circle with radius 10 is ",circle.perimeter_circle(10))
print("Area of a circle with radius 10 is : ",area_circle(10))
print("Area of a Rectangle with length and width 10 is :",rectangle.area_rec(10,10))
print("Permeter of a Rectangle with length and width 10 is :",rectangle.perimeter_rec(10,10))
print("Area of a cuboid with length,width,height 10 is :",cuboid.area_cuboid(10,10,10))
print("Permeter of a cuboid with length,width,height 10 is :",cuboid.perimeter_cuboid(10,10,10))
print("Area of a spere with radius 10 is : ",sphere.area_sphere(10))
print("Permeter of a spere with radius 10 is ",sphere.perimeter_sphere(10))
R