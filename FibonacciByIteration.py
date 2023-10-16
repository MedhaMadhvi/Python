#Python program to print Fibonacci series using iteration.
num1 = 0
num2 = 1
n = 1
num = int(input("Enter no. of terms:"))
if num <= 0:
    print("Incorrect input")
elif num == 1:
   print(num1, end=" " )
else:
    print(num1, end=" ")
    print(num2, end=" ")
    while n < num-1:
        next_num = num1+num2
        print(next_num, end=" ")
        num1 = num2
        num2 = next_num
        n += 1