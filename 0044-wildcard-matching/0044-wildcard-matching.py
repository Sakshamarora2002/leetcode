class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        star_index, match_index = -1, -1

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star_index = j
                match_index = i
                j += 1
            elif star_index != -1:
                j = star_index + 1
                match_index += 1
                i = match_index
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
