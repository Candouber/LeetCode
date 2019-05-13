class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        num = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                res.append(0)
        if 0 in nums:
            for i in range(len(res)):
                nums.remove(0)
        nums.extend(res)
