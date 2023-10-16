# Python program to display all integers within the range 100 -200 whose sum of digits is an even number.
print("Number whose Sum of Digits is even :", end="")
list=[]
for i in range(100,201):
    i=str(i)
    sum=0
    for j in i:
        j=int(j)
        sum=sum+j
    if sum%2==0:
        list.append(i)
print(list)
