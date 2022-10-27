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