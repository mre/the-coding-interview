import java.util.HashMap;
import java.util.Vector;


public class PairSum {

	public static void pairs(int sum, Integer[] arr) {
		HashMap<Integer, Boolean> seen = new HashMap<>();
		for (int i : arr) {
			int complement = sum - i;
			if ( seen.containsKey(complement)) {
				System.out.println(i + "," + complement);
			} else {
				seen.put(i, true);
			}
		}
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		pairs(10, new Integer[]{3, 4, 5, 6, 7}); // [[6, 4], [7, 3]]
		pairs(8, new Integer[]{3, 4, 5, 4, 4}); // [[3, 5], [4, 4], [4, 4], [4, 4]]
		pairs(8, new Integer[]{4}); // []
		pairs(0, new Integer[]{4,-4}); // [[-4,4]]
	}

}
