from pairs_store import PairsStore
"""
## Given a list of sorted unique integers, return a tuple list of pairs that sum to K
"""
class PairsSearch(object):
    def __init__(self, nums, K):
        # Initialize a HashMap ƒor our sums and pairs
        self.pairs = PairsStore()
        self.nums = nums
        self.K = K

    def run(self):
        N = len(self.nums)
        print(f'Number list:{self.nums}')

        for i in range(N):
            # never sum same pairs
            for j in range(i,N-i):
                x = self.nums[i]
                y = self.nums[j]

                # if x and y sum to K then store the pair in the list
                if (x + y) == self.K:
                    if( x > y):
                        tmp = x
                        x = y
                        y = tmp
                    print(f'i:{i} j:{j} x:{x} y:{y} sum:{x+y}')
                    self.pairs.insert(x,y)
        return self.pairs.get_pairs(self.K)            
