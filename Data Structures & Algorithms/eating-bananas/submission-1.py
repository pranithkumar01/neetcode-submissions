class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l=1
        r=max(piles)
        res=r

        while l<=r:
            k=(l+r)//2
            totalTime=0
            for p in piles:
                totalTime+=math.ceil(float(p)/k) 
            if totalTime<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res

        # speed =1
        # while True:
        #     totalTime=0
        #     for pile in piles:
        #         totalTime+=math.ceil(pile/speed)
        #     if totalTime<=h:
        #         return speed
        #     speed +=1
        # return speed
        # # count=0
        # # k=1
        # # i=0
        # # while i <len(piles) or count > h:
        # #     print(i)
        # #     if count>h:
        # #         count=0
        # #         k+=1
        # #         i=0
                
        # #     elif piles[i]==k:
        # #         count+=1
        # #         i+=1
        # #     elif piles[i]>k:
        # #         count+= (piles[i]/k)
        # #         i+=1
        # #     elif piles[i]<k:
        # #         count +=1
        # #         i+=1
            
        # # return k


        