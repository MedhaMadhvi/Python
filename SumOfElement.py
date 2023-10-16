#Python program to display the sum of n numbers using a list.
sum = 0
num = int(input("Enter number of element in set: "))
list1 = []
print("Enter numbers:")
for i in range(num):
    L = int(input())
    list1.append(L)
for ele in range(0, num):
    sum = sum + list1[ele]
print("Sum of all elements in given list: ", sum)
