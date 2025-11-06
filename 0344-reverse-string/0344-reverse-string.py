class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if i<j:
                    s[i],s[j]=s[j],s[i]
        return s
       
        
        
