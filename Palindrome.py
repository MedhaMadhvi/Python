#Python program to check whether a string is palindrome or not.
str = input("Enter a string:")
j = -1
count = 0
for i in str:
    if i != str[j]:
        count=1
        break
    j-=1
if count == 0:
    print(str, "is palindrome")
else:
    print(str, "is not palindrome")
