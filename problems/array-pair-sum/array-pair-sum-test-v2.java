import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ArrayPairSumTest {

    private ArrayPairSum arrayPairSum;

    @Before
    public void setUp() {
        arrayPairSum = new ArrayPairSum();
    }

    @Test(expected = IllegalArgumentException.class)
    public void testArrayPairSum_ShouldThrowException_WhenInputArrayIsNull() {

        // Arrange
        ArrayList<Integer> inputArray = null;
        int sum = 10;

        // Act
        arrayPairSum.finArrayPairSums(sum, inputArray);
    }

    @Test
    public void testArrayPairSum_ShouldReturnEmptyArray_WhenInputArrayIsEmpty() {

        // Arrange
        ArrayList<Integer> inputArray = new ArrayList<Integer>();
        int sum = 10;

        // Act
        List returnedArray = arrayPairSum.finArrayPairSums(sum, inputArray);

        // Assert
        assertEquals(inputArray, returnedArray);
    }

    @Test
    public void testArrayPairSum_ShouldReturnPairSums_WhenInputArrayHasValues_Case1() {

        // Arrange
        ArrayList<Integer> inputArray = new ArrayList<>(Arrays.asList(3, 4, 5, 6, 7));
        int sum = 10;
        ArrayList<ArrayList<Integer>> expectedArray = new ArrayList<>();
        expectedArray.add(new ArrayList<>(Arrays.asList(3, 7)));
        expectedArray.add(new ArrayList<>(Arrays.asList(4, 6)));

        // Act
        List returnedArray = arrayPairSum.finArrayPairSums(sum, inputArray);

        // Assert
        assertEquals(expectedArray, returnedArray);
    }

    @Test
    public void testArrayPairSum_ShouldReturnPairSums_WhenInputArrayHasValues_Case2() {

        // Arrange
        ArrayList<Integer> inputArray = new ArrayList<>(Arrays.asList(3, 4, 5, 4, 4));
        int sum = 8;
        ArrayList<ArrayList<Integer>> expectedArray = new ArrayList<>();
        expectedArray.add(new ArrayList<>(Arrays.asList(3, 5)));
        expectedArray.add(new ArrayList<>(Arrays.asList(4, 4)));
        expectedArray.add(new ArrayList<>(Arrays.asList(4, 4)));
        expectedArray.add(new ArrayList<>(Arrays.asList(4, 4)));

        // Act
        List returnedArray = arrayPairSum.finArrayPairSums(sum, inputArray);

        // Assert
        assertEquals(expectedArray, returnedArray);
    }

    @Test
    public void testArrayPairSum_ShouldReturnPairSums_WhenInputArrayHasValues_Case3() {

        // Arrange
        ArrayList<Integer> inputArray = new ArrayList<>(Arrays.asList(1, 5, 4, 7, 5, 3, 3));
        int sum = 8;
        ArrayList<ArrayList<Integer>> expectedArray = new ArrayList<>();
        expectedArray.add(new ArrayList<>(Arrays.asList(1, 7)));
        expectedArray.add(new ArrayList<>(Arrays.asList(5, 3)));
        expectedArray.add(new ArrayList<>(Arrays.asList(5, 3)));
        expectedArray.add(new ArrayList<>(Arrays.asList(5, 3)));
        expectedArray.add(new ArrayList<>(Arrays.asList(5, 3)));

        // Act
        List returnedArray = arrayPairSum.finArrayPairSums(sum, inputArray);

        // Assert
        assertEquals(expectedArray, returnedArray);
    }
}
