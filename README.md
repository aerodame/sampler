# sampler
This is a show and tell REPO of sample code.

## Problem Statement
Given a list of unique random integers, 
return all instances of unique integer pairs that sum to k.

## Design Approach
Build a hash where the sum of all pair purmutations are hash keys.  Record each
pair of numbers as a number string in a value string array corresponding to the 
sum key.

###Classes and Methods: 
Class: PairsSearch - primary class for performing the search.
   Methods: initialize(n) - builds a random unique array of integers, and indexes the pairs sum.
	    (private) index_pairs_sum
	    report(k) - returns all integer pairs that sum to k
Class: PairsStore - helper class for storing pairs of numbers and their sum key

## Ruby Implementation
We build our Ruby algorithm in TDD fashion using RSpec and call the project "pairs_search"
Files:  pairs_search.rb - main class for performing the search.
	pair_store.rb   - helper class for storing pairs of numbers and their sum key

File:pairs_search.rb
``` Ruby
require './pair_store'
# ---------------------------------------------------------
# PairsSearch - Given n to initialize an array of unique 
# 		random integers of size n, return all 
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
```
## Java Implementation
Files:  pairs_search.java - mainclass for performing the search.
	pairs_store.java  - helper class for storing pairs of numbers and their sum key

## Dockerize!


