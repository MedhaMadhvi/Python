# Python program to delete an element from a list by index.
num = int(input("Enter number of element in list: "))
lst = []
print("Enter numbers:")
for i in range(num):
    L = int(input())
    lst.append(L)
print("List Before deletion", lst)
n = int(input("Enter index to delete element from list : "))
try:
    lst.pop(n)
    print("List After deletion", lst)
except IndexError:
    print("Deletion out of range")

