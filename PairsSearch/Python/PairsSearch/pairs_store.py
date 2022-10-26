"""
PairsStore - Storing pairs of numbers and their sum key.   Note that this is a general purpose
pairs store that could store pairs for numerous keys (hence the use of a Hashmap).  A simpler
version of this would just be a list to store pairs for ONE key.
"""
class PairsStore:
    def __init__(self):
        # Initialize a HashMap ƒor our sums and pairs
        self.T = {}

# get any pairs at key = k
    def get_pairs(self, k):
        return self.T[k]

# dump hash map
    def dump_map(self):
        print(f'Dump HashMap of {len(self.T)} sums')

        # Dump the entire HashMap
        for k in self.T:
            print(f'sum:{k}, pairs: {self.T[k]}')

    # Insert pair and sum (sum is the key in the HashMap)
    def insert(self, x, y):
        sum = x + y
        pair = f'({x},{y})'

        # get the key exists) then append the new string
        if sum in self.T:
            self.T[sum].append(pair)

        # we must initialize the value (list) at key(sum), then append
        else:
            self.T[sum] = [pair]