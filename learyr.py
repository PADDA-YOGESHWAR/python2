n=int(input("Enter the year : "))
p = int(input("Enter the number of lear years to know : "))
for i in range(n,n+p*4):
    if (i%4==0 and i%100 !=0 or i%400 ==0):
        print(i)
    else:
        pass