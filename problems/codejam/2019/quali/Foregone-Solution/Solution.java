package fr.yirrilo.contest.codejam.tk19.qualif.a;

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
			String testCase = sc.nextLine();
			String answer = "Case #"+i+": "+solveTestCase(testCase);
			System.out.println(answer);
			solution.append(answer);
		}
		
		return solution.toString();
	}

	private static String solveTestCase(String testCase) {
		String[] reference = testCase.split("");
		String[] first=new String[reference.length];
		String[] second=new String[reference.length];
		for(int i=0;i<reference.length;i++) {
			if("4".equals(reference[i])) {
				first[i] = "2";
				second[i] = "2";
			} else {
				first[i] = reference[i];
				second[i] = "0";
			}
		}
		String num1 = String.join("",first);
		String num2 = String.join("",second).replace("^0", "");
		return num1 + " " + num2 ;
	}

}
