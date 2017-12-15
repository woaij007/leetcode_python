class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        print len(bits) - 1
        print len(bits)
        if bits[len(bits)-1] == 0 and bits[len(bits)-2] == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    bits = [1, 0, 0]
    print Solution().isOneBitCharacter(bits)