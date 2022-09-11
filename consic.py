a=int(input("Enter the number of elements you want to enter : "))
list=[]
sum =0
for i in range(a):
    list.append(int(input()))
print(list)
for i in range(a):
    if(list[i-1]==list[i]):
        sum = sum +1
print(sum)