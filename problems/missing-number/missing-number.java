import java.util.stream.IntStream;

//java-8 stream solution
public int missing_number(int[] arr){
    //using stream to sum up numbers of array
    int sum = IntStream.of(arr).sum();
    //using gauss adition to add all numbers up to n
    int incremental_sum = (arr[arr.length-1] * (arr[arr.length-1] + 1))/2;
    return incremental_sum-sum;
}
