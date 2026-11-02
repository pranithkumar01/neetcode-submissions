class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1        
        # l= 0
        # r=len(nums)-1
        

        
        # while l<=r:
        #     m=(l+r)//2
        #     if target==nums[m]:
        #         return m
        #     # left sorted
        #     if nums[l]<=nums[m]:
        #         if nums[m]< target or nums[l]>target:
        #             l=m+1
        #         else:
        #             r=m-1
        #     else:
        #         if nums[m]>target or target > nums[r]:
        #             r=m-1
        #         else:
        #             l=m+1
        # return -1
        
