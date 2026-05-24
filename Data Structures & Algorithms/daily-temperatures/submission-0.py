class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i in range(len(temperatures)):
            days=0
            found=False
            for j in range(i+1,len(temperatures)):
                
                if temperatures[i]<temperatures[j]:
                    days=j-i
                    found=True
                    break
            res.append(days if found else 0)
                    
               

        return res

        