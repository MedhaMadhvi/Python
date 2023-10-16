import cmath
a = float(input("Enter first coefficient: "))
b = float(input("Enter second coefficient: "))
c = float(input("Enter third coefficient: "))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are : ', sol1, "and", sol2)