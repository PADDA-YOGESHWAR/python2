names = ["Lucky","Munna","jay","Lucky","jay"]
companies = ["dell","apple","MS","dell","tcs"]
zipped = zip(names,companies)
print(zipped)#returns the type of the list and also the address
zipped2 = list(zip(names,companies))
print(zipped2)#returns as a list with some pairs of indexes
zipped3 = set(zip(names,companies))
print(zipped3)#returns as set which will ignore dupicates and an unordered list
zipped4 = dict(zip(names,companies))
print(zipped4)#returns a a dictionary as key value pairs
zipped5 = list(zip(names,companies))
for (a,b) in zipped5:
    print(a,b)#just prints the elements 