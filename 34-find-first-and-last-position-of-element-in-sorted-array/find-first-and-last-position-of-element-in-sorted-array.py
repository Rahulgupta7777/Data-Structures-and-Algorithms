class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        low=0
        high=len(nums)-1
        first=-1
        last=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        low=0
        high=len(nums)-1
        while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    last=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
        return [first,last]