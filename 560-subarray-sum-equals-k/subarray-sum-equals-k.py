class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        su=0
        ans=0
        w_map={0:1}
        for i in nums:
            su+=i
            if su-k in w_map:
                ans+=w_map[su-k]
            w_map[su]=w_map.get(su,0)+1 
        return ans       