from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        sl = SortedList()
        for i in range(len(nums)):
            if i > k: sl.remove(nums[i-k-1])
            idxl = sl.bisect_left(nums[i]-t)
            idxr = sl.bisect_right(nums[i]+t)
            if idxl != idxr: return True
            sl.add(nums[i])
        return False