#Python program to check whether the given integer is a prime number or not .
num = int(input("Enter an integer number : "))
m = num
m = m//2
for i in range(2,m):
    if(num % i == 0):
        print(num, "is not prime")
        break
else:
        print(num," is prime")
