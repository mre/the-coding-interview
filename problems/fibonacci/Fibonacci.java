import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

import org.junit.Assert;

public class Fibonacci {
	
	
	public int FibonacciaAt(int number) {
		List<Integer> fibonacciaSequence = new ArrayList<Integer>();
		fibonacciaSequence.add(0);
		fibonacciaSequence.add(1);
		
		if (number > 2) {
			while (number > fibonacciaSequence.size()) {
				int nextNumberInSequence = fibonacciaSequence.get(fibonacciaSequence.size()-1) + fibonacciaSequence.get(fibonacciaSequence.size()-2);
				fibonacciaSequence.add(nextNumberInSequence);
			}
			
		} else {
			return fibonacciaSequence.get(number-1);
		}
		
		return fibonacciaSequence.get(number-1);

	}
	
	@Test
	public void FibonacciAtTest() {
		Assert.assertEquals(this.FibonacciaAt(1), 0);
		Assert.assertEquals(this.FibonacciaAt(2), 1);
		Assert.assertEquals(this.FibonacciaAt(3), 1);
		Assert.assertEquals(this.FibonacciaAt(4), 2);
		Assert.assertEquals(this.FibonacciaAt(5), 3);
		Assert.assertEquals(this.FibonacciaAt(6), 5);
		Assert.assertEquals(this.FibonacciaAt(7), 8);
		Assert.assertEquals(this.FibonacciaAt(8), 13);
		Assert.assertEquals(this.FibonacciaAt(9), 21);
		Assert.assertEquals(this.FibonacciaAt(10), 34);
		Assert.assertEquals(this.FibonacciaAt(20), 4181);
		Assert.assertEquals(this.FibonacciaAt(30), 514229);
	}

}
