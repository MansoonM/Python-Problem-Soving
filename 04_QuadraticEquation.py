#complex Math Module
#quadratic equation = ax**2 + bx +c =0
#a,b,c is real number, a!=0

import cmath
a= int(input("Enter number (a != 0): "))
b= int(input("Enter number: "))
c= int(input("Enter number: "))

#formula for discriminant
d= b**2 - (4*a*c)

root1= (-b-cmath.sqrt(d))/(2*a)
root2= (-b+cmath.sqrt(d))/(2*a)

print("The roots are ", root1, root2)