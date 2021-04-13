"""
    Author: Adam Farid
    Problem: 485 Max Consecutive Ones
    Given a binary array nums, return the maximum number of consecutive 1's in the array. 
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxOne = -1
        for num in nums:
            #If we encounter a 1 increment the count
            if num == 1:
                count+=1
            #If we encounter a 0 set the count to 0 so that we can start counting 1's again
            if num == 0: count = 0
            #Now we simply check if the count is bigger than previously seen and update the maxOne variable
            if count > maxOne:
                maxOne = count
        return maxOne