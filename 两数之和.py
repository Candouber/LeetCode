def function(nums, target):
    for x in range(len(nums)-1):
        if (target-nums[x]) in nums :
            a = nums.index(target-nums[x]
        if a != x:
            return [x,nums.index(target-nums[x])]
        else:
            continue
