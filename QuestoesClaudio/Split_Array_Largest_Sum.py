class Solution(object):
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            
            subarray_count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > mid:
                    subarray_count += 1
                    current_sum = num
                else:
                    current_sum += num
            
            if subarray_count > k:
                left = mid + 1
            else:
                right = mid
        
        return left