#bubble sort works well and easyest algorithm technique
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)
nums =[5,3,8,6,7,2]
sort(nums)
print(nums)