class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        cc = len(grid[1])
        rc = len(grid)
        maxgrid = []
        
        for i in range(0,cc-2):
            maxsubgridrow = []
            for j in range(0, rc-2):
                listed = grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]
                
                maxsubgridrow.append(max(listed))
                print(maxsubgridrow)
            maxgrid.append(maxsubgridrow)
        return(maxgrid)
                
