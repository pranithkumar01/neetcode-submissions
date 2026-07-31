class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        
        # countS, countT={},{}

        # for i in range(len(s)):
        #     countS[s[i]]=1+countS.get(s[i],0)
        #     countT[t[i]]=1+countT.get(t[i],0)
        # print(countS,countT)
        # for c in countS:
        #     if countS[c]!=countT.get(c,0):
        #         return False
            
        # return True



        if len(s)!=len(t):
            return False
        cs={}
        ct={}

        for i in range(len(s)):
            cs[s[i]]=1+cs.get(s[i],0)
        for i in range(len(s)):
            ct[t[i]]=1+ct.get(t[i],0)
        if cs==ct:
            return True
        return False
        
        