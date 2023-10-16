#Python program to find the largest number in a list without using built-in functions.
num = int(input("Enter number of element in set: "))
lst = []
print("Enter numbers:")
for i in range(num):
    L = int(input())
    lst.append(L)
max = 0
for i in lst:
    if i > max:
        max = i

print('The largest number in list is', max)