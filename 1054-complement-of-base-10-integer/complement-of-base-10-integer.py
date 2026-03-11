class Solution:
    def bitwiseComplement(self, n: int) -> int:
        N=n
        if N == 0:
            return 1
        todo, bit = N, 1
        while todo:
            # Flip the current bit
            N = N ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return N
        