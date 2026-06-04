class NumMatrix {
    int[][] T;
    public NumMatrix(int[][] matrix) {
        T = new int[matrix.length + 1][matrix[0].length + 1];
        for(int i=1; i < T.length; i++) {
            for(int j=1; j < T[0].length; j++) {
                T[i][j] = matrix[i - 1][j - 1] +  T[i - 1][j] + T[i][j - 1] - T[i - 1][j - 1];
            }
        }
        //prefix sum = curr value in matrix + prev row + prev col - duplicate row/col
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        //increment row1, row2, col1, col2
        row1++;row2++;col1++;col2++;
        //return ans = prefix[r2][c2] - prefix[r2][c1 - 1] - prefix[r1-1][c2]
        return T[row2][col2] - T[row2][col1 - 1] - T[row1 - 1][col2] + T[row1 - 1][col1 - 1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */