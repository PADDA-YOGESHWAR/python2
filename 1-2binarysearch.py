#binary search is better than linear search when the list of elements are more. in case of binary search we must have the elements in sorted order
def Bsearch(lst,n):
    l=0
    u=len(lst)-1
    while l<=u:
        mid=(l+u)//2
        if lst[mid]==n:
            globals()['pos2']=mid
            return True
        else:
            if lst[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
pos2=-1
lst = [1,2,3,4,5,6,7,8,9]
n = 9
if Bsearch(lst,n):
    print("element found in location ",pos2+1)
else:
    print("element not found")