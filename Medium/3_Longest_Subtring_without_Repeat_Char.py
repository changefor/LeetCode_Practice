class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global start, now,result, nowMax, dict
        start = 0
        now = start
        result = 0
        nowMax = 0
        dict = {}
        if len(s) == 0:
            return nowMax;

        while now in range(len(s)):
            if s[now] not in dict or dict[s[now]] < start:
                result += 1
                if result > nowMax:
                    nowMax = result
            else:
                start = dict[s[now]] + 1
                result = now - start + 1
            dict[s[now]] = now
            now += 1
        #if result > nowMax:
        #    nowMax = result
        return nowMax


s1 = "abcabcabc"
s2 = "ewwekw"
s3 = "b"
s4 = "pwwkew"

s = Solution()
print(s.lengthOfLongestSubstring(s1))
print(s.lengthOfLongestSubstring(s2))
print(s.lengthOfLongestSubstring(s3))
print(s.lengthOfLongestSubstring(s4))


