#Python program to generate the prime numbers from 1 to N.
num= int(input("Input the range: "))
for num in range(2, num+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
