class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        curBit = n % 2
        n = n / 2
        while n:
            if curBit == n % 2: return False
            curBit = n % 2
            n = n / 2
        return True
            
if __name__ == "__main__":
    n = 7
    print Solution().hasAlternatingBits(n)