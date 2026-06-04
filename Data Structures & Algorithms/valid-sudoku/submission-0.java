class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][]seenR = new boolean[9][9];
            boolean[][]seenC = new boolean[9][9];
            boolean[][]seenB = new boolean[9][9];
        for(int i=0; i < 9; i++) {
            
            for(int c=0; c < 9; c++) {
                //char curr = board[i][c];
                if (board[i][c] == '.') {
                    continue;
                }
                int num = board[i][c] - '1';
                if (seenR[i][num]) {
                    return false;
                }
                seenR[i][num] = true;
                if (seenC[c][num]) {
                    return false;
                }
                seenC[c][num] = true;
                int boxRow = i / 3;
                int boxCol = c / 3;
                int boxIndex = boxRow * 3 + boxCol;
                if (seenB[boxIndex][num]) {
                    return false;
                }
                seenB[boxIndex][num] = true;
            }
        }
        return true;
    }
}
