class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s=sum(arr[:k])
        ex=s
        c=0
        if s>=k*threshold:
            c+=1
        for i in range(k,len(arr)):
            s=s-arr[i-k]+arr[i]
            if s>=k*threshold:
                c+=1
        return c        