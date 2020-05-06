class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(S):
            last_index[c] = i
        
        i, j, res = 0, 0, []
        last_part = -1
        while i < len(S):
            j = max(j, last_index[S[i]])
            if i == j:
                res.append(j - last_part)
                last_part = j
                j += 1
                
            i += 1
        
        return res
