import org.junit.Before;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AlphanumericStringSortTest {

    private AlphanumericStringSort alphanumericStringSort;

    @Before
    void setUp() {
        alphanumericStringSort = new AlphanumericStringSort();
    }

    @Test
    void sortAlphaNumericString_ShouldReturnInputString_WhenStringIsNull() {

        // Arrange
        String originalString = null;
        String expectedString = null;

        // Act
        String resultString = alphanumericStringSort.alphaNumericStringSort(originalString);

        // Assert
        assertEquals(expectedString, resultString);
    }

    @Test
    void sortAlphaNumericString_ShouldReturnInputString_WhenStringIsEmpty() {

        // Arrange
        String originalString = "";
        String expectedString = "";

        // Act
        String resultString = alphanumericStringSort.alphaNumericStringSort(originalString);

        // Assert
        assertEquals(expectedString, resultString);
    }

    @Test
    void sortAlphaNumericString_Case1() {

        // Arrange
        String originalString = "3Lj4h5B";
        String expectedString = "hjBL435";

        // Act
        String resultString = alphanumericStringSort.alphaNumericStringSort(originalString);

        // Assert
        assertEquals(expectedString, resultString);
    }

    @Test
    void sortAlphaNumericString_Case2() {

        // Arrange
        String originalString = "3jJW9QKjbG";
        String expectedString = "bjjGJKQW39";

        // Act
        String resultString = alphanumericStringSort.alphaNumericStringSort(originalString);

        // Assert
        assertEquals(expectedString, resultString);
    }

    @Test
    void sortAlphaNumericString_Case3() {

        // Arrange
        String originalString = "Sorting0123456789";
        String expectedString = "ginortS0246813579";

        // Act
        String resultString = alphanumericStringSort.alphaNumericStringSort(originalString);

        // Assert
        assertEquals(expectedString, resultString);
    }

    @Test
    void sortAlphaNumericString_Case4() {

        // Arrange
        String originalString = "0123456789";
        String expectedString = "0246813579";

        // Act
        String resultString = alphanumericStringSort.alphaNumericStringSort(originalString);

        // Assert
        assertEquals(expectedString, resultString);
    }
}
