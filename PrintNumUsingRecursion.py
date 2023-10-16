def num(n):
    if n>= 0:
        print(n)
        num(n-1)
number= int(input("Enter a number:"))
num(number)