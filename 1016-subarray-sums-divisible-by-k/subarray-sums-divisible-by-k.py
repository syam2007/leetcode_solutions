class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        su=0
        ans=0
        w_map={0:1}
        for i in nums:
            su+=i
            if su%k in w_map:
                ans+=w_map[su%k]
            w_map[su%k]=w_map.get(su%k,0)+1 
        return ans       