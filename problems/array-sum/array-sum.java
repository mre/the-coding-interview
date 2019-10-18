import java.util.Arrays;
import java.util.stream.Stream;

public class ArraySum {

    int arraySum(Object[] arr) {
        return flatten(arr).mapToInt(o -> (int) o).sum();
    }

    private Stream<Object> flatten(Object[] array) {
        return Arrays.stream(array)
            .flatMap(o -> o instanceof Object[] ? flatten((Object[]) o) : Stream.of(o));
    }
}
