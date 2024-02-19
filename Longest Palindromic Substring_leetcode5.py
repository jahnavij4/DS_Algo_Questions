class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=""
        def isPalindrome(sub):
            return sub==sub[::-1]
        for i in range(1,n+1):
            dp[i]=dp[i-1]
            for j in range(i):
                if isPalindrome(s[j:i]):
                    if len(s[j:i])>len(dp[i-1]):
                        dp[i]=s[j:i]
        return dp[n]
