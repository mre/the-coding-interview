
public class Shuffle {

	public static void main(String[] args) {
		System.out.println(is_shuffle("abc", "def", "dabecf"));
		System.out.println(is_shuffle("bac", "def", "dabecf"));
		System.out.println(is_shuffle("otto", "anna", ""));
		System.out.println(is_shuffle("otto", "anna", "oatntnoa"));
	}

	private static boolean is_shuffle(String string1, String string2, String string3) {
		if (string1.length() + string2.length() != string3.length()) {
			return false;
		}
		
		char[] str1 = string1.toCharArray();
		char[] str2 = string2.toCharArray();
		int ptr1 = 0, ptr2 = 0;
		for (char c : string3.toCharArray()) {
			if (ptr1 < string1.length() && c == str1[ptr1]) {
				ptr1++;
				continue;
			} else if (ptr2 < string2.length() && c == str2[ptr2]) {
				ptr2++;
				continue;
			} else {
				return false;
			}
		}
		return true;
		
	}
}
