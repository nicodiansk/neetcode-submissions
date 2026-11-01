class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        res = nums[0]
        while left <= right:
            if nums[left]<nums[right]:
                res = min(nums[left], res)
                break
            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[mid]>nums[right]:
                left = mid +1
            else:
                right = mid -1

        return res
        