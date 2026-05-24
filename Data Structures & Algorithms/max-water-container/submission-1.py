class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Two pointers
        l=0
        r=len(heights)-1
        res=0
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            res=max(area,res)
            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        return res

        #Brute Force
        # res=0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         area= (j-i)*min(heights[i],heights[j])
        #         if res<area:
        #             res=area
        # return res
        