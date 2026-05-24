class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket
        hm={}
        freq=[[] for i in range(len(nums)+1)]
        
        for i in nums:
            hm[i]=1+hm.get(i,0)
        
        for i,v in hm.items():
            freq[v].append(i)
        
        res=[]
        
        for i in range(len(freq)-1,0,-1):
            for somthing in freq[i]:
                res.append(somthing)
                if len(res)==k:
                    return res









        #Heap

        # hm = defaultdict()
        
        # for i in nums:
        #     hm[i]=+1+hm.get(i,0)
        # print(hm)

        # heap=[]
        # for num in hm.keys():
        #     heapq.heappush(heap,(hm[num],num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # print(heap)
        # res=[]

        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res


           