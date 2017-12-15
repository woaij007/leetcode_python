class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is 1:
                    result += 4
                    print result
                    if j > 0 and grid[i][j-1] is 1:
                        result -= 2
                    if i > 0 and grid[i-1][j] is 1:
                        result -= 2
        return result

if __name__ == '__main__':
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print Solution().islandPerimeter(grid)