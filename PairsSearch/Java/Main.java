// https://github.com/aerodame/sampler
import java.io.Console;
import java.io.IOException;

public class Main {

	public static void main (String args[]) throws IOException {
		 

		Console c = System.console();
		if (c == null) {
			System.err.println("No console.");
			System.exit(1);
		}

		String strN = c.readLine("ENTER number of integers to pair[3-100]: ");
		Integer n = Integer.parseInt(strN);
		if ((n < 3) || (n > 100)) {
			System.err.println("Illegal number of values");
			System.exit(1);
		}

		String strK = c.readLine("ENTER sum value to search[4-200]: ");
		Integer k = Integer.parseInt(strK);

		if ((k < 4) || (k > 200)) {
			System.err.println("Illegal sum value");
			System.exit(1);
		}
		
		PairsSearch p = new PairsSearch(n);
		p.report(k);
	}
/*


// might get nil from no matches, so catch that error if it occurs
		try {
// puts "Result: #{p.report(k).size} sums found"
// p.report(k).each do |x| puts "(#{x})" end
		}
		catch (e)
		{
			System.out.println("no matches found");
		}
	}
*/
}