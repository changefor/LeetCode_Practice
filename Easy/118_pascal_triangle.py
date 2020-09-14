from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        global top, result
        result = []
        top = [1]
        result.append(top)
        for i in range(numRows):
            if i == 0:
                continue
            else:
                now = []
                now.append(1)
                for j in range(len(top)):
                    if j == (len(top)-1):
                        break
                    else:
                        now.append(top[j] + top[j+1])
                now.append(1)
                result.append(now)
                top = now
        return result

ret = Solution().generate(5)

for l in ret:
    print(l)