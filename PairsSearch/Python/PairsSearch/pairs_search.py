import random
"""
PairsStore - Storing pairs of numbers and their sum key.   Note that this is a general purpose
pairs store that could store pairs for numerous keys (hence the use of a Hashmap).  A simpler
version of this would just be a list to store pairs for ONE key.
"""
class PairsSearch(object):
    def __init__(self, n=3, m=10):
        # Initialize a HashMap ƒor our sums and pairs
        self.n = n
        self.m = m
        self.nums = self.__rand_unique(n,m)

    def __rand_unique(self,n,m) -> list[int]:
        if (n > m):
            return [None]
        else:
            rary = [None] * n
            j = 0
            # keep scanning for new random numbers until array is full
            while (j < n):
                r = int(random.random()*m)

                # add only non-zero unique numbers
                if (r == 0): continue	

                not_found = True
                for i in range(n):
                    # if any elements in array are already there then bail
                    if (r == rary[i]):   
                        not_round = False 
                        break 
                # clear to store another unique random int    
                if(not_found):
                    rary[j] = r 
                    j = j+1
            return sorted(rary)            