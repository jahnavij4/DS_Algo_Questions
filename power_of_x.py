class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign=-1 if n<0 else 1
        def power(x,n,sign):
            if n==0: 
                return 1
            return power(x*x,n//2,sign) if n%2==0 else x* power(x*x,n//2,sign)
              # if sign>0 else (x*power(x,n//2,sign))
        return power(x,n,1) if n>0 else 1/power(x,n*sign,-1)
