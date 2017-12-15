class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s += ' '
        currentWord = ''
        reverseWords = ''
        for char in s:
            if char != ' ':
                currentWord += char
            if char is ' ':
                reverseWord = ''
                for i in range(len(currentWord) - 1, -1, -1):
                    reverseWord += currentWord[i]
                reverseWords = reverseWords + reverseWord + ' '
                currentWord = ''
            
        return reverseWords[0:-1]

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print Solution().reverseWords(s)