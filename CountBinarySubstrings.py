class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sArray = []
        current = int(s[0])
        arrayNum = 0
        for char in s:
            print char
            print str(current)
            if char == str(current):
                arrayNum += 1
            else: 
                sArray.append(arrayNum)
                arrayNum = 1
                current = 1 - current
        print sArray
        if len(sArray) == 1: return 0
        else:
            result = 0
            for i in range(len(sArray) - 1):
                result += min(sArray[i], sArray[i + 1])
            return result 

if __name__ == "__main__":
    s = '00110'
    print Solution().countBinarySubstrings(s)