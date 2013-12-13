import java.util.HashMap;
import java.util.Vector;


public class Anagram {

	public static void main(String[] args) {
		System.out.println(occurences("AdnBndAndBdaBn", "dAn"));
		System.out.println(occurences("AbrAcadAbRa", "cAda"));
	}

	static int hash(String str) {
		/* 
		 * Map letters to prime numbers... the Java way. :(
		 * We should only do this once and cache the result for
		 * better performance.
		 */
		HashMap<Character, Integer> letter_map = new HashMap<>();
		String letters = "abcdefghijklmnopqrstuvwxyz";
		Integer[] primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
		for (int i = 0; i < letters.length(); ++i) {
			// Zip anyone?
			letter_map.put(letters.charAt(i), primes[i]);
		}

		int result = 0;
		str = str.toLowerCase(); // Don't care about uppercase
		for (char c : str.toCharArray()) {
			result += letter_map.get(c);
		}
		return result;
	}

	private static int occurences(String parent, String child) {
		int child_hash = hash(child);

		int start = 0;
		int end = start + child.length();

		int occured = 0;
		while (end < parent.length()) {
			String sub = parent.substring(start, end);
			if (hash(sub) == child_hash) {
				occured++;
			}
			start++;
			end++;
		}
		return occured;
	}
}

