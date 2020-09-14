from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        global result
        result = []
        for i in range(numRows):
            new = [None]*(i+1)
            result.append(new)

        result[0][0] = 1
        for i in range(numRows):
            if i==0:
                continue
            for j in range(i+1):
                if j == 0 or j==i:
                    result[i][j] = 1
                else:
                    ## [2][1] = [1][0]+1[1]
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result

ret = Solution().generate(5)

for l in ret:
    print(l)