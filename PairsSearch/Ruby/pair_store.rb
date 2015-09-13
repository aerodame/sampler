# https://github.com/
# ---------------------------------------------------------
# PairStore - Storing pairs of numbers and their sum key
# ---------------------------------------------------------
class PairStore
	attr_accessor :T

	## Create a hash table for our sums and pairs
	def initialize
		@T={}
	end

	## get any pairs at key = k
	def get_pairs(k)
		@T[k]
	end

	## Insert pair and sum
	def insert(x,y)
		sum = x+y
		@T[sum] = Array.new if @T[sum].nil?
		@T[sum] << "#{x},#{y}"
	end
end
