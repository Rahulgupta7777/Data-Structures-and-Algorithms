class Solution(object):
    def solveSudoku(self, board, i=0, j=0):

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []


        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    d = int(board[i][j]) - 1
                    mask = 1 << d
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i // 3) * 3 + (j // 3)] |= mask

        def backtrack(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            box_id = (i // 3) * 3 + (j // 3)


            used = rows[i] | cols[j] | boxes[box_id]

            for d in range(9):
                mask = 1 << d
                if not (used & mask):

                    board[i][j] = str(d + 1)
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[box_id] |= mask

                    if backtrack(index + 1):
                        return True


                    board[i][j] = "."
                    rows[i] ^= mask
                    cols[j] ^= mask
                    boxes[box_id] ^= mask

            return False

        backtrack(0)
