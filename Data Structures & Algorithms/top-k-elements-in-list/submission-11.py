class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict()
        
        for i in nums:
            hm[i]=+1+hm.get(i,0)
        print(hm)

        heap=[]
        for num in hm.keys():
            heapq.heappush(heap,(hm[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        print(heap)
        res=[]

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


           