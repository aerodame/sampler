# https://github.com/testdouble/contributing-tests/wiki/Greeting-Kata
require './pair_store'
# ---------------------------------------------------------
# PairsSearch - Given n to initialize an array of unique 
# 				random integers of size n, return all 
#               instances of number unique pairs that 
#               sum to k.
# ---------------------------------------------------------
class PairsSearch
	attr_accessor :iter,:nums

	## Generate n random-unique integers
	def initialize(n)
		@nums=(1..n).to_a.sort{ rand() - 0.5 }
		index_pairs_sum
	end

	## index all pairs that key to their sum
	private def index_pairs_sum
		n = @nums.size-1
		@pairs = PairStore.new
		@iter = 0 

		## incrementing loop over forward permutations
		for i in 0..n
			# never sum same pairs
			for j in (i+1)..n
				x,y = @nums[i],@nums[j]
				x,y =  y,x if (x>y) 
				@pairs.insert(x,y)
				@iter = @iter + 1
			end
		end	
	end

	## print out the results
	def report(k)
		@pairs.get_pairs(k)
	end
end