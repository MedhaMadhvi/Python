#Python program to implement linear search.
def linear_Search(list1, n, key):
    for i in range(0, n):
        if (list1[i] == key):
            return i
    return -1
num = int(input("Enter number of element in list: "))
list1 = []
print("Enter numbers:")
for i in range(num):
    L = int(input())
    list1.append(L)
key = int(input("Enter number to search in list : "))
result = linear_Search(list1, num, key)
if (result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
