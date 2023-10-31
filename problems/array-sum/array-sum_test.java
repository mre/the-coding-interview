import org.junit.Before;
import org.junit.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ArraySumTest {

    private ArraySum arraySumCl;

    @Before
    public void setUp() {
        arraySumCl = new ArraySum();
    }

    @Test
    public void testArraySum_ShouldReturnSumOfAllElements_Case1() {

        // Arrange
        Object[] arr = {1, 2, new Object[]{3, 4, new Object[]{5}}};
        int expectedSum = 15;

        // Act
        int obtainedSum = arraySumCl.arraySum(arr);

        // Assert
        assertEquals(expectedSum, obtainedSum);
    }

    @Test
    public void testArraySum_ShouldReturnSumOfAllElements_Case2() {

        // Arrange
        Object[] arr = {1, 4, 7, 5};
        int expectedSum = 17;

        // Act
        int obtainedSum = arraySumCl.arraySum(arr);

        // Assert
        assertEquals(expectedSum, obtainedSum);
    }

    @Test
    public void testArraySum_ShouldReturnSumOfAllElements_Case3() {

        // Arrange
        Object[] arr = {1, 4, 7, new Object[]{new Object[]{7, 2, 4}, 3, 4, new Object[]{4, 6, 3, 4}}};
        int expectedSum = 49;

        // Act
        int obtainedSum = arraySumCl.arraySum(arr);

        // Assert
        assertEquals(expectedSum, obtainedSum);
    }
}
