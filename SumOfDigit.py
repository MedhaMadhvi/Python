#Python program to find the sum of the digits of an integer using a while loop.
num = int(input("Enter an integer number : "))
print("Sum of Digits :", end="")
sum = 0
while num != 0:
    digit = num % 10
    num //= 10
    sum = sum + digit
print(sum)
