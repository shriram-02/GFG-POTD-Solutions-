class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        ans = float('inf')
        
        for i in range(x // s + 2):
            for j in range(x // m + 2):
                area = i * s + j * m
                if area >= x:
                    ans = min(ans, i * cs + j * cm)
                else:
                    k = (x - area + l - 1) // l
                    ans = min(ans, i * cs + j * cm + k * cl)
        
        return ans