class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if len(word)> len(board) * len(board[0]):
            return False

        word_count=Counter(word)
        board_count=Counter([word for w in board for word in w])

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        for ch,count in word_count.items():
            if count> board_count[ch]:
                return False

        def dfs(row, col,ind):

            if ind==len(word):
                return True

            if row<0 or col<0 or row >=len(board) or col>=len(board[0]) or board[row][col]!=word[ind]:
                return False

            temp=board[row][col]
            board[row][col]="#"

            found=(dfs(row,col+1,ind+1) or
                   dfs(row+1,col,ind+1) or
                   dfs(row-1,col, ind+1) or
                   dfs(row,col-1,ind+1))

            board[row][col]=temp
            return found



        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True

        return False