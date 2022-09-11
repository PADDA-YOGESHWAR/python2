# Program to check if a number is prime or not

num = int(input("Enter a number :"))
count = 0
if num > 1:
    for i in range(1, num):
        if (num % i) == 0:
            count = count+1
            break
if count==2:
    print(num, "is a PRIME NUMBER")
else:
    print(num, "is a COMPOSITE NUMBER")
