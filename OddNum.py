#Python program to find the odd numbers in an array.
num = int(input("Enter number of element in list: "))
lst = []
print("Enter numbers:")
for i in range(num):
    L = int(input())
    lst.append(L)
for n in lst:
    if n % 2 != 0:
        print(n, end=" ")
