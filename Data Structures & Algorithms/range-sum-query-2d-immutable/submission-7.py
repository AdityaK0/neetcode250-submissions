class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        # for i in ranxge(len(self.matrixBounds)):
        #     row1 = self.matrixBounds[i][0]
        #     col1 = self.matrixBounds[i][1]
        #     row2 = self.matrixBounds[i][2]
        #     col2 = self.matrixBounds[i][3]
        self.matrix = matrix
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        self.prefixMatrix = [ [0 for c in range(cols+1)] for r in range(rows+1)]

        # instead of finding 1st row and 1st column prefix will find all together 
        # this is also help us to not have go through checks everytime while 
        # finding left part and above part

        for r in range(rows):
            for c in range(cols):
                self.prefixMatrix[r+1][c+1] = self.prefixMatrix[r+1][c]+self.prefixMatrix[r][c+1]+self.matrix[r][c] - self.prefixMatrix[r][c]


        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        row2+=1
        col1+=1
        col2+=1

        # area = self.prefixMatrix[row2][col2]

        #left = self.prefixMatrix[row2][col1-1]
        # above = self.prefixMatrix[row1-1][col2]
        # topLeft = self.prefixMatrix[row1-1][col1-1]

        return (self.prefixMatrix[row2][col2] - self.prefixMatrix[row2][col1-1] - self.prefixMatrix[row1-1][col2] + self.prefixMatrix[row1-1][col1-1])

       
        # in 2 loops

        # grid_sum = 0
        # for r in range(row1,row2+1):
        #     for c in range(col1,col2+1):
        #         grid_sum+=self.matrix[r][c]

        # return grid_sum        
        # creating grid 
        # grid_sum = 0


        # if row1 == row2:
        #     for k in range(col1, col2 + 1):
        #         grid_sum += self.matrix[row1][k]
        #     return grid_sum

        # # step 1 : create upper part
 
        # for k in range(col1,col2+1):
        #     grid_sum+=self.matrix[row1][k]

        # # step 2 : create lower part

        # for j in range(col2,col1-1,-1):
        #     grid_sum+=self.matrix[row2][j]


        # # step 3 : middle part remaining rows row1+1(as we have already covered row1 ) to row2

        # for r in range(row1+1,row2):
        #     for c in range(col1,col2+1):
        #         grid_sum+=self.matrix[r][c]

        # return grid_sum             

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)