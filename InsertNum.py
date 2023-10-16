#Python program to insert a number to any position in a list.
num = int(input("Enter number of element in list: "))
lst = []
print("Enter numbers:")
for i in range(num):
    L = int(input())
    lst.append(L)
n = int(input("Enter number to insert in list : "))
position = int(input("Enter position where number has to be inserted : "))
lst.insert(position-1,n)
print(lst)
