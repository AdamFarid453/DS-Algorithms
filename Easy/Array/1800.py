"""
    Author: Adam Farid
    Problem: 1800. Maximum Ascending Subarray Sum
    Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
"""

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxNum = -100
        sumRange = 0
        for i in range(len(nums)):
            if (i==0 or nums[i-1] < nums[i]):
                sumRange+= nums[i]
            else:
                sumRange= nums[i]
            maxNum = max(maxNum,sumRange)
        return maxNum
            