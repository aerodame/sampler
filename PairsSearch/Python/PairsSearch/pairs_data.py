import random
"""
PairsData - this generate N random unique integers less than M
"""
class PairsData(object):
    def __init__(self, N=3, M=10):
        self.n = N
        self.m = M
        self.nums = self.__rand_unique(N,M)

    def __rand_unique(self,n,m) -> list[int]:
        cache_set = set()
        if (n > m):
            return [None]
        else:
            # use python set to quickly generate a unique list of random ints
            while(len(cache_set) < n):
                r = int(random.random()*m)
                if (r > 0):
                    cache_set.add(r)
            return sorted(list(cache_set))            