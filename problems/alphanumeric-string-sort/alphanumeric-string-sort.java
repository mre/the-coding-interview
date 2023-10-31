import java.util.ArrayList;
import java.util.stream.Collectors;

public class AlphanumericStringSort {

    /**
     * Method to specifically sort a String that can contain characters and numbers.
     * The sorting specification goes like this:
     * 1 - All sorted lowercase letters are ahead of uppercase letters.
     * 2 - All sorted uppercase letters are ahead of digits.
     * 3 - All sorted even digits are ahead of sorted odd digits.
     *
     * @param stringToBeSorted The string to be sorted.
     *
     * @return The sorted string.
     */
    static String alphaNumericStringSort(String stringToBeSorted) {

        if(stringToBeSorted == null || stringToBeSorted.trim().length() == 0) {
            return stringToBeSorted;
        }

        // StringBuilder structure of the original String, in order to facilitate operations
        StringBuilder sb = new StringBuilder(stringToBeSorted);

        // Structure that will hold the sorted result
        ArrayList<Character> resultChars = new ArrayList<>();

        // Index where the char should be inserted in result chars structure
        int tempIndex = 0;

        // Adding first char
        resultChars.add(0, sb.charAt(0));

        // Deleting the inserted char from the StringBuilder representation of the original string
        sb.deleteCharAt(0);

        // While the StringBuilder has chars to be processed
        while (sb.length() != 0) {

            char firstChar = sb.charAt(0);

            for (int j = 0; j < resultChars.size(); j++) {
                char secondChar = resultChars.get(j);

                // Get Ascii values
                int firstCharAscii = firstChar;
                int secondCharAscii = secondChar;

                // If chars have the same 'case', we order them by ascii code, because they are in the same group of chars
                if((Character.isLowerCase(firstChar) && Character.isLowerCase(secondChar)) ||
                    (Character.isUpperCase(firstChar) && Character.isUpperCase(secondChar))) {
                    if(firstCharAscii > secondCharAscii) {
                        tempIndex = j + 1;
                    }
                    // If chars are from different types or they are numbers
                } else if (firstCharAscii < secondCharAscii || sortNumbers(firstChar, secondChar)) {
                    tempIndex = j + 1;
                }
            }

            // Update sorted list of characters with the new character and its computed position
            resultChars.add(tempIndex, firstChar);
            sb.deleteCharAt(0);
            // Reset temporary index in order to process next chars
            tempIndex = 0;
        }
        return resultChars.stream().map(c -> c.toString()).collect(Collectors.joining());
    }

    /**
     * Auxiliar method to sort numbers based on their parity.
     *
     * @param firstChar The first char
     * @param secondChar The second char
     *
     * @return The flag that tells if we should insert the char a position forward or not
     */
    private static boolean sortNumbers(char firstChar, char secondChar) {

        if(Character.isDigit(firstChar) && Character.isDigit(secondChar)) {
            int firstCharNumber = Character.getNumericValue(firstChar);
            int secondCharNumber = Character.getNumericValue(secondChar);

            // First char even and second char odd
            if(firstCharNumber % 2 == 0 && secondCharNumber % 2 != 0) {
                return false;
                // First char odd and second char even
            } else if (firstCharNumber % 2 != 0 && secondCharNumber % 2 == 0) {
                return true;
                // First char and second char same parity, so we evaluate the values of them
            } else {
                return firstCharNumber > secondCharNumber;
            }
        }
        return false;
    }

    public static void main(String[] args) {

        // Arrange
        String originalString = "Lj4h35B";
        String expectedString = "hjBL435";

        // Act
        String resultString = alphaNumericStringSort(originalString);

        System.out.println("Sorted string -> " + resultString);
    }
}
