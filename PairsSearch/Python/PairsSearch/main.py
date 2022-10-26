from pairs_search import PairsSearch
from pairs_store import PairsStore

## Given N random numbers between 1 and M in a list, list all of the pair sums
N = 6
M = 64

ps = PairsSearch(N, M)
pairs = PairsStore()

nums = ps.nums
print(f'Number list:{nums}')

for i in range(N):
    # never sum same pairs
    for j in range(N-i):
        x = nums[i]
        y = nums[j]
        # only store (x,y) => where x < y
        if( x > y):
            tmp = x
            x = y
            y = tmp
        pairs.insert(x,y)
pairs.dump_map()        