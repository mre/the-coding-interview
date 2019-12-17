import java.io.InputStream;
import java.util.Scanner;

public class Solution {

	public static void main( String[] argv ) throws Exception {
		InputStream inputStream = System.in;
		doJob(inputStream);
	}

	public static String doJob(InputStream inputStream) {
		Scanner sc = new Scanner(inputStream);
		StringBuilder solution = new StringBuilder();
		int testCaseNumber = Integer.valueOf(sc.nextLine());
		for(int i = 1; i <= testCaseNumber; i++) {
			int size = Integer.valueOf(sc.nextLine());
			String path = sc.nextLine();
			String answer = "Case #"+i+": "+solveTestCase(path, size);
			System.out.println(answer);
			solution.append(answer);
		}
		
		return solution.toString();
	}

	private static String solveTestCase(String testCase, int size) {
		String[] reference = testCase.split("");
		String[] solution = new String[reference.length];
		for(int i=0;i<reference.length;i++) {
			if("E".equals(reference[i])) {
				solution[i] = "S";
			} else {
				solution[i] = "E";
			}
		}
		return String.join("", solution);
	}

}
