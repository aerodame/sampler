// https://github.com/aerodame/sampler
import java.util.Map;
import java.util.Set;
import java.util.HashMap;
import java.util.Arrays;
import java.util.Vector;

/* 
* PairStore - Storing pairs of numbers and their sum key
*/
public class PairStore {
//	private Map<Integer, Array> T;
	private Map<Integer, Vector<String>> T;

	// Create a hash table for our sums and pairs
	public PairStore() {
		T = new HashMap<Integer, Vector<String>>();
	}

	// get any pairs at key = k
	public String get_pairs(int k) {
		return T.get(k).toString();
	}

	// dump map
	public void dump_map() {
		System.out.println("Dump HashMap["+T.size()+"]");

		// Dump the entire HashMap
		Set<Map.Entry<Integer, Vector<String>>> set = T.entrySet();
		for (Map.Entry<Integer, Vector<String>> x : set) {
			Vector<String> v = x.getValue();
			System.out.println("T["+x.getKey()+"]: " + v.toString());
		}
	}		
	// Insert pair and sum
	public void insert(int x, int y) {
		Integer sum = x+y;
		// get the Vector (if it exists) then append the new string
		Vector<String> w = T.get(sum);
		if(w == null) {
			Vector<String> v = new Vector<String>();
			v.add("("+x+","+y+")");
			T.put(sum, v);
		} else {
			w.add("("+x+","+y+")");
			T.put(sum, w);
		}
	}
}