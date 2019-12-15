import java.util.Arrays;
import java.util.function.BiFunction;
import java.util.stream.IntStream;

class AdventOfCode20190202 {
    private static int intComputer(int[] data) {
        for (int ip = 0; data[ip] != 99; ip += 4) {
            switch (data[ip]) {
                case 1:
                    data[data[ip + 3]] = data[data[ip + 1]] + data[data[ip + 2]];
                    break;

                case 2:
                    data[data[ip + 3]] = data[data[ip + 1]] * data[data[ip + 2]];
                    break;

                default:
                    throw new Error("Unknown opcode " + data[ip]);
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
