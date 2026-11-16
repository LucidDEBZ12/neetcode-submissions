class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_length=0
        start=0
        for i in range(len(s)):
            len1=self.expand_around_center(s,i,i)
            len2=self.expand_around_center(s,i,i+1)
            length=max(len1,len2)
            if length>max_length:
                max_length=length
                start=i-(length-1)//2
        return s[start:start+max_length]

    def expand_around_center(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return (right-left-1)