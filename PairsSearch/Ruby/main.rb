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
