class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    empty.append((r, c))

                else:
                    num = board[r][c]

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def solve(idx):

            if idx == len(empty):
                return True

            r, c = empty[idx]

            box = (r // 3) * 3 + c // 3

            for num in "123456789":

                if (num not in rows[r] and
                    num not in cols[c] and
                    num not in boxes[box]):

                    board[r][c] = num

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    if solve(idx + 1):
                        return True

                    board[r][c] = "."

                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            return False

        solve(0)
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:

#         def valid(num, r, c):
#             for i in range(9):
#                 if (board[r][i] == num or
#                     board[i][c] == num or
#                     board[3*(r//3) + i//3][3*(c//3) + i%3] == num):
#                     return False
#             return True

#         def solve():
#             for r in range(9):
#                 for c in range(9):
#                     if board[r][c] == ".":
#                         for num in "123456789":
#                             if valid(num, r, c):
#                                 board[r][c] = num

#                                 if solve():
#                                     return True

#                                 board[r][c] = "."

#                         return False

#             return True

#         solve()