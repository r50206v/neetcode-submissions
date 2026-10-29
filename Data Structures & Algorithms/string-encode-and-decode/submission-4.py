class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, idx = [], 0

        while idx < len(s):
            jdx = idx

            while s[jdx] != "$":
                jdx += 1
            
            length = int(s[idx: jdx])
            res.append(s[jdx + 1: jdx + length + 1])
            idx = jdx + length + 1
        return res
            