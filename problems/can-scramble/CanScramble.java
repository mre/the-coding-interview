import java.util.HashMap;
import java.util.Map;

public class CanScramble {
    public static void main(String[] args) {
        assert canScramble("abc", "cba");
        assert !canScramble("ac", "bb");
        assert !canScramble("aab", "bba");
    }

    private static boolean canScramble(final String lhs, final String rhs) {
        return lhs.length() == rhs.length()
            && scrambleMap(lhs).equals(scrambleMap(rhs));
    }

    private static Map<Character, Integer> scrambleMap(final String s) {
        final Map<Character, Integer> m = new HashMap<>();
        for (final char c : s.toCharArray()) {
            m.merge(c, 1, Integer::sum);
        }
        return m;
    }
}
