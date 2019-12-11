public class solution {
    public static void main(String[] args) {
        System.out.println(
            args[0].lines().mapToInt((x) -> Integer.parseInt(x) / 3 - 2).sum()
        );
    }
}
