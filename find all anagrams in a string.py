# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hmap = {}
        result = []
        for i in range(len(p)):
            if p[i] not in hmap:
                hmap[p[i]]=1
            else:
                hmap[p[i]]=hmap[p[i]]+1
        match = 0
        for i in range(len(s)):
            # incoming character
            inc = s[i]
            if inc in hmap:
                count = hmap[inc]
                count=count-1
                if count==0:
                    match=match+1
                hmap[inc]=count
            # outgoing character
            if i>=len(p):
                out = s[i-len(p)]
                if out in hmap:
                    count=hmap[out]
                    count=count+1
                    if count==1:
                        match=match-1
                    hmap[out]=count
            
            if match==len(hmap):
                result.append(i-len(p)+1)
        return result
