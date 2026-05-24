class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        a=1
        for i in range(len(nums)):
            a=1
            for j in range(len(nums)):
                if j==i:
                    j+=1
                else:
                    a*=nums[j]
            res[i]=a
            
        return res

        