from pairs_store import PairsStore
import random
""" 
PairsSearch - Given n and m, initialize an array of unique random (1 to m)
              integers of size n, return all instances of number 
              unique pairs that sum to k.
"""
class PairsSearch:
	def __init__(self,n,m):
		pass
	    self.n=n
		self.nums = self.__rand_unique(n,m)
		# self.__index_pairs_sum()		
        # pairs.dump_map()

    # Insert pair and sum (sum is the key in the HashMap)
    def insert(self, x, y):
        sum = x + y
        pair = f'({x},{y})'

	## Private method to Generate n random unique integers between 1 and m (m >= n)
	# def rand_unique(self, n, m):
    #     if (n > m):
	# 		return [None]
	# 	else:	
    #     	rary = [None] * n
	# 		return rary
        # # print("Creating empty list of None: ", rary)

		# j = 0
        # # keep scanning for new random numbers until array is full
		# while (j < n):
		# 	e = int(random.random()*m)

        #     # add only non-zero unique numbers
		# 	if (e == 0) continue

		# 	# check to see if e is already in return_array
		# 	not_found = True	
        #     for i in range(n):
		# 		# if any elements in array are already there then bail
		# 		if (e == rary[i]):
		# 			not_found = False
		# 			break
		# 	# clear to write another element
		# 	if(not_found):
		# 		rary[j] = e
		# 		j=j+1
		# return rary


	# def report(self,k):
	#     print(f'ans: {pairs.get_pairs(k)}')

    ## Private method to index the pairs sum
	# def __index_pairs_sum(self):
	# 	pairs = PairsStore()
	# 	# index all pairs, iterate over n and 
    #     for i in range(n):
	# 		# never sum same pairs
    #         for j in range(n-i):
	# 			x = self.nums[i]
	# 			y = self.nums[j]
	# 			# only store (x,y) => where x < y
	# 			if( x > y):
    #                 tmp = x
	# 				x = y
	# 				y = tmp
	# 			pairs.insert(x,y)
