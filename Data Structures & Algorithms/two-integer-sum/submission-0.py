class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #tecnica del complemento

        c = {}

        for i, n in enumerate(nums):
            c[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in c and c[diff]!=i:
                return [i,c[diff]]
        return []