import java.util.Arrays;
import java.util.function.BiFunction;

class AdventOfCode20190201 {
    private static void apply(int[] data, final int i, final BiFunction<Integer, Integer, Integer> op) {
        data[data[i + 3]] = op.apply(data[data[i + 1]], data[data[i + 2]]);
    }

    public static void main(String[] args) {
        final int[] data = Arrays.stream(args[0].split(",")).mapToInt(Integer::parseInt).toArray();

        for (int i = 0; data[i] != 99; i += 4) {
            switch (data[i]) {
                case 1:
                    apply(data, i, Math::addExact);
                    break;

                case 2:
                    apply(data, i, Math::multiplyExact);
                    break;

                default:
                    throw new IllegalArgumentException("Unknown opcode " + data[i] + ": something went wrong");
            }
        }

        final StringBuilder sb = new StringBuilder();
        for (int datum : data) {
            if (sb.length() != 0) {
                sb.append(',');
            }
            sb.append(datum);
        }
        System.out.println(sb);
    }
}
