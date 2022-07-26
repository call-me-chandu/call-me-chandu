x=int(input("enter the first side of the triangle"))
y=int(input("enter the second side of the triangle"))
z=int(input("enter the third side of the triangle"))
if x==y==z:
    print("it is an equilateral triangle")
elif x==y!=z:
    print("it is isoscalene triangle")
else:
    print("else")
