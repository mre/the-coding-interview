import java.util.Arrays;

final class AlnumStringSort {
    public static void main(final String[] args) {
        final char[] input = args[0].toCharArray();
        Arrays.sort(input);

        final StringBuilder[] parts = {new StringBuilder(), new StringBuilder(), new StringBuilder(), new StringBuilder()};

        for (final char c : input) {
            if ('a' <= c && c <= 'z') {
                parts[0].append(c);
            } else if ('A' <= c && c <= 'Z') {
                parts[1].append(c);
            } else if ("02468".indexOf(c) != -1) {
                parts[2].append(c);
            } else {
                parts[3].append(c);
            }
        }

        final StringBuilder acc = parts[0];
        for (int i = 1; i < parts.length; i++) {
            acc.append(parts[i]);
        }
        System.out.println(acc);
    }
}
