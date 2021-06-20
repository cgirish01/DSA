def twoSum(nums, target):
        array = {}
        for i,num in enumerate(nums):
            match = target - num
            if match in array:
                return [nums.index(match) ,i]
            else:
                array[num] = True
        return []

nums=[int(x) for x in input().split()]
target=int(input())
ans=twoSum(nums, target)
print(ans)