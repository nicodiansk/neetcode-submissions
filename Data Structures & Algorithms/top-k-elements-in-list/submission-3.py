class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket_freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1+ count.get(num, 0)
        for num, cnt in count.items():
            bucket_freq[cnt].append(num)
        
        res = []
        for i in range(len(bucket_freq)-1, 0, -1):
            for elem in bucket_freq[i]:
                res.append(elem)
                if len(res) == k:
                    return res

        return res
