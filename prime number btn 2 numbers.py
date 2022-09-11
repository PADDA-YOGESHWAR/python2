start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
print("The prime numbers between",start,"and",end,"is :")
for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)
