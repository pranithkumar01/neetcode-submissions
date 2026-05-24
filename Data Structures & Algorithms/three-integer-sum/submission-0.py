class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=set()
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                       t=[nums[i],nums[j],nums[k]]
                       s.add(tuple(t))
        return [list(i) for i in s]

        