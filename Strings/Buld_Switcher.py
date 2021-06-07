import re
class Solution:
    def replace(self, s, ch):
        pattern = ch + '{2,}'
        s = re.sub(pattern, ch, s)
        return s
    
    def minFlips(self, target: str) -> int:
        init = ''.join(['0' for _ in range(len(target))])
        if target == init:
            return 0
        l = target.find("1")
        sub_t = target[l:]
        r1 = self.replace(sub_t, '1')
        r2 = self.replace(r1, '0')
        return len(r2)
