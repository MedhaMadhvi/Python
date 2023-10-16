#Python program to find the geometric mean of n numbers.
import math
num = int(input("Enter number of element in list: "))
product = 1
lst = []
print("Enter numbers:")
for i in range(num):
    L = int(input())
    lst.append(L)
    product = lst[i] * product
GM = pow(product, (1/num))

print("Geometric Mean:", GM)
