## Problem Statement
Given a list of unique random integers, 
return all instances of unique integer pairs that sum to k.

## Design Approach
Build a hash where the sum of all pair purmutations are hash keys.  Record each
pair of numbers as a number string in a value string array corresponding to the 
sum key.

###Classes and Methods: 
|Element | Description          |                                                                     |
|--------|----------------------|---------------------------------------------------------------------|
|**Class**  | *PairsSearch*     | primary class for performing the search                             |
|**Method** | *initialize(n)*   | builds a random unique array of integers, and indexes the pairs sum |
|**Method** | *index_pairs_sum* | performs all permuations of elements and computes sum               |
|**Method** | *report(k)*       | returns all integer pairs that sum to k                             | 

## Ruby Implementation
We build our Ruby algorithm in TDD fashion using RSpec and call the project "pairs_search".

###File Design
|File    | Description                                                                          |
|--------|----------------|---------------------------------------------------------------------|
|**pairs_search.rb**      |main class for performing the search                                 |
|**pair_store.rb**        |helper class for storing pairs of numbers and their sum key          |
|**main.rb**              |command line executable to test the PairsStore                       |
|**pairs_search_spec.rb** |rspec test case file                                                 |
|**spec_helper.rb**       |rspec autogenerated file (NOTE: must add a require statement below)  |

**File:** pairs_search.rb - primary class for performing the search
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

**File:** pair_store.rb - class to handle indexing sums and their pairs
```Ruby
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
```

**File:** main.rb - command line executable to test the PairsStore
```Ruby
require './pairs_search'

  puts "ENTER number of integers to pair[3-100]:"
  n=gets.chomp.to_i
  if (n < 3) || (n > 100)
    puts "Illegal number of values"
    abort
  end

  puts "ENTER sum value to search[4-200]:"
  k=gets.chomp.to_i

  if (k < 4) || (k > 200)
    puts "Illegal sum value"
    abort
  end

  p = PairsSearch.new(n)

  # might get nil from no matches, so catch that error if it occurs
  begin
    puts "Result: #{p.report(k).size} sums found"
    p.report(k).each do |x| puts "(#{x})" end
  rescue
    puts "no matches found"
  end
```

###Command Line Test
Let's go ahead and run through the execution of ```PairsSearch``` and see some results.
```
$ ruby main.rb
ENTER number of integers to pair[3-100]:
10
ENTER sum value to search[4-200]:
15
Result: 3 sums found
(5,10)
(6,9)
(7,8)

$ ruby main.rb
ENTER number of integers to pair[3-100]:
25
ENTER sum value to search[4-200]:
15
Result: 7 sums found
(7,8)
(3,12)
(2,13)
(4,11)
(5,10)
(1,14)
(6,9)
... and so on
```

###TDD
Finally we would ensure that we have test converage over our classes and methods.  We use the "RSpec" method and the first step is to initialize RSpec capability within our project folder.
```
$ rspec --init
```
This creates a spec folder and places a spec_helper.rb file into this sub-folder.
We also need to create a test file ```pairs_search_spec.rb``` and place it in this same sub-folder.</br>
One little thing that needs to be done is to add a require statement into the top of our helper file.</br>

Insert ```require './pairs_search'``` into pairs_search_spec.rb at the top of the code block.
```Ruby
# a bunch of autogenerated comments...
require './pairs_search'
RSpec.configure do |config|
...
end
```

**File:** pairs_search_spec.rb
```Ruby
require 'spec_helper'

describe PairsSearch do 

	it "Generate 7 unique integers for input" do
		expect(PairsSearch.new(7).nums.sort).to eq([1,2,3,4,5,6,7])
	end 

	it "Tests 5 random integers that sum to 6" do	
		expect(PairsSearch.new(5).report(6).sort).to \
		eq(["1,5", "2,4"])
	end

	it "Tests 7 random integers that sum to 12" do	
		expect(PairsSearch.new(7).report(12).sort).to \
		eq(["5,7"])
	end

	it "Tests 10 random integers that sum to 10" do	
		expect(PairsSearch.new(10).report(10).sort).to \
		eq(["1,9", "2,8", "3,7", "4,6"])
	end

	it "Tests 32 random integers that sum to 60" do	
		expect(PairsSearch.new(32).report(60).sort).to \
		eq(["28,32", "29,31"])
	end	
end
```
###TDD Execution
Now, to run our TDD tests we simply type
```
$ rspec
.....

Finished in 0.00331 seconds (files took 0.10297 seconds to load)
5 examples, 0 failures
```

## Java Implementation
Ruby gives us a quick way to be able to prototype and debug the basic elements of our algorithm.  
However, some environments require the use of Java as the preferred language. Therefore, we will
translate the ruby code by equivalent functionality and then compare performance and line count
between the two.

**Files:**  pairs_search.java - mainclass for performing the search.
	pairs_store.java  - helper class for storing pairs of numbers and their sum key

## Dockerize!
Now finally, we will take everything we've learned above in our "polyglot" adventure and apply this to 
creating a *Dockerized* Linux container implementation of PairsSearch.  The basic design approach will
be to create a simple web server that can take 2 inputs from a browser page and then render an output
that is equivalent to our command line language versions, but in HTML to the user's webpage.



