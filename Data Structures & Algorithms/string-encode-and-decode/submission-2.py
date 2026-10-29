class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            s_len = len(s)
            res += str(s_len) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while (i < len(s)):
            s_len_str = ''
            while (s[i] != '#'):
                s_len_str += s[i]
                i += 1
            s_len_int = int(s_len_str)
            i += 1
            s_build = ""
            j = i
            while j < i + s_len_int:
                s_build += s[j]
                j += 1
            strs.append(s_build)
            i = j
        return strs

