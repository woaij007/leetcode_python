class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        i = 0
        j = 1
        maxLength = 1
        print len(s) - i, maxLength
        while len(s) - i < maxLength:
            print i,j,maxLength
            while s[j] not in s[i:j]:
                j += 1    
                print i,j
            if j - i > maxLength:
                maxLength = j - i
            i += 1
        return maxLength

if __name__ == '__main__':
    s = "abcdcd"
    print Solution().lengthOfLongestSubstring(s)
