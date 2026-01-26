class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumi=0
        for i in range(len(nums)):
            if i%2==0:
                sumi+=nums[i]
            else:
                sumi-=nums[i]
        return sumi

        