num = int(input("Enter an integer number : "))
print("Number in reverse order :")
while num != 0:
    digit = num % 10
    print(digit, end="")
    num //= 10