public class BubbleSort {

	public static void main(String[] args) {
		Integer[] res = bubble(new Integer[]{3,5,7,9,5,3,1});
		for (int i : res) {
			System.out.print(i + " ");
		}
		System.out.println();
		res = bubble(new Integer[]{4,1,2,3});
		for (int i : res) {
			System.out.print(i + " ");
		}
	}

	private static Integer[] bubble(Integer[] integers) {
		for (int curr = 0; curr < integers.length; ++curr) {
			for (int other = curr + 1; other < integers.length; ++other) {
				if (integers[curr] > integers[other]) {
					int tmp = integers[curr];
					integers[curr] = integers[other];
					integers[other] = tmp;
				}
			}
		}
		return integers;
	}
}
