class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(set(nums))
        s_list=[]
        if not s:
            return 0
        for i in s:
            s_list.append(i)
        print(s_list)
        max_length = 1
        current_length = 1

        
        for i in range(len(s_list)-1):
            if s_list[i]+1 == s_list[i+1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)  
                current_length = 1
        
        return max(max_length, current_length)



            
        
            

        