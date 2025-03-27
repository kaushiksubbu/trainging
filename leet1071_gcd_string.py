class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        common = ""
        x = len(str1)
        y = len(str2)
        m = min(x, y)
        for i in range(m):
            if str1[i] == str2[i]:
                common += str1[i]
        ln = len(common) / 2
        if (ln % 2) == 0:
            if common[0 : int(ln)] == common[int(ln):]:
                gcd = common[0 :int(ln)]
        else:
            gcd = common
        return gcd
