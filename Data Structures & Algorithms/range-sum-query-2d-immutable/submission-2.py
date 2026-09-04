class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]


        for row in range(len(self.prefix) - 1):
            for col in range(len(self.prefix[0]) - 1):
 
                left = self.prefix[row + 1][col]
                top = self.prefix[row][col + 1]
                diagonal = self.prefix[row][col]
                current = self.matrix[row][col]

                self.prefix[row + 1][col + 1] = current + left + top - diagonal
              
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        left = self.prefix[row1][col2 + 1]
        top = self.prefix[row2 + 1][col1]
        diagonal = self.prefix[row1][col1]


        return self.prefix[row2 + 1][col2 + 1] - left - top + diagonal
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)