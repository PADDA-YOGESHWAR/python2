#triple single quotes are not comments they are used for a spcial doctumentation purpose 
#python is compiler language as well as interpeter language
#python code--> compiled in compiler --> generates a byte code --> interpreted (we need to interpret because to get protability) in python virtual machine --> machine language
#in python we no need to give seperate commands to complie and run the programm we  just give "python filename.py"
def search(lst,n):
    i=0
    while(i<len(lst)):
        if(lst[i]==n):
            globals()['pos'] = i
            return True
        i=i+1
    return False
lst = [1,2,3,4,5,6,7,8,9]
n = 9
pos=0
if search(lst,n):
    print("element found in location ",pos+1)
else:
    print("element not found")
