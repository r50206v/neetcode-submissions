class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # seenHash = {}

        # for idx in range(len(strs)):
            
        #     sorted_str = "".join(sorted(strs[idx]))
        #     if seenHash.get(sorted_str):
        #         seenHash[sorted_str].append(strs[idx])
        #     else:
        #         seenHash[sorted_str] = [strs[idx]]
        
        # return list(seenHash.values())

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

