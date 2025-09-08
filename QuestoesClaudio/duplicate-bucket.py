class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        buckets = {}
        bucket_size = valueDiff + 1

        for i, num in enumerate(nums):
            bucket_index = num // bucket_size
            
            if bucket_index in buckets:
                return True
            
            if (bucket_index - 1) in buckets and abs(num - buckets[bucket_index - 1]) <= valueDiff:
                return True
            
            if (bucket_index + 1) in buckets and abs(num - buckets[bucket_index + 1]) <= valueDiff:
                return True
            
            buckets[bucket_index] = num
            
            if i >= indexDiff:
                old_bucket_index = nums[i - indexDiff] // bucket_size
                if old_bucket_index in buckets:
                    del buckets[old_bucket_index]
        
        return False