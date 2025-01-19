class Solution(object):
    def twoSum(self, nums, target):
        l, r = 0, len(nums) - 1
        nums = [[n, i] for n, i in enumerate(nums)]
        nums.sort(key=lambda x:x[1])

        while l < r:
            tmp = nums[l][1] + nums[r][1]

            if tmp > target:
                r -= 1
            elif tmp < target:
                l += 1
            else:
                return [nums[l][0], nums[r][0]]
