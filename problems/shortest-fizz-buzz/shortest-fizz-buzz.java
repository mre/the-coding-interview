class ShortestFizzBuzz {
  public static void main(String[] args) {
  
  for (int x = 1; x <= 100; x++) {
    System.out.println();
    if (x % 3 == 0) {
      System.out.print("Fizz");
    }
    if (x % 5 == 0) {
      System.out.print("Buzz");
    } if (x % 3 != 0 && x % 5 != 0) {
      System.out.print(x);
    }
  }
  }
}
