class Solution:
    def splitArray(self, nums, m):
        def canSplit(maxSum):
            current_sum = 0
            splits = 1
            
            for num in nums:
                if current_sum + num <= maxSum:
                    current_sum += num
                else:
                    splits += 1
                    current_sum = num
                    if splits > m:
                        return False
            return True
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
