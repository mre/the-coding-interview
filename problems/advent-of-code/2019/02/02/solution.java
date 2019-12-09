import java.util.Arrays;
import java.util.function.BiFunction;
import java.util.stream.IntStream;

class AdventOfCode20190202 {
    private static void apply(int[] data, final int i, final BiFunction<Integer, Integer, Integer> op) {
        data[data[i + 3]] = op.apply(data[data[i + 1]], data[data[i + 2]]);
    }

    private static int intComputer(int[] data) {
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
        return data[0];
    }

    public static void main(String[] args) {
        final int[] input = Arrays.stream(args[0].split(",")).mapToInt(Integer::parseInt).toArray();

        IntStream.rangeClosed(0, 99).forEach(noun -> {
            IntStream.rangeClosed(0, 99).forEach(verb -> {
                int[] data = input.clone();
                data[1] = noun;
                data[2] = verb;
                if (intComputer(data) == 19690720) {
                    System.out.println(100 * noun + verb);
                    System.exit(0);
                }
            });
        });

        System.exit(1);
    }
}
