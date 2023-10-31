import java.util.ArrayList;
import java.util.Arrays;

public class ArrayPairSum {

    protected ArrayList<ArrayList<Integer>> finArrayPairSums(int sum, ArrayList<Integer> numbersList) {

        // Validations
        if (numbersList == null) {
            throw new IllegalArgumentException("The input array cannot be null!");
        }
        if (numbersList.isEmpty()) {
            return new ArrayList<>();
        }

        // Structure to be returned that will hold all the sum pairs
        ArrayList<ArrayList<Integer>> pairSums = new ArrayList();

        while (numbersList.size() > 1) {
            int firstNumber = numbersList.get(0);
            for (int i = 1; i < numbersList.size(); i++) {
                int secondNumber = numbersList.get(i);

                // We add the pair if their sum is equal to the sum value passed as argument
                if (firstNumber + secondNumber == sum) {
                    pairSums.add(new ArrayList<>(Arrays.asList(firstNumber, secondNumber)));
                }
            }

            // In the end of the iteration, we remove the first value of the list that was just processed and process again
            numbersList.remove(0);
        }
        return pairSums;
    }
}
