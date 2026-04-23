from mypack.basicshapes import areaofsquare, perimeterofsquare, areaofrectangle
from mypack.circle import areaofcircle, perimeterofcircle

radius = int(input('Enter Radius: '))

print('Area: ', areaofcircle(rad=radius))
print('Perimeter: ', perimeterofcircle(rad=radius))

si = int(input('Enter the side sq: '))
print('Area:', areaofsquare(side=si))
print('Perimeter: ', perimeterofsquare(side=si))

l = int(input('Enter the length of rectangle: '))
b = int(input('Enter the breadth of rectangle: '))
print('Area: ', areaofrectangle(l, b))