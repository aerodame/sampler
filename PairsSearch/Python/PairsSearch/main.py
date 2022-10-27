from pairs_data import PairsData
from pairs_search import PairsSearch

## Given N random numbers between 1 and M in a list, list all of the pairs that sum to K
N = 12
M = 62
K = 20

pd = PairsData(N, M)
nums = pd.nums
print(f'Searching {nums} for all pairs that sum to {K}')
ps = PairsSearch(nums, K)
search_result = ps.run()
print(search_result)      