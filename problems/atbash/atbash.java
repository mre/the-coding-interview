import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class AtBash {

    private static char[] letters = IntStream.rangeClosed('a', 'z')
        .mapToObj(c -> "" + (char) c).collect(Collectors.joining()).toCharArray();

    private static String cipher(String text) {
        StringBuilder cipheredText = new StringBuilder();
        int index;
        for (char c : text.toCharArray()) {
            index = IntStream.range(0, letters.length)
                .filter(i -> letters[i] == Character.toLowerCase(c))
                .findFirst()
                .orElse(-1);
            cipheredText.append(Character.isLowerCase(c) ? Character.toUpperCase(letters[25 - index]) : Character.toLowerCase((letters[25 - index])));
        }
        return cipheredText.toString();
    }

    public static void main(String[] args) {
        System.out.println(cipher("irk"));
        System.out.println(cipher("LOW"));
        System.out.println(cipher("hob"));
        System.out.println(cipher("hold"));
        System.out.println(cipher("AaZz"));
    }
}
