#Python program to find the Nth term in a Fibonacci series using recursion.
def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
num = int(input("Enter no. of terms:"))
print(Fibonacci(num))