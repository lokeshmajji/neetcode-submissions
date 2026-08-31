class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) +  "#" +  s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            k = i
            while s[i+1] != "#":
                i += 1
            sl = int(s[k:i+1])
            print(sl)
            if i+1 < len(s) and s[i+1] == "#":
                ds = s[i+2:i+2+sl]
                print(ds)
                res.append(ds)
            i = i+2+sl
        return res        
