class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
            
        def rob(start, end):
            rob1, rob2 = 0,0
            print(nums[start:end])
            for n in nums[start:end]:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(rob(1, len(nums)), rob(0, len(nums)-1))