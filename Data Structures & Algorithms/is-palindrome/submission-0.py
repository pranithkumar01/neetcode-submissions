
class Solution:
    def isPalindrome(self, s: str) -> bool:
    #    a=""
    #    for i in s:
    #     if i.isalnum():
    #         a+=i.lower()
    #    return a==a[::-1]

         a=""
         for i in s:
            if(ord("a")<=ord(i)<=ord("z") or ord("A")<=ord(i)<=ord("Z") or ord("0")<=ord(i)<=ord("9")):
                a+=i.lower()
         return a==a[::-1]


