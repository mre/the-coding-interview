import java.util.Arrays;

class solution {
    public static void main(String[] args) {
        final int[] data = Arrays.stream(args[0].split(",")).mapToInt(Integer::parseInt).toArray();

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

        final StringBuilder sb = new StringBuilder();
        for (final int datum : data) {
            if (sb.length() != 0) {
                sb.append(',');
            }
            sb.append(datum);
        }
        System.out.println(sb);
    }
}
