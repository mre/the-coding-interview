public class solution {
    public static void main(String[] args) {
        int sum = 0;
        for (int x : args[0].lines().mapToInt(Integer::parseInt).toArray()) {
            while (x > 0) {
                x = Math.max(0, x / 3 - 2);
                sum += x;
            }
        }
        System.out.println(sum);
    }
}
