class Solution:
    def chooseSwap(self, s):
        first = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
        
        best = s  # default: no swap helps
        
        chars = sorted(first.keys())
        
       
        for i, b in enumerate(chars):
            for a in chars[:i]:  # a < b
                # Swap helps if first[b] < first[a] (first change is b->a, improvement)
                if first[b] < first[a]:
                    candidate = s.translate(str.maketrans(a + b, b + a))
                    if candidate < best:
                        best = candidate
        
        return best