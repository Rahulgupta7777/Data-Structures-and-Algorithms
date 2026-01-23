class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
       
        if n%2!=0 and n!=1:
            return False
        temp=n
        count=0
        while temp%2==0:
            temp=temp//2
            count+=1
        return temp==1 and 2**count==n


        