class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result ^= i
            print result
        
        return result

if __name__ == "__main__":
    nums=[1,2,1,2,3,4,6,3,4,5,6]
    print Solution().singleNumber(nums)