import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class solution {
    public static void main(String[] args) {
        final int[] input = Arrays.stream(args[0].split(",")).mapToInt(Integer::parseInt).toArray();
        final int k = input[0];
        final Set<Integer> seen = new HashSet<>();
        final List<Pair> pairs = new ArrayList<>();

        for (int i = 1; i < input.length; i++) {
            final int n = input[i];
            final int x = k - n;
            if (x != n) {
                if (seen.contains(x)) {
                    pairs.add(new Pair(Math.min(x, n), Math.max(x, n)));
                } else {
                    seen.add(n);
                }
            }
        }

        final StringBuilder sb = new StringBuilder();
        sb.append('[');
        for (Pair pair : pairs) {
            sb.append(pair);
            sb.append(", ");
        }
        sb.setLength(sb.length() - 2);
        sb.append(']');
        System.out.println(sb);
    }

    static class Pair {
        final int first;
        final int second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }

        @Override
        public int hashCode() {
            return Objects.hash(first, second);
        }

        @Override
        public boolean equals(final Object other) {
            return other instanceof Pair && first == ((Pair) other).first && second == ((Pair) other).second;
        }

        @Override
        public String toString() {
            return "(" + first + ", " + second + ")";
        }
    }
}
