#week02-3.py
#392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)
        i = 0
        for k in range(N2):
            if i < N1 and s[i] == t[k]:
                i += 1
        if i == N1:
            return True
        else:
            return False
