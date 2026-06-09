class Solution:
    def canSeatAllPeople(self, k, seats):
        n = len(seats)
        
        for i in range(n):
            if seats[i] == 0:
                left = (i == 0 or seats[i - 1] == 0)
                right = (i == n - 1 or seats[i + 1] == 0)
                
                if left and right:
                    seats[i] = 1
                    k -= 1
                    if k <= 0:
                        return True
        
        return k <= 0