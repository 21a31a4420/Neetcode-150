class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            a=''.join(sorted(i))
            res[a].append(i)
        return list(res.values())
        # for i in strs:
        #     count=[0]*26
        #     for c in i:
        #         count[ord(c)-ord('a')]+=1
        #     k=tuple(count)
        #     res[k].append(i)
        # return list(res.values())
