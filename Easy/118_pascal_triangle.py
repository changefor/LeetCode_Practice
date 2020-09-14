from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        global result
        result = []
        if numRows == 0:
            return result
        result.append([1])
        for i in range(1, numRows):
            new = [None] * (i+1)
            result.append(new)
            for j in range(i+1):
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    ## [2][1] = [1][0]+1[1]
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

ret = Solution().generate(5)

for l in ret:
    print(l)