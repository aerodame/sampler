// https://github.com/aerodame/sampler
import java.util.HashSet;
import java.util.Random;
import java.util.Vector;

/* 
* PairsSearch - Given n to initialize an array of unique 
* 				random integers of size n, return all 
*               instances of number unique pairs that 
*               sum to k.
*/
public class PairsSearch {

	private Integer n; 
	private Integer[] nums;
	private PairStore pairs;

	public PairsSearch(Integer n) {
		// create n random unique integers
		this.n = n;
		nums = rand_unique(n);
		index_pairs_sum();
		// pairs.dump_map();
	}

	public void report(Integer k) {
		System.out.println("ans: "+pairs.get_pairs(k));
	}

	private void index_pairs_sum() {
		pairs = new PairStore();
		// index all pairs
		for(int i=0; i < n; i++) {
			// never sum same pairs
			for(int j=i+1; j < n; j++) {
				int x = nums[i];
				int y = nums[j];
				// only store (x,y) => where x < y
				if(x>y) {
					int tmp = x;
					x = y;
					y = tmp;
				}
				pairs.insert(x,y);
			}
		}
	}

	// Generate n random unique integers between 1 and n
	private Integer[] rand_unique(Integer n) {

		Random rand = new Random();
		Integer[] return_array = new Integer[n];

		int j = 0;
        // keep scanning for new random numbers until array is full
		while (j < n) {
			Integer e = rand.nextInt(n+1);

            // add only non-zero unique numbers
			if (e == 0) continue;

			// check to see if e is already in return_array
			boolean not_found = true;	
			for(int i=0; i < n; i++) {
				// if any elements in array are already there then bail
				if (e == return_array[i]) {
					not_found = false;
					break;
				} 
			}
			// clear to write another element
			if(not_found) {
				return_array[j] = e;
				j++;
			}
		}
		return return_array;
	}
}